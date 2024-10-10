# Steam-Mod-Inspector
Script for quickly getting ModName ModID, WorkshopID from the collection in Steam (Most useful for server builds of Project Zomboid)
# How it works
Fetching Mod Information:
Once the URL is provided, the script begins scanning the collection. It makes an HTTP request to fetch the page content.
Using BeautifulSoup, the script parses the HTML to locate individual mod entries within the collection. It extracts relevant data, such as mod titles and their associated links.
![Screenshot_1](https://github.com/user-attachments/assets/893ea3b1-ab70-4bc8-9c6b-69e85a632d5d)
## Requirements
- Python 3.12 or later
- The following packages:
  - requests==2.31.0
  - beautifulsoup4==4.12.2

## How to Install
1. Clone this repository:
   ```
   git clone https://github.com/lardanik/Steam-Mod-Inspector
   ```
   ```
   cd Steam-Mod-Inspector
   ```
## Install dependencies:
```
   pip install -r requirements.txt
```
OR
```
pip install requests==2.31.0
pip install beautifulsoup4==4.12.2
```
## How to Run
Run the script: steam_workshop_monitor.py
