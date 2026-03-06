import ccxt_patch
import asyncio

async def main():
    exchange_client = ccxt_patch.weex()
    markets = await exchange_client.load_markets()

    print(exchange_client.markets)

if __name__ == '__main__':
    asyncio.run(main())

