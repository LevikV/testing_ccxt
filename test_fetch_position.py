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
        'useragent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
        'sidecar': "01ac8581d5a48dcd4d36b61c558de02abcfd505eeb84356b5fbd27817978b3c502",
        'vs': "Z5m7GGm8dKHsRC9swHY67gy9fjcV46q1",
        'terminalcode': "71d0f8857eef4038863b48e52ed61ef5",
        'token': "eyJhbGciOiJSUzI1NiJ9.eyJqdGkiOiIzZDM2ZGUzNy03ZDljLTQ4ZDktYmU4Ni0zZDljZmExMDAzNmI1NTk0ODgxMTkiLCJ1aWQiOiJvZ3REQUtkaEE4MWcvUVg0WUVjWXBnPT0iLCJzdWIiOiJjb20qKioqQGdtYWlsLmNvbSIsImlwIjoiMFJ1Q0oxNmZCZkVsSDF6N3YvSXFPUT09IiwiZGlkIjoiQlNlVVJhOGpZVWVpY25RVFQrSm8yV2liUmFsYk9pVk1rRFRMQ0pLVGFSQ2cyTXZxWm1pSEU2YnRhK3Q5SCtxQSIsInN0cyI6MCwiaWF0IjoxNzc0NDM0MzAwLCJleHAiOjE3ODIyMTAzMDAsInB1c2hpZCI6Im9Oakw2bVpvaHhPbTdXdnJmUi9xZ0E9PSIsImF0bCI6IjEiLCJpc3MiOiJ1cGV4In0.1DCWJ3dnUiu4PO0hcSm14O9uPey1U_XZcJTkON4H6F_Lf-loFawtXvvyaK3EM2V80uTKmEU1wOTqjqWQN1L07adgKRWh1Vu7-DCeCrB-IPb40XzyVLaFiLbQVXfa3smNOqE99oxctPyl1yThtse4nC2vEyI7oupZGAXuaGxf6_w",
    }
    exchange_client = ccxt_patch.bitunix(params)
    symbol = 'BTC/USDT:USDT'
    
    try:
        data = await exchange_client.fetch_position(symbol)
    finally:
        await exchange_client.close()

    print(data)

if __name__ == '__main__':
    asyncio.run(main())

