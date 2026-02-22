Userinput = input("Scrivi cosa vuoi fare col mio emulatore: ")

if Userinput.find("manda") != -1:
    split1 = Userinput.split("manda(")[1]
    split2 = split1.split(")")[0]
    
    print("sono riuscito a mandare quello che volevi!")
    print(split2)
    
elif Userinput.find("somma") != 1:
    split1 = Userinput.split("somma(")[1]
    split2 = split1.split(")")[0]
    split3 = split2.split("+")
    result = 0
    
    print("sono riuscito a calcolare quello che volevi!")
    
    for string in split3:
        number = int(string)
        result+=number
    print("risultato: "+result)
elif Userinput.find("/aiuto"):
    print(" Esistono attualmente 2 commandi: manda() e somma() ")
    print("manda(): richiede 1 argomento, una stringa, scrivici dentro il testo da mandare all'output")
    print("somma(): richiede 1 argomento, la somma di 2 o più numeri.")
    
else:
    print("il commando non esiste nel mio terminale.")
    print("chiudi il programma, riaprilo e scrivi /aiuto per sapere i commandi esistenti!")
