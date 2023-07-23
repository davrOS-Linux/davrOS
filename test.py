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
