# Scraping Data from Brickz.my

Date created: 24 Aug 2023
Date revised: TBD

Author(s): Yu Yuen Hern

## The Need for Login
In previous version of the website, it seems login was needed in order to access more than 10 transactions per real estate project. In the latest version (as of 24 Aug 2023), it seems that this restriction has been removed.

## Navigating Housing Projects
The scraper needs to know the list of available housing projects in the region of interest: Kuala Lumpur and Selangor (Klang Valley).

The URI is in the following format:
```
https://www.brickz.my/transactions/residential/{STATE}/
```
At this point, the scraper should obtain all the project name with the corresponding links and the number of transactions, and save it as a CSV file.

## Navigating the Pages of Transactions
In each housing project, there are pages of transactions. The number of pages is at the `pagination` class. The max value can be used to loop all the pages and get each table.

The URI is in the following format:
```
https://www.brickz.my/transactions/residential/{STATE}/{AREA}/{PROJECT}/{TYPE}/page/1/
```
At this point, the scraper should obtain the max number of pages of each project and save it in the previous CSV file.

Upon further investigation of the website, it seems each page is always 20 transactions. Thus, the number of pages can be calculated using the number of transactions obtained in the previous step, and rounding it up:
```
number_of_pages = round(number_of_transactions / 20)
```

## Location of Data in the Webpage
The data that we need is under the `table` tag, with `thead` as headers and `tbody` as the body. The `th` tag contains the name of the column while `tr` contains the data that we need.

This can be done recursively using a loop.