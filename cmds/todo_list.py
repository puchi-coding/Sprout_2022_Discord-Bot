# 檔名：todo_list.py
# 功能：加入、單一刪除、全部刪除、遍歷代辦事項
import discord
from discord.ext import commands
import re
import os

# 一項 Todo 的 class
class Todo:
    # 初始化
    def __init__(self, date, label, item):
        # 判斷是否為合法的日期 (不是很完整的判斷)
        d = re.compile("[0-9]{1,2}/[0-9]{1,2}")
        assert d.match(date)
        self.date = date
        self.label = label
        self.item = item

    # 小於 < (定義兩個 Todo 之間的「小於」，sort 時會用到)
    def __lt__(self, other):
        return self.date < other.date and self.label < other.label and self.item < other.item

    # 等於 = (判斷兩個 Todo 是否相等)
    def __eq__(self, other):
        return self.date==other.date and self.label==other.label and self.item==other.item

    # 回傳一個代表這個 Todo 的 string
    def __repr__(self):
        return f"{self.date} {self.label} {self.item}"

# Todo list 相關 commands
class Todo_list(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # 儲存 todo_list
        self.todo_list = []

    # 加入代辦事項到todo_list
    @commands.command()
    async def add(self, ctx, date, label, *, item):
        try:
            # 依照輸入建立一個 Todo object
            t = Todo(date, label, item)
        except Exception as e:
            # 建立失敗
            print(e)
            await ctx.send("無效")
            return
            # 重複寫入會直接刪除
        if t in self.todo_list:
            self.todo_list.remove(t)
            await ctx.send("已存在，無法寫入")

        else:
            # 把 Todo 加進 list
            self.todo_list.append(t)
            # 按照日期排序，若實作了 Todo 的 __lt__ 則可以直接用 sort() 排序
            self.todo_list.sort()
            # 印出加入成功的訊息
            await ctx.send('"{}"已加入'.format(item))

    #刪除代辦事項
    @commands.command()
    async def done(self, ctx, date, label, *, item): # * 代表 label 後面所有的字都會放到 item 內
        try:
            # 依照輸入建立一個 Todo object
            t = Todo(date, label, item)
        except Exception as e:
            # 建立失敗
            print(e)
            await ctx.send("無效")
            return
        # 執行單一刪除
        self.todo_list.remove(t)
        self.todo_list.sort()

        # 印出單一刪除的成功訊息
        await ctx.send('"{}"已刪除'.format(item))

    # 查看代辦事項
    @commands.command()
    async def show(self, ctx, label=None):
        # 遍歷所有的代辦事項
        for i in self.todo_list:
            await ctx.send(i)

    # 將全部的的代辦事項刪除
    @commands.command()
    async def clear(self, ctx):
        # 執行全部刪除
        self.todo_list.clear()
        # 印出全部刪除的成功訊息
        await ctx.send("全部刪除成功")

def setup(bot):
    bot.add_cog(Todo_list(bot))
