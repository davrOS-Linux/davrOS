import subprocess

# Function for running shell commands
def run(command_string):
    subprocess.run(command_string, shell=True)

def stage_0():
    print("[davrOS]: stage 0: Repository Configuration")

    # add chaotic aur (because why not, right?... right?)
    run("pacman-key --recv-key FBA220DFC880C036 --keyserver keyserver.ubuntu.com")
    run("")
    run("pacman-key --lsign-key FBA220DFC880C036")
    run("pacman -U 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-keyring.pkg.tar.zst' 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-mirrorlist.pkg.tar.zst'")
    run('echo "[chaotic-aur]\nInclude = /etc/pacman.d/chaotic-mirrorlist " >> /etc/pacman.conf')

def stage_1():
    print("[davrOS]: stage 1: Package Installation")

    # install all the packages listed in the pkg.txt file using pacman
    run("pacman -Syyu --needed - < pkg.txt")

    # install some stuff from the aur using paru
    run("paru -Su eww")

def stage_2():
    run("[davrOS]: stage 2: Configuration")
    run("mkdir ~/.config")
    username = input("Please enter your user account that you will be using: ")
    print("chosen username: ")
    deck = None
    while deck == None:
        deck = input("Are you using a Steam Deck? (y, n) ")
        if deck == "y":
            deck = True
            print("deck: True")
        elif deck == "n":
            deck = False
            print("deck: False")
        else:
            deck = None
    return username

def stage_2_1():
    print("[davrOS]: stage 2.1: Configuring neovim")

    # install nvchad (because its epic)
    run("git clone https://github.com/NvChad/NvChad ~/.config/nvim --depth 1 && nvim")
    print("[davrOS]: stage 2.2: configuring zsh")
