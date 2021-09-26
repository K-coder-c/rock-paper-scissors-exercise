# rock-paper-scissors-exercise

Iteratively develop a command-line Python application which will allow a human user to play a game of Rock-Paper-Scissors against a computer (NPC) opponent.

To successfully run and access this program:
First: (base) kcashiogwu@Kcs-MacBook-Air GitHub % cd /Users/kcashiogwu/Documents/Github/rock-paper-scissors-exercise 

To activate this environment, use:  

conda create -n my-first-env python=3.8
conda activate my-game-env

After activating the virtual environment, install package dependencies (see the ["requirements.txt"](/requirements.txt) file):

```sh
pip install -r requirements.txt
```


To run the program: python game.py

An example Python application for anyone to run to test their local development environment setups.

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip


> NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial `cd` step above).

## Setup

In the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your desired username (then make sure to SAVE the ".env" file aftwards):

    USER_NAME="Jon Snow"
    SECRET_PASSWORD="super duper secret"

> NOTE: the ".env" file is usually the place for passing configuration options and secret credentials, so as a best practice we don't upload this file to version control (which is accomplished via a corresponding entry in the [".gitignore"](/.gitignore) file). This means we need to instruct each person who uses our code needs to create their own local ".env" file.


> NOTE: if you see an error like "ModuleNotFoundError: No module named '...'", it's because the given package isn't installed, so run the `pip` command above to ensure that package has been installed into the virtual environment.
