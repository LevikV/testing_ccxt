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
    symbol = 'BTC/USDT:USDT'
    exchange_client = ccxt_patch.weex(params)
    data_margin_mode = await exchange_client.set_margin_mode('isolated', symbol)
    data_leverage = await exchange_client.set_leverage(1, symbol)
    data = await exchange_client.create_order(symbol, 'limit', 'sell', 0.0002, 71400)
    print(data)

if __name__ == '__main__':
    asyncio.run(main())

