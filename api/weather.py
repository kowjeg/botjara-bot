import httpx


client = httpx.AsyncClient()


async def get_temperature():
    try:
        response = await client.get('https://api.open-meteo.com/v1/forecast?latitude=55.75&longitude=37.62&current_weather=true')

        data = response.json()
        return data['current_weather']['temperature']
    except (httpx.TimeoutException, httpx.RequestError, httpx.HTTPStatusError, KeyError):
        return None