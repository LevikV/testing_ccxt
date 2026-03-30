import ccxt_patch
import asyncio

async def main():
    exchange_client = ccxt_patch.bitunix()
    symbols=['HFT/USDT', 'HFT/USDT:USDT']
    try:
        data = await exchange_client.fetch_tickers(symbols)
    except Exception as e:
        print(e)
    finally:
        await exchange_client.close()

    print(data)

if __name__ == '__main__':
    asyncio.run(main())