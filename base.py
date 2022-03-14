from telethon import TelegramClient, events, errors
import time

api_id = 14241570
api_hash = '8463878da2bbc8105d99087852fc3ef4'
client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage)
async def main(event):
	try:
		await event.reply('Some text')

	except errors.FloodWaitError as e:
		time.sleep(e.seconds)


client.start()
client.run_until_disconnected()