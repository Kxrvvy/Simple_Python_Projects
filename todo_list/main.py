import os
import json
from datetime import datetime
import textwrap

from add_task import add_tasks
from delete_task import delete_task
from mark_complete import mark_complete
from view_all_task import view_all_tasks
from view_completed_task import view_completed_tasks
from view_pending_tasks import view_pending_tasks


def main():
    
    
    print("========================================")
    print("           TO-DO LIST MANAGER           ")
    print("========================================")

    while True:
        print("\nMenu:")
        print(" 1. Add new task \n",
              "2. View all tasks \n",
              "3. Delete task \n",
              "4. View pending tasks \n",
              "5. View completed tasks \n",
              "6. Exit")
        choice = input("What are we going to do today? ").strip()
        print("\n")
        choice = int(choice)

        match choice:
            case 1:
                add_tasks()
                break
            case 2:
                view_all_tasks()
                break
            case 3:
                delete_task()
                break
            case 4:
                view_pending_tasks()
                break
            case 5:
                view_completed_tasks()
                break
            case 6:
                break
            case _:
                print("Invalid Option")


if __name__ == "__main__":
    main()
