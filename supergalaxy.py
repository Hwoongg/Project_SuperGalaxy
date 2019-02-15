# 봇을 구동하기 위한 파일 임포트
import asyncio
import discord
import datetime
import os

app = discord.Client() # 디코 클라이언트 명령을 app으로 변경

# 토큰을 넣는다
token = "NTQ1MTY5Njk0NzQzNTkyOTYx.D0Vw1w.t_kjgVhBKoSBoBgQqvjKz4RPKRs"

# 봇이 구동되었을 때 동작되는 코드부분이다.
@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ") # 화면에 봇의 이름, 아이디가 출력된다.
    print(app.user.name)
    print(app.user.id)
    print("============")
    #봇이 플레이중인 게임을 설정할 수 있다. 아래의 "반갑습니다"를 수정하면 된다.
    await app.change_presence(game=discord.Game(name="인생", type=1))

    if os.path.isfile("chatLog.txt"): # 파일 유무 체크
        print("chatLog 파일이 존재합니다!")
        f = open("chatLog.txt",'r')
        f.close()
    else:
        print("chatLog 파일이 존재하지 않습니다!")
        f = open("chatLog.txt",'w') # 쓰기전용으로 파일을 연다. 생성용으로 사용
        f.write()
        f.close()

# 봇이 새로운 메시지를 수신했을 때 동작되는 코드이다.
@app.event
async def on_message(message):
    
    now = datetime.datetime.now()
    print("채팅이 감지되었습니다.")
    f = open("chatLog.txt",'a')
    chatMsg = message.author.name + ' : ' + message.content + '\n'
    f.write(chatMsg)
    f.close()

    if message.author.bot:  # 메시지를 보낸 사람이 봇이라면
        return None  # 무시한다

    if message.content == '!명령어':  # !명령어 라는 채팅을 보낸다면
        embed = discord.Embed(title="명령어 목록", description="!시간 : 쓸모없는 기능", color=0x00ff00)
        #embed.set_footer(text="이거슨 푸터")
        #embed.set_image(url="https://i.imgur.com/xzPCXp8.jpg") # 이미지
        await app.send_message(message.channel, embed=embed)
        
    if message.content == '자냐': 
        await app.send_message(message.channel, "안잔당")

    if message.content.startswith('ㅅㅂ'):
        await app.send_message(message.channel, "시발!")

    if message.content.startswith('ㅎㅇ'):
        await app.send_message(message.channel, "호우!")

    if message.content == '!시간':
        embed = discord.Embed(title="컴퓨터에 시계없니", description="현재 시간입니다.", color=0x00ff00)
        embed.set_footer(text = str(now.year) + "년" + 
        str(now.month) + "월" + str(now.day) + "일  | " + 
        str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
        await app.send_message(message.channel, embed=embed)

app.run(token)
