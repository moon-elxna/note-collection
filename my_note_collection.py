# first simple version

import json

print("YOUR NOTE COLLECTION")
# pull dictionary from json file
with open("my_note_collection.json", 'r') as file:
    note_collection= json.load(file)
questionA = " "
while questionA:
    #question is gonna repeat after each complete action-loop
    print("What do you want to do?")
    print("choose: [view notes], [add note], [edit notes], [add folder], [save]")
    questionA = input()

    #does add a note in the choosen nested dictionary
    while questionA == "add note" or questionA == "[add note]" or questionA == "addnote":
        note = []
        note_name = input("title of note: ")
        date_creation = input("date of creation (DD-MM-YY): ")
        note_content = input("content of note:")
        note.append(date_creation)
        note.append(note_content)
        #print keys from all nested dictionaries
        keys_with_dict_values = [key for key, value in note_collection.items() if isinstance(value, dict)]
        print("choose folder to store the note: ", keys_with_dict_values)
        #takes input and find the folder with same name
        folder = input()
        if folder in note_collection:
            note_collection[folder][note_name] = note
        break #is needed to repeat asking questionA

    #show notes which are already saved and which you added and dindt save 
    while  questionA == "view notes" or questionA == "[view notes]"or questionA == "view" or questionA == "viewnotes":
        print("choose: [all], [folder] ")
        questionB = input()
        #shows all "folders"
        if questionB == "all" or questionB == "[all]":
            print(note_collection)
        #shows choosen "folder"
        elif questionB == "folder" or questionB == "[folder]":
            #print keys from all nested dictionaries
            keys_with_dict_values = [key for key, value in note_collection.items() if isinstance(value, dict)]
            print("choose folder: ", keys_with_dict_values)
            folder = input()
            if folder in note_collection:
                print(note_collection[folder])
        break
    
    #adds a new nested dictionary as "folder" for notes
    while  questionA == "add folder" or questionA == "[add folder]" or questionA == "addfolder":
        folder_name = input("folder name: ")
        folder_content = {}
        note_collection[folder_name] = folder_content
        break

    #edit notes
    #choose folder x - print notes from chossen folder x - choose note ? - print chosen note ? - save edit as extra with editing date ?
    while  questionA == "edit notes" or questionA == "[edit notes]"or questionA == "edit" or questionA == "editnotes":
        #print keys from all nested dictionaries
        keys_with_dict_values = [key for key, value in note_collection.items() if isinstance(value, dict)]
        print("choose folder: ", keys_with_dict_values)
        folder = input()
        if folder in note_collection:
            print(note_collection[folder])
        break

    #saves the main dictionary with all notes in a json file
    #this data is going to be pulled out , next time the programm is started
    while questionA == "save" or questionA == "[save]" :
        with open("my_note_collection.json", "w") as file:
            json.dump(note_collection, file)
        print("Your notes are saved!")
        break
