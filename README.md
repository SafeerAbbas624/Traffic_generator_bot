# Traffic Generator Bot

This project is a web bot that performs a series of actions on Google and other websites. It is designed to simulate user behavior on the internet.

## Introduction

The web bot is a Python script that uses the Selenium library to automate web browsing. It performs the following actions:

- Selects a random proxy and user agent from a predefined list
- Navigates to Yahoo.com
- Searches for Google.com on Yahoo.com
- Navigates to Google.com
- Searches for a random keyword from a predefined list
- Clicks on the first search result
- Navigates to the clicked website
- Clicks on a random link from a predefined list

## Workflow

The web bot follows the following workflow:

1. Import the required libraries
2. Define a list of proxies and user agents
3. Define a list of keywords to search for on Google
4. Define a list of links to click on after searching for a keyword
5. Enter an infinite loop
6. Inside the loop, select a random proxy and user agent
7. Create a new browser instance with the selected proxy and user agent
8. Spoof the timezone and geolocation to a random value
9. Navigate to Yahoo.com
10. Perform some actions to mimic user behavior, such as scrolling down and clicking on the search button
11. Search for Google.com on Yahoo.com
12. Navigate to Google.com
13. Search for a random keyword from the list of keywords
14. Try to find a website from the list of links in the search results
15. If a website is found, click on it
16. Navigate to the clicked website
17. Try to find a link from the list of links on the website
18. If a link is found, click on it
19. Close the browser instance
20. Wait for 60 seconds before starting the next iteration of the loop

## Installation

To install the required libraries, run the following commands:

### Linux/Mac

```bash
pip install selenium
pip install webdriver-manager
```

### Windows

```bash
pip install selenium
pip install webdriver-manager
```
### Usage
To run the web bot, execute the following command:

```bash

python web_bot.py
```

The web bot will start running and perform the actions described in the workflow section.

## Changing Keywords and Links

To change the keywords and links, modify the following lines of code:

```Python

# Keywords to put it in google search
key = [
    "Put Your keywords here seprated by inverted commas."
]

# Websites to click on after google search
sites = ["Put your link here you want the bot to click on. seprated by commas."
         ]
```

Replace the keywords and links with the desired values.

