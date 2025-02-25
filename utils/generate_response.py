import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

from utils.calculate_cosine_similarity import calculate_cosine_similarity

models = [
    "Qwen/Qwen1.5-0.5B-Chat",
    "Qwen/Qwen2.5-0.5B",
    "Qwen/Qwen2.5-1.5B",
    "Qwen/Qwen2.5-3B",
    "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
]


def generate_response(query, context_chunks, threshold=0.5, similarity_rate=20, model_index=3):
    similarity_scores = calculate_cosine_similarity(query, context_chunks)
    count_above_threshold = sum(score >= threshold for score in similarity_scores)
    percentage_above_threshold = (count_above_threshold / len(similarity_scores)) * 100

    if percentage_above_threshold <= similarity_rate:
        return "⚠️ Sorry, I couldn't find relevant information to answer your question."

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model_name = models[model_index]
    quantization_config = BitsAndBytesConfig(
        load_in_8bit=True,  # Use 8-bit quantization
        bnb_8bit_compute_dtype=torch.float16
    )
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float16,
        # device_map="auto",
        quantization_config=quantization_config,
        trust_remote_code=True
    ).eval()
    model = torch.compile(model)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Format the prompt with query and context
    context = "\n".join(context_chunks)
    messages = [
        {"role": "user",
         "content": f"<think>\nUse the following context to answer the question:\n\nContext:\n{context}\n\nQuestion: {query}\n\nAnswer:"}
    ]

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    model_inputs = tokenizer(
        [text],
        return_tensors="pt",
        padding=True,
        truncation=True,
    ).to(device)

    # Generate the response
    generated_ids = model.generate(
        model_inputs.input_ids,
        attention_mask=model_inputs.attention_mask,
        max_new_tokens=256,
        do_sample=True,
        temperature=0.7,
        top_k=50,
        top_p=0.9,
        num_return_sequences=1,
        pad_token_id=tokenizer.eos_token_id
    )
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]

    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

    return response
