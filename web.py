import streamlit as st
import functions


def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


todos = functions.get_todos()

st.title("My ToDo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity!")

st.checkbox("Buy grocery")
st.checkbox("throw the trash")

for todo in todos:
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.remove(todo)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo", placeholder="Add a new ToDo",
              label_visibility="hidden",
              on_change=add_todo, key="new_todo")
