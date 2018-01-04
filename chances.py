import random

def randomChances():
    chancesYou = ["Chances in one million that",
                  "Odds against one million that",
                  "Futures where",
                  "Possibile events which could mean",
                  "Number of parallel universes in which",
                  "Options which could guarentee that"]
    return random.choice(chancesYou)

def randomYou():
    you = ["you escape unharmed",
    "you still see the light of day",
    "you live another day",
    "you set yourself free",
    "you don't die horribly",
    "you see your family again",
    "all is not lost",
    "your victory",
    "you live another " + randomTime(),
    "nothing bad happens",
    "you obtain " + randomNoun(),
    "you achieve " + randomNoun()]
    return random.choice(you)

def randomTime():
    return random.choice(["three", "five", "ten", "thirty"]) + " " +  random.choice(["seconds", "minutes"])

def randomChoice():
    return random.choice(["Choices resulting in", "Ways to achieve", randomChances() + " you achieve"])

def randomNoun():
    noun = ["a second chance",
            "a decisive victory",
            "anything but death",
            "some safety",
            "a few more seconds of life",
            "another " + randomTime() + " of life",
            "success",
            "your freedom",
            "your survival"]
    return random.choice(noun)

def randomNum():
    return random.choice([
        str(random.randint(0, 1000000)),
        str(random.randint(0, 500)),
        str(random.randint(0, 10)),
        ])

def randomPhrase():
    phrase = random.choice([randomChoice() + " " + randomNoun(), randomChances() + " " + randomYou()])
    return phrase + ": " + randomNum()
