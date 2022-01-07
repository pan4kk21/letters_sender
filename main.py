with open("Input/Names/invited_names.txt") as data:
    names = data.readlines()

for name in names:
    with open("Input/Letters/starting_letter.txt") as data:
        example = data.read().replace("[name]", name.strip())
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as data2:
            data2.write(example)
