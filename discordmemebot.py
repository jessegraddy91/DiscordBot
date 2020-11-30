from discord.ext import commands
import random, requests, json, os
import boto
from boto.s3.connection import S3Connection
from boto.s3.key import Key

#s3 = S3Connection(os.environ['S3_KEY'], os.environ['S3_SECRET'])

c = boto.connect_s3()
bucket = conn.create_bucket('mybucket')
b = c.get_bucket('mybucket') # substitute your bucket name here

k = Key(b)
k.key = os.environ['S3_KEY']
print(k.get_contents_as_string())



#print(s3['S3_SECRET'])
#TOKEN = s3['S3_SECRET']

bot = commands.Bot(command_prefix='!')

# channel game-articles id is 729264852039630861

# for prod:
# active_channel = sys.argsv[1]
#for during dev:
#regular discord
#active_channel = 729264852039630861
# channel_name = sys.argsv[2]
#channel_name = 'game-articles'

active_channel = 728440770952036423
channel_name = 'gaming-articles'

#BASE = "http://127.0.0.1:5000/"

@bot.event
async def on_ready():
    random.seed()
    print(f'{bot.user} has connected to Discord!')
    await bot.get_channel(active_channel).send('DankMemeBot ready for Memes')

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

@bot.command(name='disc_meme_bot')
async def disc_meme_bot(ctx):
    if ctx.channel.name == channel_name:
        await bot.get_channel(active_channel).send('Bye Bye!')
        await bot.close()


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

    if 'hey' in message.content and message.channel.id == active_channel:
        response = random.choice(question_resp)
        await bot.get_channel(active_channel).send(response)

    if 'and now we know' in message.content and message.channel.id == active_channel:
        response = 'and knowing is half the battle'
        await bot.get_channel(active_channel).send(response)    

    await bot.process_commands(message)



bot.run(TOKEN)
