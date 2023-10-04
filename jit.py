"""
This is a script to work with git offline and collaborate with others.
By - Dagim G. Astatkie (dagimg-dot)
Wednesday, October 04 2023
"""
import json
import sys
import enum
import os
import subprocess as sp

args = sys.argv
Enum = enum.Enum


class Commands(Enum):
    """
    Enum class for all available commands
    """
    PULL = "pull"
    PUSH = "push"


AVAILABLE_COMMANDS = [command.value for command in Commands]


def help():
    print("\nAvailable commands: ")
    commands_help = """
    -> push - to push to your local-remote
    -> pull - to pull from your local-remote
    """
    print(commands_help)


def getLocalRemotePath():
    remote_path_command = "git remote -v"
    output = sp.getoutput(remote_path_command)
    line_1 = output.splitlines()
    path = line_1[0].split("\t")[1].split(" ")[0]
    return path


def switchBranch(branch, path):
    switch_command = f"git switch {branch}"
    os.chdir(path)
    sp.getoutput(switch_command)


def push(current_dir):
    push_command = 'git push'
    os.chdir(current_dir)
    sp.check_output(push_command, shell=True)


def pull(current_dir):
    pull_command = 'git pull'
    os.chdir(current_dir)
    sp.check_output(pull_command, shell=True)


def setupPush():
    path = getLocalRemotePath()
    if path == "":
        print("error: local-remote repository not setup")
    else:
        current_dir = os.getcwd()
        switchBranch("master", path)
        push(current_dir)
        switchBranch("main", path)


def setupPull():
    path = getLocalRemotePath()
    if path == "":
        print("error: local-remote repository not setup")
    else:
        current_dir = os.getcwd()
        switchBranch("master", path)
        pull(current_dir)
        switchBranch("main", path)


def parseArgs():
    if len(args) == 1:
        print("JIT - One step away to collaborate with others offline using git")
        help()
    else:
        command = args[1]
        if command not in AVAILABLE_COMMANDS:
            print(f"error: Unknown command '{args[1]}'")
            help()
        else:
            if command == Commands.PUSH.value:
                setupPush()
            elif command == Commands.PULL.value:
                setupPull()


parseArgs()
