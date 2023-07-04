import pandas as  pd

class Provider:
    def __init__(self):
        self.df = pd.read_csv("dSST.csv")

    def return_all(self):

        ''' 
            function that rerurns entire dataframe
        
            return:
                    The dataframe as Json file
        '''
        df_t = self.df.T
        return df_t.to_json()

    def return_year(self,*years):
        '''
        function checks if years list is len one of two
        
        henks:
                The input from year to year as a list

        return:
                Json file type to the remote server
        '''
        if len(years) == 1:
            df = self.df.loc[self.df["Year"] >= years[0]]
            df_t = df.T
            return df_t.to_json()
        if len(years) == 2:
            df = self.df.loc[self.df["Year"] >= years[0]].loc[self.df['Year']<= years[1]]
            df_t = df.T
            return df_t.to_json()


    