from pakudex import Pakudex

def menu():
    print()
    print("Pakudex Main Menu")
    print("-----------------")
    print("1. List Pakuri")
    print("2. Show Pakuri")
    print("3. Add Pakuri")
    print("4. Evolve Pakuri")
    print("5. Sort Pakuri")
    print("6. Exit")
    print()

def main():
    print("Welcome to Pakudex: Tracker Extraordinaire!")

    while True:
        capacity = input("Enter max capacity of the Pakudex: ")

        if capacity.isdigit():
            capacity = int(capacity)
            pakudex = Pakudex(capacity)
            print(f"The Pakudex can hold {pakudex.get_capacity()} species of Pakuri.")
            break
        else:
            print("Please enter a valid size.")


    while True:
        menu()

        user_choice = input("What would you like to do? ")

        if user_choice == "1": #lists all pakuri in pakudex
            if pakudex.get_size() == 0:
                print("No Pakuri in Pakudex yet!")
            else:
                print("Pakuri In Pakudex: ")
                for index, species in enumerate(pakudex.get_species_array(), start=1):
                    print(f"{index}. {species}")

        elif user_choice == "2": #shows stats about inputted pakuri
            species = input("Enter the name of the species to display: ")
            stats = pakudex.get_stats(species)

            if stats:
                print()
                print(f"Species: {species}")
                print(f"Attack: {stats[0]}")
                print(f"Defense: {stats[1]}")
                print(f"Speed: {stats[2]}")
            else:
                print("Error: No such Pakuri!")

        elif user_choice == "3": #adds inputted pakuri to pakudex
            if pakudex.get_size() >= capacity:
                print("Error: Pakudex is full!")
                continue

            species = input("Enter the name of the species to add: ")
            if species not in [p.get_species() for p in pakudex.pakuri_list]:
                pakudex.add_pakuri(species)
                print(f"Pakuri species {species} successfully added!")
            else:
                print("Error: Pakudex already contains this species!")

        elif user_choice == "4": #evolves the inputted pakuri from pakudex
            species = input("Enter the name of the species to evolve: ")

            if species in [p.get_species() for p in pakudex.pakuri_list]:
                pakudex.evolve_species(species)
                print(f"{species} has evolved!")
            else:
                print("Error: No such Pakuri!")

        elif user_choice == "5": #sorts the pakuri
            pakudex.sort_pakuri()
            print("Pakuri have been sorted!")

        elif user_choice == "6": #closes the program
            print("Thanks for using Pakudex! Bye!")
            quit()

        else: #invalid input error message
            print("Unrecognized menu selection!")

if __name__ == '__main__':
    main()