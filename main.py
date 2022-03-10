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
webhookID = setting['webhookID']

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
	channel = message.channel
	if message.content == '$$$owocf':
		print("STARTING AUTO COINFLIP")
		webhook = await client.fetch_webhook(webhookID)
		await webhook.send(content="Starting Auto CoinFlip")
		nextflipvalue = startValue
		while True:
			await message.channel.send('owo coinflip ' + str(nextflipvalue))
			time.sleep(6)
			async for message in channel.history(limit=1):
				content = message.content
				if 'captcha' in content:
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
		webhook = await client.fetch_webhook(webhookID)
		await webhook.send(content="Starting Auto Hunt")
		while True:
			await message.channel.send('owo hunt')
			time.sleep(6)
			async for message in channel.history(limit=1):
				content = message.content
				if 'captcha' in content:
					print("CAPTCHA DETECTED, EXITING")
					await channel.send("CAPTCHA DETECTED, STOPPING")
					await webhook.send('@everyone CAPTCHA DETECTED, STOPPING')
					return True
				if 'lootbox' in content:
					print("LOOTBOX FOUND")
					await message.pin()
					await channel.send("LOOTBOX FOUND")
				# If you don't have any gems equipped,
				# the word 'found' doesn't show up... but 'spent' does lol
				if 'found' in content or 'spent' in content:
					print("SUCCESS")
					await channel.send("SUCCESS")
			time.sleep(random.uniform(11, 16))

	if message.content == '$$$owob':
		print("STARTING AUTOBATTLE")
		webhook = await client.fetch_webhook(webhookID)
		await webhook.send(content="Starting Auto Battle")
		while True:
			await message.channel.send('owo battle')
			time.sleep(6)
			async for message in channel.history(limit=1):
				content = message.content
				if 'captcha' in content:
					print("CAPTCHA DETECTED, EXITING")
					await channel.send("CAPTCHA DETECTED, STOPPING")
					await webhook.send('@everyone CAPTCHA DETECTED, STOPPING')
					return True
				if 'weapon crate' in content:
					print("LOOTBOX FOUND")
					await message.pin()
					await channel.send("WEAPON CRATE FOUND")
				if len(message.embeds) > 0:
					print("SUCCESS")
					await channel.send("SUCCESS")
			time.sleep(random.uniform(11, 16))

	if message.content == '$$$owohb':
		print("STARTING AUTOHUNT AND AUTOBATTLE")
		webhook = await client.fetch_webhook(webhookID)
		await webhook.send(content="Starting Auto Hunt / Battle")
		while True:
			await message.channel.send('owo hunt')
			time.sleep(6)
			async for message in channel.history(limit=1):
				content = message.content
				if 'captcha' in content:
					print("CAPTCHA DETECTED, EXITING")
					await channel.send("CAPTCHA DETECTED, STOPPING")
					await webhook.send('@everyone CAPTCHA DETECTED, STOPPING')
					return True
				if 'lootbox' in content:
					print("LOOTBOX FOUND")
					await message.pin()
					await channel.send("LOOTBOX FOUND")
				# If you don't have any gems equipped,
				# the word 'found' doesn't show up... but 'spent' does lol
				if 'found' in content or 'spent' in content:
					print("SUCCESS")
					await channel.send("SUCCESS")
			time.sleep(random.uniform(3, 6))
			await message.channel.send('owo battle')
			time.sleep(4)
			async for message in channel.history(limit=1):
				content = message.content
				if 'captcha' in content:
					print("CAPTCHA DETECTED, EXITING")
					await channel.send("CAPTCHA DETECTED, STOPPING")
					await webhook.send('@everyone CAPTCHA DETECTED, STOPPING')
					return True
				if 'weapon crate' in content:
					print("LOOTBOX FOUND")
					await message.pin()
					await channel.send("WEAPON CRATE FOUND")
				if len(message.embeds) > 0:
					print("SUCCESS")
					await channel.send("SUCCESS")
			time.sleep(random.uniform(2, 6))			

	if message.content == '$$$owowo':
		print("STARTING AUTO OWO")
		webhook = await client.fetch_webhook(webhookID)
		await webhook.send(content="Starting Auto OwO")
		while True:
			await message.channel.send('owo')
			print("OwO Sent")
			time.sleep(random.uniform(16, 17))

	if message.content == '$$$owobuywc':
		print("STARTING AUTO WEAPON CRATE PURCHASE")
		webhook = await client.fetch_webhook(webhookID)
		await webhook.send(content="Starting Auto Weapon Crate Purchase")
		while True:
			await message.channel.send('owo buy 100')
			async for message in channel.history(limit=1):
				content = message.content
				if 'captcha' in content:
					print("CAPTCHA DETECTED, EXITING")
					await channel.send("CAPTCHA DETECTED, STOPPING")
					await webhook.send('@everyone CAPTCHA DETECTED, STOPPING')
					return True
			time.sleep(random.uniform(5,7))

client.run(token, bot=False)
