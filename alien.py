# PYTHON ASSIGNMENT:
#ALIEN TASK:
# Python Program that display meaning of word said by alien in English Language:
# Python Program that display meaning of word said  by human in alien language:
import json
print("====================  ENGLISH /  ALIEN  TRANSLATOR=========================")
while True:
    print("SELECT ANY ONE OPTION :")
    print("Enter 1 if you wanna know the meaning of word in english language!")
    print("Enter 2 if you wanna add new word in english dictionary!")
    print("Enter 3 if you wanna know the meaning of word in alien language:")
    print("Enter 4 if you wanna add new word in alien dictionary!")
    print("Enter 5 to exist!")
    choice = int(input("Enter your choice:"))
    if choice == 1:  
        alien_input = input("Enter the word you wanna change in english language:")
        alien_input = alien_input.lower()
        with open("data1.json")as f:
            hd = json.load(f)
        try:
            for keys,values in hd.items():
                if keys == alien_input:
                    print("The meaning of this word in alien language is:",values) 
        except:
            print("This word doesn't exist in our dictionary!")     
    elif choice == 2:
        new_word = input("Enter the word you want to Add in human dictionary!")
        with open("data.json")as f:
            human_dictionary = json.load(f)
        human_dictionary[new_word] = input("Enter the meaning of this word which doesn't exist before!")
        print(human_dictionary)
    elif choice == 3:  
        human_input = input("Enter the word you wanna change in alien language:")
        human_input = human_input.lower()
        with open("data.json")as f:
            alien_dictionary = json.load(f)
        try:
            for word,values in alien_dictionary.items():
                if word == human_input:
                    print("the meaning of this word in alien language is:",values)
        except:
                print("This word currently doesn't exist is our dictionary!!")
    elif choice == 4:
        new_word = input("Enter the word you wanna add in alien dictionary:")
        with open("data1.json")as f:
            alien_dictionary = json.load(f) 
        alien_dictionary[word] = input("Enter the meaning of this word which doesn't exist before!!")
        print(alien_dictionary)
    elif choice == 5:
        break  
    else:
        print("You enter wrong number!")      
 








        


     
