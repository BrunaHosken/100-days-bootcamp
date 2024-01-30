#mail merge

PLACEHOLDER = "[name]"

with open("./mail_merge_files/input/letters/starting_letter.txt") as file:
    starting_letter = file.read()

with open("./mail_merge_files/input/names/invited_names.txt") as file:
    invited_names = file.readlines()

    for name in invited_names:
        final_name = name.strip()
        letter = starting_letter.replace(PLACEHOLDER, final_name)
        with open(f"./mail_merge_files/output/ready_to_send/letter_for_{final_name}.txt", mode="w") as file:
            file.write(f"{letter}")