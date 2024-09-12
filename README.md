This script shuts down or restarts your computer

Prerequisites
None

How to run the script
Steps on how to run the script along with suitable examples.

Type the following on the command line: python PowerOptions.py

Press enter and wait for prompt. Type “r” to restart or “s” to shut down

Example: python PowerOptions.py Use 'r' for restart and 's' for shutdown: r

Screenshot/GIF showing the sample use of the script
python PowerOptions.py Use 'r' for restart and 's' for shutdown: r



WEBSCRAPPING PROJECT
# Web Scraping Script

This Python script is designed to scrape quotes and authors from a specified website. It uses the `requests` library to fetch web page content and `BeautifulSoup` to parse the HTML.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

You can install the required libraries using pip:

```bash
pip install requests beautifulsoup4

NOTE

Adjust Selectors: The script looks for quotes in <span> tags with class 'text' and authors in <small> tags with class 'author'.
You might need to update these selectors based on the actual HTML structure of the target website.
Handle Errors: The script does not include error handling for failed requests or missing elements. Consider adding error handling for a more robust solution.
Respect Terms of Service: Ensure that scraping is allowed on the website you are targeting by checking its robots.txt file and terms of service.

