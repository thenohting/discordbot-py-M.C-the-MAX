from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == f'{PREFIX}call':
        await message.channel.send("callback!")

    if message.content.startswith(f'{PREFIX}hello'):
        await message.channel.send('Hello!')
        
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == '!help': #메시지 입력
        await message.channel.send('안녕하세요. 모의 자산 투자 봇입니다.')

    if message.content.startswith("!사진"): #사진 입력
        file = discord.File("C:/python workspace/QRCodeImg.jpg")
        await message.channel.send(file=file)

    if message.content.startswith("!매수"): #매수
        file = openpyxl.load_workbook("C:\python workspace\자산.xlsx")
        sheet = file.active
        learn = message.content.split(" ")
        for i in range (1,1001):
            if sheet["A" + str(i)].value == ".":
                sheet["A" + str(i)].value = learn[1]
                sheet["B" + str(i)].value = learn[2]
                await message.channel.send('매수 진행되었습니다.')
                break
        file.save("C:\python workspace\자산.xlsx")


try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
