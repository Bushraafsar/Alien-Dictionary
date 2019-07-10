# PYTHON ASSIGNMENT:
#ALIEN TASK:
# Python Program that display meaning of word said by alien in English Language:
# Python Program that display meaning of word said  by human in alien language:
alien_dictionary ={
    "hi" : "ha",
    "are" : "ary",
    "you" : "yaa",
    "destroying" : "doodoo",
    "earth" : "ee",
    "what" : "woe",
    "do" : "da",
    "want" : "wanna",
    "revenge" : "reve",
    "from" : "far",
    "take" : "hake",
    "to" : "tu",
    "we" : "woe"


}
human_dictionary = {
    "woe" : "we",
    "ary" : "are",
    "he" : "here",
    "tu" : "to",
    "hake" : "take",
    "reve" : "revenge",
    "far" : "from",
    "yaa" : "you",
    "ha" : "hi",
    "wo" : "who",
    "da" : "do",
    "wanna" : "want",
    "woe" : "what"

}
print("====================  ENGLISH /  ALIEN  TRANSLATOR=========================")
while True:
    print("SELECT ANY ONE OPTION :")
    print("Enter 1 if you wanna know the meaning of word in english language!")
    print("Enter 2 if you wanna add new word in english dictionary!")
    print("Enter 3 if you wanna know the meaning of word in alien language:")
    print("Enter 4 if you wanna add new word in alien dictionary!")
    print("Enter 5 to exit!")
    choice = int(input("Enter your choice:"))
    if choice == 1:  
        alien_input = input("Enter the word you wanna change in english language:")
        try:
           for word,values in human_dictionary.items():
                if word == alien_input:
                    print("The meaning of this word in alien language is:",values)
        except:
            print("This word currently doesn't exist is our dictionary!")
    if choice == 2:
        new_word = input("Enter the word you want to Add in human dictionary!")
        human_dictionary[new_word] = input("Enter the meaning of this word which doesn't exist before!")
        print(human_dictionary)
    if choice == 3:  
        human_input = input("Enter the word you wanna change in alien language:")
        try:
            for word,values in alien_dictionary.items():
                if word == human_input:
                    print("the meaning of this word in alien language is:",values)
        except:
            print("This word currently doesn't exist is our dictionary!!")
    if choice == 4:
        new_word = input("Enter the word you wanna add in alien dictionary:")
        alien_dictionary[word] = input("Enter the meaning of this word which doesn't exist before!!")
        print(alien_dictionary)
    if choice == 5:
        break    
 








        


     
