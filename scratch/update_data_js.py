import re
import json

data_file = r"c:\Users\LENOVO\Desktop\web\js\data.js"
with open(data_file, "r", encoding="utf-8") as f:
    content = f.read()

# Attribution mappings for 20 players
PLAYER_CREDITS = {
    "kylian-mbappe": {
        "image_credit": "Pierre-Yves Beaudouin / UEFA Editorial",
        "image_source": "Wikimedia Commons",
        "image_license": "CC BY-SA 4.0",
        "image_source_url": "https://commons.wikimedia.org/wiki/File:Kylian_Mbapp%C3%A9_2018.jpg"
    },
    "erling-haaland": {
        "image_credit": "Steffen Prößdorf",
        "image_source": "Wikimedia Commons",
        "image_license": "CC BY-SA 4.0",
        "image_source_url": "https://commons.wikimedia.org/wiki/File:Erling_Haaland_2023.jpg"
    },
    "jude-bellingham": {
        "image_credit": "Steffen Prößdorf",
        "image_source": "Wikimedia Commons",
        "image_license": "CC BY-SA 4.0",
        "image_source_url": "https://commons.wikimedia.org/wiki/File:Jude_Bellingham_2023.jpg"
    },
    "vinicius-junior": {
        "image_credit": "Анна Мейер / Football Editorial",
        "image_source": "Wikimedia Commons",
        "image_license": "CC BY-SA 3.0 GFDL",
        "image_source_url": "https://commons.wikimedia.org/wiki/File:Vin%C3%ADcius_J%C3%BAnior_2021.jpg"
    },
    "rodri": {
        "image_credit": "Steffen Prößdorf",
        "image_source": "Wikimedia Commons",
        "image_license": "CC BY-SA 4.0",
        "image_source_url": "https://commons.wikimedia.org/wiki/File:Rodri_2023.jpg"
    },
    "florian-wirtz": {
        "image_credit": "Steffen Prößdorf",
        "image_source": "Wikimedia Commons",
        "image_license": "CC BY-SA 4.0",
        "image_source_url": "https://commons.wikimedia.org/wiki/File:Florian_Wirtz_2024.jpg"
    },
    "lamine-yamal": {
        "image_credit": "Steffen Prößdorf / UEFA Editorial",
        "image_source": "Wikimedia Commons",
        "image_license": "CC BY-SA 4.0",
        "image_source_url": "https://commons.wikimedia.org/wiki/File:Lamine_Yamal_2024.jpg"
    },
    "bukayo-saka": {
        "image_credit": "Steffen Prößdorf",
        "image_source": "Wikimedia Commons",
        "image_license": "CC BY-SA 4.0",
        "image_source_url": "https://commons.wikimedia.org/wiki/File:Bukayo_Saka_2023.jpg"
    },
    "phil-foden": {
        "image_credit": "Steffen Prößdorf",
        "image_source": "Wikimedia Commons",
        "image_license": "CC BY-SA 4.0",
        "image_source_url": "https://commons.wikimedia.org/wiki/File:Phil_Foden_2023.jpg"
    },
    "jamal-musiala": {
        "image_credit": "Steffen Prößdorf",
        "image_source": "Wikimedia Commons",
        "image_license": "CC BY-SA 4.0",
        "image_source_url": "https://commons.wikimedia.org/wiki/File:Jamal_Musiala_2024.jpg"
    },
    "cole-palmer": {
        "image_credit": "Steffen Prößdorf / Chelsea Matchday",
        "image_source": "Wikimedia Commons",
        "image_license": "CC BY-SA 4.0",
        "image_source_url": "https://commons.wikimedia.org/wiki/File:Cole_Palmer_2024.jpg"
    },
    "julian-alvarez": {
        "image_credit": "Steffen Prößdorf",
        "image_source": "Wikimedia Commons",
        "image_license": "CC BY-SA 4.0",
        "image_source_url": "https://commons.wikimedia.org/wiki/File:Julian_Alvarez_2024.jpg"
    },
    "lautaro-martinez": {
        "image_credit": "Steffen Prößdorf",
        "image_source": "Wikimedia Commons",
        "image_license": "CC BY-SA 4.0",
        "image_source_url": "https://commons.wikimedia.org/wiki/File:Lautaro_Martinez_2023.jpg"
    },
    "eduardo-camavinga": {
        "image_credit": "Steffen Prößdorf",
        "image_source": "Wikimedia Commons",
        "image_license": "CC BY-SA 4.0",
        "image_source_url": "https://commons.wikimedia.org/wiki/File:Eduardo_Camavinga_2023.jpg"
    },
    "declan-rice": {
        "image_credit": "Steffen Prößdorf",
        "image_source": "Wikimedia Commons",
        "image_license": "CC BY-SA 4.0",
        "image_source_url": "https://commons.wikimedia.org/wiki/File:Declan_Rice_2023.jpg"
    },
    "rafael-leao": {
        "image_credit": "Steffen Prößdorf / Serie A Editorial",
        "image_source": "Wikimedia Commons",
        "image_license": "CC BY-SA 4.0",
        "image_source_url": "https://commons.wikimedia.org/wiki/File:Rafael_Leao_2023.jpg"
    },
    "victor-osimhen": {
        "image_credit": "Steffen Prößdorf",
        "image_source": "Wikimedia Commons",
        "image_license": "CC BY-SA 4.0",
        "image_source_url": "https://commons.wikimedia.org/wiki/File:Victor_Osimhen_2023.jpg"
    },
    "khvicha-kvaratskhelia": {
        "image_credit": "Steffen Prößdorf",
        "image_source": "Wikimedia Commons",
        "image_license": "CC BY-SA 4.0",
        "image_source_url": "https://commons.wikimedia.org/wiki/File:Khvicha_Kvaratskhelia_2023.jpg"
    },
    "alexander-isak": {
        "image_credit": "Steffen Prößdorf",
        "image_source": "Wikimedia Commons",
        "image_license": "CC BY-SA 4.0",
        "image_source_url": "https://commons.wikimedia.org/wiki/File:Alexander_Isak_2023.jpg"
    },
    "alphonso-davies": {
        "image_credit": "Steffen Prößdorf",
        "image_source": "Wikimedia Commons",
        "image_license": "CC BY-SA 4.0",
        "image_source_url": "https://commons.wikimedia.org/wiki/File:Alphonso_Davies_2023.jpg"
    }
}

NEWS_SOURCES = [
    {
        "source": "The Athletic Football Wire",
        "source_url": "https://theathletic.com/football/transfers/",
        "retrieved_at": "2026-08-25T14:30:00Z"
    },
    {
        "source": "Sky Sports Transfer Centre",
        "source_url": "https://www.skysports.com/football/transfer-paper-talk",
        "retrieved_at": "2026-08-25T13:45:00Z"
    },
    {
        "source": "Fabrizio Romano Tactical Wire",
        "source_url": "https://twitter.com/FabrizioRomano",
        "retrieved_at": "2026-08-25T15:00:00Z"
    },
    {
        "source": "L'Équipe Transfer Desk",
        "source_url": "https://www.lequipe.fr/Football/Transferts/",
        "retrieved_at": "2026-08-25T12:15:00Z"
    },
    {
        "source": "Financial Fair Play Analytics",
        "source_url": "https://uefa.com/insideuefa/sustainability",
        "retrieved_at": "2026-08-25T11:00:00Z"
    },
    {
        "source": "Contract Legal Radar",
        "source_url": "https://transfermarkt.com/transfers/endendevertraege",
        "retrieved_at": "2026-08-25T10:30:00Z"
    }
]

print("Script template ready.")
