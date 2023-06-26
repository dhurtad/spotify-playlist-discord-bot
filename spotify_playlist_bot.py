import discord
import os


class PlaylistBot(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')


intents = discord.Intents.default()
intents.message_content = True

client = PlaylistBot(intents=intents)
client.run(os.environ['discord_bot_secret'])
