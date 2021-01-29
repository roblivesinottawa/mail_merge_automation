PLACEHOLDER = "[name]"

# open the letter with the names and use readlines to see the names as a list
with open("names/invited_names.txt") as names_invited:
    names = names_invited.readlines()
    # print(names)

# open the letter and loop through the names 

with open("letter/starting_letter.txt") as  start_letter:
    content = start_letter.read()
    for name in names:
        # strip removes the blank spaces between strings
        stripped_name = name.strip()
        # replace something in the content of letter
        new_letter = content.replace(PLACEHOLDER, stripped_name)
        with open(f"output/invite_for{stripped_name}", mode="w") as invitation:
            invitation.write(new_letter)