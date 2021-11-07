# TODO: Create a letter using starting_letter.txt


def get_names():
    names = []
    with open("./Input/Names/invited_names.txt", "r") as f:
        words = f.read()
        for each_name in words.split():
            names.append(each_name)
        return names


def replace_text(recipient: str):
    with open("./Input/Letters/starting_letter.txt", "r") as f:
        text = f.read()
        ready_text = text.replace("[name]", recipient)
        return ready_text


for name in get_names():
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w+") as g:
        g.write(replace_text(name))

# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
