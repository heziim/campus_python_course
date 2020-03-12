#!/opt/rh/rh-python36/root/usr/bin/python
    
def main():
    
    import os.path
    from os import path
    
    MAX_TRIES = 6
    
    HANGMAN_ASCII_ART = """
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/
    
    """
    
    HANGMAN_PHOTOS = {
        '0':  """
        x-------x""",
    
        '1': """
        x-------x
        |
        |
        |
        |
        |""",
    
        '2': """
        x-------x
        |       |
        |       0
        |
        |
        |
            """,
    
        '3': """
        x-------x
        |       |
        |       0
        |       |
        |
        |
            """,
    
        '4': """
        x-------x
        |       |
        |       0
        |      /|\\
        |
        |
            """,
    
        '5': """
        x-------x
        |       |
        |       0
        |      /|\\
        |      /
        |
            """,
    
        '6': """
        x-------x
        |       |
        |       0
        |      /|\\
        |      / \\
        |
            """,
    }
    
    
    def print_start_game():
        """Print start screen hangman, and number of max tries to guess a word, which is 6.
        """
        print(HANGMAN_ASCII_ART)
        print(MAX_TRIES)
    
    def choose_word(file_path, index):
        """Choose a word to guess in the game from a text file.
        :param file_path: text file of words delimited by space
        :param index: word location index within the file
        :type file_path: str
        :type index: str
        :return: The secret word to play with
        :rtype: str
        """
        with open(file_path, "r") as input_file:
            words = input_file.read()
            word = words.split(" ")
            last_item = ( len(word) )
            index = int(index)  
            if ( index > last_item ):
                index = ( index % last_item )
            global secret_word
            secret_word = word[index-1]
            return secret_word
    
    def check_valid_input(letter_guessed, old_letters_guessed):
        """Check that input by is one vaild letter and also not in the list of letters guessed.
        :param letter_guessed: guess input by user
        :param old_letters_guessed: list of letters that the user used
        :type letter_guessed: str
        :type old_letter_guessed: list
        :return: True if input is ok, else False
        :rtype: bool
        """
        if (len(letter_guessed) == 1) and letter_guessed.isalpha() and (letter_guessed not in old_letters_guessed):
            return True
        else:
            return False
    
    def try_update_letter_guessed(letter_guessed, old_letters_guessed):
        """Add letters that guessed to the old letters list.
        :param letter_guessed: guess input by user
        :param old_letters_guessed: list of letters that the user used
        :type letter_guessed: str
        :type old_letter_guessed: list
        :return: True if letter is vaild, False if letter not vaild or has been guessed
        :rtype: bool
        """
        if check_valid_input(letter_guessed, old_letters_guessed):
            old_letters_guessed.append(letter_guessed)
            return True 
        else:
            print('X')
            old_letters_guessed.sort()
            updated_str_old_letters_guessed = " -> ".join(old_letters_guessed)
            print(updated_str_old_letters_guessed.lower())
            return False 
    
    def show_hidden_word(secret_word, old_letters_guessed):
        """Show the hidden word status.
        :param secret_word: word to play with 
        :param old_letters_guessed: list of letters that the user used
        :type secret_word: str
        :type old_letter_guessed: list
        :return: Word status, letters and _ in the right postions,
        :rtype: str
        """
        word = ""
        for i in secret_word:
            if i in old_letters_guessed:
                word = word + " " +(i)
            else:
                word = word + " _"
        return word
    
    def check_win(secret_word, old_letters_guessed):
        """Check if user win the hangman game.
        :param secret_word: word to play with 
        :param old_letters_guessed: list of letters that the user used
        :type secret_word: str
        :type old_letter_guessed: list
        :return: True if all letters that in list of letters gueessed are in secret word, else, False.
        :rtype: bool
        """
        j=len(secret_word)
        for i in secret_word:
            j -= 1
            if i in old_letters_guessed:
                if j == 0:
                    return True
                else: 
                    continue
            else:
                return False
    
    def print_hangman(num_of_tries):
        """Print the hangman picture, transfer to dict key.
        :param num_of_tries: number of try of guess
        :type num_of_tries: str
        """
        print(HANGMAN_PHOTOS[str(num_of_tries)])
    
    
    num_of_tries = 0
    old_letters_guessed = []
    letter_guessed = "$"
    file_path = "$" 
    index = "$"
    
    print_start_game()
    
    while not path.exists(file_path) or not path.isfile(file_path):
        file_path = input("Enter file path: ")
        if path.exists(file_path) and  path.isfile(file_path):
            break
        print("Please enter a vaild file name / check your typed path")
        continue
    
    while not index.isnumeric():
        index = input("Enter index: ")
        if index.isnumeric():
            break
        print("Please enter a vaild index number")
        continue
    
    print('\nLet’s start!\n')
    print_hangman(num_of_tries)
    choose_word(file_path, index)
    print('\n')
    print("_ " * len(secret_word))
    print('\n')
    
    while not check_valid_input(letter_guessed, old_letters_guessed) and ( num_of_tries < MAX_TRIES ): 
        letter_guessed = input("Guess a letter: ")
        letter_guessed = letter_guessed.lower()
        if try_update_letter_guessed(letter_guessed, old_letters_guessed):
            if (letter_guessed not in secret_word):
                print(':(') 
                num_of_tries += 1
                print_hangman(num_of_tries)   
                print(show_hidden_word(secret_word, old_letters_guessed))
                if ( num_of_tries == 6 ):
                    print('\nLOSE\n')
            elif check_win(secret_word, old_letters_guessed): 
                print(show_hidden_word(secret_word, old_letters_guessed))
                print('\nWIN\n')
                break
            else:
                print(show_hidden_word(secret_word, old_letters_guessed))
    
if __name__ == "__main__":
    main()
