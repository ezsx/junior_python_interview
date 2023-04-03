import asyncio
from aiohttp import web

async def handle(request):
    return web.Response(text="Hello, World!")
    pass

async def main():
    app = web.Application()
    app.router.add_get('/', handle)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()

    print("Server started at http://localhost:8080")
    await asyncio.Event().wait()

if __name__ == '__main__':
    asyncio.run(main())
