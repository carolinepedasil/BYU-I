# I added an additional sentence at the end of the story asking for two more words (noun and place) to extend the narrative.
# The program also handles "a" vs. "an" based on the vowel/consonant rule.

# Function to determine if 'a' or 'an' should be used based on the word's first letter.
def get_article(word):
    if word[0].lower() in 'aeiou':
        return 'an'
    else:
        return 'a'

print("Please enter the following:")

adjective = input("adjective: ")
animal = input("animal: ")
verb1 = input("verb: ")
exclamation = input("exclamation: ").capitalize()
verb2 = input("verb: ")
verb3 = input("verb: ")
# Exceeding Requirements/Showing Creativity:
noun = input("noun: ")
place = input("place: ")

story = f"""
The other day, I was really in trouble. It all started when I saw {get_article(adjective)} very
{adjective} {animal} {verb1} down the hallway. "{exclamation}!" I yelled. But all
I could think to do was to {verb2} over and over. Miraculously,
that caused it to stop, but not before it tried to {verb3}
right in front of my family. 
Afterward, I found {get_article(noun)} {noun} lying on the floor in {place}.
"""

print("\nYour story is:")
print(story)
