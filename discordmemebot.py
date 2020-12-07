from discord.ext import commands
import discord, random, requests, json, os

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

def sponge_it(msg_text):
    sponged = msg_text.replace('!sponge', '')
    sponged.lower()
    
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

    if 'hey' in message.content and message.channel.id == active_channel:
        response = random.choice(question_resp)
        await bot.get_channel(message.channel.id).send(response)

    if 'and now we know' in message.content:# and message.channel.id == active_channel:
        response = 'and knowing is half the battle'
        #maybe .TextChannel instead of channel with .id
        await bot.get_channel(message.channel.id).send(response)    

    #if message.author.id == 229840154397769728: #garf        
        #await message.add_reaction('<:our_hero:433858373402755072>')
    if message.author.id == 241347961429164032: #old sam   
        await message.add_reaction('<:old_sam:421865584003645451>')
    #if message.author.id == 319700740241227776: #craig
        #await message.add_reaction('<:craig:782520684185518092>')
    #if message.author.id == 145332658916950017: #phazon
        #await message.add_reaction('<:PepeMods:663971013192712202>')
        #await message.add_reaction('<:pepe_special:421872337990975488>')
    #if message.author.id == 333380600557862923: #rinyer
        #await message.add_reaction('<:Shibe_WG:539580961327808514>')


    #785313284664066059 sponge_mock
    if message.content.startswith('!sponge ') and message.channel.id == 728412068880973875:
        await bot.get_channel(728412068880973875).send(sponge_it(message.content))
        #.add_reaction('<:sponge_mock:785313284664066059>')
        bot_msg = discord.utils.get(await message.channel.history(limit=1).flatten(), author=728172902394101770)
        print(bot_msg)
        await message.delete()

    await bot.process_commands(message)



bot.run(TOKEN)



