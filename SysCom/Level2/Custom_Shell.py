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
def make_directory(command):
def create_file(command):
def open_file(command):