from discord.ext import commands
from discord.utils import get
import random, requests, json, os

TOKEN = os.environ['S3_SECRET']

bot = commands.Bot(command_prefix='!')

#gfs playground
#active_channel = 728440770952036423
#channel_name = 'game-articles'

#SDM info
active_channel = 729264852039630861
channel_name = 'gaming-articles'

@bot.event
async def on_ready():
    random.seed()
    print(f'{bot.user} has connected to Discord!')
    #await bot.get_channel(active_channel).send('DankMemeBot ready for Memes')

"""
@bot.command(name='article')
async def search_article(ctx, search_qry):
    if ctx.channel.name == channel_name:
        await bot.get_channel(active_channel).send('Query Results from PCG: ' + search_result)
"""
"""
@bot.command(name='bigarticle')
async def main_article(ctx):
    if ctx.channel.name == channel_name:
        pass
        await bot.get_channel(active_channel).send('Main Article from PCG: ' + response)
"""
"""
@bot.command(name='mostrecentart')
async def recentestart(ctx):
    if ctx.channel.name == channel_name:
        r = requests.get(BASE + '/latest-article')
        print(r.text)
        r_json = json.loads(r.text)
        await bot.get_channel(active_channel).send('id: ' + str(r_json['id']) + ', link: ' + r_json['link'])
        # await bot.get_channel(active_channel).send('Most Recent Article from PCG: ' + response)


@bot.command(name='randart')
async def randart(ctx):
    if ctx.channel.name == channel_name:
        r = requests.get(BASE + '/latest-article')
        pos_dict = json.loads(r.text)

        r2 = requests.get(BASE + f"/article/{random.randint(0,pos_dict['id'])}")
        rand_dict = json.loads(r2.text)

        random_article = rand_dict['link']

        await bot.get_channel(active_channel).send('Random Recent Article from PCG: ' + random_article)
"""

"""
@bot.command(name='disc_meme_bot')
async def disc_meme_bot(ctx):
    if ctx.channel.name == channel_name:
        await bot.get_channel(active_channel).send('Bye Bye!')
        await bot.close()
"""

@bot.event
async def on_message(message):
    question_resp = [
        'henlo',
        'sup',
        'yo dawg',
        'oi mang',
        'ima bot dude',
        'i like cats',
        'games are cool',
        'i like orange juice',
        'garf is the best',
        'craig likes witcher',
        'phazon likes the star war',
        'old sam likes gold',
        'rinya likes yarn',
        'ferret likes guinea pigs',
        'everyone here likes memes'
    ]

    if 'hey' in message.content:# and message.channel.id == active_channel:
        response = random.choice(question_resp)
        await bot.get_channel(message.channel.id).send(response)

    if 'and now we know' in message.content:# and message.channel.id == active_channel:
        response = 'and knowing is half the battle'
        #maybe .TextChannel instead of channel with .id
        await bot.get_channel(message.channel.id).send(response)    

    #if message.author.id == 229840154397769728:
        #await bot.add_reaction(emoji="old_sam:783863390220320779")
        #emoji = 'our_hero'
        #await message.add_reaction(emoji)

    # we do not want the bot to reply to itself
    if message.author == bot.user:
        return
    if message.author.id == 229840154397769728:
        print(f'author id: {message.author.id}')
        print(f'message content: {message.content}')
        
        await message.add_reaction('<:our_hero:433858373402755072>')
        
    await bot.process_commands(message)



bot.run(TOKEN)
