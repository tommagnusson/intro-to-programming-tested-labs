
emotions = ['anger','disgust','fear','happiness','sadness','surprise']

interactions = ['reward','punish','threaten','joke']

newEmotions = [
    [5, 0, 0, 5], # anger
    [5, 4, 2, 0], # disgust
    [5, 2, 2, 3], # fear
    [3, 4, 2, 3], # happiness
    [5, 0, 2, 3], # sadness
    [3, 4, 2, 3]  # surprise
]

# Starts out happy
currentEmotion = 3

def showEmotion(emotionIndex):
    print(f'I have the emotion {emotions[emotionIndex]}.')


def introduce():
    print('I\'m an AI with emotions. Interact with me to change my emotions!')
    showEmotion(currentEmotion)
    pass

def loop():
    while True:
        interaction = getInteraction()
        if interaction == -1:
            break
        emotion = lookupEmotion(currentEmotion, interaction)
        showEmotion(emotion)

    print('Bye.')


def main():
    introduce()
    loop()

# Get the mode of interaction from the user
# Params: none
# Returns: an integer indicating one of reward, punish, joke, or threaten
def getInteraction():
    interaction = input(f'Type in one of the following interactions: { ", ".join(interactions) } or q to quit.')
    if interaction.startswith('q'):
        return -1

    print(f'You {interaction} me...')
    indexByInteraction = {k: v for v, k in enumerate(interactions)} # TODO: memoize, only one computation necessary
    return indexByInteraction[interaction]

# TODO: do we really need a separate function for this? Refactor opportunity
def lookupEmotion(currEmotion, userAction):
    return newEmotions[currEmotion][userAction]

if __name__ == "__main__":
    main()
