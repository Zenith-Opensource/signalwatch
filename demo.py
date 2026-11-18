import json
from collections import Counter
from pathlib import Path
import workflows

reports = Counter()
with Path(__file__).with_name("data.jsonl").open() as source:
    for line in source:
        row = json.loads(line)
        result = getattr(workflows, row["operation"])(*row["inputs"])
        reports[row["operation"]] += 1
        if reports[row["operation"]] <= 2:
            print(row, "=>", result)
print("Processed:", dict(reports))
