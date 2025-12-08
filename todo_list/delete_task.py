from create_json import load_tasks, save_tasks





def delete_task():
    from main import main
    
    data = load_tasks()

    if not data["tasks"]:
        print("No task to delete.")
        return

    try:    
        del_task = int(input("Enter task ID you want to delete: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    task_to_delete = None
    
    for task in data["tasks"]:
        if task["id"] == del_task:
            task_to_delete = task
            break
    
    if task_to_delete: 
        data["tasks"].remove(task_to_delete)
        save_tasks(data)
        print("Successfully deleted.")
    else:
        print(f"No id {del_task} found ")
        
    data["next_id"] -= 1
    
    save_tasks(data)
    
    go_back = input("Do you want to go back to menu (y/n): ")
    print("\n")
    
    if go_back == 'y':
        main()
    else:
        return  
