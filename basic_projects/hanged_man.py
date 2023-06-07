import random

field = [
    "   _______   ",
    "   |    |    ",
    "   |    O    ",
    "   |  _/|\_  ",
    "   |    |    ",
    "   |  _/ \_  ",
    " __|__       "
]

categories = [
    [],
    ["table", "chair", "computer"],
    ["bee", "lion", "bear", "elephant"]
]

mistake = 0
score = 0

while True:
    print("0 => special\n1 => item\n2 => animal")
    try:
        category_index = int(input("Choose a category: "))
        category = categories[category_index]
        break
    except ValueError:
        print("Enter a number!")
    except IndexError:
        print("Invalid category!")

if category_index == 0:
    while True:
        try:
            num_special = int(input("How many words do you want to add: "))
            break
        except ValueError:
            print("Enter a number!")

    for _ in range(num_special):
        special_word = input("Word: ").strip()
        category.append(special_word)

word = random.choice(category).upper()
word_show = '#' * len(word)

print("\n\n\n\n\n\n\n\n\n\n")
print(" ".join(word_show))

showbox = ""

while True:
    guess = input("Your guess: ").upper()

    if guess in word and guess != word:
        print("\n*** Right guess! ***")
        word_show = ''.join(
            [char if char == guess or shown_char != '#' else '#' for char, shown_char in zip(word, word_show)]
        )
    else:
        mistake += 1
        for row in field[:mistake]:
            print(row)
        print(f"\n*** Wrong guess! ***")
        print(f"Remaining health: {7 - mistake}".center(10, "*"))

    if guess == word or '#' not in word_show:
        jump = word_show.count('#') + 1
        score = len(word) * (7 - mistake) * jump
        print(f"\n*** Congratulations! You won! ***")
        print(f"The word was: {word}")
        print(f"Your Score: {score}")
        break

    if len(guess) != 1:
        mistake += 1
        print(f"\n*** Wrong guess! ***")
        print(f"Remaining health: {7 - mistake}".center(10, "*"))
        if len(guess) != len(word):
            print("\nJust guess a single letter or the entire word itself!\n")
        else:
            print("\nWrong guess\n")
        continue

    if guess in showbox:
        print(f"You already guessed the letter '{guess}'!\n")
        continue

    

    showbox += guess

    if mistake == 7:
        print(f"\n*** Game Over! ***")
        print(f"The word was: {word}")
        break
    
    print(" ".join(word_show))