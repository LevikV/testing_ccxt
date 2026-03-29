import traceback
import ccxt_patch
import asyncio


async def main():
    weex = ccxt_patch.weex({
        "apiKey": 'weex_e23757a3867debd25002e6bbb814122b',#"weex_72f59e5446a5a15d37787a56cc48f75a",
        "secret": '440460e0d6322a28ce89f9cd0e94d43b847ac58a27b75d59fdd1c310749bb240',#"29ea72629fe1263c17c930625b018198148c833a685f841cedf41173dfcf7fee",
        "password": '12fdFFr2',
        'timeout': 50000,
        #"aiohttp_proxy": "http://VTO4VzC87K7ld5k:gmxZebld5D4feuR@46.203.240.215:58153",
    })
    try:
        print('markets')
        await weex.load_markets()
        print('markets+')

    except Exception as e:
        print(traceback.format_exc())
    finally:
        print('called')
        await weex.close()


if __name__ == '__main__':
    asyncio.run(main())