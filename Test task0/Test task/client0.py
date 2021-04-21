# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 13:04:12 2021

@author: Flyin
"""
import sys
import aiohttp
import asyncio

async def main(data):
    #print("main start")
    async with aiohttp.ClientSession() as session:
        #print("ses start")
        #async with session.get('http://localhost:8080/h') as resp:
            #print(resp.status)
            #print(await resp.text())

        async with session.post('http://localhost:8080/post', data=data) as resp:
            print(resp.status)
            return(await resp.text())

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    if len(sys.argv) > 1:
        text = open(sys.argv[1], 'r', encoding="utf-8")
        data = text.read()
        print(loop.run_until_complete(main(data)))
    else:
        print(loop.run_until_complete(main("I am here. I'm like to eat.")))
