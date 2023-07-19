import discord
from discord import app_commands
from discord.ext import commands
from discord.ext import tasks
from python_aternos import Client, Lists
import subprocess
import asyncio

aternos_client = Client()

user = ENTER_YOUR_USERNAME
passw = ENTER_YOUR PASSWORD
#hashpassw = ENTER_YOUR_MD5_HASHED_PASSWORD
#atcookie = ATERNOS_SESSION_COOKIE_VALUE

aternos_client.login(user, passw)
#aternos_client.login_hashed(user, hashpassw)
#aternos_client.login_with_session(atcookie)
aternos = aternos_client.account

servs = aternos.list_servers()
serv = servs[0]
serv.fetch()

servadr = serv.address

bot = commands.Bot(command_prefix='evaa', intents=discord.Intents.all())

result = subprocess.check_output(['python', 'status.py'])
server_status = result.decode('utf-8')


@bot.event
async def on_ready():
    print('Logged in.'.format(bot))
    try:
        synced = await bot.tree.sync()
        print(f'synced {len(synced)} command(s)')
    except Exception as e:
        print(e)


@tasks.loop(seconds=5)
async def check_server(channel, interaction):
    proc = await asyncio.create_subprocess_exec('python', 'status.py', stdout=asyncio.subprocess.PIPE)
    while True:
        line = await proc.stdout.readline()
        if not line:
            break
        status_value = line.decode('utf-8').strip()
        if status_value == 'online':
            await channel.send(
                content=f"Server is online! Join the server at `{servadr}` on both Bedrock, and Java editions.")
            check_server.cancel()
        else:
            pass


@bot.tree.command(name='start', description='Use this command to start the server.')
async def chat(interaction: discord.Interaction):
    servs = aternos.list_servers()
    serv = servs[0]
    serv.fetch()
    serv.start(headstart=True)
    await interaction.response.send_message("Server will start in a few minutes...")
    channel = interaction.channel
    check_server.start(channel, interaction)


@bot.tree.command(name='whitelist')
@app_commands.describe(message='Enter your username to whitelist.')
async def chat(interaction: discord.Interaction, message: str):
    servs = aternos.list_servers()
    serv = servs[0]
    serv.fetch()
    whitelist = serv.players(Lists.whl)
    whitelist_list = str(whitelist.list_players())
    if message in whitelist_list:
        await interaction.response.send_message("You are already whitelisted!")
    else:
        whitelist.add(message)
        await interaction.response.send_message(f"Added `{message}` to whitelist!")


@bot.tree.command(name='showwhitelist', description='Use this command to show the usernames whitelisted.')
async def chat(interaction: discord.Interaction):
    servs = aternos.list_servers()
    serv = servs[0]
    serv.fetch()
    whitelist = serv.players(Lists.whl)
    whitelist_list = str(whitelist.list_players())
    rewhitelist_list = ",".join([f"`{word}`" for word in whitelist_list.split(",")])
    refined_whitelist = rewhitelist_list.replace("[", "").replace("]", "").replace("'", "")
    if refined_whitelist == '``':
        await interaction.response.send_message(
            "No one is whitelisted yet... Use `/whitelist` command to whitelist yourself.")
    else:
        await interaction.response.send_message(refined_whitelist)


@bot.tree.command(name='status', description='Use this command to know the status of the server.')
async def chat(interaction: discord.Interaction):
    proc = await asyncio.create_subprocess_exec('python', 'status.py', stdout=asyncio.subprocess.PIPE)
    line = await proc.stdout.readline()
    status_value = line.decode('utf-8').strip()
    await interaction.response.defer()
    await asyncio.sleep(3)
    await interaction.followup.send(f"Server is {status_value}.")


@bot.tree.command(name='ipaddress', description='Use this command to get the IP Address of the server.')
async def chat(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"Server's IP address is `{servadr}`. You can join the server from both, Bedrock Edition and Java Edition using the same IP address.")


TOKEN = ENTER_YOUR_BOT_TOKEN

bot.run(TOKEN)
