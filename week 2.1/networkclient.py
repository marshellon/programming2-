import asyncio
import aiohttp

class NetworkClient:
    def __init__(self, base_url):
        self.base_url = base_url

    async def fetch_data(self, endpoint, callback):
        url = self.base_url + endpoint

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                result = await callback(data)
                return result

async def process_data(data):
    # Process the received data and calculate the average temperature
    years = data.keys()
    temperatures = []

    for year in years:
        temperature = data[year]['J-D']  # Access the temperature value
        temperatures.append(temperature)

    average_temperature = sum(temperatures) / len(temperatures)

    return {'average_temperature': average_temperature}

async def main():
    base_url = "http://localhost:9000/data/"
    client = NetworkClient(base_url)

    # Define the list of endpoint calls to be made
    # endpoints = ["all", "year/2019", "year/2020"]
    endpoints = [info for info in base_url.split("/") if info]
    # Gather the results of all the endpoint calls
    tasks = [client.fetch_data(endpoint, process_data) for endpoint in endpoints]
    results = await asyncio.gather(*tasks)

    # Print the results
    for result in results:
        print(result)

# Run the asyncio event loop
asyncio.run(main())
