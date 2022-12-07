import discord
import json
import requests


TOKEN = ''
wkey = ''
W2GKeys = {}
class MyClient(discord.Client):
    
    
    async def on_ready(self):
        await client.change_presence(activity=discord.Game(name='!w2g'))
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if message.author.id == self.user.id:
            return



        if message.content.startswith('!help'):
           
            embed=discord.Embed(title="Help",  url='https://dino.reuther05.de', color=0x133857)
            embed.add_field(name="!w2g", value="creates Watch2Gether room", inline=False)
            embed.add_field(name="!w2g <link>", value="creates Watch2Gether room with preloaded video", inline=False)
            await message.channel.send(embed=embed)

        if message.content.startswith('!w2g'):
            yt_link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            print(f'{message.content}'[5:])
            newLink = f'{message.content}'[5:]
            if len(newLink) == 0:
                print("no link")
            else:
                yt_link = newLink
            url = 'https://api.w2g.tv/rooms/create.json'
            

            headers = {'Accept':'application/json','Content-Type':'application/json'}
            data = {'w2g_api_key':wkey,'share':yt_link,'bg_color':'#133857','bg_opacity':"30"}
            data = requests.post(url=url , headers=headers , params=data).json()
            
            streamkey = data['streamkey']
            embed=discord.Embed(title="W2G Room Link",  url='https://w2g.tv/' + streamkey, color=0x133857)
            embed.add_field(name="Roomkey: ", value=streamkey, inline=True)
            await message.channel.send(embed=embed)
            print(message.channel)
            W2GKeys[message.channel.id] = streamkey
            print(W2GKeys)

        if message.content.startswith('!w2add'):
            print(W2GKeys)
            yt_link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            print(f'{message.content}'[7:])
            newLink = f'{message.content}'[7:]
        
            try:
                streamkey = W2GKeys[message.channel.id]
                print(streamkey)
            except KeyError:
                error=discord.Embed(title="No room found",  url='https://dino.reuther05.de', color=0x133857)
                error.add_field(name="No room found in this channel: ", value="please use !w2g <link>", inline=False)
                await message.channel.send(embed=error)
                return 

            if len(newLink) == 0:
                error=discord.Embed(title="W2G Room Link",  url='https://w2g.tv/' + streamkey, color=0x133857)
                error.add_field(name="No link found in command: ", value="please use !w2add <link>", inline=False)
                await message.channel.send(embed=error)
                return 
            yt_link = newLink

            url = 'https://api.w2g.tv/rooms/' + streamkey +'/sync_update'

            headers = {'Accept':'application/json','Content-Type':'application/json'}
            data = {'w2g_api_key':wkey,'item_url':yt_link}

            try:
                requests.post(url=url , headers=headers , params=data).json()
            except:
                print()
            update=discord.Embed(title="W2G Room Link",  url='https://w2g.tv/' + streamkey, color=0x133857)
            update.add_field(name="Room updated: ", value=streamkey, inline=False)
            await message.channel.send(embed=update)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents, command_prefix='!', description="W2G Create Room Bot")

client.run(TOKEN)


