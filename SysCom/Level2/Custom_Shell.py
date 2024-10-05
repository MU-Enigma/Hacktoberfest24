import os
import sys


def main():
    valid_commands = ['cd', 'mkdir', 'touch', 'open']
    
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input().strip().split()
        
        if len(command) == 0:
            continue
            
        if command[0] not in valid_commands:
            sys.stdout.write(f"{command[0]}: command not found\n")
            continue
        
        if command[0] == 'cd':
            change_directory(command)
        elif command[0] == 'mkdir':
            make_directory(command)
        elif command[0] == 'touch':
            create_file(command)
        elif command[0] == 'open':
            open_file(command)

def change_directory(command):
    try:
        if len(command) > 1:
            os.chdir(command[1])
        else:
            os.chdir(os.path.expanduser("~"))  # Default to home directory
    except FileNotFoundError:
        sys.stdout.write(f"{command[1]}: No such file or directory\n")



def make_directory(command):
    if len(command) > 1:
        try:
            os.mkdir(command[1])
        except FileExistsError:
            sys.stdout.write(f"{command[1]}: Directory already exists\n")
        except Exception as e:
            sys.stdout.write(f"Error: {e}\n")
    else:
        sys.stdout.write("mkdir: missing operand\n")


def create_file(command):
    if len(command) > 1:
        for filename in command[1:]:
            try:
                # Open the file in append mode or just create it if it doesn't exist
                with open(filename, 'a'):
                    # Updating the file's last access and modification times
                    os.utime(filename, None)
            except Exception as e:
                sys.stdout.write(f"Error creating file: {filename}\n")
    else:
        sys.stdout.write("touch: missing file operand\n")


def open_file(command):
    pass