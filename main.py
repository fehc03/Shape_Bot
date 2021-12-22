# Application ID = 860977362195841045
# Token = ODYwOTc3MzYyMTk1ODQxMDQ1.YODFpw.M4aKArgPUjx4c1yPwXnMlUp_XyU
# https://discord.com/api/oauth2/authorize?client_id=860977362195841045&permissions=2151152192&scope=bot

from asyncio import events
from functools import total_ordering
from re import S
from discord import channel, guild, message, voice_client
from discord.colour import Color
from discord.ext import commands
import random
import discord
from discord.utils import get
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
import requests


####### Data

food = ["ผัดกระเพรา","ก๋วยเตี๋ยว","ผัดซิอิ้ว","ข้าวผัด","เย็นตาโฟ","สุกี้แห้ง","แกงจืดเต้าหู้หมูสับ"
        ,"หอยทอด","ยำวุ้นเส้น","ราดหน้า","ไข่เจียว","ไข่ตุ๋นหมูสับ","ยำวุ้นเส้น"]

ty = ["ดีไหม  😚 ","ก็น่าจะดีนะ  🤪","อร่อยเเน่เรารับประกัน  🤩 ","ก็อร่อยดีนะ  👍","ลองไหมม  🤩"]

game = ["Phantasy Star Online 2: New Genesis พึ่งเปิดเลยนะ  🤩","Blue Protocol ตอนนี้ยังไม่เปิดในไทย  😕","Apex Legends อย่าพึ่งเบื่อนะ  🤪",
        "Warzone อีกสักครั้งดีไหม  😎","CS:GO คืนสู่เหย้าไป!! ","Escape From Tarkov ตื่นเต้นดีนะ  😜","Overwatch อย่าลืมน้องนะ  😭","PUBG ยังไม่เบื่อกันเนอะ",
        "Rainbow Six Siege  เข้าเกมส์เลยย!! ","Dota 2 มาเล่นกัน  🤤","League of Legends เข้าเกมส์เลย  🤠","Fortnite สนุกเลยแหละ 🤩"]

sad = ["เดี๋ยวมันก็ผ่านไปนะ  🥰","เราทำดีที่สุดแล้ว  😁","มันคือบทเรียนที่แสนวิเศษเลยนะ  🥳","ความท้าทายทำให้เราเข้มแข็ง  🙂 ","เราจะไม่เดียวดายเมื่อเกิดปัญหา  😚"
        ,"ใคร ๆ ก็เจอปัญหาด้วยกันทั้งนั้นสู้ๆ  😋",]

bot = commands.Bot (command_prefix = "%")


@bot.event
async def on_ready():                                              
    print(f"Login as in : {bot.user}" )

#--------------------------------------------------------------Command--------------------------------------------------------------------------------

@bot.command()
async def test(ctx):
    await ctx.channel.send("Hello")
    
@bot.command()
async def h(ctx):

    Embed = discord.Embed(title="Shape bot Help !!", description= "รวมคำสั่งน้องเชพ  😁🐹", color= 0xebba34)
    Embed.add_field(name="⚙️ %h",value = "ขอความช่วยเหลือจากน้องเชพ  🐹",inline = False)
    Embed.add_field(name="⚙️ %send",value = "Test ว่าน้องพิมได้ไหม", inline = False)
    Embed.add_field(name="⚙️ คำสั่งพุดคุย  🐹",value =  " %hello, %name, ทำไรอยู่, กินไรดี, เล่นไรดี", inline = False)
    Embed.add_field(name="⚙️ %food",value = "ถ้าคิดไม่ออกว่าจะกินอะไรน้องจะช่วยเลือกให้  🍔", inline = False)
    Embed.add_field(name="⚙️ %sad",value = "เวลาท้อใจพิมคำสั่งนี้เถอะนะ 😢", inline = False)
    Embed.add_field(name="⚙️ %game",value = "น้องจะช่วยเลือกเกมให้นะ  🤪", inline = False)
    Embed.set_thumbnail( url ="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/0cdd4af8-ae84-43c4-96a5-2a1ebe4c883f/d9pcb4v-0fb0fd4d-b7b1-40a6-b186-90b99b3c0633.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzBjZGQ0YWY4LWFlODQtNDNjNC05NmE1LTJhMWViZTRjODgzZlwvZDlwY2I0di0wZmIwZmQ0ZC1iN2IxLTQwYTYtYjE4Ni05MGI5OWIzYzA2MzMuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.L7TFQvXVD5og3PjEb4xSsYEKjfP9-NuBezLCxthUggQ")
    Embed.add_field(name="⚙️ %hmusic",value = "คู่มือคำสั่งเล่นเพลง   😁", inline = False)
    Embed.add_field(name="⚙️ %logout",value = "ปิดระบบน้อง   👩🏼‍💻", inline = False)
    #Embed.add_field(name="%....",value = ".................", inline = False)

    await ctx.channel.send(embed= Embed)


@bot.command()
async def hmusic(ctx):
    Embed = discord.Embed(title="Hamster Music Help !!", description= "รวมคำสั่งเล่นเพลง  😁🐹", color= 0xebba34) 
    Embed.add_field(name="⚙️ %play",value = "%play ตามด้วยลิ้ง URL ของเพลง  🐹",inline = False)
    Embed.add_field(name="⚙️ %quit",value = "ให้น้องออกจากห้อง", inline = False)
    Embed.set_thumbnail( url ="https://c.tenor.com/HJvqN2i4Zs4AAAAj/milk-and-mocha-cute.gif")
    Embed.add_field(name="⚙️ %stop",value = "หยุดเพลงที่เล่น ", inline = False)
    await ctx.channel.send(embed= Embed)

@bot.command()
async def send(ctx):
    await ctx.channel.send("เราพิมได้นะ  🤖") 

#-------------------------------------------------------------------------- Chat-----------------------------------------------------------------------


@bot.event                                                      
async def on_message(message):
    if message.content == ("%sad"):
        o = random.randint(0,len(sad))
        await message.channel.send (sad[o])

    if message.content == ("เศร้า"):
        o = random.randint(0,len(sad))
        await message.channel.send (sad[o])

    if message.content == ("%game"):
        o = random.randint(0,len(game))
        await message.channel.send (game[o])

    if message.content == ("เล่นไรดี"):
        o = random.randint(0,len(game))
        await message.channel.send (game[o])

    if message.content == ("%food"):
        o = random.randint(0,len(food))
        r = random.randint(0,len(ty))
        await message.channel.send (food[o] +" " + ty[r])

    if message.content == ("กินไรดี"):
        o = random.randint(0,len(food))
        r = random.randint(0,len(ty))
        await message.channel.send (food[o] +" " + ty[r])

    elif message.content == ("%hello"):
        await message.channel.send ("หวัดดี "+ str(message.author.name))

    elif message.content == ("หวัดดี"):
        await message.channel.send ("หวัดดี "+ str(message.author.name))

    elif message.content == ("%name"):
        await message.channel.send( "เราชื่อ  🐹  " + str(bot.user.name))
    
    elif message.content == ("%รักเราไหม"):
        await message.channel.send( "เรารัก " + str(message.author.name)+ (" เสมอนะ"))

    elif message.content == ("จุ๊บๆ"):
        await message.channel.send((" จุ๊บด้วยยย"))
        
    elif message.content == ("%ไอ้บอทโง่"):
        await message.channel.send("เราฉลาดกว่าเองละกัน   😕🐹 ")

    elif message.content == ("%m"):
        await message.channel.send(" 😚🐹")
        
    elif message.content == ("%logout"):
        await bot.logout()

    await bot.process_commands (message)
    
#----------------------------------------------------------------------- Music---------------------------------------------------------------------

@bot.command()
async def play(ctx, url):  #เล่นเพลง
    channel = ctx.author.voice.channel
    voice_client = get(bot.voice_clients, guild = ctx.guild )

    if voice_client == None:
        await ctx.channel.send ("ฟังเพลงกันน 😚")
        await channel.connect()
        voice_client = get(bot.voice_clients, guild = ctx.guild)

    Chef_OPTION = {"fomat":"bestaudio", "nonplaylist":"True"}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    if not voice_client.is_playing():
        with YoutubeDL(Chef_OPTION) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        voice_client.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        voice_client.is_playing()
    else:
        await ctx.channel.send ("น้องกำลังเล่นเพลงอยู่ 🐹")
        return

@bot.command()
async def stop(ctx):
    voice_client = get (bot.voice_clients,guild = ctx.guild )
    await ctx.channel.send ("หยุดด !! ")
    if voice_client == None:
        await ctx.channel.send ("Hamster is not connect to Voice Channel  🐹")
        return
    voice_client.stop()

@bot.command()
async def quit(ctx):
    await ctx.channel.send("ไปแล้วน้าาาา  🐹")
    await ctx.voice_client.disconnect()

#-------------------------------------------------------------------Ban---------------------------------------------------------------------


#Kick
@bot.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.channel.send(f'Kick {member.mention}')

#Ban
@bot.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.channel.send(f'Banned {member.mention}')

#Unban
@bot.command()
async def unban(ctx, *,member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.spilt('#')

    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return
            
bot.run ("ODYwOTc3MzYyMTk1ODQxMDQ1.YODFpw.M4aKArgPUjx4c1yPwXnMlUp_XyU")
