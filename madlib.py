"""
This code generates a madlibs story from user input.
CREDIT to https://www.madtakes.com/libs/187.html for story.
by Gabriel Lee.
"""

# Blocks of story
letterFromCamp_story = [
                        'Dear ',
                        '\nI am having a(n) ',
                        ' time at camp. The counselor is ',
                        ' and the food is ',
                        '.I met ',
                        ' and we became ',
                        ' friend. Unfortunately, '
                        ' is ',
                        ' and I ',
                        ' my ',
                        ' so we could not go ',
                        ' like everybody else. I need more ',
                        ' and a ',
                        ' sharpener, so please ',
                        ' ',
                        ' more when you ',
                        ' back.'
                        ]
# Required words for story
letterFromCamp_words = [
                        'RELATIVE',
                        'ADJECTIVE',
                        'ADJECTIVE',
                        'ADJECTIVE',
                        'NAME OF PERSON IN ROOM',
                        'ADJECTIVE',
                        'ADJECTIVE',
                        'VERB ENDING IN "ED"',
                        'BODY PART',
                        'VERB ENDING IN "ING"',
                        'NOUN (PLURAL)',
                        'NOUN',
                        'ADVERB',
                        'VERB',
                        'VERB',
                        ]


# Letter from Camp madlibs execution code
def playLetterFromCamp():

    # gets words from user. returns in a list.
    def getUserInput():
        letterFromCamp_userInput = []
        for i in range(len(letterFromCamp_words)):
            userInput = input(
                "Provide one " + letterFromCamp_words[i] + ": "
            )
            # creates a list of user inputted words. Entry for every word
            # required
            letterFromCamp_userInput.append(userInput)
        return letterFromCamp_userInput

    # prints blocks of story with user inputted words slotted inbetween
    def printStory(userInput):
        print("\nWord input done. Generating story...\n\n")
        for i in range(len(letterFromCamp_story)):
            print(letterFromCamp_story[i], end="")
            pass
            # stops from printing an extra word after the last line of story
            if i != (len(letterFromCamp_story) - 1):
                print(userInput[i], end="")

    # prints story from user input
    printStory(getUserInput())
    print("\n")


# MAIN
playLetterFromCamp()
