PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as names:
    names_list = names.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    read_letter = letter.read()
    for name in names_list:
        new_letter = read_letter.replace(PLACEHOLDER, name)
        print(new_letter)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as invitation:
            invitation.write(new_letter)
        # with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as invitation:
        # 	invitation.write(new_letter)

