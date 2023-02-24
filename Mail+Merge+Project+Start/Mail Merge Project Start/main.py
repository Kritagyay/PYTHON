with open ("/Users/hp/PycharmProjects/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt") as people:
    list_people=people.readlines()


with open ("./Input/Letters/starting_letter.txt") as letter:
    letter_content=letter.read()
    for i in list_people:
        changed_name=i.strip()
        new_letter=letter_content.replace("[name]",changed_name)
        with open (f"./Output/ReadyToSend/letter_for_{changed_name}.txt",mode='w') as final_letter:
            final_letter.write(new_letter)
