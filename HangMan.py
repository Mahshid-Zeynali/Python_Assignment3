import random

words = ['book', 'tree', 'python', 'bag', 'umbrella', 'dog', 'clock', 'engineer', 'toothpaste', 'shirmoz']

# i = random.randint(0, len(words)-1)
# word = words[i]

word = random.choice(words) # clock0
len = len(word)
joon = 10

while joon > 0:
    print('- ' * len) # - - - - -

    user_character = input().lower() # s

    if user_character in word:
        word = word.replace(user_character, "")
        print('yes')

    else:
        joon = joon - 1
        print('no')

    if word == "" :
        print("You won")
        break
    
