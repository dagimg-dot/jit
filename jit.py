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
    """
    General help that prints available commands
    """
    print("\nAvailable commands: ")
    commands_help = """
    -> push - to push to your local-remote
    -> pull - to pull from your local-remote
    """
    print(commands_help)


def getLocalRemotePath():
    """
    Returns the remote repo path if it exists
    """
    remote_path_command = "git remote -v"
    output = sp.getoutput(remote_path_command)
    if output == "":
        return ""
    elif output.find("not a git repository") != -1:
        print("error: not a git repository")
        exit(0)
    else:
        line_1 = output.splitlines()
        path = line_1[0].split("\t")[1].split(" ")[0]
        return path


def changeDir(path):
    """
    Changes directory to the provided path
    """
    try:
        os.chdir(path)
    except:
        print("error: the remote drive is not connected")
        exit(0)


def createBranch(name):
    """
    Creates a new branch with the provided name
    """
    command = f"git checkout -b {name}"
    sp.getoutput(command)


def checkBranch(path, current_dir):
    """
    Checks the branch number and create a new one that `jit` can work with
    """
    changeDir(path)
    command = 'git branch'
    branch_list = sp.getoutput(command)
    if len(branch_list.splitlines()) == 1:
        createBranch("master")
        os.chdir(current_dir)


def switchBranch(branch, path):
    """
    Switches to the provided branch in the remote repo
    """
    try:
        switch_command = f"git switch {branch}"
        changeDir(path)
        sp.getoutput(switch_command)
    except:
        print("error: the remote drive is not connected")
        exit(0)


def share(current_dir, command):
    """
    Pushes or Pulls commits to the remote repo
    """
    try:
        os.chdir(current_dir)
        output = sp.getoutput(command)
        if output.find("The current branch main has no upstream branch") != -1:
            first_push_command = "git push --set-upstream origin main"
            sp.call(first_push_command)
        elif output.find("There is no tracking information for the current branch") != -1:
            set_branch_command = "git branch --set-upstream-to=origin/main main"
            first_pull_command = "git pull"
            sp.call(set_branch_command)
            sp.call(first_pull_command)
        else:
            print(output)
    except:
        print("")


def setupSharing(share_command):
    """
    Setup sharing (pulling and pushing)
    """
    path = getLocalRemotePath()
    if path == "":
        print("error: local-remote repository not setup")
    else:
        current_dir = os.getcwd()
        checkBranch(path, current_dir)
        try:
            switchBranch("master", path)
            command = f"git {share_command}"
            # Pull or Push based on the argument passed above
            share(current_dir, command)
            switchBranch("main", path)
        except:
            print("error: read the git error stack above")


def parseArgs():
    """
    Parse arguments passed in the command line
    """
    if len(args) == 1:
        print("JIT - One step away to collaborate with others offline using git")
        help()
    else:
        command = args[1]
        if command not in AVAILABLE_COMMANDS:
            print(f"error: Unknown command '{args[1]}'")
            help()
        else:
            setupSharing(command)


parseArgs()
