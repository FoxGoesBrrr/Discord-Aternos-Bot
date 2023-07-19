# Hey!!

## Introduction

Welcome to the official repository of my Discord bot! I'm a solo developer who created this bot to simplify Aternos Minecraft server management right from your Discord server. As a fellow Minecraft enthusiast, I know how important it is to have a hassle-free experience when it comes to running your server.

🚀 **Features**:

**Whitelist Management**: Easily add names to the whitelist, giving your friends and players access to your server. Use `/whitelist <username>` to add your username.

**Whitelist Check**: Quickly see who's on your server's whitelist with a simple command. Use `/showwhitelist` to check if your (or your friend's) username is whitelisted.

**Server Start**: Initiate server startup with just one command, making your world accessible to all players. Use `/start` to start the server.

**Server Status**: Stay informed about your Aternos Minecraft server's real-time status, so you always know if it's available. Use `/status` to check the status of the server.

**Basic Server Info**: Get a snapshot of your server's key details, including player count and current version. Use `/ipaddress` to check and share the IP address of the server.



⚙️ **How to Use**:

Invite my bot to your Discord server using the provided link.
Set up your Aternos Minecraft server credentials in the bot's configuration.
Enjoy effortless server management with intuitive commands.

🙏 **Acknowledgments**:
I want to extend my gratitude to DarkCat09 for their awesome Python-Aternos module. Their work has been instrumental in helping me develop this bot and make Aternos server control possible from Discord.

🤝 **Contribution**:
As a solo developer, I'm always open to community contributions! If you have any ideas, encounter issues, or want to suggest new features, please don't hesitate to create issues or submit pull requests. Together, let's enhance this bot and make it even more useful for the Minecraft community!

🚀 Take charge of your Aternos Minecraft server using my Discord bot. Let's embark on an exciting server management journey! 🎉

And also, this is a prototype and the bot is highly inefficient with the resources as of now... But works. 👍

## Setup

Make sure you have...

* Latest version of python
* python-aternos module (Can be installed by running `pip install python-aternos` in cmd)
* subprocess module (Can be installed by running `pip install subprocess` in cmd)
* discord.py module (Can be installed by running `pip install discord.py` in cmd)
* Aternos username and password (or ATERNOS_SESSION cookie)
* Discord bot and its token
* Your bot is in your server with `292057852928` as the permission integer

Follow these steps to use the bot:

1. Click on `<> Code` and click on  `Download zip`.
2. After the zip file is downloaded, unzip the file.
3. Open main.py use notepad (or whatever software) and change the values of `user`, `passw` and `TOKEN`.
4. Open status.py and do the same (there is no `TOKEN` in this file). 
5. Open cmd in that folder and run `py main.py`.

Now you got your bot running in your server!

