import os
import pandas as pd
from Bio import Entrez
from readData import Read
def search(query):
    Entrez.email = '853818291@qq.com'
    handle = Entrez.esearch(db='pubmed',
                            sort='relevance',
                            retmax='8',
                            retmode='xml',
                            term=query)
    results = Entrez.read(handle)
    return results

def fetch_details(id_list):
    ids = ','.join(id_list)
    Entrez.email = '853818291@qq.com'
    handle = Entrez.efetch(db='pubmed',
                           retmode='xml',
                           id=ids)
    results = Entrez.read(handle)
    return results

if __name__ == '__main__':

    for file in os.listdir('./CSO Catetogy'):
        if os.path.splitext(file)[-1] == '.xlsx':
            abstracts = []
            rd = Read()
            rd.read_cat(file)
            terms = rd.bat_data()
            for i,term in enumerate(terms):
                term = ' '.join(term)
                print(i,term)
                try:
                    results = search(term)
                    id_list = results['IdList']
                    papers = fetch_details(id_list)
                    for j, paper in enumerate(papers['PubmedArticle']):
                        try:
                            abstracts.append(paper['MedlineCitation']['Article']['Abstract']['AbstractText'][0])
                            if (i+1)%20==0:

                                df = pd.DataFrame({
                                    'category': [rd.category]*len(abstracts),
                                    'abstract': abstracts
                                })
                                with open('abstracts/'+file+'.csv','a+') as f:
                                    df.to_csv(f,header=False)
                                    abstracts = []
                        except Exception as e:
                            pass
                except : pass
