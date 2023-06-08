# modules
from Bio import Entrez
from multiprocessing import Process
from articleprinter import ArticlePrinter
import ssl

# keys and utensils
ssl._create_default_https_context = ssl._create_unverified_context

class ArticleHarvister:

    def __init__(self):
        self.artricle_id = input("provide an article ID:")
        Entrez.email = "m.e.martinus@st.hanze.nl"
        self.api_key = ""
        self.get_file()



    def get_file(self):
        """
        use:
                Get all the references of an given article
        retunrns:
                    List: With refences of the givin aricle ID
        """
        information_dict = {}
        counter = 0
        file = Entrez.elink(dbfrom="pubmed",
                        db="pmc",
                        LinkName="pubmed_pmc_refs",
                        id=self.artricle_id,
                        api_key=self.api_key)
        results = Entrez.read(file)
        references = [f'{link["Id"]}' for link in results[0]["LinkSetDb"][0]["Link"]] 

        for reference in references:
            if counter < 10:
                counter += 1
                handle = Entrez.efetch(db="pubmed",
                                id=reference ,
                                retmode="xml",
                                api_key=self.api_key)
                information_dict[reference] = handle.read()
        return information_dict
    
            
                  



if __name__ == "__main__":
    print('Waiting for the process...')
    harvister = ArticleHarvister()
    dict = harvister.get_file()
    printer = ArticlePrinter()
    process = Process(target=printer.printer(dict))
    process.start()
    print('Files printed in folder')
    process.join()
    
    
   



  




    