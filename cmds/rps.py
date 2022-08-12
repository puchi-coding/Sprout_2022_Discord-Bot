# 檔名：rps.py
# 功能：一般猜拳、安妮亞模式猜拳、查看規則
import discord, random
from discord.ext import commands
from core import Cog_Extension


class rps(Cog_Extension):
    # 一般猜拳
    @commands.command()
    async def rps(self, ctx, message):
        # 玩家的選擇
        choices = ["剪刀","石頭","布"]
        # 對手的選擇
        bot_ans = random.choice(choices) # 對手隨機出 剪刀、石頭、布
        
        
        # 遊戲的判定:
        if message not in choices: # 如果輸入不存的元素，則說明遊戲規則
            await ctx.send("你不會猜拳嗎?那麼你應該看看規則。輸入:$rule")

        else:
            # 如果兩方相同則平手
            if bot_ans == message:
                await ctx.send(f"我們都是{message}，所以平手...")
                await ctx.send("https://cdn.discordapp.com/attachments/985427205381316621/992803978247163924/487FFE3B-E6CF-4F29-901D-16D1DE55411A.jpg")
                

            # 石頭、布的可能
            if bot_ans == "石頭":
                if message == "布":
                    await ctx.send(f"我出{bot_ans}。你贏了...過分,魔鬼")
                    await ctx.send("https://cdn.discordapp.com/attachments/985427205381316621/992804410319179799/FA56521F-44E0-4BA9-902F-A90294598C79.jpg")

            if bot_ans == "布":
                if message == "石頭":
                    await ctx.send(f"我出{bot_ans}。廢物⌓‿⌓廢物")
                    await ctx.send("https://cdn.discordapp.com/attachments/985427205381316621/992802877561122877/spy-x-family-anya-forger.gif")

            # 石頭、剪刀的可能
            if bot_ans == "剪刀":
                if message == "石頭":
                    await ctx.send(f"我出{bot_ans}。你贏了...過分,魔鬼")
                    await ctx.send("https://cdn.discordapp.com/attachments/985427205381316621/992804410319179799/FA56521F-44E0-4BA9-902F-A90294598C79.jpg")

            if bot_ans == "石頭":
                if message == "剪刀":
                    await ctx.send(f"我出{bot_ans}。廢物⌓‿⌓廢物")
                    await ctx.send("https://cdn.discordapp.com/attachments/985427205381316621/992802877561122877/spy-x-family-anya-forger.gif")


            # 布、剪刀的可能
            if bot_ans == "布":
                if message == "剪刀":
                    await ctx.send(f"我出{bot_ans}。你贏了...過分,魔鬼")
                    await ctx.send("https://cdn.discordapp.com/attachments/985427205381316621/992804410319179799/FA56521F-44E0-4BA9-902F-A90294598C79.jpg")

            if bot_ans == "剪刀":
                if message == "布":
                    await ctx.send(f"我出{bot_ans}。廢物⌓‿⌓廢物")
                    await ctx.send("https://cdn.discordapp.com/attachments/985427205381316621/992802877561122877/spy-x-family-anya-forger.gif")
 
    # 遊戲規則
    @commands.command()
    async def rule(self, ctx):
        await ctx.send("遊戲規則")
        embed=discord.Embed(title="猜拳規則(點我)", url="https://zh.wikipedia.org/zh-tw/%E7%9F%B3%E5%A4%B4%E3%80%81%E5%89%AA%E5%AD%90%E3%80%81%E5%B8%83", description="這是猜拳規則，請詳讀一遍。", color=0x2e91b2)
        embed.set_author(name="Puchi", url="https://puchi-coding.github.io/", icon_url="https://img.onl/QsMBlW")
        embed.set_thumbnail(url="https://img.onl/3vyNwO")
        embed.add_field(name="指令打法:", value="$rps 「你要出的拳法」\n$anya_rps 「你要出的拳法」\n$rule", inline=False)
        embed.set_footer(text="⌓‿⌓")
        await ctx.send(embed=embed)   

    # 安妮亞模式猜拳
    @commands.command()
    async def anya_rps(self, ctx):
        
        await ctx.send("遊戲開始!") # 輸入完指令馬上顯示遊戲開始


        while True:
            
            def is_valid(m):
                return m.author == ctx.author # 判斷玩家輸出的message是否合適
    
            # 玩家的選擇
            choices = ["剪刀", "石頭", "布"]

            # 對手的選擇
            bot_choices = ["剪刀", "石頭", "布"] # 三種可能性
            
            bot_remove_1 = random.choice(bot_choices) # 對手隨機取一個遊戲中不會出出來的值

            bot_choices.remove(bot_remove_1) # 將這個值取走

            bot_ans = random.choice(bot_choices) # 對手隨機選擇剩餘的選項

            await ctx.send(f"對手不會出{bot_remove_1}，所以我要出...") # 遊戲開始後馬上顯示被隨機取走的值

            msg = await self.bot.wait_for("message", check=is_valid, timeout=300.0) #設置處理玩家輸出的message
            message = msg.content.strip() # 處理message空白問題

            # 遊戲的判定:
            if message == "退出":
                await ctx.send("已退出")
                break
            else:        
                if message not in choices: # 如果輸入不存的元素，則說明遊戲規則
                    await ctx.send("你不會猜拳嗎?那麼你應該看看規則。輸入:$rule")

                else:
                    # 如果兩方相同則平手
                    if bot_ans == message:
                        await ctx.send(f"我們都是{message}，所以平手...")
                        await ctx.send("https://cdn.discordapp.com/attachments/985427205381316621/992803978247163924/487FFE3B-E6CF-4F29-901D-16D1DE55411A.jpg")

                    # 石頭、布的可能
                    if bot_ans == "石頭":
                        if message == "布":
                            await ctx.send(f"我出{bot_ans}。你贏了...過分,魔鬼")
                            await ctx.send("https://cdn.discordapp.com/attachments/985427205381316621/992804410319179799/FA56521F-44E0-4BA9-902F-A90294598C79.jpg")

                    if bot_ans == "布":
                        if message == "石頭":
                            await ctx.send(f"我出{bot_ans}。廢物⌓‿⌓廢物")
                            await ctx.send("https://cdn.discordapp.com/attachments/985427205381316621/992802877561122877/spy-x-family-anya-forger.gif")

                    # 石頭、剪刀的可能
                    if bot_ans == "剪刀":
                        if message == "石頭":
                            await ctx.send(f"我出{bot_ans}。你贏了...過分,魔鬼")
                            await ctx.send("https://cdn.discordapp.com/attachments/985427205381316621/992804410319179799/FA56521F-44E0-4BA9-902F-A90294598C79.jpg")

                    if bot_ans == "石頭":
                        if message == "剪刀":
                            await ctx.send(f"我出{bot_ans}。廢物⌓‿⌓廢物")
                            await ctx.send("https://cdn.discordapp.com/attachments/985427205381316621/992802877561122877/spy-x-family-anya-forger.gif")


                    # 布、剪刀的可能
                    if bot_ans == "布":
                        if message == "剪刀":
                            await ctx.send(f"我出{bot_ans}。你贏了...過分,魔鬼")
                            await ctx.send("https://cdn.discordapp.com/attachments/985427205381316621/992804410319179799/FA56521F-44E0-4BA9-902F-A90294598C79.jpg")

                    if bot_ans == "剪刀":
                        if message == "布":
                            await ctx.send(f"我出{bot_ans}。廢物⌓‿⌓廢物")
                            await ctx.send("https://cdn.discordapp.com/attachments/985427205381316621/992802877561122877/spy-x-family-anya-forger.gif")
                
def setup(bot):
    bot.add_cog(rps(bot))