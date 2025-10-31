from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class HFClient:
    def __init__(self, model_name):
        self.model_name = model_name
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.model = AutoModelForCausalLM.from_pretrained(model_name)
            if torch.cuda.is_available():
                self.model.to('cuda')
        except Exception:
            self.tokenizer = None
            self.model = None

    def generate(self, prompt, max_tokens=1, temperature=0.0):
        if not self.model or not self.tokenizer:
            return ""
        inputs = self.tokenizer(prompt, return_tensors='pt')
        if torch.cuda.is_available():
            inputs = {k:v.to('cuda') for k,v in inputs.items()}
        with torch.no_grad():
            out = self.model.generate(**inputs, max_new_tokens=max_tokens, do_sample=False)
        text = self.tokenizer.decode(out[0], skip_special_tokens=True)
        return text
