
from create_json import load_tasks, save_tasks



def mark_complete():
    from main import main
    
    data = load_tasks()

    if not data["tasks"]:
        print("No data saved yet.")
        return

    to_complete = input("Enter ID of the task you completed: ")
    to_complete = int(to_complete)

    task_complete = None
    for task in data["tasks"]:
        if to_complete == task["id"]:
            task_complete = task 
            break 
        
    if task_complete:
        task_complete["status"] = "completed"
        save_tasks(data)
        print("Congrats in completing the task!")
    else:
        print("no task found.")
    
    go_back = input("\nDo you want to go back to menu (y/n): ")
    print("\n")
    
    if go_back == 'y':
        main()
    else:
        return   