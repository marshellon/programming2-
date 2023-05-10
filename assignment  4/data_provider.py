import pandas as pd

class DataProvider:
    def __init__(self):
        self.df = pd.read_csv("dSST.csv")

    def return_year(self,*henks):
        '''
        function checks if henks is len of two
        
        henks:
                The input from year to year as a list

        return:
                Json file type to the remote server
        '''
        if len(henks) == 1:
            df = self.df.loc[self.df["Year"] >= henks[0]]
            df_t = df.T
            return df_t.to_json()

        if len(henks) == 2:
            df = self.df.loc[self.df["Year"] >= henks[0]].loc[self.df['Year']<= henks[1]]
            df_t = df.T
            return df_t.to_json()

    def return_all(self):
        ''' 
            function that rerurns entire dataframe
        
            return:
                    The dataframe as Json file
        '''
        df_t = self.df.T 
        return df_t.to_json()



