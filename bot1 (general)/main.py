import discord 
from dotenv import load_dotenv
import os
from responses import getResponses
from datetime import datetime


## Step 0:

# Load the .env file
load_dotenv()

# Fetch the token from the .env file
my_key = os.getenv("MY_KEY1")

## Step 1: Bot Set Up:

# Gives the bot access to all the intents (permissions) we gave it
intents: discord.Intents = discord.Intents.default()

# Making message_content = true
intents.message_content = True 

#Making Client
Client: discord.Client = discord.Client(intents=intents)


## Step 2: Message functionality

async def send_message(message: discord.message, user_message: str) -> None:

    if not user_message:
        print("Message was empty because intents probably wasn't enabled")
        return 

    # triggers the private message functionality
    if is_private := user_message[0] == "?":
        # Ignores the "?" part of the message
        user_message[1 :]

    elif with_indicator := user_message[0] == "!":

        user_message[1 :]
    
    try:
    
        response, view = getResponses(user_message)

        if isinstance(response, discord.Embed):
        
            await message.author.send(embed=response, view=view) if is_private else await message.channel.send(embed=response, view=view)
        
        else:

            if is_private:
        
                await message.author.send(response) 
            
            elif with_indicator:
                
                await message.channel.send(response)
    
    except Exception as e:
    
        print(e)


## Step 3 Handling the startup of the bot:

empty = ""

@Client.event
async def on_ready()-> None:
    print(f"{Client.user} is now running!")

    try:    
        with open(file=r"discordBots\inPython\mainDiscordCode\bot1 (general)\messages.txt", mode="r") as file:
            content = file.read()

    except FileNotFoundError:
        #if the file doesn't exist, create it with an initial count of 0
        content = "number of times ran: 0"

    #emptying the file
    with open(file=r"discordBots\inPython\mainDiscordCode\bot1 (general)\messages.txt", mode="w") as file:

        file.write(empty)

    #Parse the current count from the content
    try:

        count = int(content.split(":")[-1].strip())
    
    # makes it 0 if it does not exist
    except ValueError:

        print("Error: Invalid content format")
        count = 0
    
    #increases count
    count += 1

    updated_content = f"number of times ran: {count}"

    with open(file=r"discordBots\inPython\mainDiscordCode\numberOfRuns.txt", mode= "w") as file:
        
        file.write(updated_content)

# step 4: handling incoming messages:
@Client.event
async def on_message(message: discord.message) -> None:

    if message.author == Client.user:
        return
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    if user_message[0] != "" and (is_private := user_message[0] == "?"): 

        print(f"[{channel}], {username}: ' {user_message[1 :]}'")        
    
        with open(file=r"discordBots\inPython\mainDiscordCode\messages.txt", mode="r") as a:

            lines = a.readlines()

            lines += f"\n {datetime.now()}    [{channel}], {username}: '{user_message[1 :]} \n Response from bot: {getResponses(user_input=user_message)}"

        with open(file=r"discordBots\inPython\mainDiscordCode\messages.txt", mode="w") as file:

            file.writelines(lines)

        await send_message(message=message, user_message=user_message)

    elif user_message[0] != "" and (with_indicator := user_message[0] == "!"):

        print(f"[{channel}], {username}: ' {user_message [1 :]}'")
    
        with open(file=r"discordBots\inPython\mainDiscordCode\bot1 (general)\messages.txt", mode="r") as a:

            lines = a.readlines()

            lines += f"\n {datetime.now()}    [{channel}], {username}: '{user_message[1 :]} \n Response from bot: {getResponses(user_input=user_message)}"

        with open(file=r"discordBots\inPython\mainDiscordCode\bot1 (general)\messages.txt", mode="w") as file:

            file.writelines(lines)

        await send_message(message=message, user_message=user_message)

# Step 5 Main entry point:

def main() -> None:

    Client.run(token=my_key)

# Step 6 Running the code:

main()

