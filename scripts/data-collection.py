# Import libraries
import requests
import pandas as pd
from bs4 import BeautifulSoup

'''
DEFINING VARIABLES/LISTS
'''

# Define differnet URL needed
urls = ['https://en.wikipedia.org/wiki/Data_science',
             'https://en.wikipedia.org/wiki/Deep_learning',
             'https://en.wikipedia.org/wiki/Explainable_artificial_intelligence',
             'https://en.wikipedia.org/wiki/Data_and_information_visualization',
             'https://en.wikipedia.org/wiki/Natural_language_processing',
             'https://en.wikipedia.org/wiki/Data_engineering']

# Define differnet topics (Each wiki page)
topics = ['Data Science',
          'Deep Learning',
          'Explainable AI',
          'Data Visualization',
          'NLP',
          'Data Engineering']

'''
FUNCTIONS
'''

# API retrieval Functon
def api_data(url):
    # Divider variable
    div = (f'\n')

    # Get response fropm the API
    response = requests.get(url)

    # Pull the paragraphs out of the raw html data
    raw_html = response.content
    soup = BeautifulSoup(raw_html, 'html.parser')
    information = soup.find_all('p')

    # Remove all the HTML tags
    paras = [i.text for i in information]

    # Removed '\n' element if there is one
    if '\n' in paras:
        paras.remove('\n')

    # Join all the paragraphs together and add a divider between each
    final_info = div.join(paras)

    # Return final state of information (Uncleaned)
    return final_info


def main():
    # Create a list of data
    wiki_information = [api_data(url) for url in urls]

    # Store both data and topics in a df
    wiki_data_df = pd.DataFrame({'topics': topics,
                        'information': wiki_information})

    # Save df to the data folder
    wiki_data_df.to_csv('/home/lewis/code/Chat-Bot/data/Wiki-info-data.csv', sep=',', index=False)


if __name__ == '__main__':
    main()
