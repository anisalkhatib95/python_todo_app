FILEPATH = "todo.txt"

def read_file(file_path=FILEPATH):
    with open(file_path, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_file(list_to_write, filepath=FILEPATH):
    with open(filepath, "w") as file_local:
        file_local.writelines(list_to_write)