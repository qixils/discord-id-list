from discord.ext import commands  # import discord.py rewrite's command extension


def dataProcessor(guild, dataSet):
    # Takes a guild and it's emojis, roles, etc. and parses them into a string with names & IDs
    output = ""
    for data in dataSet:
        output += "{}/{} - {}/{}\n".format(guild.name,
                                           guild.id, data.name, data.id)
    return output


bot = commands.Bot(command_prefix='$')
ownerID = 140564059417346049


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def idlist(ctx, arg):
    # Valid inputs: `roles`, `emojis`
    if ctx.author.id == ownerID:
        idlist = eval("dataProcessor(ctx.guild, ctx.guild.{})".format(arg))
        print(idlist+'------')

# Run bot using token from `bot-token.txt` file
bot.run(open("bot-token.txt").read().split("\n")[0])
