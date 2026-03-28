import ccxt_patch
import asyncio
from datetime import datetime

async def main():
    api_key = 'weex_e23757a3867debd25002e6bbb814122b'
    api_secret = '440460e0d6322a28ce89f9cd0e94d43b847ac58a27b75d59fdd1c310749bb240'
    api_password = '12fdFFr2'
    params = {
        'apiKey': api_key,
        'secret': api_secret,
        'password': api_password,
        'timeout': 50000,
    }
    exchange_client = ccxt_patch.bitunix()
    symbol = 'XRP/USDT'
    ts_iso_from = '20.03.2026 00:00:00'
    dt = datetime.strptime(ts_iso_from, '%d.%m.%Y %H:%M:%S')
    since = int(dt.timestamp() * 1000)
    try:
        data = await exchange_client.fetch_ohlcv(symbol, '1m', since=since, limit=10)
    finally:
        await exchange_client.close()

    print(data)

if __name__ == '__main__':
    asyncio.run(main())

