from random import randint
import subprocess
words = ["dog", "book", "bag", "shop", "apple", "house", "library", "office", "telephone"]
random_word = words[randint(0,len(words) - 1)]
guess_word = list("_"*len(random_word))
misstakes_remain = 3
misstakes_done = 0
while True:
    print("".join(guess_word))
    print("ur chances: [%s%s]"%(misstakes_remain*"*", misstakes_done*"-"))
    guess = input("# guess: ")
    if guess in random_word:
        for i in range(len(random_word)):
            if random_word[i] is guess:
                guess_word[i] = random_word[i]
    else:
        misstakes_done += 1
        misstakes_remain -= 1
    if misstakes_done == 3:
        print("Bad lock!")
        break
    elif "_" not in "".join(guess_word):
        subprocess.call("clear")
        print("".join(guess_word))
        print("u Won!")
        break
    else:
        subprocess.call("clear")