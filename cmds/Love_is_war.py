# 檔名：Love_Is_War.py
# 功能：天氣預報查詢、月亮盈虧查詢、外國匯率查詢
import discord, requests, datetime, time
from discord.ext import commands
from core import Cog_Extension

date = datetime.datetime.now() # 今日日期
date_specil = datetime.datetime.now().strftime("%m%d") # 今日月份、日期特殊格式

class Love_Is_War(Cog_Extension):
    # 天氣預報查詢
    @commands.command()
    async def weather(self, ctx, message):

        # 可查詢縣市
        city_choice = ["臺北市", "新北市", "桃園市", "臺中市", "臺南市", "高雄市", "基隆市", "新竹縣", "新竹市", "苗栗縣", "彰化縣", "南投縣", "雲林縣", "嘉義縣", "嘉義市", "屏東縣", "宜蘭縣", "花蓮縣", "臺東縣", "澎湖縣", "金門縣", "連江縣"]
        
        # 如果縣市不存在
        if message not in city_choice:
            await ctx.send(f"輸入:$weather 「你要查詢的城市」。")
            await ctx.send(f"可查詢的城市{city_choice}")
        # 縣市存在，抓取中央氣象局的資料
        else:
            url = "https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-001?Authorization=CWB-D30AF877-64CF-455F-B0BD-94DFE83029E1&downloadType=WEB&format=JSON" # 網址抓取
            data = requests.get(url) # 取得 JSON 檔案的內容為文字
            data_json = data.json() # 轉換成 JSON 格式
            location = data_json["cwbopendata"]["dataset"]["location"] # 爬取"cwbopendata"、"dataset"、"location"
            
            for i in location:
                city = i["locationName"] # 抓取城市
                wx8 = i["weatherElement"][0]["time"][0]["parameter"]["parameterName"] # 抓取天氣狀況
                mint8 = i["weatherElement"][1]["time"][0]["parameter"]["parameterName"] # 抓取最低溫
                maxt8 = i["weatherElement"][2]["time"][0]["parameter"]["parameterName"] # 抓取最高溫
                ci8 = i["weatherElement"][2]["time"][0]["parameter"]["parameterName"] # 抓取舒適度
                pop8 = i["weatherElement"][2]["time"][0]["parameter"]["parameterName"] # 抓取降雨機率
                
                if message == city:
                    await ctx.send(f"{city}。{datetime.date.today()}。天氣狀況:{wx8}。最低溫{mint8}。最高溫{maxt8}。舒適度{ci8}。降雨機率{pop8}。") # 印出結果
    
    # 月亮盈虧
    @commands.command()
    async def moon(self, ctx):
        url = f"https://www.cwb.gov.tw/Data/astronomy/moon/{date.year}{date_specil}.jpg" # 網址圖片抓取，更改網址中的日期可得今日月亮
        await ctx.send(url) # 印出圖片
        time.sleep(3) #等待3秒
        await ctx.send("就算要花上人的壽命也無法對抗的時間。\n就算在兩人之間有著令人絕望的距離。\n我會一直等待著你...") # 印出輝夜姬想讓人告白第二季第三集的台詞

    # 外國匯率
    @commands.command()
    async def money(self, ctx):
        url = "https://rate.bot.com.tw/xrt/flcsv/0/day" # 網址抓取
        rate = requests.get(url) # 取得 JSON 檔案的內容為文字
        rate.encoding = "utf-8" # 設置utf-8字元編碼
        rt = rate.text # 擷取 JSON 檔案文字內容
        rts = rt.split("\n")
        for i in rts: # 各國匯率一一匯出       
            try:                             
                a = i.split(",")             
                await ctx.send(a[0] + ":" + a[12])
            except:
                break





def setup(bot):
    bot.add_cog(Love_Is_War(bot))
    