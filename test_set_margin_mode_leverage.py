import ccxt_patch
import asyncio

async def main():
    api_key = 'd1210d02d3712a006d51921040ba0e82'
    api_secret = 'a53ae00e6b798aebf526003c475f73b7'
    #api_password = '12fdFFr2'
    params = {
        'apiKey': api_key,
        'secret': api_secret,
        #'password': api_password,
    }
    symbol = 'BTC/USDT:USDT'
    exchange_client = ccxt_patch.bitunix(params)
    try:
        data_margin_mode = await exchange_client.set_margin_mode('isolated', symbol)
        data_leverage = await exchange_client.set_leverage(1, symbol)
    except Exception as e:
        print(e)
    finally:
        await exchange_client.close()
    
    print(data_leverage)
    print(data_margin_mode)

if __name__ == '__main__':
    asyncio.run(main())

