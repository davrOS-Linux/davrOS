from modules.bash import run
from modules.config import config_dirs
from modules.display_manager import set_display_manager

# Function for running shell commands

def stage_0():
    run("SUDO=''\nif (( $EUID != 0 )); then\n    SUDO='sudo'\nfi")

    print("[davrOS]: stage 0: Repository Configuration")

    # add chaotic aur (because why not, right?... right?)
    run("pacman-key --recv-key FBA220DFC880C036 --keyserver keyserver.ubuntu.com")
    run("pacman-key --lsign-key FBA220DFC880C036")
    run("pacman -U 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-keyring.pkg.tar.zst' "
        "'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-mirrorlist.pkg.tar.zst'")
    run('echo "[chaotic-aur]\nInclude = /etc/pacman.d/chaotic-mirrorlist " >> /etc/pacman.conf')


def stage_1():
    print("[davrOS]: stage 1: Package Installation")

    # install all the packages listed in the pkg.txt file using pacman
    run("pacman -Syyu --needed - < pkg.txt")

    # install some stuff from the aur using paru
    run("paru -Su eww")


def stage_2():
    print("[davrOS]: stage 2: Configuration")
    run("mkdir ~/.config")
    username = input("Please enter your user account that you will be using: ")
    print("chosen username: ")

    steam = None

    while steam is None:
        steam = input("Would you like to use Steam? (y, n) ")
        if steam == "y":
            steam = True
        elif steam == "n":
            steam = False
        else:
            steam = None
            print("Error: Invalid Choice")

    deck = None

    while deck is None:
        deck = input(
            "Are you using a Steam Deck? (This option determines if steam shortcuts are placed if steam gets "
            "installed and also installs necessary software and drivers for the Steam Deck hardware.) (y, n) ")
        if deck == "y":
            deck = True
            print("deck: True")
        elif deck == "n":
            deck = False
            print("deck: False")
        else:
            deck = None
            print("Error: Invalid Choice")
    return username

    chimera = None

    while chimera == None:
        chimera = input("Would you like Chimera installed? Allows you to remotely install games through a Web UI. (y, n)")
        if chimera == "y":
            chimera = True
            print("chimera: True")
            run("paru -S chimera")
        elif chimera == "n":
            chimera = False
            print("chimera: False")
        else:
            chimera = None
            print("Error: Invalid Choice")
        return chimera

    emudeck = None

    while emudeck == None:
        emudeck = input("Would you like Emudeck? If yes, the installer will be placed on your Desktop. (y, n)")
        if emudeck == "y":
            emudeck = True
            print("emudeck: True")
        elif emudeck == "n":
            print("emudeck: False")
        else:
            emudeck = None
            print("Error: Invalid Choice")
        return emudeck

def stage_2_1(username, emudeck):
    print("[davrOS]: stage 2.1: Configuring neovim")

    # install NvChad (because its epic)
    run("git clone https://github.com/NvChad/NvChad ~/.config/nvim --depth 1 && nvim")
    print("[davrOS]: stage 2.2: configuring zsh")

    # install zsh4humans (because its epic)
    run('if command -v curl >/dev/null 2>&1; then\n  sh -c "$(curl -fsSL '
        'https://raw.githubusercontent.com/romkatv/zsh4humans/v5/install)"\nelse\n  sh -c "$(wget -O- '
        'https://raw.githubusercontent.com/romkatv/zsh4humans/v5/install)"\nfi')

    print("[davrOS]: stage 2.3: configuring hyprland")

    run('if command -v curl >/dev/null 2>&1; then\n  curl -fsSL '
        'https://raw.githubusercontent.com/yuckdevchan/davrOS/main/custom/config/hypr/hyprland.conf\nelse\n  wget -O- '
        'https://raw.githubusercontent.com/yuckdevchan/davrOS/main/custom/config/hypr/hyprland.conf\nfi')

    run("mkdir ~/.config/hypr")
    run("mv hyprland.conf ~/.config/hypr/hyprland.conf")

    print("[davrOS]: stage 2.4: configuring neofetch")

    run("wget -O- https://raw.githubusercontent.com/yuckdevchan/davrOS/main/custom/config/neofetch/config.conf")
    run("rm -rf ~/.config/neofetch")
    run("mkdir ~/.config/neofetch")
    run("mv config.conf ~/.config/neofetch/config.conf")

    print("[davrOS]: stage 3.0: system config")
    print("[davrOS]: stage 3.1: display manager / login manager")

    # Modular display manager management - adding a new one is easy.
    # All you have to do is add another item with the arch linux package name.
    display_managers = {
        "sddm": "Recommended, works well with NVIDIA GPUs. Designed for KDE.",
        "lightdm": "Works well with NVIDIA GPUs. Very lightweight.",
        "ly": "not recommended - Not supported for usage with Hyprland.",
        "gdm": "Does not work with NVIDIA GPUs. Designed for GNOME.",
        "No Display Manager": None
    }

    dm_number = 0
    display_manager_choices = []

    for dm in display_managers.keys():
        if display_managers[dm] is None:
            v_comment = ""
        else:
            v_comment = f"- {display_managers[dm]}"
        dm_number = dm_number + 1
        print(f"{str(dm_number)}: {dm} {v_comment}")
        display_manager_choices.append(str(dm_number))

    chosen_display_manager = None

    while chosen_display_manager not in display_manager_choices:
        chosen_display_manager = input("[davrOS]: Chose a Display Manager: ")
        if chosen_display_manager not in display_manager_choices:
            print("[davrOS]: error: Invalid Choice")

    print(f"Chosen display manager: {chosen_display_manager}")
    set_display_manager(chosen_display_manager)

    config_dirs_list = [
        "~/.config/zsh",
        "~/.config/hyprland",
        "~/.config/nvim",
        "~/.config/neofetch"
    ]

    config_dirs(config_dirs_list, username, emudeck)
