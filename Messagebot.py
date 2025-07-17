import discord
from discord.ext import commands
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is logged in as {bot.user}")

@bot.command()
async def dmuser(ctx, user_id: int, *, message: str):
    try:
        user = await bot.fetch_user(user_id)
        await user.send(message)
        await ctx.send(f"✅ DM sent to <@{user_id}>")
    except discord.NotFound:
        await ctx.send("❌ User not found.")
    except discord.Forbidden:
        await ctx.send("🚫 Can't DM this user. They might have DMs off.")
    except Exception as e:
        await ctx.send(f"⚠️ Error: {e}")

import os

keep_alive()
bot.run(os.getenv("DISCORD_BOT_TOKEN"))
