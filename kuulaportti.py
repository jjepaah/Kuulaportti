"""

Tarvittavat kirjastot:
py -m pip install requests
py -m pip install beautifulsoup4

"""

import requests
import time
from bs4 import BeautifulSoup

games_found = 0;

while games_found <= 10:
    URL = "https://www.kuulaportti.fi/game/all/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(id="all_games_list")
    game_elements = results.find_all("tr")

    games_found = len(game_elements)-1

    if games_found == 10:
        print("Peliä ei löytynyt")
    else:
        for x in range(20):
            print("Peli löytyi! Peli löytyi! Peli löytyi! Peli löytyi! Peli löytyi!")

    time.sleep(600)
