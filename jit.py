"""
This is a script to work with git offline and collaborate with others.
By - Dagim G. Astatkie (dagimg-dot)
Wednesday, October 04 2023
"""
import sys
import enum
import os

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


def setupLocalRemote():
    if len(args) == 2:
        print("usage: jit local-remote <path>")
        print("error: the following arguments are required: path")
    else:
        path = args[2]
        if checkPath(path):
            if checkGit(path):
                pass
            else:
                print("error: the path you entered is not a git repository")
        else:
            print("error: the path you entered does not exist")


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


parseArgs()
