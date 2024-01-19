# Import libraries
import requests
import pandas as pd
from bs4 import BeautifulSoup

'''
DEFINING VARIABLES/LISTS
'''

# Defining all urls
urls = ['https://en.wikipedia.org/wiki/Data_science','https://en.wikipedia.org/wiki/Machine_learning','https://en.wikipedia.org/wiki/Deep_learning',
       'https://en.wikipedia.org/wiki/Big_data','https://en.wikipedia.org/wiki/Predictive_analytics','https://en.wikipedia.org/wiki/Regression_analysis',
       'https://en.wikipedia.org/wiki/Statistical_classification', 'https://en.wikipedia.org/wiki/Natural_language_processing',
       'https://en.wikipedia.org/wiki/Data_Preprocessing', 'https://en.wikipedia.org/wiki/Feature_engineering', 'https://en.wikipedia.org/wiki/Time_series',
       'https://en.wikipedia.org/wiki/Cluster_analysis', 'https://en.wikipedia.org/wiki/Dimensionality_reduction','https://en.wikipedia.org/wiki/Data_cleansing',
       'https://en.wikipedia.org/wiki/Data_warehouse','https://en.wikipedia.org/wiki/Data_governance','https://en.wikipedia.org/wiki/Information_privacy',
       'https://en.wikipedia.org/wiki/Data_and_information_visualization','https://en.wikipedia.org/wiki/Exploratory_data_analysis',
       'https://en.wikipedia.org/wiki/A/B_testing','https://en.wikipedia.org/wiki/Ensemble_learning','https://en.wikipedia.org/wiki/Cross-validation_(statistics)',
       'https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff','https://en.wikipedia.org/wiki/Hyperparameter_optimization','https://en.wikipedia.org/wiki/Statistical_inference',
       'https://en.wikipedia.org/wiki/Anomaly_detection','https://en.wikipedia.org/wiki/Feature_scaling','https://en.wikipedia.org/wiki/Random_forest',
       'https://en.wikipedia.org/wiki/Support_vector_machine','https://en.wikipedia.org/wiki/Unsupervised_learning', 'https://en.wikipedia.org/wiki/Supervised_learning',
       'https://en.wikipedia.org/wiki/Data_mining','https://en.wikipedia.org/wiki/Pattern_recognition','https://en.wikipedia.org/wiki/Statistical_hypothesis_testing',
       'https://en.wikipedia.org/wiki/Web_scraping','https://en.wikipedia.org/wiki/Spatial_analysis','https://en.wikipedia.org/wiki/Social_network_analysis',
       'https://en.wikipedia.org/wiki/Data_journalism','https://en.wikipedia.org/wiki/Health_care_analytics','https://en.wikipedia.org/wiki/Financial_analysis',
       'https://en.wikipedia.org/wiki/Market_segmentation','https://en.wikipedia.org/wiki/Business_analytics','https://en.wikipedia.org/wiki/Sentiment_analysis',
       'https://en.wikipedia.org/wiki/Quantitative_research','https://en.wikipedia.org/wiki/Data-informed_decision-making', 'https://en.wikipedia.org/wiki/Ethics_of_artificial_intelligence']

# Defining all topics
topics = ['Data Science','Machine Learning','Deep Learning','Big Data','Predictive Analytics','Regression Analysis','Classification in Machine Learning',
'Natural Language Processing','Data Pre-processing','Feature Engineering','Time Series Analysis','Cluster Analysis',
'Dimensionality Reduction','Data Cleaning','Data Warehousing','Data Governance','Data Privacy',
'Data Visualization','Exploratory Data Analysis (EDA)','A/B Testing','Ensemble Learning','Cross-Validation',
'Bias-Variance Tradeoff','Hyperparameter Tuning','Statistical Inference','Outlier Detection','Feature Scaling',
'Random Forest','Support Vector Machines (SVM)','Unsupervised Learning','Supervised Learning','Data Mining',
'Pattern Recognition','Hypothesis Testing','Web Scraping','Spatial Analysis','Social Network Analysis','Data Journalism',
'Healthcare Analytics','Financial Analytics','Market Segmentation','Business Analytics',
'Sentiment Analysis','Quantitative Research','Data-driven Decision Making','Ethical AI']

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
    information = [api_data(url) for url in urls]

    # Store both data and topics in a df
    data_df = pd.DataFrame({'topics': topics,
                     'information': information})

    # Save df to the data folder
    data_df.to_csv('/home/lewis/code/Chat-Bot/data/Wiki-info-data.csv', sep=',', index=False)


if __name__ == '__main__':
    main()
