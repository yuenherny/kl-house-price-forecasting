# Scraping Data from Brickz.my

Date created: 24 Aug 2023
Date revised: TBD

Author(s): Yu Yuen Hern

## Website Structure
### The Need for Login
In previous version of the website, it seems login was needed in order to access more than 10 transactions per real estate project. In the latest version (as of 24 Aug 2023), it seems that this restriction has been removed.

### Navigating Housing Projects
The scraper needs to know the list of available housing projects in the region of interest: Kuala Lumpur and Selangor (Klang Valley).

The URI is in the following format:
```
https://www.brickz.my/transactions/residential/{STATE}/
```
At this point, the scraper should obtain all the project name with the corresponding links and the number of transactions, and save it as a CSV file.

### Navigating the Pages of Transactions
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

### Location of Data in the Webpage
The data that we need is under the `table` tag, with `thead` as headers and `tbody` as the body. The `th` tag contains the name of the column while `tr` contains the data that we need.

This can be done recursively using a loop.

## Selection of Scraping Tools
There are a few categories of web scraping tools available in the market, and the most popular approaches are:
1. Code-based:
    - `requests`
    - `requests-html`
    - `selenium`
2. UI-based:
    - UiPath
    - BluePrism
    - Automation Anywhere

and each has their own fair share of advantages and disadvantages.

### Python `requests` and `requests-html` library
The most primitive way is to directly cURL the HTML from the website. However, Brickz.my has anti-bot measures in place:
1. Error #1: `Enable JavaScript and cookies to continue`
    - Solved using `AsyncHTMLSession` from `requests-html` instead of `requests`
2. Error #2: `Checking if the site connection is secure`
    - Solves by passing headers into the request body
    ```
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }
    ```
3. Error #3: `www.brickz.my needs to review the security of your connection before proceeding`
    - These error suggests that the website might greet us with a CAPTCHA challenge and render JS files, hence using `requests` and its related counterparts is not enough, and the access must be done from a real web browser, as suggested by [this StackOverflow thread](https://stackoverflow.com/questions/74022759/site-restricting-access-to-web-scraper)
    - This leaves us with `selenium` and UI-based methods, where a browser is opened to access the website

### Python `selenium` library