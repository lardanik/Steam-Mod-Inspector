# Steam-Mod-Inspector
Script for quickly getting ModName ModID, WorkshopID from the collection in Steam (Most useful for server builds of Project Zomboid)
# How it works
Fetching Mod Information:
Once the URL is provided, the script begins scanning the collection. It makes an HTTP request to fetch the page content.
Using BeautifulSoup, the script parses the HTML to locate individual mod entries within the collection. It extracts relevant data, such as mod titles and their associated links.
