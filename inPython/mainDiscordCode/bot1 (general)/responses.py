from random import choice, randint
from socials import total_message


def getResponses(user_input: str):
    lowered = user_input.lower()

    if lowered == "":
        return "well you're awfully silent", None

    elif "hello" in lowered:
        return "Hello there", None

    elif "how are you" in lowered:
        return "I'm good how are you?", None

    elif "bye" in lowered:
        return "Goodbye my friend", None

    elif "roll dice" in lowered:
        return f"The dice shows the number {randint(1, 6)}", None

    elif "socials" in lowered:
        return total_message, None
    
    elif "number of times ran" in lowered:

        with open(file=r"discordBots\inPython\mainDiscordCode\bot1 (general)\numberOfRuns.txt", mode="r") as file:

            ran = file.read()

        return ran, None

    else:
        return choice(["I do not understand",
                       "My feeble brain is not smart enough, please dumb it down more",
                       "Rephrase it please"]), None
