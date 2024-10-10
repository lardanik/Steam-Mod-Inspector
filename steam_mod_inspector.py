import requests
from bs4 import BeautifulSoup
import re
import time
import os
from tkinter import Tk
from tkinter import filedialog
from concurrent.futures import ThreadPoolExecutor
import sys

ascii_art = """\
██╗░░░░░░█████╗░██████╗░██████╗░░█████╗░███╗░░██╗██╗██╗░░██╗
██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔══██╗████╗░██║██║██║░██╔╝
██║░░░░░███████║██████╔╝██║░░██║███████║██╔██╗██║██║█████═╝░
██║░░░░░██╔══██║██╔══██╗██║░░██║██╔══██║██║╚████║██║██╔═██╗░
███████╗██║░░██║██║░░██║██████╔╝██║░░██║██║░╚███║██║██║░╚██╗
╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝╚═╝░░╚═╝
"""

print(ascii_art)

# Link to the Steam Workshop collection
collection_url = input("Link to the Steam Workshop collection: ")

def fetch_mod_info(workshop_link):
    mod_page_response = requests.get(workshop_link)
    if mod_page_response.status_code == 200:
        mod_soup = BeautifulSoup(mod_page_response.text, 'html.parser')
        description_element = mod_soup.find('div', {'class': 'workshopItemDescription'})

        if description_element:
            description = description_element.text
            # Searching Mod ID in description
            mod_id_match = re.search(r'Mod ID:\s*(\S+)', description)
            if mod_id_match:
                mod_id = mod_id_match.group(1)
            else:
                mod_id = "Not found"
        else:
            mod_id = "Description not found"

        return mod_id
    else:
        print(f"Failed to get mod page: {workshop_link}")
        return None

def fetch_mods_from_collection(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        mods = []
        mod_elements = soup.find_all('div', {'class': 'collectionItemDetails'})

        with ThreadPoolExecutor() as executor:
            # Collect links to mod pages
            workshop_links = [mod.find('a')['href'] for mod in mod_elements]
            # Receive information about each mod in parallel
            mod_ids = list(executor.map(fetch_mod_info, workshop_links))

            for mod, mod_id in zip(mod_elements, mod_ids):
                title = mod.find('div', {'class': 'workshopItemTitle'}).text.strip()
                workshop_link = mod.find('a')['href']
                workshop_id = workshop_link.split('id=')[-1]

                mods.append({
                    'title': title,
                    'workshop_id': workshop_id,
                    'mod_id': mod_id
                })

        return mods
    else:
        print("Unable to access collection page.")
        return []

print("Scanning...")

mods = fetch_mods_from_collection(collection_url)

clear_line()
print("Scanning complete!")
print("Choose where to save the file.")

root = Tk()
root.withdraw()
save_path = filedialog.asksaveasfilename(
    title="Save File",
    defaultextension=".txt",
    filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
)

if save_path:
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    with open(save_path, 'w', encoding='utf-8') as file:
        for mod in mods:
            file.write(f"ModName: {mod['title']}, Workshop ID: {mod['workshop_id']}, Mod ID: {mod['mod_id']}\n")

    print(f"Mod information saved to file {save_path}.")
else:
    print("Path to save the file is not selected.")
