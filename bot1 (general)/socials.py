with open(file=r"discordBots\inPython\mainDiscordCode\bot1 (general)\information.txt", mode="r") as i:

    lines = i.readlines()

lines = [line.strip() for line in lines]

def Socials():

    number = []

    socialName = []

    link = []

    for item in lines:

        if item.lower() == "end of socials":

            break

        else:

            parts = item.split(":", 2)

            if len(parts) == 3:

                number.append(parts[0])

                socialName.append(parts[1])

                link.append(parts[2])

            else:

                continue

    return number, socialName, link

number, socialName, link = Socials()


def joinSocials():

    totalMessage = ""

    for i in range(len(number)):

        totalMessage = totalMessage + f"{number[i]}. {socialName[i]}: {link[i]}" + "\n"

    return totalMessage

total_message = joinSocials()