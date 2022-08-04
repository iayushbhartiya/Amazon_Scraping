Summary:

The project is about scrapping a minimum hundred URLs :

The URL will be in format of"https://www.amazon.{country}/dp/{asin}".The
country code and Asin parameters are in the CSV file
https://docs.google.com/spreadsheets/d/1BZSPhk1LDrx8ytywMHWVpCqbm8URT
xTJrIRkD7PnGTM/edit?usp=sharing. The CSV file contains 1000 rows.

The project involves following libraries:

scrapy - fetching and extracting the data from given websites.
json - storing and loading the data in JSON format.

Explanation:

1. Created a project directory using - scrapy startproject Amazon
   This projects contains few inbuilt file such as pipelines.py, midlewares.py etc.
   This project contains a directory as spiders, in which we will store the created spider py files to crawl the website.

2. As there were 100 urls to fetch , used ms excel to concatenate the ASIN cells in single array and Country as well.
   Then I defined start_request to generate a list of all the URLs. Defined method parse to scrape data.
   Finally handeled 200 error to return Unavailable URl.
   By using command scrapy crawl amazon -o items.json all the yielded entries were stored in json format in items.json


Challanges, Errors and Exceptions faced:

    Handling error was quite challenging to resolve still not able to resolve all errors.
    Parsing price was also challenging as many urls have different classes which I'm not able to resolve.

I am glad I got to work on this assignment, and I learned a lot about webscraping while doing this.
THANK YOU.