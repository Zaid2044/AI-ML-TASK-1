import random

class pet:
  def __init__(self, name, species, age):
    self.name = name
    self.species = species
    self.age = age
    
  def display_info(self):
    print(f"  Name: {self.name}")
    print(f"  Species: {self.species}")
    print(f"  Age: {self.age} year(s) old")


class Dog(pet):
  def __init__(self, name, age, breed):
    super().__init__(name, "Dog", age)
    self.breed = breed

  def display_info(self):
    super().display_info()
    print(f"  Breed: {self.breed}")


class Cat(pet):
  def __init__(self, name, age, breed):
    super().__init__(name, "Cat", age)
    self.breed = breed

  def display_info(self):
    super().display_info()
    print(f"  Breed: {self.breed}")




available_pets = {}
pet_preferences = {
    "Dog": ("Likes Bones", "Needs Regular Walks", "Enjoys Fetch"),
    "Cat": ("Likes Tuna", "Enjoys Napping in Sunbeams", "Prefers a Clean Litter Box")}

def generate_unique_id():
  while True:
    pet_id = random.randint(1, 99)
    if pet_id not in available_pets:
      return pet_id
    
def add_pet():
    print("\n--- Add a New Pet ---")
    while True:
        species_choice = input("Enter species (Dog/Cat): ").strip().capitalize()
        if species_choice in ["Dog", "Cat"]:
            break
        else:
            print("Invalid species. Please enter 'Dog' or 'Cat'.")

    while True:
            name = input("Enter pet's name: ").strip()
            age = int(input("Enter pet's age (years): "))
            if age < 0:
                print("Age cannot be negative.")
            break

    new_pet = None

    if species_choice == "Dog":
            while True:
                breed = input("Enter dog's breed: ").strip()
                if breed:
                    new_pet = Dog(name, age, breed)
                    break
                else:
                    print("Breed cannot be empty.")
    elif species_choice == "Cat":
             while True:
                color = input("Enter cat's color: ").strip()
                if color:
                    new_pet = Cat(name, age, color)
                    break
                else:
                    print("Color cannot be empty.")

    pet_id = generate_unique_id()
    available_pets[pet_id] = new_pet
    print(f"\nSuccess! {new_pet.species} '{new_pet.name}' added with Pet ID: {pet_id}")


def view_pets():
    print("\n--- Available Pets for Adoption ---")
    if not available_pets:
        print("No pets currently available for adoption.")
        return

    for pet_id, pet_obj in available_pets.items():
        print(f"Pet ID: {pet_id}")
        pet_obj.display_info()

        species = pet_obj.species
        if species in pet_preferences:
            print("  Preferences/Notes:")
            for pref in pet_preferences[species]:
                print(f"    - {pref}")
        print("-" * 20)


def adopt_pet():
    print("\n--- Adopt a Pet ---")
    if not available_pets:
        print("No pets currently available for adoption.")
        return

    view_pets()
    while True:
            adopt_id_str = input("Enter the Pet ID of the pet you want to adopt (or 'cancel'): ").strip()
            if adopt_id_str.lower() == 'cancel':
                print("Adoption cancelled.")
                return

            adopt_id = int(adopt_id_str)
            if adopt_id in available_pets:
                adopted_pet = available_pets.pop(adopt_id)
                print(f"\nCongratulations! You have adopted {adopted_pet.species} '{adopted_pet.name}' (ID: {adopt_id}).")
                print("Please give them a loving home!")
                return
            else:
                print("Invalid Pet ID. Please choose from the list above.")


def display_menu():
    """Prints the main menu options."""
    print("\n===== Pet Adoption System Menu =====")
    print("1. View Available Pets")
    print("2. Add a New Pet")
    print("3. Adopt a Pet")
    print("4. Exit")
    print("====================================")

if __name__ == "__main__":
        dog1_id = generate_unique_id()
        available_pets[dog1_id] = Dog("Buddy", 3, "Golden Retriever")
        cat1_id = generate_unique_id()
        available_pets[cat1_id] = Cat("Whiskers", 2, "Tabby")
        dog2_id = generate_unique_id()
        available_pets[dog2_id] = Dog("Lucy", 5, "Beagle")


while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            view_pets()
        elif choice == '2':
            add_pet()
        elif choice == '3':
            adopt_pet()
        elif choice == '4':
            print("\nThank you for using the Pet Adoption System. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")

        input("\nPress Enter to continue...")
