import random

knock_knock = [
    "Knock knock. Who’s there? Cow says. Cow says who? No, a cow says mooooo!",
    "Knock knock. Who’s there? A little old lady. A little old lady who? All this time, I had no idea you could yodel.",
    "Knock knock. Who’s there? Tank. Tank who? You’re welcome.",
    "Knock Knock. Who’s there? Voodoo. Voodoo who? Voodoo you think you are, asking all these questions?",
    "Knock, Knock. Who’s there? Nobel. Nobel who? Nobel, that’s why I knocked!"
    "Knock, knock. Who’s there? Luke. Luke who? Luke through the peep hole and find out."
]

riddle_dict = {
    "I’m tall when I’m young, and I’m short when I’m old. What am I? ": "candle",
    "What month of the year has 28 days? ": "All of them",
    "What question can you never answer yes to?": "are you sleeping",
    "I am in school and home.I have a mouse. You can use me for work. You can use me for email. What am I? ": "computer"
}


def jokebot(type):
    if type == "Knock Knock" or type == "knock knock":
        jokenum = random.randint(0, 3)
        out = knock_knock[jokenum]
        return (out)
    elif type == "Riddle" or type == "riddle":
        riddle, answer = random.choice(list(riddle_dict.items()))
        r = input(riddle)
        if r == answer:
            return "You got it correct"
        else:
            return "You got it wrong the correct answer is" + answer
