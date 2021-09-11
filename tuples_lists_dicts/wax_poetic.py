import random

# create five list of different word types
nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

def make_poem():
    """Create a randomly generated poem, returned as multiline string."""
    # pull three nouns randomly
    n1 = random.choice(nouns)
    n2 = random.choice(nouns)
    n3 = random.choice(nouns)
    # make sure that all nouns are different
    while n1 == n2:
        n2 = random.choice(nouns)
    while n1 == n3 or n2 == n3:
        n3 = random.choice(nouns)
    
    #pull three different verbs
    v1 = random.choice(verbs)
    v2 = random.choice(verbs)
    v3 = random.choice(verbs)
    # make sure all verbs are different 
    while v1 == v2:
        v2 = random.choice(verbs)
    while v1 == v3 or v2 == v3:
        v3 = random.choice(verbs)
    
    # pull three different adjectives
    adj1 = random.choice(adjectives)
    adj2 = random.choice(adjectives)
    adj3 = random.choice(adjectives)
    # make sure all words are different
    while adj1 == adj2:
        adj2 = random.choice(adjectives)
    while adj1 == adj3 or adj2 == adj3:
        adj3 = random.choice(adjectives)
    
    # pull 2 different prepositions
    prep1 = random.choice(prepositions)
    prep2 = random.choice(prepositions)
    # make sure all words are different
    while prep1 == prep2:
        prep2 = random.choice(prepositions)
    
    # pull one random adverb
    adv = random.choice(adverbs)

    # identify first letter (a vowel or not)
    if "aiueo".find(adj1[0]) != -1:
        article = "An"
    else:
        article = "A"
    
    # create the poem
    poem = (
        f"{article} {adj1} {n1}\n\n"
        f"{article} {adj1} {n1} {v1} {prep1} {prep1} the {adj2} {n2}\n"
        f"{adv}, the {n1} {v2}\n"
        f"the {n2} {v3} {prep2} a{adj3} {n3}"
    )
    
    return poem

poem = make_poem()
print(poem)