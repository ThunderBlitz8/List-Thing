def fr_list_thing():
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
    show_list = "o"
    create_file = "o"
    load_file = "o"
    user_input = "oui"
    user_option = "oui"
    user_sort = "oui"
    user_find = ""
    list_name = ""
    file_list_name = ""
    replace_value = ""
    insert_value = ""
    
    while True:
        user_option = input("Options: Ajouter valeurs, Supprimer valeurs, Remplacer valeur, Insérer valeur, Donner un nom à ta liste, Voir liste, Trier liste, Trouver dans liste, Supprimer liste, Sauvegarder liste, Charger liste, Taille de ta liste, Préférences, Sortir\nEntrer une de ces options ici: ")
        user_option = user_option.lower()
        if user_option == "ajouter valeurs":
            print("Entrer une valeur ajouter à ta liste. Taper ENTER quand l'input est blanc arrêter vous ajoutez plus de valeurs.")
            while user_input != "":
                user_input = input("Entrer une valeur: ")
                if user_input == "":
                    user_input = "oui"
                    break
                else:
                    user_list.append(user_input)
        elif user_option == "supprimer valeurs":
            list_cycle()
            remove_index = int(input("Sélectionner un numéro de liste supprimer: "))
            remove_index -= 1
            user_list.pop(remove_index)
            if show_list == "o":
                list_cycle()
        elif user_option == "remplacer valeur":
            list_cycle()
            replace_index = input("Sélectionner un numéro de liste remplacer: ")
            replace_value = input("Qu'est-ce que devrait numéro de liste " + replace_index + " être remplacé avec?: ")
            replace_index = int(replace_index)
            replace_index -= 1
            user_list[replace_index] = replace_value
            if show_list == "o":
                list_cycle()
        elif user_option == "insérer valeur":
            list_cycle()
            insert_index = input("Quel numéro de liste voulez-vous inserer une valeur dans?: ")
            insert_value = input("Quelle valeur voulez-vous ajouter dans numéro de liste " + insert_index + "?: ")
            insert_index = int(insert_index)
            insert_index -= 1
            user_list.insert(insert_index, insert_value)
            if show_list == "o":
                list_cycle()
        elif user_option == "donner un nom à ta liste":
            list_name = input("Entrer un nom pour ta liste: ")
        elif user_option == "voir liste":
            list_cycle()
        elif user_option == "Trier liste":
            print("Triant options:")
            print("Alphanumériquement croissant (priorité majuscule) - ACMA")
            print("Alphanumériquement décroissant (priorité majuscule) - ADMA")
            print("Alphanumériquement croissant (priorité en minuscules) - ACMI")
            print("Alphanumériquement décroissant (priorité en minuscules) - ADMI")
            print("Utiliser l'acronyme au lieu de la version complète.")
            user_sort = input("How would you like to sort your values: ")
            user_sort = user_sort.lower()
            if user_sort == "acma":
                user_list.sort()
                if show_list == "o":
                    list_cycle()
            elif user_sort == "adma":
                user_list.sort(reverse = True)
                if show_list == "o":
                    list_cycle()
            elif user_sort == "acmi":
                user_list.sort(key = str.lower)
                if show_list == "o":
                    list_cycle()
            elif user_sort == "admi":
                user_list.sort(key = str.lower, reverse = True)
                if show_list == "o":
                    list_cycle()
        elif user_option == "supprimer liste":
            list_name = ""
            user_list.clear()
            print("Liste a supprimé.")
        elif user_option == "sauvegarder liste":
            create_file = input("Sauvegardant une liste dans ce fichier écrasera toutes les valeurs existantes. Voulez-vous procéder? O ou N: ")
            create_file.lower()
            if create_file == "o":
                f = open("list_file.txt", "w+")
                if not list_name:
                    list_name = input("Entrer un nom pour ta liste: ")
                f.write(list_name + "\n")
                for x in user_list:
                    f.write(x + "\n")
                f.close()
                print("Fichier a sauvegardé. Rouvrir le fichier voir les modifications.")
        elif user_option == "charger liste":
            if user_list:
                load_file = input("Chargant le sauvegardé fichier écrasera quelconque valeurs existantes à la liste dans ce programme. Voulez-vous procéder? O ou N: ")
            load_file.lower()
            if load_file == "o":
                f = open("list_file.txt", "r")
                user_list.clear()
                for x in f:
                    x = x.rstrip()
                    x = x.lstrip()
                    user_list.append(x)
                file_list_name = user_list[0]
                list_name = file_list_name
                f.close()
                print("Liste a chargé.")
                user_list.pop(0)
        elif user_option == "taille de ta liste":
            if list_name == "":
                list_name == "ta liste"
            print("Le taille de " + list_name + " est " + str(len(user_list)) + " valeurs.")
            if list_name == "ta liste":
                list_name = ""
        elif user_option == "préférences":
            show_list = input("Voulez-vous ta liste être visible après avoir fait les modifications à lui (supprimant, triant et remplacant valeurs)? O ou N?: ")
        elif user_option == "trouver dans liste":
            user_find = input("Quel voulez-vous trouver? Entrer une lettre, une numéro, un mot ou un group de mots: ")
            for x in user_list:
                if user_find in x:
                    print(x)
        elif user_option == "sortir":
            break
