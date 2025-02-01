import funcs
import PySimpleGUI as Sg
import os

if os.path.exists("todo.txt"):
    with open("todo.txt", "w") as file:
        pass

label_add = Sg.Text("Add a TODO")
textbox_add = Sg.InputText(tooltip="Enter a TODO item", key="add_todo")
button_add = Sg.Button("Add")
todos_list = Sg.Listbox(values=funcs.read_file(), key="todos",
                        enable_events=True, size=(45, 10))
button_edit = Sg.Button("Edit")
button_remove = Sg.Button("Remove")
button_exit = Sg.Button("Exit")
window = Sg.Window("TODO App",
                   layout=
                   [
                       [label_add],
                       [textbox_add, button_add],
                       [todos_list, button_edit],
                       [button_remove, button_exit]
                   ],
                   font=("Helvetica", 20))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = funcs.read_file()
            new_todo = values["add_todo"] + '\n'
            todos.append(new_todo)
            funcs.write_file(todos)
            window["todos"].update(values=funcs.read_file())
            window["add_todo"].update(value="")

        case "Edit":
            item_to_edit = values["todos"][0]
            new_todo = values["add_todo"]
            todos = funcs.read_file()
            index = todos.index(item_to_edit)
            todos[index] = new_todo
            funcs.write_file(todos)
            window["todos"].update(values=todos)
            window["add_todo"].update(value="")

        case "todos":
            window["add_todo"].update(value=values["todos"][0])

        case "Remove":
            todos = funcs.read_file()
            item_to_delete = values["todos"][0]
            index = todos.index(item_to_delete)
            todos.pop(index)
            funcs.write_file(todos)
            window["todos"].update(values=todos)
            window["add_todo"].update(value="")

        case "Exit":
            break

        case Sg.WIN_CLOSED:
            break

window.close()