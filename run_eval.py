import argparse
from core.runner import EvalRunner

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--model", type=str, required=True)
    p.add_argument("--dataset", type=str, required=True)
    p.add_argument("--metrics", type=str, default="factuality,coherence")
    p.add_argument("--save", action="store_true")
    return p.parse_args()

if __name__ == "__main__":
    args = parse_args()
    runner = EvalRunner(model_name=args.model, dataset_path=args.dataset)
    results = runner.run(metrics=args.metrics.split(","))
    print("\n=== Evaluation Report ===")
    for m, score in results.items():
        print(f"{m:12s}: {score:.3f}")
    if args.save:
        runner.save_report(results)
