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
            yt_link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            print(f'{message.content}'[5:])
            newLink = f'{message.content}'[5:]
            if len(newLink) == 0:
                print("no link")
            else:
                yt_link = newLink
            url = 'https://api.w2g.tv/rooms/create.json'
            wkey = ''

            headers = {'Accept':'application/json','Content-Type':'application/json'}
            data = {'w2g_api_key':wkey,'share':yt_link,'bg_color':'#133857','bg_opacity':"30"}

            data = requests.post(url=url , headers=headers , params=data).json()
            
            streamkey = data['streamkey']
            embed=discord.Embed(title="W2G Room Link",  url='https://w2g.tv/' + streamkey, color=0x133857)
            await message.channel.send(embed=embed)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents, command_prefix='!', description="W2G Create Room Bot")

client.run(TOKEN)


