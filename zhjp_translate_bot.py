import discord
from discord.ext import commands
from discord.commands import Option
import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = discord.Bot(
		command_prefix="!",
        intents=discord.Intents.all(),  # 全てのインテンツを利用できるようにする
        activity=discord.Game("翻訳"),  # "〇〇をプレイ中"の"〇〇"を設定,
)

@bot.event
async def on_ready():
    print('Bot is ready')

@bot.slash_command(description="Translate text to Chinese")
async def translate_to_chinese(ctx, text: str = Option(description="Text to translate", required=True)):
    prompt = f"Translate from Japanese to Traditional Chinese:\n{text}\nOutput:"
    
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    result = response.choices[0].text.strip()
    await ctx.respond(result)

@bot.slash_command(description="Translate text to Japanese")
async def translate_to_japanese(ctx, text: str = Option(description="Text to translate", required=True)):
    prompt = f"Translate from traditional Chinese to Japanese:\n{text}\nOutput:"
    
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    result = response.choices[0].text.strip()
    await ctx.respond(result)

bot.run(os.environ.get("DISCORD_API_KEY"))