def en_list_thing():    
    def list_cycle():
        list_number = 1
        print("\n" + list_name)
        for i in user_list:
            print(str(list_number) + ") " + i)
            list_number += 1
    
    user_list = []
    remove_index = 0
    replace_index = 0
    insert_index = 0
    show_list = "y"
    create_file = "y"
    load_file = "y"
    user_input = "yes"
    user_option = "yes"
    user_sort = "yes"
    user_find = ""
    list_name = ""
    file_list_name = ""
    replace_value = ""
    insert_value = ""
    
    while True:
        user_option = input("Options: Add values, Remove value, Replace value, Insert value, Name list, Show list, Sort list, Find in list, Delete list, Save list, Load list, Length, Preferences, Exit\nEnter one of these options here: ")
        user_option = user_option.lower()
        if user_option == "add values":
            print("Enter a value to add to your list. Press enter when the input is blank to stop adding more values.")
            while user_input != "":
                user_input = input("Enter a value: ")
                if user_input == "":
                    user_input = "yes"
                    break
                else:
                    user_list.append(user_input)
        elif user_option == "remove value":
            list_cycle()
            remove_index = int(input("Select a list number to remove: "))
            remove_index -= 1
            user_list.pop(remove_index)
            if show_list == "y":
                list_cycle()
        elif user_option == "replace value":
            list_cycle()
            replace_index = input("Select a list number to be replaced: ")
            replace_value = input("What should list number " + replace_index + " be replaced with?: ")
            replace_index = int(replace_index)
            replace_index -= 1
            user_list[replace_index] = replace_value
            if show_list == "y":
                list_cycle()
        elif user_option == "insert value":
            list_cycle()
            insert_index = input("Which list number do you want to insert a value into?: ")
            insert_value = input("What value do you want to add into list number " + insert_index + "?: ")
            insert_index = int(insert_index)
            insert_index -= 1
            user_list.insert(insert_index, insert_value)
            if show_list == "y":
                list_cycle()
        elif user_option == "name list":
            list_name = input("Enter a name for your list: ")
        elif user_option == "show list":
            list_cycle()
        elif user_option == "sort list":
            print("Sort options:")
            print("Alphanumerically ascending (uppercase priority) - AAU")
            print("Alphanumerically descending (uppercase priority) - ADU")
            print("Alphanumerically ascending (lowercase priority) - AAL")
            print("Alphanumerically descending (lowercase priority) - ADL")
            print("Use the acronym instead of the full version.")
            user_sort = input("How would you like to sort your values: ")
            user_sort = user_sort.lower()
            if user_sort == "aau":
                user_list.sort()
                if show_list == "y":
                    list_cycle()
            elif user_sort == "adu":
                user_list.sort(reverse = True)
                if show_list == "y":
                    list_cycle()
            elif user_sort == "aal":
                user_list.sort(key = str.lower)
                if show_list == "y":
                    list_cycle()
            elif user_sort == "adl":
                user_list.sort(key = str.lower, reverse = True)
                if show_list == "y":
                    list_cycle()
        elif user_option == "delete list":
            list_name = ""
            user_list.clear()
            print("List deleted.")
        elif user_option == "save list":
            create_file = input("Saving a list to this file will overwrite any existing data. Do you wish to proceed? Y or N: ")
            create_file.lower()
            if create_file == "y":
                f = open("list_file.txt", "w+")
                if not list_name:
                    list_name = input("Enter a name for your list: ")
                f.write(list_name + "\n")
                for x in user_list:
                    f.write(x + "\n")
                f.close()
                print("File saved. Reopen document to see changes.")
        elif user_option == "load list":
            if user_list:
                load_file = input("Loading the saved list will overwrite any existing values in the list in this program. Do you wish to proceed? Y or N: ")
            load_file.lower()
            if load_file == "y":
                f = open("list_file.txt", "r")
                user_list.clear()
                for x in f:
                    x = x.rstrip()
                    x = x.lstrip()
                    user_list.append(x)
                file_list_name = user_list[0]
                list_name = file_list_name
                f.close()
                print("List loaded.")
                user_list.pop(0)
        elif user_option == "length":
            if list_name == "":
                list_name == "your list"
            print("The length of " + list_name + " is " + str(len(user_list)) + " values.")
            if list_name == "your list":
                list_name = ""
        elif user_option == "preferences":
            show_list = input("Do you want your list to be shown after making changes to it (removing, sorting and replacing values)? Y or N?: ")
        elif user_option == "find in list":
            user_find = input("What would you like to find? Type in a letter, number, character, word or phrase: ")
            for x in user_list:
                if user_find in x:
                    print(x)
        elif user_option == "exit":
            break
