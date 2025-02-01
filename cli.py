import funcs
import  time


def main() -> None:
    now = time.strftime("%b %d, %Y %H:%M:%S")
    print(now)
    while True:
        todos = funcs.read_file()
        user_action = input(
"""
+------------------------+
|        Options         |
+------------------------+
| Add "todo item"        |
| Show                   |
| Edit "todo number"     |
| Complete "todo number" |
| Exit                   |
+------------------------+
Insert action ->  """)

        user_action = user_action.lower().strip()

        if user_action.startswith("add"):
            todo = user_action[4:].strip()
            added = todo.strip('\n')
            todos.append(todo + '\n')
            funcs.write_file(todos)
            print(f"\n{added} was added to the list")

        elif user_action.startswith("show"):
            print("+----------------------------+")
            for index, item in enumerate(todos):
                item = item.strip("\n")
                print(f"{index + 1}- {item}")
            print("+----------------------------+")

        elif user_action.startswith("edit"):
            try:
                item_to_edit = int(user_action[5:].strip())
                old_item = todos[item_to_edit - 1].strip('\n')
                edited_item = input("Input the new item: ")
                todos[item_to_edit - 1] = edited_item + "\n"
                funcs.write_file(todos)
                print(f'Item "{old_item}" was edited and is now: "{edited_item}"')

            except ValueError:
                print("Invalid input. Enter the number of the item you wish to edit.")
                continue

        elif user_action.startswith("complete"):
            try:
                completed = int(user_action[9:].strip())
                removed = todos[completed - 1].strip('\n')
                todos.pop(completed - 1)
                funcs.write_file(todos)

            except IndexError:
                print("There is no item with this number.")
                continue

            except ValueError:
                print("Invalid input. Enter the number of the item you wish to complete.")
                continue

            print(f"{removed} was removed from the list")
        elif user_action.startswith("exit"):
            break

        else:
            print("Invalid input")
            continue

main()