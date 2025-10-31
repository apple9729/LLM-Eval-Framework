import json, os
from datetime import datetime

class Report:
    def save(self, results, output_dir="results/reports"):
        os.makedirs(output_dir, exist_ok=True)
        filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        path = os.path.join(output_dir, filename)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=4, ensure_ascii=False)
        print(f"[+] Report saved at {path}")
