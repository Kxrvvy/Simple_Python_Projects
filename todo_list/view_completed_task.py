import textwrap
from create_json import load_tasks



def view_completed_tasks():
    from main import main
    
    data = load_tasks()

    if not data["tasks"]:
        print("No task to view.")
        return

    desc_width = 20

    for task in data["tasks"]:
        if task["status"] == "completed":
            
            print(f"{'ID': <3} | {'Description': <20}|{'Due Date': <10}| {'Priority': <8} | {'Status': <8}")
            print("-"*3 + "-+-" + "-"*20 + "+" + "-" *10 + "+-" + "-"*8 + "-+" + "-"*8)
            
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
        else:
            print("\n" + "=" * 40)
            print(" No task completed yet.")
            print( "=" * 40)
            
    go_back = input("\nDo you want to go back to menu (y/n): ")
    print("\n")
    
    if go_back == 'y':
        main()
    else:
        return  