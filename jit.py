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


ARG1 = [command.value for command in Commands]


def help():
    print("\nAvailable commands: ")
    commands_help = """
    -> local-remote - to add a local-remote
    -> push - to push to your local-remote
    -> pull - to pull from your local-remote
    """
    print(commands_help)


def setupLocalRemote():
    if len(args) == 2:
        print("usage: jit local-remote <path>")
        print("error: the following arguments are required: path")


def parseArgs():
    if len(args) == 1:
        print("JIT - One step away to collaborate with others offline using git")
    else:
        if args[1] not in ARG1:
            print(f"error: Unknown command '{args[1]}'")
            help()
        else:
            if args[1] == Commands.LOCAL_REMOTE.value:
                setupLocalRemote()


parseArgs()
