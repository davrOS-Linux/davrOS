from bash import run

def config_dirs(config_dirs_list, chosen_username):
    for config_dir_item in config_dirs_list:
        run(f"mv {config_dir_item} /home/{chosen_username}")
