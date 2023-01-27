FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    '''
    Read a text file and return the list of to-do items.
    :param filepath: path to the file
    :return: instance of list of todos
    '''
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    '''
    Write the to-do items list in the text file.
    :param todos_arg: pass the updated list to be saved in the file
    :param filepath: filepath to the file where the to-do list is saved. Default filepath is provided.
    :return: The function does not return anything. Only write the new value in the file.
    '''
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


'''
if __name__ function: if we run the functions.py file the lines after the "if" are executed...hence if this file is
the main running file it executes all. When the function is called from the main file, then the two lines after the 
if function will not run. 
'''
if __name__ == "__main__":
    print("Hello")
    print(get_todos())

# print("Hello from functions")
