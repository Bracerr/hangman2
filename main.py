from random import choice

HANGMAN = (
    """
     ------
     |    |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |    |
     | 
     |   
     |    
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   
     |   
     |     
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |   
     |    
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |   
     |   
    ----------
    """
)

max_wrong = len(HANGMAN) - 1
WORDS = ("пососи", "пиздец", "гавноу")

word = choice(WORDS)
so_far = "_" * len(word)
wrong = 0
used = []

while wrong < max_wrong and so_far != word:
    print(f"{HANGMAN[wrong]}")
    print(f"Слово - {so_far}")
    print(f"Оставшееся колличество попыток - {max_wrong - wrong}")
    a = input("Введите вашу букву: ")

    while a in used:
        print("Вы уже вводили букву", a)
        a = input("Введите свое предположение: ")

    used.append(a)
    if a in word:
        new = ''
        print(f"\nВы угадали букву {a}!")
        for i in range(len(word)):
            if a == word[i]:
                new += a
            else:
                new += so_far[i]
        so_far = new
    else:
        print(f'\nБуквы {a} не было в слове :(')
        wrong += 1

print("-"*45)
if wrong == max_wrong:
    print(f"\nВы проиграли. Загаданное слово было: {word}")
else:
    print("\nПоздравляю! Вы выиграли! ^_^")
