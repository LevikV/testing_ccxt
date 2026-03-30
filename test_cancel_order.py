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
        'timeout': 50000,
    }
    exchange_client = ccxt_patch.bitunix(params)
    symbol = 'XRP/USDT:USDT'
    order_id = '2038456902333808640'
    try:
        data = await exchange_client.cancel_order(order_id, symbol)
    except Exception as e:
        print(e)
    finally:
        await exchange_client.close()

    print(data)

if __name__ == '__main__':
    asyncio.run(main())

