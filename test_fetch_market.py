import ccxt_patch
import asyncio

async def main():
    exchange_client = ccxt_patch.bitunix()
    symbol = 'XRP/USDT:USDT'
    data = await exchange_client.fetch_markets()
    market = data[symbol]

    print(data)

if __name__ == '__main__':
    asyncio.run(main())

