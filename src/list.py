from french_list_thing import fr_list_thing
from english_list_thing import en_list_thing

language = ""

f = open("list_thing_language.txt", "r")
for x in f:
    x.rstrip()
    x.lstrip()
    language = x
f.close()

if language == "english" or language == "anglais":
    language = input("What language do you want to use this program in? English or French: ")
    language = language.lower()
    if language == "english":
        f = open("list_thing_language.txt", "w")
        f.write(language)
        en_list_thing()
    elif language == "french":
        f = open("list_thing_language.txt", "w")
        f.write(language)
        fr_list_thing()
elif language == "french" or language == "français":
    language = input("Dans quelle langue voulez-vous utiliser ce programme? anglais ou français: ")
    language = language.lower()
    if language == "français":
        f = open("list_thing_language.txt", "w")
        f.write(language)
        fr_list_thing()
    elif language == "anglais":
        f = open("list_thing_language.txt", "w")
        f.write(language)
        en_list_thing()
