from datetime import datetime 
from create_json import load_tasks, save_tasks



def add_tasks():
    from main import main
    
    data = load_tasks()

    while True:
        description = input("Task Description: ").strip()

        if description:
            break
        print("Empty description. Input a task")

    while True:
        duedate = input("Date Due (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(duedate, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format! Please use YYYY-MM-DD (e.g., 2024-12-15)")

    while True:
        priority = input("Task priority (Low, Medium, High): ").lower().strip()

        if priority in ["low", "medium", "high"]:
            break
        print("Invalid priority. Please enter high, medium, or low.")

    created_at = datetime.now().strftime("%Y-%m-%d")

    task = {
        "id": data["next_id"],
        "description": description,
        "due_date": duedate,
        "priority": priority,
        "status": "pending",
        "created_at": created_at
    }

    # add task to the list
    data["tasks"].append(task)

    # increment next_id
    data["next_id"] += 1

    # Save task
    save_tasks(data)

    # message
    print("task added!")
    
    go_back = input("\nDo you want to go back to menu (y/n): ")
    print("\n")
    
    if go_back == 'y':
        main()
    else:
        return  