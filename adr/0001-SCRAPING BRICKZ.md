# Scraping Data from Brickz.my

Date created: 24 Aug 2023
Date revised: TBD

Author(s): Yu Yuen Hern

## The Need for Login
In previous version of the website, it seems login was needed in order to access more than 10 transactions per real estate project. In the latest version (as of 24 Aug 2023), it seems that this restriction has been removed.

## Location of Data in the Webpage
The data that we need is under the `table` tag, with `thead` as headers and `tbody` as the body. The `th` tag contains the name of the column while `tr` contains the data that we need.

## Navigating the Pages
The number of pages is at the `pagination` class. The max value can be used to loop all the pages and get each table.
