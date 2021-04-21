# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 10:24:40 2021

@author: Flyin
"""
import aiohttp
from aiohttp import web
import time
from parsetext import parsetext




async def hello(request):
    return web.Response(text= "Hello, world")

async def wait(request):
    time.sleep(30)
    return web.Response(text= "Hello, world after Wait")

async def post_handler(request):
    #print(request)
    data = (await request.text())
    result = parsetext(data)
    #print(await request.read())
    return web.Response(text=str(result))


if __name__=='__main__':
    app = web.Application()
    app.add_routes([web.get('/h', hello),
                    web.post('/post', post_handler)])
    app.router.add_get("/w", wait)
    app.router.add_get("/", wait)    
    web.run_app(app)