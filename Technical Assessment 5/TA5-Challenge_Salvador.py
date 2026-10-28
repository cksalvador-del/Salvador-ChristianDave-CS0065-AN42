
import string

# List of happy and sad words
happy_words = [
    "happy", "joy", "love", "great", "wonderful",
    "excellent", "excited", "smile", "glad", "beautiful",
    "amazing", "delighted", "cheerful", "fantastic"
]

sad_words = [
    "sad", "cry", "hate", "bad", "terrible",
    "angry", "upset", "lonely", "unhappy", "hurt",
    "depressed", "miserable", "disappointed", "pain"
]

# Function to count happy words
def number_happy(sentence):
    words = sentence.lower().translate(
        str.maketrans("", "", string.punctuation)
    ).split()

    count = 0
    for word in words:
        if word in happy_words:
            count += 1

    return count

# Function to count sad words
def number_sad(sentence):
    words = sentence.lower().translate(
        str.maketrans("", "", string.punctuation)
    ).split()

    count = 0
    for word in words:
        if word in sad_words:
            count += 1

    return count

# Ask the user for a sentence
sentence = input("Enter a sentence: ")

# Compute happiness and sadness levels
happy = number_happy(sentence)
sad = number_sad(sentence)

# Display results
print("Number of happy words:", happy)
print("Number of sad words:", sad)

# Determine the tone
if happy > sad:
    print("Tone: Happy (Positive)")
elif sad > happy:
    print("Tone: Sad (Negative)")
else:
    print("Tone: Neutral")
