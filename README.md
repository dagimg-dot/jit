> # JIT -  `offline` collaboration tool using git

## This project is inspired by the internet blackout in Amhara region. 

- ***What does it basically do*** ?
    - It lets you use a **USB drive** as a **remote storage** for your git repository. Then you and your collaborators will have a copy of the remote repo found in the USB drive on their local machine.
    - So, you can pull and push from this remote repo as if you are using github but the catch is - `It is offline`
- ***Why should I use it ?***
    - Bruh, I don't think you have a choice here 🤣🤣.
    - But honestly, you can still track your contributions in a group project. All your commits will be saved as yours in the remote repo as it will be in github.

### Prerequisites

1. A flash drive (USB drive)
    - This is used as a **remote storage** that you can share with the people you are collaborating with.
2. Basic knowledge of **git** and **how it works**. Some basic commands too 😁😁 !!
    - This is because you are going to write them and probably get errors too.

### Getting Started

1.  Copy your local repo to a flash drive to use it as a remote repo and maybe rename it to `your-repo-name-remote`.

2. Connect your remote repo to your local repo.
    - First check if it is already setup. If it is, you have to remove the old one 

        ```bash
        git remote -v # read the name of the remote repo
        
        git remote remove <name-of-the-remote-repo>
        ```

    - Setup the new one.

        ```bash
        git remote add origin <path-of-your-remote-repo-name> # which is found in the USB drive
        ```