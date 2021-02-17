# 03. File Manipulator

import os

while True:
	command = input().split("-")
	
	if command[0] == "End":
		break
		
	elif command[0] == "Create":
		filename = command[1]
		with open(filename, "w") as file:
			file.write("")
			
	elif command[0] == "Add":
		filename = command[1]
		file_content = command[2]
		with open(filename, "a") as file:
			file.write(file_content)
			file.write("\n")
			
	elif command[0] == "Replace":
		filename = command[1]
		old_string = command[2]
		new_string = command[3]
		if os.path.exists(filename):
			text = ""
			with open(filename, "r") as file:
				text = file.read()
			text = text.replace(old_string, new_string)
			with open(filename, "w") as file:
				file.write(text)
		else:
			print("An error occurred")
			
	elif command[0] == "Delete":
		filename = command[1]
		if os.path.exists(filename):
			os.remove(filename)
		else:
			print("An error occurred")



# other solution

import os


def create(file_path):
    with open(file_path, "w") as file:
        file.write('')


def add(file_path, content):
    with open(file_path, "a") as file:
        file.write(content+"\n")


def replace(file_path, old_str, new_str):
    try:
        with open(file_path, "r+") as file:
            text = ' '.join(file.readlines())
            replaced = text.replace(old_str, new_str)
            file.seek(0)
            file.write(replaced)
    except FileNotFoundError:
        print("An error occurred")


def delete(file_path):
    try:
        os.remove(file_path)
    except FileNotFoundError:
        print("An error occurred")


def start_operation():
    data = input().split("-")
    while not data[0] == "End":
        command, command_args = data[0], data[1:]
        mapper[command](*command_args)
        data = input().split("-")


mapper = {"Create": create,
          "Add": add,
          "Replace": replace,
          "Delete": delete}


start_operation()

















