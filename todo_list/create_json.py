import os
import json



TASK_FILE = "task.json"


def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    return {"tasks": [], "next_id": 1}


def save_tasks(data):
    with open(TASK_FILE, "w") as file:
        json.dump(data, file, indent=4)


# TEST RUN
'''
loadTask = load_task()
print(f"Task: {loadTask}")

# testing saving task
loadTask["tasks"].append({
    "id": 1,
    "description": "test task",
    "status": "pending"
})
save_task(loadTask)
print("Saved!")


loadTask = load_task()
print(f"load data: {loadTask}")
'''
