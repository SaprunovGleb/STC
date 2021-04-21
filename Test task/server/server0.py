# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 10:24:40 2021

@author: Flyin
"""

from aiohttp import web
from parsetext import parsetext
import concurrent.futures as pool

class Handler:
    
    def __init__(self):
        pass

    async def handler_parsetext(self, request):
        data = (await request.text())
        with pool.ThreadPoolExecutor() as executor:
            future = executor.submit(parsetext, data)    
        return web.Response(text=str(future.result()))


if __name__=='__main__':
    handler = Handler()
    app = web.Application()
    app.router.add_post('/parsetext', handler.handler_parsetext)   
    web.run_app(app, host='0.0.0.0', port=8080)