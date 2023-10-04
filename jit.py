"""
This is a script to work with git offline and collaborate with others.
By - Dagim G. Astatkie (dagimg-dot)
Wednesday, October 04 2023
"""
import sys
import enum

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


def parseArgs():
    if len(args) == 1:
        print("JIT - One step away to collaborate with others offline using git")
    else:
        if args[1] not in ARG1:
            print(f"Unknown command '{args[1]}'")


parseArgs()
