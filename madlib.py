
# CREDIT to https://www.madtakes.com/libs/187.html for story
letterFromCamp_story = [
                        'Dear ',
                        'I am having a(n) ',
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
                        ' more when you ',
                        ' back.'
                        ]
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


# Letter from Camp
def playLetterFromCamp():

    def getUserInput():
        for x in letterFromCamp_words:
            print("\nProvide one " + letterFromCamp_words[x] + ": ")
            userInput = raw_input()
            letterFromCamp_userInput = []
            letterFromCamp_userInput.append(userInput)
            return letterFromCamp_userInput

    def printStory(userInput):
        print("\nWord input done. Generating story...\n\n")
        for x in letterFromCamp_story:
            print(letterFromCamp_story[int(x)]
            # Stops from printing an extra word after the last line of story
            if x != len(letterFromCamp_story):
                print(userInput[x])

    # Executes both methods
    printStory(getUserInput())


# MAIN
playLetterFromCamp()
