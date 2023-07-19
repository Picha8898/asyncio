import asyncio 
import time
from urllib.parse import urlsplit

#get the http/s  status of webpage
async def get_status(url):
    #split the url into components
    url_parsed = urlsplit(url)
    print(f'{time.ctime()} fetch {url}')
    # open  the components
    if url_parsed.scheme=='https':
        reader, writer = await asyncio.open_connection(url_parsed.hostname, 443, ssl=True)
    else:
        reader, writer = await asyncio.open_connection(url_parsed.hostname, 88)
    #send GET request
    query = f'GET{url_parsed} HTTP/1.1\r\nhost: {url_parsed.hostname}\r\n\r\n'
    #write query to socket
    writer.write(query.encode())
    #wait for the bytes to be written to the socket
    await writer.drain()
    #read the single line response
    response = await reader.readline()
    #close the connection
    writer.close()
    #decode and strip white space
    status = response.decode().strip()
    print(f'{time.ctime()} done {url}')

    #return the response
    return status

#main coroutine
async def main():
    #List of top 10 website to check
    sites = ['https://www.google.com/',
             'https://www.youtube.com/',
             'https://www.facebook.com/',
             'https://www.twitter.com/',
             'https://www.instagram.com/',
             'https://www.baidu.com/',
             'https://www.wikipedia.org/',
             'https://www.yandex.ru/',
             'https://www.yahoo.com/',
             'https://www.whatsapp.com/'
             ]
    # create all coroutine requests
    coros = [get_status(url) for url in sites]
    #execute all coroutines and wait
    results = await asyncio.gather(*coros)
    #process all results
    for url, status in zip(sites, results):
        #report status
        print(f'{time.ctime()} {url:30}:\t{status}')
        
#run the asyncio program
asyncio.run(main())