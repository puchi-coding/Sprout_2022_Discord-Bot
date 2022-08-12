# 檔名：guess.py
# 功能：猜數字遊戲、排行榜(未完成)
import discord
import random
from discord.ext import commands
from core import Cog_Extension

class guess(Cog_Extension):
    
    @commands.command() 
    async def guess(self, ctx):
        
        def is_valid(m):
            return m.author == ctx.author # 判斷玩家輸出的message是否合適

        await ctx.send("猜數字遊戲開始") 

        ans = "".join(random.sample("123456789", 4)) # 取4個數字
        print("答案 :", ans) # 在後台顯示答案

        # 遊戲判斷
        for _ in range(30):
            g = await self.bot.wait_for("message", check=is_valid, timeout=300.0) # 設置處理玩家輸出的message
            guess = g.content.strip() # 處理message空白問題
            # 退出遊戲設置
            if guess.lower() == "退出":
                await ctx.send("已退出")
                return
            # 判別message合法性
            if guess.isdigit() == False:
                await ctx.send("不合法")
                continue
             # nA、nB設置 
            a_count, b_count = 0, 0

            for i in range(len(guess)):
                if guess[i] == ans[i]: # 判斷位置和數字完全正確的個數
                    a_count += 1

                if guess[i] in ans: # 判斷數字正確位置不正確的個數
                    b_count += 1

            b_count -= a_count # 去除nA、nB重疊的數字

            
            if guess == ans : 
                await ctx.send("答對!") # 全部猜對後的顯示
                return
            else:
                await ctx.send(f"{a_count}A{b_count}B") # 部分猜對的顯示
                
                

        await ctx.send(f"遊戲結束! 答案為{ans}") # 印出答案

    


def setup(bot):
    bot.add_cog(guess(bot))