

import requests
from pprint import pprint

token = "2619421814940190"

ur = [
    f'https://www.superheroapi.com/api.php/{token}/search/Hulk',
    f'https://www.superheroapi.com/api.php/{token}/search/Thanos',
    f'https://www.superheroapi.com/api.php/{token}/search/Captain%America',
]


def requests_get(url_all):
    g = (requests.get(url) for url in url_all)
    return g


def hero():
    super_hero = []
    for item in requests_get(ur):
        intelligence = item.json()
        for power in intelligence['results']:
            super_hero.append({
                'name': power['name'],
                'intelligence': power['powerstats']['intelligence'],
            })
        pprint(super_hero)


    intelligence_hero = 0
    for intel_hero in super_hero:
        if intelligence_hero < int(intel_hero['intelligence']):
            intelligence_hero = int(intel_hero['intelligence'])
            name = intel_hero['name']

    pprint(f"Самый крутой интеллект у {name}, интеллект его равен: {intelligence_hero}")

hero()
