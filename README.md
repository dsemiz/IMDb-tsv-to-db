# IMDb-tsv-to-db

This project uses BeautifulSoup, Pandas, and Sqlalchemy to scrape, download, and convert the IMDb database (compressed into several different tables and formatted as .tsv) into a single SQLite formatted database. 

I made this project because I was practising SQL (after not using it daily for some time) and was disappointed to find it in the wrong file structure/format. Alternative databases for practice (such as Chinook) are fairly small and didn't provide many opportunities for advanced SQL queries.

The runtime is fairly long due to the size of the downloads, it may take up to 40 minutes on a slow internet connection. 
