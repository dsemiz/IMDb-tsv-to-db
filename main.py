import pandas as pd
from sqlalchemy import create_engine
import requests
from bs4 import BeautifulSoup


def download(url):

    # Creates the IMDb.db file and establishes a connection

    engine = create_engine('sqlite:///IMDb.db', echo=True)
    sqlite_connection = engine.connect()

    # Downloads the zipped file from the archive and names a table after it

    url = url

    sqlite_table = url[28:-7].replace('.', '_')

    print(f'Downloading file from {url}')

    print('')

    download_df = pd.read_csv(url, compression='gzip', header=0, sep='\t', low_memory=False)

    # Convert Pandas dataframe to sqlite table and send it to our connected database

    print(f'Converting {sqlite_table} dataframe to SQL table')

    print('')

    download_df.to_sql(sqlite_table, sqlite_connection, if_exists='replace')

    # This is set to 'replace' any existing table of the same name. Other options are 'fail' and 'append'

    print('Conversion completed')

    print('')

    sqlite_connection.close()  # Closes the connection


def main():

    request = requests.get('https://datasets.imdbws.com/')  # URL that has all the download links

    imdb_soup = BeautifulSoup(request.text, 'html.parser')  # Sets up the soup

    download_urls = imdb_soup.findAll('a')  # Finds every URL in the soup

    for url in download_urls[1:]:  # Loops through each URL except the first one (not a download link)
        url = str(url)  # Turns the soup objects into strings
        handle_url = url.find('"', 10)  # Finds the second " so that we can use it in a substring
        url = url[9:handle_url]  # Substrings the soup object into a proper URL
        download(url)  # Calls our download function, downloading from each link that it finds


if __name__ == '__main__':
    main()
