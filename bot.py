import requests
import os
import datetime
import discord
from dotenv import load_dotenv
from discord.ext import commands
from dateutil.relativedelta import relativedelta
import time


load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True 
bot = commands.Bot(command_prefix='/', intents=intents)


API = "https://ctftime.org/api/v1/events/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36",
    "Accept": "application/json"
}
def call_api(start, finish, url, limit=10):
    params = {
        'limit': limit,
        'start': start,
        'finish': finish}
    try:
        response = requests.get(url, params=params, headers=headers)
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"Error: {e}, {response.status_code}"



def format_json(ctf_json):
    # Use fixed-width font for better alignment
    table = "```md\n"
    table += f"{'Title':<35} {'Start Date':<12} {'Finish Date':<12} {'StartTime':<10} {'FinishTime':<10} {'URL'}\n"
    table += "-" * 130 + "\n"
    for ctf in ctf_json:
        title = ctf.get('title', 'N/A')[:35]  # Limit to 35 characters
        start = ctf.get('start', 'N/A')[0:10]
        finish = ctf.get('finish', 'N/A')[0:10]
        start_time = datetime.datetime.fromisoformat(ctf.get('start', 'N/A').replace('Z', '+00:00')).strftime('%H:%M')
        end_time = datetime.datetime.fromisoformat(ctf.get('finish', 'N/A').replace('Z', '+00:00')).strftime('%H:%M')
        url = ctf.get('url', 'N/A')[:35]  # Limit URL length
        table += f"{title:<35} {start:<12} {finish:<12} {start_time:<10} {end_time:<10} {url}\n"
    table += "```"
    return table

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print("------------------------")

    

@bot.command()
async def ctf(ctx, start: str = None, end: str = None):
    now = datetime.datetime.now()

    if not start and not end:
        start_date = now

        end_date = now + relativedelta(months=1)

    else:
        try:
            start_date = datetime.datetime.strptime(start, "%d-%m-%Y")

            end_date = datetime.datetime.strptime(end, "%d-%m-%Y")

        except ValueError:
            await ctx.send("Invalid date format! Use 'DD-MM-YYYY'")
            return
        

    start_timestamp = int(time.mktime(start_date.timetuple()))
    end_timestamp = int(time.mktime(end_date.timetuple()))

    response = call_api(start_timestamp, end_timestamp, API )    
    

    if isinstance(response, str):
        await ctx.send(response)
    else:
        if len(response) == 0:
            await ctx.send(f"No CTF events found between {start_date.date()} and {end_date.date()}.")
        else:
            formatJson = format_json(response)
            await ctx.send(formatJson)

if __name__ == '__main__':
    token = os.getenv('DISCORD_TOKEN')
    if token is None:
        raise ValueError("No Discord token found in environment variables.")
    bot.run(token)







