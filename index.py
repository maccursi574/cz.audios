import discord
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)

green = discord.Colour(0x04D275)
orange = discord.Colour(0xFEA347)
red = discord.Colour(0xD2003F)
grey = discord.Colour(0x36393F)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Bot en ligne !")

@bot.event
async def on_member_join(member):
    guild = bot.get_guild(1051462125324869742)
    channel = guild.get_channel(1051462128218951700)
    await channel.send(f'Hello {member.mention}, welcome to this server !')
    await member.send(f"Hello, thanks for joining the cz.audios server. Don't hesitate to take your <#1051483862322122782> :wink:")

@bot.command()
@commands.has_role('Owner')
async def clear(ctx, amount=1000):
    await ctx.channel.purge(limit=amount)

@bot.command()
@commands.has_role('Owner')
async def rules(ctx):
    embed = discord.Embed(title="Server Rules", description="**1 • **Do not harass others or organize, promote, or participate in harassment. Disagreements happen and are normal, but making continuous, repetitive, or severe negative comments or circumventing a block or ban can cross the line into harassment and is not okay.\n\n**2 • **Do not organize, promote, or participate in hate speech or hateful conduct. It’s unacceptable to attack a person or a community based on attributes such as their race, ethnicity, caste, national origin, sex, gender identity, gender presentation, sexual orientation, religious affiliation, age, serious illness, disabilities, or other protected classifications.\n\n**3 • **Do not make threats of violence or threaten to harm others. This includes indirect or suggestive threats, as well as sharing or threatening to share someone’s personally identifiable information (also known as doxxing).\n\n**4 • **Do not use Discord for the organization, promotion, or support of violent extremism. This also includes glorifying violent events, the perpetrators of violent acts, or similar behaviors.\n\n**5 • **We report illegal content and grooming to the National Center for Missing and Exploited Children.\n\n**6 • **We strongly discourage and may take action against vigilante behavior, as it can interfere with our investigation and ability to report to law enforcement.\n\n**7 • **Do not make adult content available to anyone under the age of 18. You must be age 18 or older to participate in adult content on Discord. You must apply the age-restricted label to any channels or servers if they contain adult content or other restricted content such as violent content.\n\n**8 • **Do not use adult content in avatars, server banners, server icons, invite splashes, emoji, stickers, or any other space that cannot be age-restricted.\n\n**9 • **Do not share sexually explicit content of other people without their consent, or promote the sharing of non-consensual intimate materials (images, video, or audio), sometimes known as revenge porn.\n\n**10 • **Do not share content that glorifies or promotes suicide or self-harm, including any encouragement to others to cut themselves or embrace eating disorders such as anorexia or bulimia.\n\n**11 • **Self-harm threats used as a form of emotional manipulation or coercion are also prohibited.\n\n**12 • **Do not share real media depicting gore, excessive violence, or animal harm, especially with the intention to harass or shock others.\n\n**13 • **Do not share content that violates anyone's intellectual property or other rights.\n\n**14 • **Do not sexualize children in any way. You cannot share content or links which depict children in a pornographic, sexually suggestive, or violent manner, including illustrated or digitally altered pornography that depicts children (such as lolicon, shotacon, or cub) and conduct grooming behaviors.", color=red)
    await ctx.message.delete()
    await ctx.send(embed=embed)

@bot.command()
@commands.has_role('Owner')
async def pronouns(ctx):
    embed = discord.Embed(title="What are your pronouns?", description=":cloud: • he/him\n:shell: • she/her\n:dove: • they/them\n:fish_cake: • any pronouns\n:bubbles: • other", color=0x3ba1b3)
    await ctx.send(embed=embed)

bot.run("MTA1MTQ2NjI2MjQ1MjEwOTM4Mw.GdC9KV.-Qxj1zGV0vC7jHgMaVpR5jIgMGYcbS7YknQV4U")