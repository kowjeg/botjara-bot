import httpx


client = httpx.AsyncClient()


async def get_temperature(lat: float, lon: float) -> float | None:
    try:
        response = await client.get(f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true')

        data = response.json()
        return data['current_weather']['temperature']
    except (httpx.TimeoutException, httpx.RequestError, httpx.HTTPStatusError, KeyError):
        return None