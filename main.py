import random
import hangman_art
import hangman_words


print(hangman_art.logo)

chosen_word=random.choice(hangman_words.words)
word_length=len(chosen_word)

# 'display' will show the number of blanks
display=[]
for letter in chosen_word:
    display.append("_")

lives=6
end_of_game=False
letter_present=False

while not end_of_game:
    guess= input("Guess a letter : ").lower()
    
    if guess in display:
      print(f"{guess} already guessed!")

    for position in range(word_length):
        letter=chosen_word[position]

        if letter==guess:
            display[position]=letter
            letter_present=True
    
    
    if letter_present==False:
        lives-=1
        if lives==0:
            print("You lose, better luck next time!")
            # print(stages[0])
            end_of_game=True
    letter_present=False
    # joining all the words in display
    print(f"{' '.join(display)}")

    if '_' not in display:
        end_of_game=True
        print("You win!")
        
    if lives !=6:
        print(hangman_art.stages[lives])

        


