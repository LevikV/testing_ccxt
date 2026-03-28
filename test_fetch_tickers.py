import ccxt_patch
import asyncio

async def main():
    exchange_client = ccxt_patch.bitunix()
    data = await exchange_client.fetch_tickers(symbols=['BTC/USDT', 'XRP/USDT:USDT'])

    print(data)

if __name__ == '__main__':
    asyncio.run(main())

