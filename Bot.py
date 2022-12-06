import discord

TOKEN = ''


class MyClient(discord.Client):
    async def on_ready(self):
        await client.change_presence(activity=discord.Game(name='!w2g'))
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True


client = MyClient(intents=intents, command_prefix=',', description="W2G Create Room Bot")

client.run(TOKEN)
