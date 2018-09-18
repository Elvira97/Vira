# Linnea Bergman, Elvira Johansson
# Labb 3 del 2 och 3
# 12/9-2018

from bintreeFile import Bintree # Importerar bintreeFile
def main():
    with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    startord = input("vilket ord vill du starta på? ")
    slutord = input("vilket ord vill du ta dig till? ")
    makechildren(startord)

def svenska(): # Skapar ett träd med svenska ord
    svenska = Bintree()
    with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    startord = input("vilket ord vill du starta på? ")
    slutord = input("vilket ord vill du ta dig till? ")
        for rad in svenskfil:
            ordet = rad.strip()                # Ett trebokstavsord per rad
            if ordet in svenska:
                print(ordet, end = " ")
            else:
                svenska.put(ordet)             # in i sökträdet
    print("\n")

def makechildren(startord):
    
    
def gamla(): # Skapar ett träd med engelska ord
    engelska = Bintree()
    svenska = Bintree()
    with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()
            svenska.put(ordet)
    with open("engelska.txt", "r", encoding="utf-8") as engelskafil:
        for line in engelskafil:
            word = line.split(" ")
            for i in word: 
                if not i in engelska:
                    engelska.put(i)  
                    if i in svenska:
                        print(i, end = " ")
        print("\n")

def main(): # Huvudfunktionen
    svenskt_träd()
    engelskt_träd()

main()
