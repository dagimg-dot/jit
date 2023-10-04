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
    LOCAL_REMOTE = "local-remote"
    PULL = "pull"
    PUSH = "push"


AVAILABLE_COMMANDS = [command.value for command in Commands]


def help():
    print("\nAvailable commands: ")
    commands_help = """
    -> local-remote - to add a local-remote
    -> push - to push to your local-remote
    -> pull - to pull from your local-remote
    """
    print(commands_help)


def checkPath(path):
    isValid = os.path.exists(path)
    return isValid


def checkGit(path):
    isInitalized = os.path.exists(f"{path}/.git")
    return isInitalized


def setLocalRemotePath(path):
    with open("jit.config.json", "r") as f:
        config = json.load(f)

    config['local-remote-path'] = path

    with open("jit.config.json", "w") as f:
        json.dump(config, f, indent=4)


def getLocalRemotePath():
    with open("jit.config.json", "r") as f:
        config = json.load(f)
    return config["local-remote-path"]


def setupLocalRemote():
    if len(args) == 2:
        print("usage: jit local-remote <path>")
        print("error: the following arguments are required: path")
    else:
        path = args[2]
        if checkPath(path):
            if checkGit(path):
                setLocalRemotePath(path)
            else:
                print("error: the path you entered is not a git repository")
        else:
            print("error: the path you entered does not exist")


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
            if command == Commands.LOCAL_REMOTE.value:
                setupLocalRemote()
            elif command == Commands.PUSH.value:
                setupPush()
            elif command == Commands.PULL.value:
                setupPull()


parseArgs()
