import importlib

class Evaluator:
    def __init__(self, metric_names):
        self.metrics = []
        for name in metric_names:
            name = name.strip()
            module = importlib.import_module(f"evaluators.{name}")
            metric_cls = getattr(module, "Metric", None)
            if metric_cls is None:
                raise ImportError(f"Metric class not found in evaluators.{name}")
            self.metrics.append(metric_cls())

    def evaluate(self, prompt, reference, response):
        scores = {}
        for metric in self.metrics:
            try:
                scores[metric.name] = float(metric.compute(prompt, reference, response))
            except Exception:
                scores[metric.name] = 0.0
        return scores
