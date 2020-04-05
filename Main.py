import discord
import os
from discord.ext import commands, tasks
from itertools import cycle

prefix = 'i/'
bot = commands.Bot(command_prefix = prefix)

bot.remove_command('help')

status = cycle(['Infinite Truckers KR.PY', f'{prefix}도움말'])

@bot.event
async def on_ready():
    change_status.start()
    print(f'{bot.user.name}#{bot.user.discriminator} 으로 로그인 중... / 봇 고유 ID : {bot.user.id}')

@tasks.loop(seconds = 10)
async def change_status():
    await bot.change_presence(activity = discord.Game(next(status)))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        NotFound = discord.Embed(title = "명령어 오류", color = discord.Colour.red(), timestamp = ctx.message.created_at)
        NotFound.set_footer(text = ctx.author)
        NotFound.add_field(name = f"{error}", value = "명령어를 확인 후 재사용해주세요.")
        outmsg = await ctx.send(embed = NotFound)
        await outmsg.delete(delay = 20)


@bot.event
async def on_member_join(member):

    mention = member.mention
    guild = member.guild
    #await member.create_dm()
    #await member.dm_channel.send(str(f"{mention}님, {guild}에 오신걸 환영합니다!").format(mention=mention, guild = guild))

    join = discord.Embed(title="**New Member 등장 :weav:!**", description=f"{member}님이 {guild}에 들어오셨습니다!", color=discord.Colour.green())

    join.set_thumbnail(url=f"{member.avatar_url}")
    join.set_author(name=f"{member.display_name}", icon_url=f"{member.avatar_url}")
    join.set_footer(text=f"{guild.name}",icon_url=f"{guild.icon_url}")
    join.timestamp = datetime.datetime.utcnow()

    join.add_field(name="사용자 닉네임",value=f"{member.display_name}#{member.discriminator}",inline=False)
    join.add_field(name="사용자 ID",value=member.id, inline=False)
    join.add_field(name="서버 이름",value=guild.name, inline=False)
    join.add_field(name="서버 총 인원수(Bot 포함)",value=len(list(guild.members)),inline=False)
    join.add_field(name='서버 입장 시간 :', value = member.joined_at.strftime("%Y년 %m월 %d일 %H시 %M분.".encode("unicode-escape").decode()).encode().decode("unicode-escape"), inline = False)

    channel = discord.utils.get(member.guild.channels, id =int("694915936033046659"))
    await channel.send(embed=embed)

@bot.event
async def on_member_remove(member):

    mention = member.mention
    guild = member.guild

    embed = discord.Embed(title = "***Member 퇴장***", description = f"{member}님이 {guild}에서 나가셨습니다!", color = discord.Colour.green())

    remove.set_thumbnail(url=f"{member.avatar_url}")
    remove.set_author(name=f"{member.display_name}", icon_url=f"{member.avatar_url}")
    remove.set_footer(text=f"{guild.name}",icon_url=f"{guild.icon_url}")
    remove.timestamp = datetime.datetime.utcnow()

    remove.add_field(name="사용자 닉네임",value=f"{member.display_name}#{member.discriminator}",inline=False)
    remove.add_field(name="사용자 ID",value=member.id,inline=False)
    remove.add_field(name="서버 이름",value=guild.name,inline=False)
    remove.add_field(name="서버 총 인원수(Bot 포함)",value=len(list(guild.members)),inline=False)

    channel = discord.utils.get(member.guild.channels, id =int("694915936033046659"))
    await channel.send(embed = remove)

@bot.command(aliases = ['핑'])
async def Ping(ctx):

    embed = discord.Embed(colour= 0X1C8ADB, timestamp = ctx.message.created_at)
    embed.set_footer(text=f'{ctx.author}', icon_url = f'{ctx.author.avatar_url}')

    embed.add_field(name=':ping_pong: **Pong**!',value=f'__**{round(bot.latency * 1000)}ms!**__')

    outmsg = await ctx.send(embed = embed)
    await outmsg.delete(delay = 20)
    await ctx.message.delete()

@bot.command(aliases = ['IFMP_서버상태'])
async def IFMP_Status(ctx):
    response = requests.get('https://status.infinitetruckers.com/')
    readerhtml = response.text
    soup = BeautifulSoup(readerhtml, 'lxml')
    data1 = soip.find('div', class_= 'group-itmes')
    Website_Staus =


    page1 = discord.Embed(title = 'Web Ops', colour = 0X, timestamp = ctx.message.created_at )
    page1.set_footer(text = f'{ctx.author} • Page 1 / 4', icon_url = ctx.author.avatar_url)
    page1.set_thumbnail(url = '')
    page1.add_field(name = 'Website', value = '', inline = False)
    page1.add_field(name = 'API', value = '', inline = False)
    page1.add_field(name = 'Discord Bots', value = , inline = False)
    page1.add_field(name = 'Forum', value = , inline = False)

    page2 = discord.Embed(title = 'Game Servers', colour = 0X, timestamp = ctx.message.created_at)
    page2.set_footer(text = f'{ctx.author} • Page 2 / 4', icon_url = ctx.author.avatar_url)
    page2.set_thumbnail(url = '')
    page2.add_field(name = 'EU Servers', value = , inline = False)
    page2.add_field(name = 'Client Updater', value = , inline = False)

    page3 = discord.Embed(title='Exteranl', colour = 0X, timestamp = ctx.message.created_at)
    page3.set_footer(text = f'{ctx.author} • Page 3 / 4', icon_url = ctx.author.avatar_url)
    page3.set_thumbnail(url = '')
    page3.add_field(name = 'Discord',value = , inline = False)
    page3.add_field(name = 'Cloudflare',value = , inline = False)

    page4 = discord.Embed(title='Staff Ops', description='', colour= 0X, timestamp = ctx.message.created_at)
    page4.set_footer(text = f'{ctx.author} • Page 4 / 4', icon_url = ctx.author.avatar_url)
    page4.set_thumbnail(url = '')
    page4.add_field(name = 'Operations',value= ,inline = False)

    pages = [page1, page2, page3, page4]

    message = await ctx.send(embed = page1)
    await ctx.message.delete()

    await message.add_reaction('\u23ee')
    await message.add_reaction('\u25c0')
    await message.add_reaction('\u25b6')
    await message.add_reaction('\u23ed')

    i = 0
    emoji = ''

    while True:
            try:
                reaction, user = await bot.wait_for('reaction_add', timeout=30.0)

                if user == ctx.author:
                    emoji = str(reaction.emoji)

                    if emoji == '\u23ee':
                        i = 0
                        await message.edit(embed=pages[i])
                    elif emoji == '\u25c0':
                        if i > 0:
                            i -= 1
                            await message.edit(embed=pages[i])

                    elif emoji == '\u25b6':
                        if i < 3:
                            i += 1
                            await message.edit(embed=pages[i])

                    elif emoji == '\u23ed':
                        i = 3
                        await message.edit(embed=pages[i])

                if bot.user != user:
                    await message.remove_reaction(reaction, user)

            except asyncio.TimeoutError:
                break

    await message.clear_reactions()

@bot.command(aliases = ['공식_유튜버'])
async def Youtuber(ctx):

        page1 = discord.Embed(title='게임 클래스', description='IFMP KR 공식 유튜버', colour = 0XEFE417, timestamp = ctx.message.created_at )

        page1.set_footer(text = f'{ctx.author} • Page 1 / 4', icon_url = ctx.author.avatar_url)
        page1.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/608275359024152593/692728035526311936/6078a81b8676582e.jpg')

        page1.add_field(name = '게임클래스 Link',value= '''YouTuber : [Text Link](https://www.youtube.com/channel/UC9hFVidRTbrjDyTZGe1KAJA)\n
                                                          Discord : [Text link](https://discord.gg/Pt8JmXR)''',inline = False)

        page2 = discord.Embed(title='TGR KOREA', description='IFMP KR 공식 유튜버', colour = 0XFF8C0A, timestamp = ctx.message.created_at)

        page2.set_footer(text = f'{ctx.author} • Page 2 / 4', icon_url = ctx.author.avatar_url)
        page2.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/608275359024152593/692728076798394598/T1.jpg')

        page2.add_field(name = 'TGR KOREA Link',value= '''Youtube : [Text link](https://www.youtube.com/channel/UCA0dhdxmlr9lhKtsNCH0Pcg/featured)\n
                                                          Discord : [Text link](https://discordapp.com/invite/8QRFNH8)\n
                                                          Naver Cafe : [Text link](https://cafe.naver.com/tgrkorea)''',inline = False)

        page3 = discord.Embed(title='레빈 LEVIN', description='IFMP KR 공식 유튜버', colour = 0X0F2F55, timestamp = ctx.message.created_at)

        page3.set_footer(text = f'{ctx.author} • Page 3 / 4', icon_url = ctx.author.avatar_url)
        page3.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/608275359024152593/692728224471449690/AZ_Family.png')

        page3.add_field(name = '레빈 LEVIN Link',value= '''Youtube : [Text link](https://www.youtube.com/channel/UCHwJOTqwpgMw4vUlJdMVnHA)\n
                                                           Twitch : [Text link](https://www.twitch.tv/levin_able)\n
                                                           Discord : [Text link](https://discordapp.com/invite/SVe8FQw)''', inline = False)

        page4 = discord.Embed(title='레알마틴', description='IFMP KR 공식 유튜버', colour= 0Xa828a8, timestamp = ctx.message.created_at)

        page4.set_footer(text = f'{ctx.author} • Page 4 / 4', icon_url = ctx.author.avatar_url)
        page4.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/608275359024152593/692728021026734090/Real.jpg')

        page4.add_field(name = '레알마틴 Link',value= '''Youtube : [Text link](https://www.youtube.com/channel/UCCGp3bC6NtJTlv6baWXEarA)\n
                                                        Twitch : [Text link](https://www.twitch.tv/daddyrealmartin)''',inline = False)

        pages = [page1, page2, page3, page4]

        message = await ctx.send(embed = page1)
        await ctx.message.delete()

        await message.add_reaction('\u23ee')
        await message.add_reaction('\u25c0')
        await message.add_reaction('\u25b6')
        await message.add_reaction('\u23ed')

        i = 0
        emoji = ''

        while True:
               try:
                   reaction, user = await bot.wait_for('reaction_add', timeout=30.0)

                   if user == ctx.author:
                       emoji = str(reaction.emoji)

                       if emoji == '\u23ee':
                           i = 0
                           await message.edit(embed=pages[i])
                       elif emoji == '\u25c0':
                           if i > 0:
                               i -= 1
                               await message.edit(embed=pages[i])

                       elif emoji == '\u25b6':
                           if i < 3:
                               i += 1
                               await message.edit(embed=pages[i])

                       elif emoji == '\u23ed':
                           i = 3
                           await message.edit(embed=pages[i])

                   if bot.user != user:
                       await message.remove_reaction(reaction, user)

               except asyncio.TimeoutError:
                   break

        await message.clear_reactions()


access_token = os.environ["BOT_TOKEN"]
bot.run(access_toke)
