import discord
import json
import requests


TOKEN = ''


class MyClient(discord.Client):
    async def on_ready(self):
        await client.change_presence(activity=discord.Game(name='!w2g'))
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!help'):
            await message.reply('use google bro', mention_author=True)

        if message.content.startswith('!w2g'):
            yt_link = "https://youtu.be/QO7e_RiMVQg"
            url = 'https://api.w2g.tv/rooms/create.json'
            wkey = 'fj3378zier7jaovclqevkqv4qwkd4whykns2f2pg5awdqnuqyj4b74k7ocdmbs1p'
            headers = {'Accept':'application/json','Content-Type':'application/json'}
            data = {'w2g_api_key':wkey,'share':yt_link,'bg_color':'#00ff00','bg_opacity':"50"}
            data = json.dumps(data)
            headers = json.dumps(headers)
            data = requests.post(url,headers,data).json()
            streamkey = data['streamkey']
            embed=discord.Embed(title="W2G Room Link",  url='https://w2g.tv/' + streamkey, color=0xFF5733)
            await message.channel.send(embed=embed)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents, command_prefix='!', description="W2G Create Room Bot")

client.run(TOKEN)


