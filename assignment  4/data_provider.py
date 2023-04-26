import pandas as pd

class DataProvider:
    def __init__(self):
        self.df = pd.read_csv("dSST.csv")

    def return_year(self,*henks):
        '''

        '''
        print (list(henks))

        if len(henks) == 2:
            print("henk")
            df = self.df.loc[self.df["Year"] >= henks[0]].loc[self.df['Year']<= henks[1]]
            df_t = df.T
            return df_t.to_json()

    def return_all(self):
        '''

        '''

        df_t = self.df.T 
        return df_t.to_json()
    


