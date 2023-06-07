from coffeBrewRankB import Database

db = Database()

def menu():

    while (userInput:=input(menuPrompt)) != "5":
        if userInput == "1":
            addranking()
        elif userInput == "2":
            seeAll()
        elif userInput == "3":
            findBYName()
        elif userInput == "4":
            bestMethod()
        else:
            print("\nInvalid input, please try again!")

menuPrompt = """--- Coffe Ranking App ---

Please choose one of these options:

1) Add a new ranking.
2) See all ranking.
3) Find a ranking by name.
4) See which preperation method is best.
5) Exit.
Your selection: """

def addranking():
    name = input("Enter coffe name: ")
    method = input("Enter how you've prepared it: ")
    rating = int(input("Enter your rating score (0-100): "))

    db.addRow(name, method, rating)

def seeAll():
    rankings = db.getAll()

    for ranking in rankings:
        print(f"{ranking[1]} ({ranking[2]}) - {ranking[3]}/100")

def findBYName():
    name = input("Enter coffe name: ")

    rankings = db.getbyname(name)
    for ranking in rankings:
        print(f"{ranking[1]} ({ranking[2]}) - {ranking[3]}/100")

def bestMethod():
    name = input("Enter coffe name: ")

    bestMethod = db.getBestPrep(name)
    print(f"The Best preparation method for {name} is {bestMethod[2]}")

menu()