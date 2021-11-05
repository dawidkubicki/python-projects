# TODO: Create a letter using starting_letter.txt


def get_names():
    names = []
    with open("./Input/Names/invited_names.txt", "r") as f:
        words = f.read()
        for name in words.split():
            names.append(name)
        return names

for name in get_names():
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w+") as f:
        f.write("test")


# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
