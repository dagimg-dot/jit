> # JIT - `offline` collaboration tool using git

## This project is inspired by the internet blackout in Amhara region.

- **_What does it basically do_** ?
  - It lets you use a **USB drive** as a **remote storage** for your git repository. Then you and your collaborators will have a copy of the remote repo found in the USB drive on their local machine.
  - So, you can pull and push from this remote repo as if you are using github but the catch is - `It is offline`
- **_Why should I use it ?_**
  - Bruh, I don't think you have a choice here 🤣🤣.
  - But honestly, you can still track your contributions in a group project. All your commits will be saved as yours in the remote repo as it will be in github.

> > ### Prerequisites

1. A flash drive (USB drive)
   - This is used as a **remote storage** that you can share with the people you are collaborating with.
2. Basic knowledge of **git** and **how it works**. Some basic commands too 😁😁 !!
   - This is because you are going to write them and probably get errors too.

> > ### Getting Started

1.  Copy your local repo to a flash drive to use it as a remote repo and maybe rename it to `your-repo-name-remote`.

2.  Connect your remote repo to your local repo.

    - First check if it is already setup. If it is, you have to remove the old one

      ```bash
      git remote -v # read the name of the remote repo

      git remote remove <name-of-the-remote-repo>
      ```

    - Setup the new one.

      ```bash
      git remote add origin <path-of-your-remote-repo-name> # which is found in the USB drive
      ```

3.  Copy the script to the repo in your local machine

    - It is recommended to create a folder called `jit-script` and put the `jit.py` script inside

4.  Finally `pull` and `push` like you would do with git

    - The available commands are
      - PULL
      - PUSH
    - This is how you would run the script file

      ```python
      python jit-script/jit.py pull # to pull from the remote repo

      python jit-script/jit.py push # to push to the remote repo
      ```

> > ### Tips

1. If you are using jit in a project managed by `npm` you can set it up in the `package.json` `scrpits` section.

   - You can create a command called `jit` and give it a value `python jit-script/jit.py`
   - Then you can use `npm run jit <arg>` to call the script which makes it easier for you hands.

2. If the above case doesn't work for you, you can configure a bash script too !!.

> > ### Common Problems

- These are the problems I faced while testing the script file in different projects.

1. **The ownership is dubious.**

   - This error happens because we are trying to access a folder outside our file system which is the flash drive.
   - The solution is to disconnect and connect the flash drive. And the other solution is,

   ```bash
     git config --global --add safe.directory <path-to-your-remote-repo> # which is in the USB drive
   ```

2. I think all the other problems can be solved by carefully reading the git error message.
