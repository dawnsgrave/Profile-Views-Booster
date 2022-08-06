import asyncio
import aiohttp
import time
import os
os.system('cls')

camo = 'https://camo.githubusercontent.com/711db2f8d4351b2f54ec74158c8249da48aa6ecf032bee4872d7486737b8ff2a/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d68617a652d31333337'

async def main():
    async with aiohttp.ClientSession() as session:
        for x in range(1,999999):
            await session.get(camo)
            print(f'successfully sent {x} requests')

if __name__ == "__main__":
    asyncio.run(main())