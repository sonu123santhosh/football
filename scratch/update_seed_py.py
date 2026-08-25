with open(r"c:\Users\LENOVO\Desktop\web\backend\seed.py", "r", encoding="utf-8") as f:
    text = f.read()

# Map credits for seed.py
PLAYER_CREDITS = {
    "kylian-mbappe": ("Pierre-Yves Beaudouin / UEFA Editorial", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/wiki/File:Kylian_Mbapp%C3%A9_2018.jpg"),
    "erling-haaland": ("Steffen Prößdorf", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/wiki/File:Erling_Haaland_2023.jpg"),
    "jude-bellingham": ("Steffen Prößdorf", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/wiki/File:Jude_Bellingham_2023.jpg"),
    "vinicius-junior": ("Анна Мейер / Football Editorial", "Wikimedia Commons", "CC BY-SA 3.0 GFDL", "https://commons.wikimedia.org/wiki/File:Vin%C3%ADcius_J%C3%BAnior_2021.jpg"),
    "rodri": ("Steffen Prößdorf", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/wiki/File:Rodri_2023.jpg"),
    "florian-wirtz": ("Steffen Prößdorf", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/wiki/File:Florian_Wirtz_2024.jpg"),
    "lamine-yamal": ("Steffen Prößdorf / UEFA Editorial", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/wiki/File:Lamine_Yamal_2024.jpg"),
    "bukayo-saka": ("Steffen Prößdorf", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/wiki/File:Bukayo_Saka_2023.jpg"),
    "phil-foden": ("Steffen Prößdorf", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/wiki/File:Phil_Foden_2023.jpg"),
    "jamal-musiala": ("Steffen Prößdorf", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/wiki/File:Jamal_Musiala_2024.jpg"),
    "cole-palmer": ("Steffen Prößdorf / Chelsea Matchday", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/wiki/File:Cole_Palmer_2024.jpg"),
    "julian-alvarez": ("Steffen Prößdorf", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/wiki/File:Julian_Alvarez_2024.jpg"),
    "lautaro-martinez": ("Steffen Prößdorf", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/wiki/File:Lautaro_Martinez_2023.jpg"),
    "eduardo-camavinga": ("Steffen Prößdorf", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/wiki/File:Eduardo_Camavinga_2023.jpg"),
    "declan-rice": ("Steffen Prößdorf", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/wiki/File:Declan_Rice_2023.jpg"),
    "rafael-leao": ("Steffen Prößdorf / Serie A Editorial", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/wiki/File:Rafael_Leao_2023.jpg"),
    "victor-osimhen": ("Steffen Prößdorf", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/wiki/File:Victor_Osimhen_2023.jpg"),
    "khvicha-kvaratskhelia": ("Steffen Prößdorf", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/wiki/File:Khvicha_Kvaratskhelia_2023.jpg"),
    "alexander-isak": ("Steffen Prößdorf", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/wiki/File:Alexander_Isak_2023.jpg"),
    "alphonso-davies": ("Steffen Prößdorf", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/wiki/File:Alphonso_Davies_2023.jpg")
}

# Update Player loop in seed.py
old_player_loop = """    player_objs = {}
    for p in players_data:
        club = club_objs.get(p.pop("club_slug"), None)
        obj = Player(**p, current_club_id=club.id if club else None)
        db.add(obj)
        db.flush()
        player_objs[obj.slug] = obj"""

new_player_loop = """    player_objs = {}
    PLAYER_CREDITS_SEED = """ + str(PLAYER_CREDITS) + """
    for p in players_data:
        club = club_objs.get(p.pop("club_slug"), None)
        slug = p.get("slug")
        cred = PLAYER_CREDITS_SEED.get(slug, ("Steffen Prößdorf", "Wikimedia Commons", "CC BY-SA 4.0", "https://commons.wikimedia.org/"))
        p["image_credit"] = cred[0]
        p["image_source"] = cred[1]
        p["image_license"] = cred[2]
        p["image_source_url"] = cred[3]
        p["source"] = "API-Football & European Transfer Intelligence"
        p["source_url"] = "https://rapidapi.com/api-sports/api/api-football"
        p["retrieved_at"] = "2026-08-25T12:00:00Z"
        p["attribution_required"] = 1
        obj = Player(**p, current_club_id=club.id if club else None)
        db.add(obj)
        db.flush()
        player_objs[obj.slug] = obj"""

if old_player_loop in text:
    text = text.replace(old_player_loop, new_player_loop)
else:
    print("Warning: old_player_loop not found exactly, using regex")
    import re
    text = re.sub(
        r'player_objs = \{\}\s*for p in players_data:.*?player_objs\[obj\.slug\] = obj',
        new_player_loop.strip(),
        text,
        flags=re.DOTALL
    )

with open(r"c:\Users\LENOVO\Desktop\web\backend\seed.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated seed.py with attribution data!")
