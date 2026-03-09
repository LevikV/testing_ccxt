import ccxt_patch
import asyncio

async def main():
    api_key = 'weex_e23757a3867debd25002e6bbb814122b'
    api_secret = '440460e0d6322a28ce89f9cd0e94d43b847ac58a27b75d59fdd1c310749bb240'
    api_password = '12fdFFr2'
    params = {
        'apiKey': api_key,
        'secret': api_secret,
        'password': api_password,
    }
    exchange_client = ccxt_patch.weex()
    data = await exchange_client.create_order('CHZ/USDT:USDT', 'limit', 'sell', 100, 0.3770)
    print(data)

if __name__ == '__main__':
    asyncio.run(main())

