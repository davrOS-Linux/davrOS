display_managers = {
    "sddm": "Recommended",
    "lightdm": None,
    "ly": "not recommended",
    "No Display Manager": None
}

dm_number = 0
display_manager_choices = []

for dm in display_managers.keys():
    v_comment = ""
    if display_managers[dm] == None:
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

print(f"chosen display manager: {chosen_display_manager}")
