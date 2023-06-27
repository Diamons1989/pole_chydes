import random


words = ["магазин", "банан", "напої", "дерево"]
random_word = random.choice(words)
max_attempts = int(input("Введіть кількість спроб: "))
attempts = 0
guessed = False
hidden_word = "*" * len(random_word)


while attempts < max_attempts and not guessed:
    guess = input("Введіть літеру або слово: ")
    if guess == random_word:
        print("Вітаю, ви вгадали слово!")
        guessed = True
    elif len(guess) == 1 and guess.isalpha():
        if guess in random_word:
            for i in range(len(random_word)):
                if random_word[i] == guess:
                    hidden_word = hidden_word[:i] + guess + hidden_word[i + 1:]
            print(hidden_word)
        else:
            print("Такої літери немає")
    else:
        print("Спробуйте ще раз!")
    attempts += 1
if not guessed:
    print("Ви програли! Загадане слово було:", random_word)
