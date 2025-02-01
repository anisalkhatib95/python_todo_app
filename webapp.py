import streamlit as st
import funcs

todos = funcs.read_file()

def add_todo():
    todo_local = st.session_state["new_todo"] + "\n"
    todos.append(todo_local)
    funcs.write_file(todos)
    st.session_state["new_todo"] = ""


st.title("My Todo App")
st.write("Increase your productivity with this lightweight todo app")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(label=todo, key=todo)
    if checkbox:
        todos.pop(index)
        funcs.write_file(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="",
              placeholder="Enter a new todo...",
              key="new_todo",
              on_change=add_todo)