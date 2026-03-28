import ccxt_patch
import asyncio

async def main():
    symbol = 'XRP/USDT:USDT'
    exchange_client = ccxt_patch.bitunix()
    try:
        data = await exchange_client.fetch_funding_rate(symbol)
    finally:
        await exchange_client.close()

    print(data)

if __name__ == '__main__':
    asyncio.run(main())

