import random

"""A simple 8 ball program. Will develop a GUI to further my knowledge in the future."""

responses = ["It is certain.",
             "It is decidedly so.",
             "Without a doubt",
             "Yes - definitely",
             "You may rely on it.",
             "As I see it, yes.",
             "Most likely.",
             "Outlook good.",
             "Yes.",
             "Signs point to yes.",
             "Reply hazy, try again.",
             "Ask again later.",
             "Better not tell you now.",
             "Cannot predict now.",
             "Concentrate and ask again.",
             "Don't count on it.",
             "My reply is no.",
             "My sources say no.",
             "Outlook not so good.",
             "Very doubtful."]

def EightBall():
	print("Welcome to the Magic 8-Ball. Type 'quit' at any moment to exit.")
	while True:
		msg = input("Type in your question, and I will return with a response. ")
		if msg.lower() == "quit":
			break
		else:
			print(random.choice(responses))
			continue

EightBall()