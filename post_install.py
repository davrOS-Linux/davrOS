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
    steam = None
    while steam == None:
        steam = input("Would you like to use Steam? (y, n) ")
        if steam == "y":
            steam = True
        elif steam == "n":
            steam = False
        else:
            steam = None
    deck = None
    while deck == None:
        deck = input("Are you using a Steam Deck? (This option determines if steam shortcuts are placed if steam gets installed and also installs necessary software and drivers for the Steam Deck hardware.) (y, n) ")
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

    # install zsh4humans (because its epic)
    run('if command -v curl >/dev/null 2>&1; then\n  sh -c "$(curl -fsSL https://raw.githubusercontent.com/romkatv/zsh4humans/v5/install)"\nelse\n  sh -c "$(wget -O- https://raw.githubusercontent.com/romkatv/zsh4humans/v5/install)"\nfi')

    print("[davrOS]: stage 2.3: configuring hyprland")

    run('if command -v curl >/dev/null 2>&1; then\n  curl -fsSL https://raw.githubusercontent.com/yuckdevchan/davrOS/main/custom/config/hypr/hyprland.conf\nelse\n  wget -O- https://raw.githubusercontent.com/yuckdevchan/davrOS/main/custom/config/hypr/hyprland.conf\nfi')

    run("mkdir ~/.config/hypr")
    run("mv hyprland.conf ~/.config/hypr/hyprland.conf")

    print("[davrOS]: stage 2.4: configuring neofetch")

    run("wget -O- https://raw.githubusercontent.com/yuckdevchan/davrOS/main/custom/config/neofetch/config.conf")
    run("rm -rf ~/.config/neofetch")
    run("mkdir ~/.config/neofetch")
    run("mv config.conf ~/.config/neofetch/config.conf")

    print("[davrOS]: stage 3.0: system config")
    print("[davrOS]: stage 3.1: display manager / login manager")

    display_managers = {
            "sddm": "Recommended", 
            "lightdm": None, 
            "ly": "not recommended", 
            "None": None
        }

    dm_number = 0

    for dm in display_managers.keys():
        v_comment = ""
        if display_managers[dm] == None:
            v_comment = ""
        else:
            v_comment = f"- {display_managers[dm]}"
        dm_number = dm_number + 1
        print(f"{str(dm_number)}: {dm} {v_comment}")

stage_0()
stage_1()
stage_2()
stage_2_1()

