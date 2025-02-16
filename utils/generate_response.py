import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


def generate_response(query, context_chunks):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model_name = "Qwen/Qwen1.5-0.5B-Chat"
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype="auto",
        device_map="auto",
        trust_remote_code=True
    )
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Format the prompt with query and context
    context = "\n".join(context_chunks)
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user",
         "content": f"Use the following context to answer the question:\n\nContext:\n{context}\n\nQuestion: {query}\n\nAnswer:"}
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
        max_new_tokens=512,
        pad_token_id=tokenizer.eos_token_id
    )
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]

    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

    return response
