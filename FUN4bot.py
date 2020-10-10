import discord
from discord.ext import commands
import wikipedia
import random
import datetime
import asyncio




bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print ( 'Totul merge bine' )
    bot.loop.create_task ( status_task () )


async def status_task():
    while True:
        await bot.change_presence ( activity=discord.Game ( '?help', status=discord.Status.idle ) )
        await asyncio.sleep ( 10 )
        await bot.change_presence (
            activity=discord.Game ( '#traiescfun ', status=discord.Status.online ) )
        await asyncio.sleep ( 10 )
        await bot.change_presence (
            activity=discord.Game ( 'Sunt un proiect neobisnuit focut de DIOR ♡F4F#1675', status=discord.Status.online ) )
        await asyncio.sleep ( 10 )
        await bot.change_presence (
            activity=discord.Game ( 'https://discord.gg/rnJWBKr', status=discord.Status.online ) )
        await asyncio.sleep ( 10 )
        await bot.change_presence (
            activity=discord.Game ( 'Mobile Legends cu Dior, Reflex si Demon', status=discord.Status.online ) )
        await asyncio.sleep ( 15 )

@bot.command()
async def shop(ctx):
        embed=discord.Embed(title="FUN4FUNSHOPbasic", description="<:basicshop:756469041593450566>**blue:** <@&647717084977037312> <@&647719455656509462> <@&647719884024709140>\n<:basicshop:756469041593450566>**red:**<@&647549165357891604> <@&647548913070505985> <@&647723059285065732> <@&647725117639622657>\n<:basicshop:756469041593450566>**orange:** <@&647549744499130407> <@&647722725762138132>\n<:basicshop:756469041593450566>**green:** <@&647549563535622144> <@&647721098045292553> <@&647721723206172672>\n<:basicshop:756469041593450566>**yellow:** <@&591286289471373351> <@&647722065545265152>\n<:basicshop:756469041593450566>**purple:** <@&647724483460988938> <@647724755931103232> <@&647723486751490079>\n<:basicshop:756469041593450566>**noncolours:** <@&647717557867905035> <@&734508792598888571>",color=0xbdbdbd)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/697126125683343432/756475494651658330/fun.png")
        embed.set_footer(text="1500", icon_url="https://cdn.discordapp.com/emojis/706219192923455549.gif?v=1")
        await ctx.send(embed=embed)
        embed=discord.Embed(title="FUN4FUNSHOPpremium", description="<:premiumshop:756463891667746817><@&666664466007719937>\n<:premiumshop:756463891667746817><@&679407448586453023>\n<:premiumshop:756463891667746817><@&679409336346214423>\n<:premiumshop:756463891667746817><@&679407602953617410>\n<:premiumshop:756463891667746817><@&679407811758915634>\n<:premiumshop:756463891667746817><@&679408219340275732>\n<:premiumshop:756463891667746817><@&679408577324253195>\n<:premiumshop:756463891667746817><@&679408732496723968>\n<:premiumshop:756463891667746817><@&679409144322850839>\n<:premiumshop:756463891667746817><@&679409588457439262>",color=0xfbd723)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/697126125683343432/756475470945583144/fff.png")
        embed.set_footer(text="2000", icon_url="https://cdn.discordapp.com/emojis/706219192923455549.gif?v=1")
        await ctx.send(embed=embed)


bot.remove_command('help')
prefix='?'

@bot.event
async def on_member_join(member):
  embed = discord.Embed(colour=0x95fcc, description=f"Speram sa te simti cat mai bine alaturi de noi.", title=f"Bine ai venit pe server")
  embed.set_thumbnail(url=f"{member.avatar_url}")
  embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
  embed.set_image(url='https://media.discordapp.net/attachments/663305200081174531/725964570853638194/8f1ccd98-28d5-40b2-8d6e-3a2537573677.gif')
  channel = bot.get_channel(id=747526501091770558)
  if channel.guild == member.guild:
    await channel.send(embed=embed)
    await asyncio.sleep(1)
  channel1 = bot.get_channel(id=697122280639037530)
  if channel1.guild == member.guild:
    embed=discord.Embed(title="FUN4FUN", description=f"{member.mention} bine ai venit in comunitatea Fun for Fun !")
    embed.add_field(name="Ai jos cateva informatii importante ce te-ar putea ajuta ! ", value=f":pushpin:Daca doresti te poti prezenta pe canalul <#672864951391485968> pentru a afla care sunt pasiunile tale, hobby-urile si pentru a te putea integra mai rapid !\n:pushpin:Iti poti alege propriile roluri de pe canalul <#721065393950556191> pentru a debloca canalele custom  pentru roluri, precum cel de 👹anime, <:funcode:745339622443319307>coding si :paintbrush:design / arta !", inline=True)
    embed.set_footer(text="mesajul se va sterge in 120 de secunde pentru a evita spam-ul")
    msg = await channel1.send(embed=embed)
    await asyncio.sleep(120)
    await msg.delete()

@bot.event
async def on_member_remove(member):
  embed = discord.Embed(colour=0xf93302, description=f"Speram sa te intorci cat de curand", title=f"Ne pare rau ca ai plecat")
  embed.set_thumbnail(url=f"{member.avatar_url}")
  embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
  embed.set_image(url='https://media.discordapp.net/attachments/663305200081174531/725963594172465249/e1e5c147-ae20-4f74-bae4-26a222beb92e.gif')
  channel = bot.get_channel(id=747526501091770558)
  if channel.guild == member.guild:
    await channel.send(embed=embed)

#FUN COMMANDS

@bot.command()
@commands.has_permissions(ban_members=True)
async def sayd(ctx, *, say: commands.clean_content):
     await ctx.send(f'**{say}**')
@sayd.error
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    embed = discord.Embed(title = f'<:error:754413108822409386>**|**ERROR',description=f"<:x_:754406625560756274>**|{prefix}sayd**\n<:0_:754406673564696637>**|{prefix}sayd (mesaj)**\n<:hmm:754410711828004948>**|{prefix}sayd #traiescfun**",colour = discord.Colour.blue())
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def event(ctx, *, msg):
     embed=discord.Embed(title="MINI EVENT", description=f"{msg}", colour=discord.Colour.blue())
     await ctx.message.delete()
     await ctx.send(embed=embed)


@bot.command()
async def scade(ctx, left: int, right: int):
    embed = discord.Embed(title = 'Dupa calculele mele...',description = f'**rezultatul este** {(left - right)}',colour = discord.Colour.red())
    embed.set_thumbnail(url='https://media.giphy.com/media/l2JdZ6jQkHjwlCDkI/giphy.gif')
    await ctx.send(embed=embed)

@bot.command()
async def aduna(ctx, left: int, right: int):
    embed = discord.Embed(title = 'Dupa calculele mele...',description = f'**rezultatul este** {(left + right)}',colour = discord.Colour.green())
    embed.set_thumbnail(url='https://media.giphy.com/media/l2JdZ6jQkHjwlCDkI/giphy.gif')
    await ctx.send(embed=embed)

@bot.command()
async def choose(ctx, *choices: str):
    embed = discord.Embed(title = 'Grea decizie...',description = f'**O sa aleg** ****{(random.choice(choices))}****',colour = 0x00ffee)
    await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
    embed = discord.Embed()
    embed.set_image(url="https://i.imgur.com/sF6NGKq.gif")
    msg = await ctx.send(embed=embed)
    embed = discord.Embed(title = '🏓Ping!', description = (f'****🏓Pong!**** *{round(bot.latency * 1000)}* **ms**'),colour = 0x62016f)
    embed.set_thumbnail(url='https://i.pinimg.com/originals/21/02/a1/2102a19ea556e1d1c54f40a3eda0d775.gif')
    await asyncio.sleep(1)
    await msg.edit(embed=embed)
#Games
@bot.command()
async def nrguess(ctx):
    number = random.randint(10, 20)
    for i in range(0, 5):
        embed = discord.Embed(title = "**NRGUESS**",description="alege un numar de la `10` la `20`")
        msg11=await ctx.send(embed=embed)
        response = await bot.wait_for('message')
        guess = int(response.content)
        if guess > number:
            embed = discord.Embed(title = "ai ales un numar prea mare",color=0xff4747)
            await msg11.edit(embed=embed)
            await msg11.add_reaction(f"⬆️")
        elif guess < number:
            embed = discord.Embed(title = "ai ales un numar prea mic",color=0xff4747)
            await msg11.edit(embed=embed)
            await msg11.add_reaction(f"⬇️")
        else:
            embed = discord.Embed(title = "ai ales numarul corect",color=0x47ff6c)
            await msg11.edit(embed=embed)
            await msg11.add_reaction(f"☑️")
            return
        await asyncio.sleep(1)
    embed1 = discord.Embed(title = "ai atins numarul maxim de incercarii\njoc terminat",color=0xff4747)
    await ctx.send(embed=embed1)

amongtitle = ["<:player2:760848207323332629>Impostorul saboteaza nava grabeste-te sa il prinzi<:player2:760848207323332629>","<:player2:760848207323332629>Au fost gasiti playeri morti in electrical<:player2:760848207323332629>", "<:player2:760848207323332629>Un player a murit, nu sau gasit urme la fata locului<:player2:760848207323332629>", "<:player2:760848207323332629>Impostorul foloseste trapele sa scape nedetectat!<:player2:760848207323332629>", "<:player2:760848207323332629>Camerele video nu functioneaza!<:player2:760848207323332629>"]
@bot.command()
async def among_us(ctx):
    number = random.randint(1, 10)
    for i in range(0, 4):
        embed = discord.Embed(title = "**GASESTE IMPOSTORUL\ntype 1 for tutorial**",description=f"<:player:760839689338617867>1.{ctx.author.name}\n<:player:760839689338617867>2.Red\n<:player:760839689338617867>3.Blue\n<:player:760839689338617867>4.Yellow\n<:player:760839689338617867>5.Green\n<:player:760839689338617867>6.Black\n<:player:760839689338617867>7.White\n<:player:760839689338617867>8.Cyan\n<:player:760839689338617867>9.Orange\n<:player:760839689338617867>10.Purple")
        msg11=await ctx.send(embed=embed)
        response = await bot.wait_for('message')
        guess = int(response.content)
        if guess > number:
            embed = discord.Embed(title=f"{random.choice(amongtitle)}",color=0xff4747)
            embed.set_image(url="https://cdn.discordapp.com/attachments/691360396539330611/760840938368139294/PicsArt_09-30-03.30.04.jpg")
            await msg11.edit(embed=embed)
            await msg11.add_reaction(f"<:player:760839689338617867>")
            await msg11.add_reaction(f"<:player2:760848207323332629>")
        elif guess == 1:
            embed = discord.Embed(title="**TUTORIAL**",color=0xff4747)
            embed.set_image(url="https://cdn.discordapp.com/attachments/730039049863036939/760857464542855188/82d4f361-c5d6-4022-ba11-59681b0af5d1.gif")
            await msg11.edit(embed=embed)
        elif guess < number:
            embed = discord.Embed(title=f"{random.choice(amongtitle)}",color=0xff4747)
            embed.set_image(url="https://cdn.discordapp.com/attachments/691360396539330611/760840938368139294/PicsArt_09-30-03.30.04.jpg")
            await msg11.edit(embed=embed)
            await msg11.add_reaction(f"<:player:760839689338617867>")
            await msg11.add_reaction(f"<:player2:760848207323332629>")
        else:
            embed = discord.Embed(title="**VICTORIE**",description="**Impostorul a fost prins**",color=0x47ff6c)
            embed.set_image(url="https://re-actor.net/wp-content/uploads/2020/07/Among-Us.jpg")
            await msg11.edit(embed=embed)
            await msg11.add_reaction(f"☑️")
            return
        await asyncio.sleep(1)
    embed1 = discord.Embed(title = "**Ai fost omorat :(**",color=0xff4747)
    embed1.set_image(url="https://bang-phinf.pstatic.net/a/329j35/0_4b5Ud018bngx4jyz8udz7g8_wzvdxx.gif")
    await ctx.send(embed=embed1)

@bot.command()
async def task(ctx):
    number = random.randint(1000, 1500)
    for i in range(0, 10):
        embed = discord.Embed(title = "**Sparge Bancomat-ul\ntype 1 for tutorial**",description=f"**Sugestie pentru tine {ctx.author.mention}**\nCodul card-ului de credit este cuprins intre 1000 si 1500")
        embed.set_image(url="https://media.discordapp.net/attachments/697126125683343432/761157820522692628/PicsArt_10-01-12.26.49.jpg?width=826&height=499")
        msg=await ctx.send(embed=embed)
        response = await bot.wait_for('message')
        guess = int(response.content)
        if guess > number:
            embed = discord.Embed(title="Sugestie alege un numar mai mic",color=0x8a8a8a)
            embed.set_image(url="https://media.discordapp.net/attachments/697126125683343432/761167379701956638/PicsArt_10-01-01.07.21.jpg?width=826&height=499")
            await msg.edit(embed=embed)
        elif guess == 1:
            embed = discord.Embed(title="**TUTORIAL-INDISPONIBIL**",color=0x8a8a8a)
            await msg.edit(embed=embed)
        elif guess < number:
            embed = discord.Embed(title="Sugestie alege un numar mai mare",color=0x8a8a8a)
            embed.set_image(url="https://media.discordapp.net/attachments/697126125683343432/761167379701956638/PicsArt_10-01-01.07.21.jpg?width=826&height=499")
            await msg.edit(embed=embed)
        else:
            embed = discord.Embed(title="**CODUL ESTE CORECT**",color=0x8a8a8a)
            embed.set_image(url="https://media.discordapp.net/attachments/697126125683343432/761157821689364500/PicsArt_10-01-12.28.53.jpg?width=826&height=499")
            await msg.edit(embed=embed)
            return
        await asyncio.sleep(1)
    embed1 = discord.Embed(title = "**AI FOST PRINS\nMISIUNE ESUATA**",color=0xff4747)
    embed1.set_image(url="https://media.discordapp.net/attachments/697126125683343432/761157821135454228/PicsArt_10-01-12.27.56.jpg?width=826&height=499")
    await ctx.send(embed=embed1)

@bot.command(pass_context=True)
async def tpu(ctx, *, say):
    embed = discord.Embed(title = (f'{say}'),colour = 0xd19900 )
    embed.set_footer(text=f"9{ctx.author.id}9")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/697126125683343432/757181547907383396/PicsArt_09-20-01.08.56.png?width=499&height=499")
    await ctx.message.delete()
    channel = bot.get_channel(id=757177562156892161)
    await channel.send(embed=embed)
@tpu.error
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    embed = discord.Embed(title = f'<:error:754413108822409386>**|**ERROR',description=f"<:x_:754406625560756274>|**{prefix}tpu**\n<:0_:754406673564696637>**|{prefix}tpu (intrebare)**\n<:hmm:754410711828004948>**|{prefix}tpu cine a fost Stefan cel Mare?**",colour = discord.Colour.blue())
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def raspuns(ctx, *, say):
    embed = discord.Embed(title = (f'{say}'),colour = 0xd19900 )
    embed.set_author(name=f"{ctx.author.name}-a raspuns la o intrebare")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/697126125683343432/757181547907383396/PicsArt_09-20-01.08.56.png?width=499&height=499")
    channel = bot.get_channel(id=757177562156892161)
    await ctx.message.delete()
    await channel.send(embed=embed)
@raspuns.error
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    embed = discord.Embed(title = f'<:error:754413108822409386>**|**ERROR',description=f"<:x_:754406625560756274>|**{prefix}raspuns**\n<:0_:754406673564696637>**|{prefix}raspuns (cod intrebare) (raspuns)**\n<:hmm:754410711828004948>**|{prefix}raspuns 590963835548991508 nush ce sa zic**",colour = discord.Colour.blue())
    await ctx.send(embed=embed)

@bot.command()
async def dice(ctx, member: discord.Member):
    player1 = 0
    player2 = 0
    rounds = 1

    while rounds !=4:
        embed=discord.Embed(title=f"Round + {str(rounds)}", description=f"player1={ctx.author}\nplayer2={member}")
        msg=await ctx.send(embed=embed)
        player1 = random.choice(dice_roll)
        player2 = random.choice(dice_roll)
        embed=discord.Embed(title=f"Round + {str(rounds)}", description=f"**{ctx.author}** Roll: + {str(player1)}\n"f"**{member}** Roll: + {str(player2)}")
        asyncio.sleep(3)
        await msg.edit(embed=embed)

        if player1 == player2:
            embed1=discord.Embed(title=f"Round + {str(rounds)}", description=f"{ctx.author.mention} Roll: + {str(player1)}\n"f"{member.mention} Roll: + {str(player2)}\n==scor egal==!")
            embed1.set_image(url="https://media.discordapp.net/attachments/697126125683343432/753586009597542470/PicsArt_09-10-03.01.30.png?width=1026&height=342")
            await msg.edit(embed=embed1)
        elif player1 > player2:
            embed2=discord.Embed(title=f"Round + {str(rounds)}", description=f"{ctx.author.mention} Roll: + {str(player1)}\n"f"{member.mention} Roll: + {str(player2)}\n{ctx.author.mention}:trophy:a casigat!")
            embed2.set_image(url="https://media.discordapp.net/attachments/697126125683343432/753583039543509062/PicsArt_09-10-02.47.09.png")
            await msg.edit(embed=embed2)
        else:
            embed3=discord.Embed(title=f"Round + {str(rounds)}", description=f"{ctx.author.mention} Roll: + {str(player1)}\n"f"{member.mention} Roll: + {str(player2)}\n{member.mention}:trophy:a castigat!")
            embed3.set_image(url="https://media.discordapp.net/attachments/697126125683343432/753583488753467412/PicsArt_09-10-02.51.32.png?width=1026&height=342")
            await msg.edit(embed=embed3)

        rounds = rounds + 1

dice_roll = [1, 2, 3, 4, 5, 6]
@dice.error
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    embed = discord.Embed(title = f'<:error:754413108822409386>**|**ERROR',description=f"**<:x_:754406625560756274>|{prefix}dice**\n<:0_:754406673564696637>**|{prefix}dice (user mention)**\n<:hmm:754410711828004948>**|{prefix}dice <@658586951380893696>**",colour = discord.Colour.blue())
    embed.set_footer(text="pentru a incepe jocul este nevoie de 2 jucatori")
    await ctx.send(embed=embed)

responses = ['Este cert.','Este deci hotărât.','Fara indoiala.','Te poți baza pe asta.','După cum o văd, da.','Cel mai probabil.','Perspectivă bună.','Da.','Semnele indică da.','Răspundeți obosit, încercați din nou.','Intreaba mai tarziu.','Mai bine să nu vă spun acum.','Nu se poate prezice acum.','Concentrați-vă și întrebați din nou.','Nu te baza pe asta.','Răspunsul meu este nu.','Sursele mele spun că nu','Perspectiva nu e chiar atât de bună.','Foarte indoielnic.']
@bot.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    embed = discord.Embed(title = "**FUN8BALL**")
    embed.set_image(url='https://cdn.dribbble.com/users/264259/screenshots/1860410/attachments/313225/8-ball.gif')
    msg = await ctx.send(embed=embed)
    embed = discord.Embed(title = '_8BALL_' ,description = (f'**Question:** {question}?') ,colour = 0x6121b6)
    await asyncio.sleep(2)
    await msg.edit(embed=embed)
    embed1 = discord.Embed(title = '_8BALL_' ,description = (f'**Answer:** {random.choice(responses)}') ,colour = 0x6121b6)
    await asyncio.sleep(2)
    await msg.edit(embed=embed1)
@_8ball.error
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    embed = discord.Embed(title = f'<:error:754413108822409386>**|**ERROR',description=f"<:x_:754406625560756274>|**{prefix}8ball**\n<:0_:754406673564696637>**|{prefix}8ball (intrebare)**\n<:hmm:754410711828004948>**|{prefix}8ball Dior a lucrat mult la bot?**",colour = discord.Colour.blue())
    await ctx.send(embed=embed)

hgay = ['<:black:739059298679914516><:black:739059298679914516><:black:739059298679914516><:black:739059298679914516><:black:739059298679914516>0%',
        '<:green1:739060673291616357><:black1:739060840459796511><:black1:739060840459796511><:black1:739060840459796511><:black2:739060922055917581>20%',
        '<:green1:739060673291616357><:green2:739060756187840532><:green2:739060756187840532><:black1:739060840459796511><:black2:739060922055917581>60%',
        '<:green1:739060673291616357><:green2:739060756187840532><:green2:739060756187840532><:green2:739060756187840532><:black2:739060922055917581>80%',
        '<:green1:739060673291616357><:green2:739060756187840532><:green2:739060756187840532><:green2:739060756187840532><:black2:739060922055917581>90%',
        '<:green1:739060673291616357><:green2:739060756187840532><:green2:739060756187840532><:green2:739060756187840532><:green:739057842127896637>100%']
@bot.command()
async def howgay(ctx, say):
    embed = discord.Embed(title = (f'{random.choice(hgay)}') ,description = (f'**{say}**-:rainbow_flag:rate') ,colour = 0x6121b6)
    embed.set_thumbnail(url='https://media1.giphy.com/media/fXc70o9YOnocc0j8QO/source.gif')
    await ctx.send(embed=embed)
@howgay.error
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    embed = discord.Embed(title = f'<:error:754413108822409386>**|**ERROR',description=f"<:x_:754406625560756274>|**{prefix}howgay**\n<:0_:754406673564696637>**|{prefix}howgay (user mention)**\n<:hmm:754410711828004948>**|{prefix}howgay {ctx.author.mention}**",colour = discord.Colour.blue())
    await ctx.send(embed=embed)

@bot.command(aliases=['rr'])
async def RR(ctx, member: discord.Member):
    desc = 'JOACA RULETA RUSEASCA:gun:'
    embed = discord.Embed(
        colour=0x636363,
        title=f'{ctx.author} si {member}',
        description=desc,
    ).set_thumbnail(url="https://media1.tenor.com/images/7f0e29b98a6a55d1a126b09155398590/tenor.gif?itemid=10333376")
    msg = await ctx.send(embed=embed)

    bullets = [0] * 6
    bullets[random.randint(0, 5)] = 1

    users = [ctx.author, member]
    for i in range(0, 6):
        user = users[i % 2]
        if (bullets[i]) != 1:
            desc += f'\n`{user}` ai scapat :gun:'
            embed.description = desc
            await msg.edit(embed=embed)
        else:
            desc += f'\n`{user}` A nimerit glontul ghinionist si a murit :drop_of_blood:\nJOC TERMINAT!'
            embed.description = desc
            await msg.edit(embed=embed)
            return
        await asyncio.sleep(1)
@RR.error
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    embed = discord.Embed(title = f'<:error:754413108822409386>**|**ERROR',description=f"<:x_:754406625560756274>|**{prefix}RR**\n<:0_:754406673564696637>**|{prefix}RR (user mention)**\n<:hmm:754410711828004948>**|{prefix}RR <@658586951380893696>**",colour = discord.Colour.blue())
    await ctx.send(embed=embed)

#UTILITY COMMANDS

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=1):
        embed=discord.Embed(title=f"{amount} mesaje au fost sterse", color=0x4dff79)
        await ctx.channel.purge(limit=amount)
        msg = await ctx.send(embed=embed)
        embed1=discord.Embed(title=f"de catre {ctx.author}", color=0x4dff79)
        await asyncio.sleep(2)
        await msg.edit(embed=embed1)
        await asyncio.sleep(2)
        await msg.delete()
@clear.error
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    embed = discord.Embed(title = f'<:error:754413108822409386>**|**ERROR',description=f"<:x_:754406625560756274>|**{prefix}clear**\n<:0_:754406673564696637>**|{prefix}clear (amount)**\n<:hmm:754410711828004948>**|{prefix}clear 100**",colour = discord.Colour.blue())
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *,reason=None):
    embed = discord.Embed(title = (f':white_check_mark: |L-am dat afara pe {member.mention}'),description = '',colour = discord.Colour.green())
    await member.kick(reason=reason)
    await ctx.send(embed=embed)
@kick.error
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    embed = discord.Embed(title = f'<:error:754413108822409386>**|**ERROR',description=f"<:x_:754406625560756274>|**{prefix}kick**\n<:0_:754406673564696637>**|{prefix}kick (user mention `/` id)**\n<:hmm:754410711828004948>**|{prefix}kick {ctx.author.mention}**",colour = discord.Colour.blue())
    await ctx.send(embed=embed)



@bot.command()
@commands.has_permissions(ban_members=True)
async def mute(ctx, member : discord.Member):
  guild = ctx.guild
  for role in guild.roles:
    if role.name =="Muted":
      await member.add_roles(role)
      embed=discord.Embed(title=f"{member} a primit mute")
      msg=await ctx.send(embed=embed)
      await msg.add_reaction("🔇")
      return
@mute.error
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    embed = discord.Embed(title = f'<:error:754413108822409386>**|**ERROR',description=f"<:x_:754406625560756274>|**{prefix}mute**\n<:0_:754406673564696637>**|{prefix}mute (user mention)**\n<:hmm:754410711828004948>**|{prefix}mute {ctx.author.mention}**",colour = discord.Colour.blue())
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(ban_members=True)
async def unmute(ctx, member : discord.Member):
  guild = ctx.guild
  for role in guild.roles:
    if role.name =="Muted":
      await member.remove_roles(role)
      embed=discord.Embed(title=f"{member} a primit unmute")
      msg=await ctx.send(embed=embed)
      await msg.add_reaction("🔈")
      return
@unmute.error
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    embed = discord.Embed(title = f'<:error:754413108822409386>**|**ERROR',description=f"<:x_:754406625560756274>|**{prefix}unmute**\n<:0_:754406673564696637>**|{prefix}unmute (user mention)**\n<:hmm:754410711828004948>**|{prefix}mute {ctx.author.mention}**",colour = discord.Colour.blue())
    await ctx.send(embed=embed)


@bot.command()
async def info(ctx, member: discord.Member):

    roles = [role for role in member.roles]

    embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

    embed.set_author(name=f"{member}", icon_url="https://cdn.pixabay.com/photo/2016/04/21/13/28/info-symbol-1343394_640.png")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Informatii cerute de {ctx.author}", icon_url=ctx.author.avatar_url)

    embed.add_field(name="<:emoji_32:733975875997138944>ID:", value=member.id, inline=False)
    embed.add_field(name="<:emoji_32:733975875997138944>Guild name:", value=member.display_name, inline=False)

    embed.add_field(name=f"<:emoji_32:733975875997138944>Roles: ({len(roles)})", value= " ".join([role.mention for role in roles]), inline=False)
    embed.add_field(name="<:emoji_32:733975875997138944>Top role:", value=member.top_role.mention, inline=False)
    embed.add_field(name="<:emoji_33:733978468810752060>Bot:", value=member.bot)

    await ctx.send(embed=embed)

@info.error
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    embed = discord.Embed(title = f'<:error:754413108822409386>**|**ERROR',description=f"<:x_:754406625560756274>|**{prefix}info**\n<:0_:754406673564696637>**|{prefix}info (user mention)**\n<:hmm:754410711828004948>**|{prefix}info {ctx.author.mention}**",colour = discord.Colour.blue())
    await ctx.send(embed=embed)

@bot.command()
async def user(ctx, member: discord.Member):
   embed = discord.Embed(color=discord.Color.blue())
   embed.add_field(name="Intrat pe Discord:", value=member.created_at, inline=False)
   embed.add_field(name="Intrat pe Server:", value=member.joined_at, inline=True)
   embed.set_thumbnail(url='{}'.format(member.avatar_url))
   await ctx.send(embed=embed)
@user.error
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    embed = discord.Embed(title = f'<:error:754413108822409386>**|**ERROR',description=f"<:x_:754406625560756274>|**{prefix}user**\n<:0_:754406673564696637>**|{prefix}user (user mention)**\n<:hmm:754410711828004948>**|{prefix}user {ctx.author.mention}**",colour = discord.Colour.blue())
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def embed(ctx, *, say):
    embed = discord.Embed(title = (f'{say}'),colour = ctx.author.color )
    await ctx.message.delete()
    await ctx.send(embed=embed)
@embed.error
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    embed = discord.Embed(title = f'<:error:754413108822409386>**|**ERROR',description=f"<:x_:754406625560756274>|**{prefix}embed**\n<:0_:754406673564696637>**|{prefix}embed (mesaj)**\n<:hmm:754410711828004948>**|{prefix}embed #traiescfun dar colorat**",colour = discord.Colour.blue())
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(ban_members=True)
async def gnews(ctx,arg1, *, say):
    embed = discord.Embed(description = (f'{say}'),colour = 0x2246f2 )
    embed.set_image(url=arg1.format(arg1))
    channel = bot.get_channel(id=733034818496888953)
    await channel.send(embed=embed)

@bot.command()
@commands.has_permissions(ban_members=True)
async def anews(ctx,arg1, *,say):
    embed = discord.Embed(description = say,colour = 0xdf003e)
    embed.set_image(url=arg1.format(arg1))
    channel = bot.get_channel(id=733035333301829634)
    await channel.send(embed=embed)



apply1 = "Verifica-ti dm-ul"
@bot.command()
async def apply(ctx):
    embed = discord.Embed(title = 'Raspunde la urmatoarele intrebari folosind comanda ?sendapply urmata de raspunsurile la intrebari' ,description = '1)Numele tau real\n2)Numele tau de utilizator discord\n3)Varsta ta reala\n4)Ce level ai pe chat?\nDaca nu il stii il poti vedea pe <#726492320924696611>\n5)Ai citit regulamentul?\n6)Care este parerea ta sincera despre server?\n7)Crezi ca o sa fii responsabil ca membru staff?',colour = 0x317acc)
    embed.set_thumbnail(url="https://lh3.googleusercontent.com/proxy/EA86HjsFM1V1mgzVDqQSf9C6Aryfc6ZvHbz7RgLvfaVkGLvmjax6wToutbv5Eim3fI7yowoSHkuJXNnzVLN_V8PAOmfU1yyyTwVNOuDdttM8IsXVuUOyZPiedUZhV6F24w")
    await ctx.author.send(embed=embed)
    await ctx.send(apply1)

staff = ":white_check_mark:Cerere trimisa cu succes"
lords =  "<@457971938112045058> <@590963835548991508>"

@bot.command()
async def sendapply(ctx, *, say):
  embed = discord.Embed(colour=0x317acc, description= (f'{say}') , title = "Staff-Request")
  embed.set_thumbnail(url="https://www.kronos.co.uk/sites/default/files/images/industry/icons/15-kron-1566-kronosicons-police-corrections-bw-01.01-noloop.gif")
  embed.set_footer(text=f"Trimisa de - \nNM:{ctx.message.author.name}\nMN:{ctx.message.author.mention}")
  channel = bot.get_channel(id=726721199845015605)

  await channel.send(embed=embed)
  await channel.send(lords)
  await ctx.author.send(staff)




@bot.command()
@commands.has_permissions(ban_members=True)
async def dm(ctx, user_id=None, *,args=None):
  if user_id != None and args != None:
    try:
      target = await bot.fetch_user(user_id)
      await target.send(args)

      await ctx.channel.send("'" + args + "'mesajul i-a fost trimis cu succes lui:" + target.name)

    except:
        await ctx.channel.send("Nu am putut sa ii trimit mesaj user-ului")

  else:
    await ctx.channel.send("ID-ul user-ului sau argumentele nu sunt incluse")



#media commands
@bot.command()
async def avatar(ctx, member: discord.Member):
  embed=discord.Embed(title=f"Cerut de {ctx.author}", color=0x24ff99)
  msg = await ctx.send(embed=embed)
  show_avatar = discord.Embed(
  colour=member.color
  )
  show_avatar.set_image(url='{}'.format(member.avatar_url))
  await asyncio.sleep(2)
  await msg.edit(embed=show_avatar)
@avatar.error
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    embed = discord.Embed(title = f'<:error:754413108822409386>**|**ERROR',description=f"**<:x_:754406625560756274>|{prefix}avatar**\n<:0_:754406673564696637>**|{prefix}avatar (user mention)**\n<:hmm:754410711828004948>**|{prefix}avatar {ctx.author.mention}**",colour = discord.Colour.blue())
    await ctx.send(embed=embed)


wikiimagrandom = [1,2,3,4,5,6]
@bot.command()
async def wikisum(ctx, *,userInput):
    try:
            await ctx.send(format(wikipedia.summary(userInput,sentences=4)))
            picFind = wikipedia.page(userInput)
            await ctx.send(picFind.images[random.choice(wikiimagrandom)])
    except wikipedia.exceptions.DisambiguationError as e:
            await ctx.send(format(("Error: {0}".format(e))))

left = '⏪'
right = '⏩'

partner = (
" \n> **:pushpin: 1. Parteneriatul trebuie pus cu everyone fară edit sau alte mijloace de a nu da ping.**" ,

" \n> **:pushpin: 2. Pentru a avea parteneriat cu noi aveți nevoie de minim 100 de membri** " ,

" \n> **:pushpin: 3. Trebuie să fiți activi pe server și după parteneriat, nu doar de frumusețe!** ",

" \n> **:pushpin: 4. Serverul dvs. nu trebuie să incite la rasism/pornografie și  modalități de discriminare **" ,

" \n> **:pushpin: 5. Parteneriatele sunt verificate odata pe saptamana, daca va fi sters linkul de la serverul acesta, parteneriatul va fi anulat instant!**" ,


)

def predicate(message, l, r):
    def check(reaction, user):
        if reaction.message.id != message.id or user == bot.user:
            return False
        if l and reaction.emoji == left:
            return True
        if r and reaction.emoji == right:
            return True
        return False

    return check


@bot.command(pass_context=True)
async def parteneriat(ctx):
    index = 0
    msg = None
    action = ctx.send
    while True:
        res = await action(content=partner[index])
        if res is not None:
            msg = res
        l = index != 0
        r = index != len(partner) - 1
        if l:
            await msg.add_reaction(left)
        if r:
            await msg.add_reaction(right)
        react, user = await bot.wait_for('reaction_add', check=predicate(msg, l, r))
        if react.emoji == left:
            index -= 1
        elif react.emoji == right:
            index += 1
        action = msg.edit

#HELP COMMAND
@bot.command()
async def help(ctx):
     embed=discord.Embed(color=0x0091c2)
     embed.add_field(name="<:fun:731787306150658049>FUN", value="?help_fun", inline=True)
     embed.add_field(name="<:games:731786219939168318>Games", value="?help_games", inline=True)
     embed.add_field(name="<:tool:717089742163935245>Utility", value="?help_utility", inline=True)
     embed.add_field(name="<:media:731788127760547850>Media", value="?help_media", inline=True)
     embed.set_footer(text="Scrie ?allcommands sau ?allcmds pentru a obține o listă cu toate comenzile.")
     await ctx.send(embed=embed)


@bot.command(aliases=['allcmds'])
async def allcommands(ctx):
     fcmd=discord.Embed(title="<:fun:731787306150658049>FUN COMMANDS", color=0xf1f720)
     fcmd.add_field(name="▪ping", value="pong 100000ms", inline=False)
     fcmd.add_field(name="▪︎choose", value="mere sau pere?", inline=False)
     fcmd.add_field(name="▪︎aduna", value="1 1=2", inline=False)
     fcmd.add_field(name="▪︎scade", value="2 1=1", inline=False)
     fcmd.add_field(name="▪︎sayd", value="sayd", inline=False)
     fcmd.add_field(name="▪︎howgay", value="100%", inline=False)
     fcmd.set_image(url="https://media.discordapp.net/attachments/691360396539330611/731067951431680000/PicsArt_07-10-11.42.37.png?width=995&height=332")

     gcmd=discord.Embed(title="<:games:731786219939168318>Games", color=0xee331e)
     gcmd.add_field(name="▪︎8ball", value="o comanda interesanta, intreaba bot-ul si va raspunde", inline=False)
     gcmd.add_field(name="▪︎dice", value="zaruri", inline=False)
     gcmd.add_field(name="▪︎RR", value="Ruleta Ruseasca", inline=False)
     gcmd.add_field(name="▪︎nrguess", value="ghiceste numarul", inline=False)
     gcmd.add_field(name="▪︎among_us", value="Impostor", inline=False)
     gcmd.set_image(url="https://media.discordapp.net/attachments/691360396539330611/731076083721437184/PicsArt_07-10-12.15.11.png?width=995&height=335")

     ucmd=discord.Embed(title="<:tool:717089742163935245>Utility(comenzile de moderare sunt in mentenanta)", color=0xc0c0c0)
     ucmd.add_field(name="▪︎info", value="user info", inline=False)
     ucmd.add_field(name="▪︎user", value="afla cand a fost creat contul unui user", inline=False)
     ucmd.add_field(name="▪︎clear", value="sterge messajele in masa", inline=False)
     ucmd.add_field(name="▪︎kick", value="da afara un user de pe server", inline=False)
     ucmd.add_field(name="▪︎ban", value="baneaza un user", inline=False)
     ucmd.add_field(name="▪︎unban", value="da unban unui user", inline=False)
     ucmd.add_field(name="▪︎mute", value="interzice accesul de a scrie unui user", inline=False)
     ucmd.add_field(name="▪︎unmute", value="reda accesul de a scrie", inline=False)
     ucmd.add_field(name="▪︎dm", value="trimite dm unui user", inline=False)
     ucmd.add_field(name="▪︎embed", value="creeaza un embed", inline=False)
     ucmd.set_image(url="https://media.discordapp.net/attachments/691360396539330611/731077116627779615/PicsArt_07-10-12.19.19.png?width=995&height=311")

     mcmd=discord.Embed(title="<:media:731788127760547850>Media", color=0x2fb0ad)
     mcmd.add_field(name="▪︎avatar", value="vezi mai usor avatarul unui user", inline=False)
     mcmd.add_field(name="▪︎wikisum", value="wikipedia", inline=False)
     mcmd.set_image(url="https://media.discordapp.net/attachments/691360396539330611/731080335533801513/PicsArt_07-10-12.32.07.png?width=995&height=291")

     hcmd=discord.Embed(title="", color=0xfab30c)
     hcmd.set_image(url="https://media.discordapp.net/attachments/691360396539330611/731082476256231424/PicsArt_07-10-12.40.29.png?width=995&height=253")


     lcmd=discord.Embed(title="")
     lcmd.set_image(url="https://media.discordapp.net/attachments/691360396539330611/731084601988218910/PicsArt_07-10-12.48.56.png?width=995&height=278")

     scmd=discord.Embed(description= "`apply(staff)`,`parteneriat(rules)`" ,title="Comenzi disponibile doar pe serverul FUN4FUN")

     await ctx.send(embed=hcmd)
     await ctx.author.send(embed=lcmd)
     await ctx.author.send(embed=fcmd)
     await ctx.author.send(embed=gcmd)
     await ctx.author.send(embed=ucmd)
     await ctx.author.send(embed=mcmd)
     await ctx.author.send(embed=scmd)

@bot.command()
async def help_fun(ctx):
     fcmd=discord.Embed(title="<:fun:731787306150658049>FUN COMMANDS", color=0xf1f720)
     fcmd.add_field(name="▪︎ping", value="pong 100000ms", inline=False)
     fcmd.add_field(name="▪︎choose", value="mere sau pere?", inline=False)
     fcmd.add_field(name="▪︎aduna", value="undefined", inline=False)
     fcmd.add_field(name="▪︎scade", value="undefined", inline=False)
     fcmd.add_field(name="▪︎sayd", value="undefined", inline=False)
     fcmd.add_field(name="▪︎howgay", value="100%", inline=False)
     fcmd.set_image(url="https://media.discordapp.net/attachments/691360396539330611/731067951431680000/PicsArt_07-10-11.42.37.png?width=995&height=332")
     await ctx.send(embed=fcmd)

@bot.command()
async def help_games(ctx):
     gcmd=discord.Embed(title="<:games:731786219939168318>Games", color=0xee331e)
     gcmd.add_field(name="▪︎8ball", value="o comanda interesanta, intreaba bot-ul si va raspunde", inline=False)
     gcmd.add_field(name="▪︎dice", value="zaruri", inline=False)
     gcmd.add_field(name="▪︎RR", value="Ruleta Ruseasca", inline=False)
     gcmd.add_field(name="▪︎nrguess", value="ghiceste numarul", inline=False)
     gcmd.add_field(name="▪︎among_us", value="Impostor", inline=False)
     gcmd.set_image(url="https://media.discordapp.net/attachments/691360396539330611/731076083721437184/PicsArt_07-10-12.15.11.png?width=995&height=335")
     await ctx.send(embed=gcmd)

@bot.command()
async def help_utility(ctx):
     ucmd=discord.Embed(title="<:tool:717089742163935245>Utility(comenzile de moderare sunt in mentenanta)", color=0xc0c0c0)
     ucmd.add_field(name="▪︎info", value="user info", inline=False)
     ucmd.add_field(name="▪︎user", value="afla cand a fost creat contul unui user", inline=False)
     ucmd.add_field(name="▪︎clear", value="sterge messajele in masa", inline=False)
     ucmd.add_field(name="▪︎kick", value="da afara un user de pe server", inline=False)
     ucmd.add_field(name="▪︎ban", value="baneaza un user", inline=False)
     ucmd.add_field(name="▪︎unban", value="da unban unui user", inline=False)
     ucmd.add_field(name="▪︎mute", value="interzice accesul de a scrie unui user", inline=False)
     ucmd.add_field(name="▪︎unmute", value="reda accesul de a scrie", inline=False)
     ucmd.add_field(name="▪︎dm", value="trimite dm unui user", inline=False)
     ucmd.add_field(name="▪︎embed", value="creaza un embed", inline=False)
     ucmd.set_image(url="https://media.discordapp.net/attachments/691360396539330611/731077116627779615/PicsArt_07-10-12.19.19.png?width=995&height=311")
     await ctx.send(embed=ucmd)

@bot.command()
async def help_media(ctx):
     mcmd=discord.Embed(title="<:media:731788127760547850>Media", color=0x2fb0ad)
     mcmd.add_field(name="▪︎avatar", value="vezi mai usor avatarul unui user", inline=False)
     mcmd.add_field(name="▪︎wikisum", value="wikipedia", inline=False)
     mcmd.set_image(url="https://media.discordapp.net/attachments/691360396539330611/731080335533801513/PicsArt_07-10-12.32.07.png?width=995&height=291")
     await ctx.send(embed=mcmd)

bot.run('TOKEN')
