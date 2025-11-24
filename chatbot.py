from transformers import AutoTokenizer, AutoModelForCausalLM

class Chatbot:
    def __init__(self):
        model_name = "microsoft/DialoGPT-small"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

        self.chat_history_ids = None

    def encode_prompt(self, prompt: str):
        return self.tokenizer(prompt, return_tensors="pt")
    
    def decode_reply(self, reply_ids: list[int]) -> str:
        return self.tokenizer.decode(reply_ids)
    
    def generate_reply(self, prompt: str) -> str:
        prompt = prompt + "\n"
        encoded = self.encode_prompt(prompt)

        output_tokens = self.model.generate(
            encoded["input_ids"],
            pad_token_id=self.tokenizer.eos_token_id,
            do_sample=True,
            temperature=0.9,
            top_p=0.8,
            top_k=50
        )

        

        return encoded

