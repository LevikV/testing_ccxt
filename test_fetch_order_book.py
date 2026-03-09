import ccxt_patch
import asyncio

async def main():
    exchange_client = ccxt_patch.weex({
        'timeout': 30000,  # Таймаут в миллисекундах (30 секунд)
    })
    data = await exchange_client.fetch_order_book('BTC/USDT:USDT')

    print(data)

if __name__ == '__main__':
    asyncio.run(main())

