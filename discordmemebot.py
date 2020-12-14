from discord.ext import commands
import discord, random, requests, json, os

#scrod token
TOKEN = os.environ['S3_SECRET']

#SDM info
active_channel = int(os.environ['active_channel'])
try:
    print(f"active_channel type: {type(active_channel)}")
    print(f"active_channel: {active_channel}")
except:
    print(f"oopsy active_channel")
    
#SDM channel
channel_name = os.environ['channel_name']
try:
    print(f"channel_name type: {type(channel_name)}")
    print(f"channel_name: {channel_name}")
except:
    print(f"oopsy channel name")

#BASE
article_base = os.environ['article_base']
try:
    print(f"article base type: {type(article_base)}")
    print(f"article base: {article_base}")
except:
    print(f"oopsy article_base")

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    random.seed()
    print(f'{bot.user} has connected to Discord!')
    #await bot.get_channel(active_channel).send('DankMemeBot ready for Memes')

def sponge_it(msg_text):
    sponged = msg_text.replace('?sponge ', '')
    sponged = sponged.lower()
    
    final_sponge = ''
    
    rando_num = random.randint(0,1)

    i = 0
    for char in sponged:
        if i % 2 == 0 and rando_num == 0:
            final_sponge += char.upper()
        elif i % 2 != 0 and rando_num == 1:
            final_sponge += char.upper()
        else:
            final_sponge += char
            
        i += 1    
		
    return final_sponge

@bot.command(name='article')
async def search_article(ctx, search_qry):
    if ctx.channel.name == channel_name:
        r = requests.get(f"{article_base}/{search_qry}")      
        await bot.get_channel(active_channel).send(f'Query Results from PCG: {r.text}')
        
@bot.command(name='article-all')
async def get_article_all(ctx):
    if ctx.channel.name == channel_name:
        r = requests.get(f"{article_base}/all")      
        await bot.get_channel(active_channel).send('Query Results from PCG: ' + r.text)



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
        await bot.get_channel(message.channel.id).send(response)

    if 'and now we know' in message.content:# and message.channel.id == active_channel:
        response = 'and knowing is half the battle'
        #maybe .TextChannel instead of channel with .id
        await bot.get_channel(message.channel.id).send(response)    

    #if message.author.id == 229840154397769728: #me        
        #await message.add_reaction('<:our_hero:433858373402755072>')
    if message.author.id == 241347961429164032: #os   
        await message.add_reaction('<:old_sam:421865584003645451>')
    #if message.author.id == 319700740241227776: #cr
        #await message.add_reaction('<:craig:782520684185518092>')
    #if message.author.id == 145332658916950017: #ph
        #await message.add_reaction('<:PepeMods:663971013192712202>')
        #await message.add_reaction('<:pepe_special:421872337990975488>')
    #if message.author.id == 333380600557862923: #ri
        #await message.add_reaction('<:Shibe_WG:539580961327808514>')


    #785313284664066059 sponge_mock
    #.add_reaction('<:sponge_mock:785313284664066059>')
    if message.content.startswith('?sponge '):
        bot_msg = await bot.get_channel(message.channel.id).send(sponge_it(message.content))
        await bot_msg.add_reaction('<:sponge_mock:785327148680216583>')
        await message.delete()

    await bot.process_commands(message)



bot.run(TOKEN)



