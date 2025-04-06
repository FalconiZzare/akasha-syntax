import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from sentence_transformers import SentenceTransformer


class ModelSingleton:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        # Load embedding model once
        self.embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

        # Load LLM model once
        models = [
            "Qwen/Qwen1.5-0.5B-Chat",
            "Qwen/Qwen2.5-0.5B",
            "Qwen/Qwen2.5-1.5B",
            "Qwen/Qwen2.5-3B",
            "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
        ]
        model_name = models[1]
        quantization_config = BitsAndBytesConfig(
            load_in_8bit=True,
            bnb_8bit_compute_dtype=torch.float16
        )

        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16,
            device_map="auto",
            quantization_config=quantization_config,
            trust_remote_code=True
        ).eval()

        # Apply torch.compile with the best mode for your hardware
        self.model = torch.compile(self.model, mode="reduce-overhead")

        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

    def encode_text(self, texts):
        return self.embedding_model.encode(texts)

    def generate(self, messages):
        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )

        model_inputs = self.tokenizer(
            [text],
            return_tensors="pt",
            padding=True,
            truncation=True,
        ).to(self.device)

        with torch.inference_mode(), torch.amp.autocast('cuda'):
            generated_ids = self.model.generate(
                model_inputs.input_ids,
                attention_mask=model_inputs.attention_mask,
                max_new_tokens=512,
                num_beams=1,
                num_return_sequences=1,
                pad_token_id=self.tokenizer.eos_token_id
            )

        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]

        response = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        return response