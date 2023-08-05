from bash import run


def config_dirs(config_dirs_list, username, emudeck):
    for config_dir_item in config_dirs_list:
        run(f"mv {config_dir_item} /home/{username}")

    if emudeck:
        print("[davrOS]: Installing Emudeck")
        run('wget "https://www.emudeck.com/EmuDeck.desktop"')
        run(f"mkdir /home/{username}/Desktop")
        run(f"mv EmuDeck.desktop /home/{username}/Desktop")
