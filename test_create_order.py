import ccxt_patch
import asyncio

async def main():
    api_key = 'd1210d02d3712a006d51921040ba0e82'
    api_secret = 'a53ae00e6b798aebf526003c475f73b7'
    
    params = {
        'apiKey': api_key,
        'secret': api_secret,
    }
    symbol = 'NOM/USDT:USDT'
    exchange_client = ccxt_patch.bitunix(params)
    
    try:
        data = await exchange_client.create_order(symbol, 'limit', 'buy', 1000, 0.00345)
    except Exception as e:
        print(e)
    finally:
        await exchange_client.close()
    print(data)

if __name__ == '__main__':
    asyncio.run(main())