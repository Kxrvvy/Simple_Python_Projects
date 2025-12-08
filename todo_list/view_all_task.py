import textwrap
from create_json import load_tasks

from mark_complete import mark_complete


def view_all_tasks():
    from main import main
    
    data = load_tasks()

    if not data["tasks"]:
        print("No task to view.")
        return

    desc_width = 20

    print(f"{'ID': <3} | {'Description': <20}|{'Due Date': <10}| {'Priority': <8} | {'Status': <8}")
    print("-"*3 + "-+-" + "-"*20 + "+" + "-" *
          10 + "+-" + "-"*8 + "-+" + "-"*8)

    for task in data["tasks"]:
        id = task["id"]
        desc = task["description"]
        dd = task["due_date"]
        prio = task["priority"]
        stat = task["status"]
        
        wraptext = textwrap.wrap(desc, desc_width)
        
        if not wraptext:
            wraptext = [""]

        print(f"{id: <3} | {wraptext[0]: <20}|{dd: <10}| {prio: <8} | {stat: <8}")
        
        for extra in wraptext[1:]:
            print(f"{'':<3} | {extra:<20} | {'':<10} | {'':<8} | {'':<8}")
    
    choice = input("\nHave you completed a task (y/n)? ").strip().lower()
    
    if choice == 'y':
        mark_complete()
    
    if choice == 'n':
        go_back = input("\nDo you want to go back to menu (y/n): ")
        print("\n")
        if go_back == 'y':
            main()
        else:
            return   