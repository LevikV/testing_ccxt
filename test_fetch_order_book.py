import ccxt_patch
import asyncio

async def main():
    symbol = 'XRP/USDT:USDT'
    exchange_client = ccxt_patch.bitunix({
        'timeout': 30000,  # Таймаут в миллисекундах (30 секунд)
    })
    try:
        data = await exchange_client.fetch_order_book(symbol, limit=5)
    finally:
        await exchange_client.close()
    print(data)

if __name__ == '__main__':
    asyncio.run(main())

