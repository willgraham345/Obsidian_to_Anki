---
tags: note/python
type: note
---
# Basics of Web Scraping
- Web browsers convert HTML to a nice document
- Python libraries used
	- Web scraping: `BeautifulSoap` for HTML, `Scrapy` is more comprehensive
	- HTTP requests done through `requests`
- Some sites have a `robots.txt` file that specifies which parts of the site can be scraped. Respect these rules.
- Stored data can be stored in a CSV, JSON, or database

## Practice Web Scraping
- https://quotes.toscrape.com/
## Example
```python
import requests
from bs4 import BeautifulSoup

# Replace with the URL of the paper's Google Scholar page
url = "https://scholar.google.com/some-paper-url"

# Send an HTTP GET request to the Google Scholar page
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the element containing the number of citations
    citations_element = soup.find("a", {"class": "gs_or_cit"})

    if citations_element:
        # Extract and print the number of citations
        citations_text = citations_element.text
        print("Number of Citations:", citations_text)
    else:
        print("Citation count not found on the page.")
else:
    print("Failed to retrieve the page. Status code:", response.status_code)

```