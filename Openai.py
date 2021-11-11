import discord
import openai

openai.api_key = "OPENAI API TOKEN HERE"
start_sequence = "\nEllie:"
restart_sequence = "\nHuman: "
session_prompt = 'The following is a conversation with a sixteen-year-old female teenager. Her name is Ellie. She is smart,friendly and kind. She listens to KPop.'
client = discord.Client()


@client.event
async def on_ready():
    activity = discord.Game(name="Chatting")
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    global session_prompt
    if message.author == client.user or message.channel.id != 855803581603774484:
        return
    session_prompt = f"{session_prompt}{restart_sequence}{message.content}{start_sequence}"

    response = openai.Completion.create(
        engine="curie",
        prompt=session_prompt,
        temperature=1,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n", " Human:", " AI:", "Ellie:"]
    )
    bot_reply = (response["choices"][0]["text"])
    session_prompt = f"{session_prompt}{restart_sequence}{message.content}{start_sequence}{bot_reply}"
    await message.channel.send(bot_reply)

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
description = 'A Chatbot named Ellie!'

client.run("BOT TOKEN HERE")
