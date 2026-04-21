import json
from pathlib import Path

OUTDIR = Path("src/main/resources")

def make_workflow(task_count: int):
    workflow_id = f"order{task_count}"

    states = []
    for i in range(1, task_count + 1):
        state = {
            "name": f"task-{i:02d}",
            "type": "operation",
            "actions": [
                {
                    "functionRef": {
                        "refName": "passThrough"
                    }
                }
            ]
        }

        if i == task_count:
            state["end"] = True
        else:
            state["transition"] = f"task-{i+1:02d}"

        states.append(state)

    workflow = {
        "id": workflow_id,
        "version": "1.0",
        "specVersion": "0.8",
        "name": f"Order {task_count} Tasks",
        "start": "task-01",
        "functions": [
            {
                "name": "passThrough",
                "type": "custom",
                "operation": "service:java:org.acme.OrderFunctions::passThrough"
            }
        ],
        "states": states
    }

    return workflow

def write_workflow(task_count: int):
    workflow = make_workflow(task_count)
    path = OUTDIR / f"order{task_count}.sw.json"
    path.write_text(json.dumps(workflow, indent=2))
    print(f"Generated {path}")

if __name__ == "__main__":
    for n in (20, 50, 60, 70, 80, 100):
        write_workflow(n)
