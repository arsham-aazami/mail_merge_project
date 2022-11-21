PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as names:
    names_list = names.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    read_letter = letter.read()
    for name in names_list:
        striped_name = name.strip()
        new_letter = read_letter.replace(PLACEHOLDER, striped_name)
        print(new_letter)
        with open(f"./Output/ReadyToSend/letter_for_{striped_name}.txt", mode="w") as invitation:
            invitation.write(new_letter)


