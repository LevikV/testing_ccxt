import ccxt_patch
import asyncio

async def main():
    exchange_client = ccxt_patch.weex()
    data = await exchange_client.fetch_markets()

    print(data)

if __name__ == '__main__':
    asyncio.run(main())

