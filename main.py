import discord
import os
import sys
import json
import time
import random

# Importing Settings
settingU = json.load(open('settings.json'))
jtopy = json.dumps(settingU)
setting = json.loads(jtopy)
token = setting['token']
startValue = int(setting['startValue'])

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
	channel = message.channel
	if message.content == '$$$owocf':
		print("STARTING AUTO COINFLIP")
		webhook = await client.fetch_webhook('942950784180563998')
		await webhook.send(content="Starting Auto CoinFlip")
		nextflipvalue = startValue
		while True:
			await message.channel.send('owo coinflip ' + str(nextflipvalue))
			time.sleep(6)
			async for message in channel.history(limit=1):
				content = message.content
				if 'captcha' in message.content:
					print("CAPTCHA DETECTED, EXITING")
					await channel.send("CAPTCHA DETECTED, STOPPING")
					await webhook.send('@everyone CAPTCHA DETECTED, STOPPING')
					return True
				result = content.partition("and you ")
				if result[2] == "lost it all... :c":
					print("LOST")
					nextflipvalue *= 2
					await channel.send("LOST")
				elif "won" in result[2]:
					print("WON")
					nextflipvalue = startValue
					await channel.send("WON")
				else:
					print("UNDETERMINED")
					await channel.send("UNDETERMINED")
				time.sleep(random.uniform(11, 15))

	if message.content == '$$$owoh':
		print("STARTING AUTOHUNT")
		webhook = await client.fetch_webhook('942950784180563998')
		await webhook.send(content="Starting Auto Hunt")
		while True:
			await message.channel.send('owo hunt')
			time.sleep(6)
			async for message in channel.history(limit=1):
				content = message.content
				if 'captcha' in message.content:
					print("CAPTCHA DETECTED, EXITING")
					await channel.send("CAPTCHA DETECTED, STOPPING")
					await webhook.send('@everyone CAPTCHA DETECTED, STOPPING')
					return True
				if 'found' in message.content:
					print("SUCCESS")
					await channel.send("SUCCESS")
				if 'lootbox' in message.content:
					print("LOOTBOX FOUND")
					await message.pin()
					await channel.send("LOOTBOX FOUND")
			time.sleep(random.uniform(11, 16))

client.run(token, bot=False)
