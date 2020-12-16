import discord
import asyncio
import os

client = discord.Client()

#디스코드 라인을 단축시킴
d_line = '~~                                                                                                                                                                                                                                                                                                                            ~~\n'


@client.event
async def on_ready():
    
    print("===================")
    print("'블링이' 접속 완료") 
    print("===================")
    
    # 봇이 활동 중에 표시 될 이름
    game = discord.Game("테스트 중...")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event   
async def on_message(message):

 # 봇의 응답으로 인한 명령어가 출력되는 것을 무시하기 위해서 설정함
    if message.author.bot: 
        return None

    if message.content == "!명령어":
        await message.channel.send("!이리퍼  !시세  !소개  !?? 도움")

    if message.content == "!이리퍼":
        await message.channel.send("https://www.erepublik.com/ko")

    if message.content == "!소개":        
        await message.channel.send("'이리퍼블릭'이라는 단어 중에서 '블릭'이라는 단어를 귀요미하게 바꾼 단어로 '블링이' 라고 되었어요. (제작:반터울프)")

    if message.content == "!시세":        
        await message.channel.send("!자세  !무세  !음세  !하세  !공세  - !시세 도움")

    if message.content == "!시세 도움":        
        await message.channel.send("!자세 : 원자재 시세 \n!무세 : 무기 시세\n!음세 : 음식 시세\n!하세 : 하우스 시세\n!공세 : 항공 무기 시세")

# ===========================================================================================================================================================================    
# ===========================================================================================================================================================================

# 이리퍼 원자재 시세
    if message.content == "!자세":
        await message.channel.send(d_line + "Q0 무기 원자재 시세 : https://erepublik.tools/marketplace/items/0/12/1/offers\nQ0 음식 원자재 시세 : https://erepublik.tools/marketplace/items/0/7/1/offers\nQ0 집 원자재 시세 : https://erepublik.tools/marketplace/items/0/17/1/offers\nQ0 항공 원자재 시세 : https://erepublik.tools/marketplace/items/0/24/1/offers")

# 이리퍼 Q1~Q7 무기 시세

    if message.content == "!무세":
        await client.channel.send(d_line + "Q7 무기 글로벌 시세 : https://erepublik.tools/marketplace/items/0/2/7/offers\nQ6 무기 글로벌 시세 : https://erepublik.tools/marketplace/items/0/2/6/offers\nQ5 무기 글로벌 시세 : https://erepublik.tools/marketplace/items/0/2/5/offers\nQ4 무기 글로벌 시세 : https://erepublik.tools/marketplace/items/0/2/4/offers\nQ3 무기 글로벌 시세 : https://erepublik.tools/marketplace/items/0/2/3/offers\nQ2 무기 글로벌 시세 : https://erepublik.tools/marketplace/items/0/2/2/offers\nQ1 무기 글로벌 시세 : https://erepublik.tools/marketplace/items/0/2/1/offers")
    
# 이리퍼 Q1~Q7 음식 시세

    if message.content == "!음세":
        await client.channel.send(d_line + "Q7 음식 글로벌 시세 : https://erepublik.tools/marketplace/items/0/1/7/offers\nQ6 음식 글로벌 시세 : https://erepublik.tools/marketplace/items/0/1/6/offers\nQ5 음식 글로벌 시세 : https://erepublik.tools/marketplace/items/0/1/5/offers\nQ4 음식 글로벌 시세 : https://erepublik.tools/marketplace/items/0/1/4/offers\nQ3 음식 글로벌 시세 : https://erepublik.tools/marketplace/items/0/1/3/offers\nQ2 음식 글로벌 시세 : https://erepublik.tools/marketplace/items/0/1/2/offers\nQ1 음식 글로벌 시세 : https://erepublik.tools/marketplace/items/0/1/1/offers")
    
# 이리퍼 Q1~Q5 하우스 시세

    if message.content == "!하세":
        await client.channel.send(d_line + "Q1 하우스 글로벌 시세 : https://erepublik.tools/marketplace/items/0/4/1/offers\nQ2 하우스 글로벌 시세 : https://erepublik.tools/marketplace/items/0/4/2/offers\nQ3 하우스 글로벌 시세 : https://erepublik.tools/marketplace/items/0/4/3/offers\nQ4 하우스 글로벌 시세 : https://erepublik.tools/marketplace/items/0/4/4/offers\nQ5 하우스 글로벌 시세 : https://erepublik.tools/marketplace/items/0/4/5/offers")

# 이리퍼 Q1 항공 무기 시세

    if message.content == "!공세":
        await client.channel.send(d_line + "Q1 항공 무기 글로벌 시세 : https://erepublik.tools/marketplace/items/0/23/1/offers")








access_token = os.environ["BOT_TOKEN"]

client.run(access_token)
