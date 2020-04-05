import discord
import os
import random
import datetime
import asyncio
from discord.ext import commands, tasks
from itertools import cycle

prefix = '?'
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

    await member.create_dm()
    await member.dm_channel.send(f'''{mention}님, **{guild}**에 오신걸 환영합니다! 한국 커뮤니티를 이용하기 전, <#681767040868286485> 꼭 정독 해주시길 바랍니다.

커뮤니티 이용약관 미확인 및 미준수는 커뮤니티에서 불이익을 받습니다. 또한 미확인는 본인과실로 인정됩니다.

본 커뮤니티는 디스코드 보안 수준은 **중간** 설정되어 있어, 다음과 같은 조건이 되야 커뮤니티를 이용 하실 수 있습니다.

> Discord 이메일 인증
> Discord 가입 5분 경과

<@695586206934630441> 관련 질문은 <@444877320415870978> 에게 개인 DM을 해주시길 바랍니다.''')

    join = discord.Embed(title = f':wave: {member.name}님, {guild}에 오신걸 환영합니다! :tada: 아래의 내용을 읽어주세요.',
                        description = '''커뮤니티 설명: <#682171748044505088>
                        커뮤니티 이용약관: <#681767040868286485>
                        역할부여: <#681729626170851463>
                        도움: <#681728271842541582>
                        커뮤니티 카페: **https://cafe.naver.com/ifmp**''',
                        color=discord.Colour.green())

    join.set_thumbnail(url = member.avatar_url)
    join.set_author(name = guild.name, icon_url = guild.icon_url)
    join.timestamp = datetime.datetime.utcnow()


    channel = discord.utils.get(member.guild.channels, id = int("681696646039339033"))
    await channel.send(embed = join, content = '<@695586206934630441> 개인 DM을 확인해주세요. 감사합니다')

@bot.event
async def on_member_remove(member):

    guild = member.guild

    remove = discord.Embed(title = f'{member}님이, {guild}에서 나가셨습니다.', description ='잘가요! 그동안 이용해 주셔서 감사합니다!',color=discord.Colour.red())
    remove.timestamp = datetime.datetime.utcnow()

    channel = discord.utils.get(member.guild.channels, id = int("681696646039339033"))
    await channel.send(embed = remove)

@bot.event # 수정 필요
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 689731507702726657:
        channel = bot.get_channel(681729626170851463)
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

        if payload.emoji.name == 'Yes':
            role = discord.utils.get(guild.roles, name = '회원')
        elif payload.emoji.name == 'Youtube':
            role = discord.utils.get(guild.roles, name = 'Youtube')
        elif payload.emoji.name == 'Youtube':
            role = discord.utils.get(guild.roles, name = 'Youtube')
        elif payload.emoji.name == 'Youtube':
            role = discord.utils.get(guild.roles, name = 'Youtube')
        elif payload.emoji.name == 'Youtube':
            role = discord.utils.get(guild.roles, name = 'Youtube')
        else:
            role = discord.utils.get(guild.roles, name = payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
                outmsg = await member.send(f'{member}님 {role} 역할이 추가되었습니다.')
                await outmsg.delete(delay = 10)
            else:
                print('Member not found.')
        else:
            print('Role not found.')

@bot.event # 수정 필요
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 689735261655007260:
        channel = bot.get_channel(681729626170851463)
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

        if payload.emoji.name == 'Youtube':
            role = discord.utils.get(guild.roles, name = '스트리머')
        elif payload.emoji.name == 'Youtube':
            role = discord.utils.get(guild.roles, name = 'Youtube')
        elif payload.emoji.name == 'Youtube':
            role = discord.utils.get(guild.roles, name = 'Youtube')
        elif payload.emoji.name == 'Youtube':
            role = discord.utils.get(guild.roles, name = 'Youtube')
        else:
            role = discord.utils.get(guild.roles, name = payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
                outmsg = await member.send(f'{member}님 {role} 역할이 추가되었습니다.')
                await outmsg.delete(delay = 10)
            else:
                print('Member not found.')
        else:
            print('Role not found.')

@bot.event # 수정 필요
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 689731507702726657:
        channel = bot.get_channel(681729626170851463)
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

        if payload.emoji.name == 'Yes':
            role = discord.utils.get(guild.roles, name = '회원')
        elif payload.emoji.name == 'Youtube':
            role = discord.utils.get(guild.roles, name = 'Youtube')
        else:
            role = discord.utils.get(guild.roles, name = payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
                outmsg = await member.send(f'{member}님 {role} 역할이 삭제되었습니다.')
                await outmsg.delete(delay = 10)
            else:
                print('Member not found.')
        else:
            print('Role not found.')

@bot.command(aliases = ['도움말']) # 수정 필요
async def Help(ctx):

    bot_prefix = prefix

    help = discord.Embed(title = f'**{bot.user.name}** 도움말', timestamp = ctx.message.created_at, colour = 0X1C8ADB)

    help.set_footer(text = ctx.author, icon_url = ctx.author.avatar_url)
    help.set_thumbnail(url = bot.user.avatar_url)

    help.add_field(name = f'**{prefix}도움말**', value = '현재 사용한 명령어이며, BOT의 정보를 알 수 있다.', inline = False)
    help.add_field(name = f'**{prefix}관리자_도움말**', value = '서버 관리자만 사용 할 수 있는 명령어 목록이다..', inline = False)
    help.add_field(name = f'**{prefix}명령어**', value = 'https://discord.gg/link 확인해 주시길 바랍니다.', inline = False)
    help.add_field(name = f'**{prefix}핑**', value = 'Bot의 최근 통신상태 (ms) 확인할 수 있습니다.', inline = False)
    help.add_field(name = f'**{prefix}유저정보 @멘션(언급)**', value = '본인 혹은 다른 이용자의 디스코드 정보를 얻을 수 있습니다.', inline = False)
    help.add_field(name = f'**{prefix}서버정보**', value = '현재 명령어를 사용한 디스코드 서버 정보를 얻을 수 있습니다.', inline = False)
    help.add_field(name = f'**{prefix}봇정보**', value = 'Discord Bot의 정보를 알려드립니다.')
    help.add_field(name = f'**{prefix}공식_유튜버**', value = 'IFMP KR 공식 유튜버 관련 링크를 얻을 수 있습니다.', inline = False)

    outmsg = await ctx.send(embed = help)
    await outmsg.delete(delay = 20)
    await ctx.message.delete()

@bot.command(aliases = ['관리자_도움말'])  # 수정 필요
async def Admin_Help(ctx):

    bot_prefix = prefix

    admin_help = discord.Embed(title = f'**{bot.user.name}** 관리자 도움말', timestamp = ctx.message.created_at, colour = 0X1C8ADB)

    admin_help.set_footer(text = ctx.author, icon_url = ctx.author.avatar_url)
    admin_help.set_thumbnail(url = bot.user.avatar_url)

    admin_help.add_field(name = f'**{prefix}청소 (개수)**', value = '관리자의 경우, 채널의 메세지를 삭제 할 수 있습니다.', inline = False)
    admin_help.add_field(name = f'**{prefix}킥 @멘션(언급)**', value = '관리자의 경우, 멘션한 인원을 서버 추방 할 수있습니다.', inline = False)
    admin_help.add_field(name = f'**{prefix}밴 @멘션(언급)**', value = '관리자의 경우, 멘션한 인원을 영구 추방 할 수있습니다.', inline = False)

    outmsg = await ctx.send(embed = admin_help)
    await outmsg.delete(delay = 20)
    await ctx.message.delete()

@bot.command(aliases = ['핑'])
async def Ping(ctx):

    embed = discord.Embed(colour= 0X1C8ADB, timestamp = ctx.message.created_at)
    embed.set_footer(text=f'{ctx.author}', icon_url = f'{ctx.author.avatar_url}')

    embed.add_field(name=':ping_pong: **Pong**!',value=f'__**{round(bot.latency * 1000)}ms!**__')

    outmsg = await ctx.send(embed = embed)
    await outmsg.delete(delay = 20)
    await ctx.message.delete()

@bot.command(aliases = ['유저정보']) # 수정 필요
async def Userinfo(self, ctx, member : discord.Member = None ):

    member = ctx.author if not member else member
    roles = [role for role in member.roles]

    statuses = {"online": "<:Online:692919461912772629> 온라인",
                "idle": "<:Idle:692919461954715717> 자리비움",
                "dnd": "<:DND:692919461748932609> 다른 용무 중",
                "offline": "<:Offline:692919461581160459> 오프라인"}

    userinfo = discord.Embed(color = 0x5AD2FF, timestamp = ctx.message.created_at)

    status= statuses[f'{member.status}']

    userinfo.set_author(name = f'{member} - 디스코드 프로필')
    userinfo.set_thumbnail(url = member.avatar_url)
    userinfo.set_footer(text=f'요청자 - {ctx.author}',icon_url= ctx.author.avatar_url)

    userinfo.add_field(name = ':id: 디스코드 고유:', value = member.id, inline = False)
    userinfo.add_field(name = '<:Discord:692919461757583381> 닉네임 :', value = member.name+" #"+member.discriminator, inline = True)
    userinfo.add_field(name = '<:Discord:692919461757583381> 서버 닉네임 :', value = member.display_name+" #"+member.discriminator, inline = True)
    userinfo.add_field(name = '사용자 상태', value = str(status),inline = False)
    #userinfo.add_field(name = ':video_game: 게임', value = member.game, inline = False)
    userinfo.add_field(name = ':inbox_tray: 디스코드 생성일 :', value = member.created_at.strftime("%Y년 %m월 %d일".encode("unicode-escape").decode()).encode().decode("unicode-escape"), inline = False)
    userinfo.add_field(name = ':inbox_tray: 서버 입장일 :', value = member.joined_at.strftime("%Y년 %m월 %d일".encode("unicode-escape").decode()).encode().decode("unicode-escape"), inline = False)
    userinfo.add_field(name = ':robot: 봇 확인 :', value=("봇 맞습니다." if member.bot else "사람입니다."), inline = False)
    #userinfo.add_field(name = '이용자 활동',value = customActivity.name,inline=False)

    userinfo2 = discord.Embed(title=f'{member} 님의 역할 ({len(roles)})개', description = " ".join([role.mention for role in roles]), color = 0x5AD2FF, timestamp= ctx.message.created_at)
    #embed.add_field(name = "`최상위 역할` :", value = member.top_role.mention, inline = False)

    await ctx.send(embed=userinfo)
    await ctx.send(embed=userinfo2)

@bot.command(aliases = ['서버정보']) # 수정 필요
async def Serverinfo(self, ctx):

    guild = ctx.message.guild

    countrys = {"brazil" : ":flag_br: 브라질",
                "europe":":flag_eu: 유럽",
                "hongkong" : "flag_hk 홍콩",
                "india" : ":flag_in: 인도",
                "japan" : "flag_jp 일본",
                "russia" : "flag_ru 러시아",
                "singapore" : ":flag_sg: 싱가포르",
                "southafrica" : ":flag_za: 남아메리카",
                "south-korea" : ":flag_kr: 대한민국",
                "sydeny" : ":flag_au: 호주",
                "us-central" : ":flag_us: 미국 중부",
                "us-east" : ":flag_us: 미국 동부",
                "us-south" : ":flag_us: 미국 남부",
                "us-west" : ":flag_us: 미국 서부"
                }

    serverinfo = discord.Embed(colour = 0x1C8ADB, timestamp=ctx.message.created_at)

    region = countrys[f'{guild.region}']

    serverinfo.set_author(name=f"{guild} - 서버 정보 ", )
    serverinfo.set_thumbnail(url = ctx.message.guild.icon_url)
    serverinfo.set_footer(text = ctx.author, icon_url=ctx.author.avatar_url)

    serverinfo.add_field(name = ':crown: 디스코드 Owner :', value = f'**{ctx.guild.owner.display_name}#{ctx.guild.owner.discriminator}\n{ctx.guild.owner.id}**', inline = False)
    serverinfo.add_field(name = ':earth_asia: 서버 지역 :', value = str(region), inline=False)
    serverinfo.add_field(name = ':id: 서버 고유 :', value = ctx.guild.id, inline=False)
    serverinfo.add_field(name = ':birthday: 서버 생성일 : ', value=ctx.guild.created_at.strftime("%Y년 %m월 %d일".encode("unicode-escape").decode()).encode().decode("unicode-escape"), inline=False)
    serverinfo.add_field(name = "서버 인원 수", value=f'**총 인원 : {guild.member_count}명 | 회원 : {len([Member for Member in guild.members if not Member.bot])}명 | 봇 : {len([Member for Member in guild.members if Member.bot])}명**', inline=False)
    serverinfo.add_field(name = '서버 채널 수', value = f'**카테고리 : {len(guild.categories)}개 | 채팅 : {len(guild.text_channels)}개 | 음성 : {len(guild.voice_channels)}개**',inline=False)
    serverinfo.add_field(name = '시스템 채널',value = guild.system_channel,inline=False)
    #serverinfo.add_field(name = '규칙 채널',value = guild.rules_channel, inline=False)
    serverinfo.add_field(name = ":alarm_clock: 음성 AFK 시간", value = f'{(guild.afk_timeout//60)}분 ', inline=True)
    serverinfo.add_field(name = ":zzz: 음성 AFK 채널", value=str(guild.afk_channel), inline=False)
    serverinfo.add_field(name = '<:Nitro:693001752210964500> 니트로 등급 :', value = f'**{ctx.guild.premium_tier} 레벨**', inline = False)
    serverinfo.add_field(name = '<:Nitro:693001752210964500> 니트로 횟수 :', value = f'**{ctx.guild.premium_subscription_count} 번**', inline = False)

    await ctx.send(embed=serverinfo)

@bot.command(aliases = ['봇정보']) # 수정 필요
async def Botinfo(self, ctx):

    embed= discord.Embed(colour = 0x1C8ADB, timestamp=ctx.message.created_at)

    guilds = len([s for s in bot.guilds])

    embed.add_field(name= 'server count',value = guilds, inline = False)
    botinfo.add_field(name = 'BOT 언어', value = '<:Python:693356792180375583> **PYTHON**')

    await ctx.send(embed=embed)

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

bot.run('')
