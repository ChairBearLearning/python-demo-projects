import random

code = ['python', 'javacript', 'cypress', 'selenium', 'html', 'php', 'c sharp', 'phpunit']
domestic_pets = ['puppies', 'kittens', 'rabbits', 'birds', 'rodents', 'fish']
farm_animals = ['cows', 'sheep', 'horses', 'chickens', 'pigs']
electrical_appliances = ['laptops', 'computers', 'kettles', 'washing machine', 'oven', 'refrigerator', 'freezer', 'airfryer']

def randomise_mode():
 # list of available subjects and their corresponding lists
    list_options = {
        'Code': code,
        'Domestic Pets': domestic_pets,
        'Farm Animals': farm_animals,
        'Electrical Appliances': electrical_appliances
    }
    # randomly choose one of the subjects
    subject = random.choice(list(list_options.keys()))  # choose the subject name
    print(f"Randomized Subject: {subject}")
    return list_options[subject]  # return the list of words from the chosen subject

def play_game(list):
    chosen_word = random.choice(list)
    word_display = ['_' for _ in chosen_word] # "hide" letters in picked word
    attempts = 8
    # while attempts are still remaining and there are _ left in the word display
    while attempts > 0 and '_' in word_display:
        print("\n" + " ".join(word_display))
        # always convert user input as case sensitive
        guess = input("Guess a letter: ").lower()
        if guess in chosen_word:
            # we now need to replace where the letter appears in that 'hidden' underscore with the actual letter
            # enumerate here gives us access to the matching letters and their index in our chosen word to be able to 'reveal' them
            # for example in python, the letter 'p' is index 0, in second loop, letter 'y' is index 1
            for index, letter in enumerate(chosen_word):
                if letter == guess:
                    #replace index with letter to 'reveal' it
                    word_display[index] = guess
        else:
            print('Try again!')
            attempts -=1
            print(f'Attempts remaining: {attempts}')
    #end
    if "_" not in word_display:
        print(f"You guessed the word: {chosen_word}")
        completed_in = str(8 - attempts)
        print(f"You used {completed_in} attempts up to win!")
    else:
        print(f"You ran out of attempts! The word was {chosen_word}")

print("\nWhat subject would you like to play with?")
print("1. Code")
print("2. Domestic Pets")
print("3. Farm Animals")
print("4. Electrical Appliances")
print("5. Randomise Mode. This mode will pick a subject at random")
print("6. Exit")

try:
   choice = int(input("Enter your choice (1-6): "))
   if choice == 1:
      play_game(code)
   elif choice == 2:
      play_game(domestic_pets)
   elif choice == 3:
      play_game(farm_animals)
   elif choice == 4:
      play_game(electrical_appliances)
   elif choice == 5:
      random_game = randomise_mode()
      play_game(random_game)
   elif choice == 6:
      print("Goodbye! Thanks for running this demo")
   else:
      print("Invalid choice. Please enter a number from 1 to 6.")
except NameError:
            print("Only numbers accepted")
except ValueError:
            print("Only numbers accepted")
