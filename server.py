#imports all the modules that we will need
import requests
import discord
from discord.ext import commands
import socket
import json
import re

#imports token, prefix and api key from hidden.py file
from config import token, lapi_key, prefix



#function to send requests to api and get custom response
async def lookup_ip(ip_address):
	response = requests.get(f'https://api.ipdata.co/{ip_address}?api-key={lapi_key}')
	response_json = json.loads(response.text)
	return f'''
```
IP: {str(response_json['ip'])}

IP LOCATION INFO

City: {str(response_json['city'])}
Region: {str(response_json['region'])}
Region code: {str(response_json['region_code'])}
Country: {str(response_json['country_name'])}
Country code: {str(response_json['country_code'])}
Flag: {str(response_json['emoji_flag'])}
Continent: {str(response_json['continent_name'])}
Continent code: {str(response_json['continent_code'])}
Postal code: {str(response_json['postal'])}
Latitude: {str(response_json['latitude'])}
Longitude: {str(response_json['longitude'])}
Calling code: {str(response_json['calling_code'])}
Time zone: {str(response_json['time_zone']['name'])}
Time zone current time: {str(response_json['time_zone']['current_time'])}
Currency: {str(response_json['currency']['name'])}
Currency code: {str(response_json['currency']['code'])}
Currency symbol: {str(response_json['currency']['symbol'])}
Language: {str(response_json['languages'][0]['name'])}
Native language: {str(response_json['languages'][0]['native'])}


BASIC INFO

asn: {str(response_json['asn']['asn'])}
Name: {str(response_json['asn']['name'])}
Domain: {str(response_json['asn']['domain'])}
Route: {str(response_json['asn']['route'])}
Type: {str(response_json['asn']['type'])}


EXTRA INFO

TOR: {str(response_json['threat']['is_tor'])}
Proxy: {str(response_json['threat']['is_proxy'])}
Anonymous: {str(response_json['threat']['is_anonymous'])}
Abuser: {str(response_json['threat']['is_known_abuser'])}
Threat: {str(response_json['threat']['is_threat'])}
Bogon: {str(response_json['threat']['is_bogon'])}```'''



#sets the prefix and stuff...
bot = commands.Bot(command_prefix = prefix)



#on start activities for the bot
@bot.event
async def on_ready():
	
	#adds playing status
	await bot.change_presence(status=discord.Status.online, activity=discord.Game('with IP addresses'))
	
	#tells that bot is online
	print('Bot is online!')
	#tells how much servers the bot is in
	print(f'serving {len(bot.guilds)} guilds')



#ping command
@bot.command(name='ping')
async def ping(ctx):
	"""sends bot's ping"""
	#above is an description of the command
	
	#sends the ping
	await ctx.send(f'My ping is {round(bot.latency*1000)}ms')
  	
#Send anonymous DM's
@bot.command()
async def anonspam(ctx, member: discord.Member, *, content):
    channel2 = discord.utils.get(bot.get_all_channels(), name='general')
    await ctx.message.delete()
    await ctx.send(f'*Spamming...*')
               
    channel = await member.create_dm() # creates a DM channel for mentioned user
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)
    await channel.send(content)

    await channel2.send(f'**SPAM COMPLETE**');

# send whatever in the content to the mentioned user.
# Usage: +send_anon_spam @mention_user <your message here>

# THIS FUNCTION WILL SEND A DM WITH THE AUTHORS NAME.
@bot.command()
async def spam(ctx, member: discord.Member, *, content):
    channel2 = discord.utils.get(bot.get_all_channels(), name='general')
    await ctx.message.delete()
    await ctx.send(f" {ctx.message.author.mention} *is spamming...*")
    channel = await member.create_dm() # creates a DM channel for mentioned user
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await channel.send(f"**{ctx.message.author} said:** {content}")

    
    await channel2.send(f'**SPAM COMPLETE** {ctx.message.author.mention}');
    # send whatever in the content to the mentioned user along with the author's name.
 
#info (about) command
@bot.command(name='info', aliases=['about'])
async def info(ctx):
	'''gives info about the bot'''
	#above is an description of the command
	
	#description of the bot
	embed = discord.Embed(title='Geolocation', description='This discord bot lets you lookup ip addresses and domains.', color=0x00FF00)
	
	#gives info about us here
	embed.add_field(name='Made by', value='Tobinjo#001')
  
  #gives info about us here
	embed.add_field(name='Website', value='https://www.tobinjo.co.uk')
	
	#Shows the number of servers the bot is in
	embed.add_field(name='Server count', value=f'{len(bot.guilds)}')
    
	#sends the embed message
	await ctx.send(embed=embed)



#geolocate (ip) command
@bot.command(name='geo', aliases=['ip'])
async def geo(ctx, *, ip):
	"""looks up an ip address"""
	#above is the description for the command

	#runs the command
	try:
		#gets ip address
		ip_address = socket.gethostbyname(ip)
		#sends the info about the ip
		await ctx.send(await lookup_ip(ip_address))
	
	#message if there is socket error aka if there is no such an ip or domain
	except socket.gaierror:
		await ctx.send('There is no such an ip or domain')

	#if some other kind of error occurs
	except Exception as e:
		await ctx.send('Error has occured!')
		print(f'{e}\nError has occured!') 
    
#runs the bot   
bot.run(token, bot=True)
