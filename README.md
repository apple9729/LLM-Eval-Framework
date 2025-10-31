# LLM-Eval-Framework

Lightweight but production-oriented evaluation framework for large language models.

## Quick start

1. Create a Python virtual environment and install requirements:
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Run an evaluation:
```
python run_eval.py --model hf:bert-base-uncased --dataset datasets/sample_qa.json --metrics factuality,coherence,toxicity --save
```

3. Results saved in results/reports

## Project structure

See repository tree for files and modules.
