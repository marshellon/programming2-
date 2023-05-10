class  ArticlcePrinter:
    def printer(self,information_dict:dict):
        """
        use:
            gets the dictionary and safe the data as XML

        retrurn:
                NONE
        """
        for id in information_dict:
            with open (f"{id}.xml","w") as f:
                f.write(str(information_dict[id]))