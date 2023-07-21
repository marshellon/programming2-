import pandas as pd
import asyncio

class NetworkClient:
    def __init__(self,url):
        self.url = url
        self.months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        self.data = pd.read_csv("dSST.csv")
        self.process_data()
    
    def process_data(self):
        base_url = [info for info in self.url.split("/") if info]

        if len(base_url) == 2:
            year = int(base_url[1])
            df = self.data.loc[self.data["Year"] == year]
            temp_means = self.calculate_mean(df)
            asyncio.run(self.print_means(temp_means))

        elif len(base_url) == 3:
            year1, year2 = int(base_url[1]), int(base_url[2])
            df = self.data.loc[self.data["Year"] >= year1].loc[self.data['Year'] <= year2]
            temp_means = self.calculate_mean(df)
            asyncio.run(self.print_means(temp_means))

    def calculate_mean(self, df):
        temp_mean = []
        for month in df.columns:
            if month in self.months:
                temp_mean.append(df[month].sum() / len(df[month]))
        return temp_mean

    async def print_means(self, temp_means):
        z = zip(self.months, temp_means)
        for month, temp in z:
            print(f"{month}. Mean temp = {temp:.02f}")
            await asyncio.sleep(0.1)