import git
import subprocess
import os

# Remote Repository URL
remoteUrl = "git@github.com:PeraltaBoi/dotfiles.git"

# Default dotfiles path
dotfilesPath = "/home/tiago/.config/"  # you have to keep the last slash

# Repository Path
repoPath = "/home/tiago/dotfiles/scriptDotfiles/"  # you have to keep the last slash

# Array of directories to copy
directories = [
        "dunst",
        "hypr",
        "kitty",
        "nvim",
        "waybar",
        "wofi"
        ]

wd = os.getcwd()


def copyFiles():
    # copy the files to the Path
    for directory in directories:
        subprocess.run(
                [
                    "cp",
                    "-r",
                    dotfilesPath + directory,
                    repoPath + directory
                    ]
                )


def commitFiles(repo):
    # Commit the files to the repository
    for directory in directories:
        repo.git.add(
            [
                repoPath + directory
            ])
    repo.index.commit("automatic dotfile update")


def isGitRepo(path):
    try:
        _ = git.Repo(path).git_dir
        return True
    except git.exc.InvalidGitRepositoryError:
        return False


def main():
    # Check if given paths exist
    if not os.path.exists(dotfilesPath):
        print("Dotfiles path does not exist")
        print("Cannot continue")
        print("Please change the dotfilesPath variable")
        return

    if not os.path.exists(repoPath):
        print("Repository path does not exist")
        print("Creating directory")
        os.mkdir(repoPath)
        print("Directory created")

    # Check if the repo path is a git Repository
    if not isGitRepo(repoPath):
        print("No repository found")
        print("Creating repository")
        repo = git.Repo.init(repoPath)
    else:
        print("Repository found")
        print("Updating files")
        repo = git.Repo(repoPath)

    # Copy the files
    print("Copying files")
    copyFiles()

    # Commit the files
    print("Commiting changes")
    commitFiles(repo)

    # Check if the repo has a remote
    if len(repo.remotes) == 0:
        print("No remote found")
        print("Adding remote")
        repo.create_remote("origin", remoteUrl)
        
    # Push the files
    print("Pushing changes")
    os.chdir(repoPath)
    subprocess.run(["git", "push", "origin", "master"])
    os.chdir(wd)

    print("Done")


if __name__ == "__main__":
    main()
