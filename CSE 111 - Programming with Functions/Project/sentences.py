import random

def main():
    print(make_sentence(1, "past"))
    print(make_sentence(1, "present"))
    print(make_sentence(1, "future"))
    print(make_sentence(2, "past"))
    print(make_sentence(2, "present"))
    print(make_sentence(2, "future"))

def make_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase = get_prepositional_phrase(quantity)
    return f"{determiner.capitalize()} {noun} {verb} {prepositional_phrase}."

def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    return random.choice(words)

def get_noun(quantity):
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    return random.choice(words)

def get_verb(quantity, tense):
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought", "ran", "walked", "wrote"]
    elif tense == "present":
        words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "walks", "writes"] if quantity == 1 else ["drink", "eat", "grow", "laugh", "think", "run", "walk", "write"]
    elif tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will walk", "will write"]
    return random.choice(words)

def get_preposition():
    words = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below",
             "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of",
             "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    return random.choice(words)

def get_prepositional_phrase(quantity):
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    return f"{preposition} {determiner} {noun}"

main()
