import random

pet_name = input("Wha would you like to name your pet?")
hunger = 50
happiness = 50
energy = 50
alive = True
day = 1

print(f"\n Welcome! {pet_name} is now your virtual pet!")

while alive:
print("\n" + "=" * 30)
print(f"      Day:{day} : {pet_name})
print("=" * 30)
  print(f"Hunger:   {hunger}/100")
    print(f"Energy:   {energy}/100")
    print(f"Happiness:{happiness}/100")

    print("\nWhat would you like to do?")
    print("1. Feed your pet")
    print("2. Play with your pet")
    print("3. Let your pet sleep")
    print("4. Check your pet's mood")
    print("5. Quit game")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        hunger = max(0, hunger - 25)
        happiness = min(100, happiness + 5)
        energy = max(0, energy - 5)
        print(f"\nYum! {pet_name} enjoyed the food!")

    elif choice == "2":
        if energy < 15:
            print(f"\n{pet_name} is too tired to play!")
        else:
            happiness = min(100, happiness + 20)
            energy = max(0, energy - 15)
            hunger = min(100, hunger + 10)
            print(f"\n{pet_name} had so much fun!")

    elif choice == "3":
        energy = min(100, energy + 30)
        hunger = min(100, hunger + 10)
        print(f"\n{pet_name} took a lovely nap!")

    elif choice == "4":
        if hunger >= 75:
            print(f"\n{pet_name} is very hungry. Feed them!")
        elif energy <= 20:
            print(f"\n{pet_name} is exhausted. Let them sleep!")
        elif happiness <= 20:
            print(f"\n{pet_name} feels lonely. Play together!")
        else:
            print(f"\n{pet_name} is doing well and loves you!")

    elif choice == "5":
        print(f"\nGoodbye! Take care of {pet_name}!")
        break

    else:
        print("\nInvalid choice. Please enter a number from 1 to 5.")
        continue

    # Time passes after every successful action
    hunger = min(100, hunger + 5)
    energy = max(0, energy - 3)
    happiness = max(0, happiness - 2)

    # Random little events
    if random.random() < 0.25:
        event = random.choice([
            "found a toy",
            "saw a butterfly",
            "had a little adventure"
        ])
        happiness = min(100, happiness + 5)
        print(f"\nSurprise! {pet_name} {event}!")

    # Check whether your pet needs urgent care
    if hunger >= 100 or energy <= 0 or happiness <= 0:
        print(f"\nOh no! {pet_name} needs urgent care.")
        print("Game over! Try taking better care of your pet.")
        alive = False

    day += 1

print("\nThanks for playing Virtual Pet!")

