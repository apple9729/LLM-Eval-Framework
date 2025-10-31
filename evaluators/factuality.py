from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForQuestionAnswering

class Metric:
    def __init__(self):
        self.name = "factuality"
        try:
            self.qa = pipeline("question-answering", model="deepset/roberta-base-squad2", top_k=1)
        except Exception:
            self.qa = None

    def compute(self, prompt, reference, response):
        if not self.qa or not response:
            return 0.0
        try:
            res = self.qa(question=prompt, context=response)
            ans = res.get("answer", "").strip().lower()
            if not ans:
                return 0.0
            ref = reference.strip().lower()
            return 1.0 if ans in ref or ref in ans else 0.0
        except Exception:
            return 0.0
