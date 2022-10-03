import discord
from discord import activity
from discord.ext import commands
from discord.utils import get
from time import sleep


class Status(commands.Cog):

    def __init__(self, bot):
        self.bot =bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('online')

class Listen(commands.Cog):

    def __init__(self, bot):
        self.bot =bot
        self.count = 3

    count = 3 #นับครั้งที่พิมพ์ 555 เกิน 3 ครั้งบิน
    @commands.Cog.listener()
    @commands.has_permissions(kick_members=True)
    async def on_message(self, message):

        reason = 'พิมพ์คำต้องห้าม'
        forbidden_word = ['555', '55', '5555', '555+', 'lol', 'biker', 'Biker','BIKER'] #เปลี่ยนเป็นข้อมูลอื่นๆได้ เช่น คำหยาบ บอทจะเตะคนพิมพ์คำหยาบ

        if message.content in forbidden_word:
            if self.count <= 0:
                try:
                    await message.author.kick(reason=reason)
                    await message.channel.send(f"{message.author} ถูกเตะเนื่องจากคุณทำผิดกฎ")
                except:
                    print('เตะคนที่ยศเยอะกว่าไม่ได้')
                self.count = 3
                await message.channel.send("รีเซ็ตการนับเตือน")

                return
            
            await message.channel.send(f"ตรวจพบคำต้องห้ามถ้าหากตรวจพบอีก {self.count} ครั้ง คนที่พิมพ์จะถูกเตะ !")
            self.count -= 1