from telethon import TelegramClient, events, errors
import time

api_id = 
api_hash = ''
client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage)
async def main(event):
	try:
		await event.reply('Some text')

	except errors.FloodWaitError as e:
		time.sleep(e.seconds)


client.start()
client.run_until_disconnected()
