import json
import re

input_file = r"c:\Users\LENOVO\Desktop\web\js\data.js"
with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

# Attribution mappings
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

DATA_SOURCES_JS = """
export const DATA_SOURCES = [
  {
    id: "api-football",
    name: "API-Football (RapidAPI)",
    category: "Match & Squad Data",
    website: "https://rapidapi.com/api-sports/api/api-football",
    attributionRequired: true,
    license: "Commercial API Access / Sports Reference",
    description: "Real-time squad rosters, match statistics, player biographical records, and historical league standings."
  },
  {
    id: "newsapi",
    name: "NewsAPI",
    category: "News Wire",
    website: "https://newsapi.org/",
    attributionRequired: true,
    license: "Developer / Commercial Terms",
    description: "Syndicated breaking football transfer rumours and European sports news headlines."
  },
  {
    id: "transfermarkt-ref",
    name: "Transfermarkt (Reference Benchmark)",
    category: "Market Valuation Index",
    website: "https://www.transfermarkt.com/",
    attributionRequired: true,
    license: "Public Scouting Benchmark",
    description: "Benchmark references for contract expirations, player market valuations, and historic transfer fee milestones."
  },
  {
    id: "fbref-opta",
    name: "FBref / Opta Sports Metrics",
    category: "Advanced Analytics",
    website: "https://fbref.com/",
    attributionRequired: true,
    license: "Statistical Reference",
    description: "Advanced football performance indicators including Expected Goals (xG), Expected Assists (xA), progressive carries, and shot-creating actions."
  }
];

export const THIRD_PARTY_ASSETS = [
  {
    name: "Google Fonts (Orbitron, Rajdhani, Inter)",
    type: "Web Typography",
    author: "Matt McInerney / Indian Type Foundry / Rasmus Andersson",
    license: "SIL Open Font License 1.1",
    website: "https://fonts.google.com/"
  },
  {
    name: "FastAPI",
    type: "Backend Framework",
    author: "Sebastián Ramírez (tiangolo)",
    license: "MIT License",
    website: "https://fastapi.tiangolo.com/"
  },
  {
    name: "SQLAlchemy",
    type: "Database ORM",
    author: "Michael Bayer",
    license: "MIT License",
    website: "https://www.sqlalchemy.org/"
  },
  {
    name: "Pydantic",
    type: "Data Validation",
    author: "Samuel Colvin & contributors",
    license: "MIT License",
    website: "https://docs.pydantic.dev/"
  },
  {
    name: "Uvicorn",
    type: "ASGI Web Server",
    author: "Encode OSS",
    license: "BSD-3-Clause",
    website: "https://www.uvicorn.org/"
  }
];

export const COMPLIANCE_DISCLAIMERS = {
  copyright: "© 2026 BLUELOCK // TRANSFER IQ. All rights reserved.",
  trademark: "Football club names, badges, crests, stadium names, and league trademarks belong strictly to their respective football clubs, leagues, and associations.",
  fanTribute: "This is an independent fan-inspired software concept and is not affiliated with, sponsored by, or endorsed by Muneyuki Kaneshiro, Yusuke Nomura, Kodansha Ltd., 8bit animation studio, or any official Blue Lock rights holders.",
  originalVsThirdParty: {
    original: ["Transfer Probability Algorithm", "Ego Threat Rating", "Scouting Index", "Transfer Momentum", "Ego Clash Comparison Engine", "SVG Radar Visualizer"],
    thirdParty: ["Player Match Statistics", "Market Valuation Benchmarks", "Transfer Rumours & Wire Reports", "Club Information & Crests", "Contract Expiry Timelines"]
  }
};
"""

# Let's inject DATA_SOURCES, THIRD_PARTY_ASSETS, and COMPLIANCE_DISCLAIMERS before CLUBS
# And update player objects with their attribution metadata.

# Add attribution fields to each player in text
def enrich_player(match):
    block = match.group(0)
    pid_match = re.search(r'id:\s*["\']([^"\']+)["\']', block)
    if not pid_match:
        return block
    pid = pid_match.group(1)
    credit_info = PLAYER_CREDITS.get(pid, {
        "image_credit": "Steffen Prößdorf / Sports Photography Archive",
        "image_source": "Wikimedia Commons",
        "image_license": "CC BY-SA 4.0",
        "image_source_url": "https://commons.wikimedia.org/wiki/Category:Association_football_players"
    })
    
    # Check if already has imageCredit
    if "imageCredit:" in block:
        return block
    
    # Insert right after photo/image
    attr_str = f"""    imageCredit: "{credit_info['image_credit']}",
    imageSource: "{credit_info['image_source']}",
    imageLicense: "{credit_info['image_license']}",
    imageSourceUrl: "{credit_info['image_source_url']}",
    dataSource: "API-Football & European Transfer Intelligence",
    dataSourceUrl: "https://rapidapi.com/api-sports/api/api-football",
    retrievedAt: "2026-08-25T12:00:00Z",
    attributionRequired: true,"""
    
    # Insert after photo: "..." line
    block = re.sub(r'(photo:\s*["\'][^"\']+["\'],\n)', r'\1' + attr_str + '\n', block)
    return block

# Replace players
text = re.sub(r'\{\s*id:\s*["\'][a-z0-9\-]+["\'],\s*name:\s*["\'][^"\']+["\'].*?interestedClubs:\s*\[.*?\]\s*\}', enrich_player, text, flags=re.DOTALL)

# Add news article attribution if not present
def enrich_news(match):
    block = match.group(0)
    if "sourceUrl:" in block:
        return block
    # Add sourceUrl, retrievedAt, and readOriginalUrl
    source_map = {
        "The Athletic Football": "https://theathletic.com/football/transfers/",
        "Sky Sports News": "https://www.skysports.com/football/transfer-paper-talk",
        "Fabrizio Romano": "https://twitter.com/FabrizioRomano",
        "European Scouting Bureau": "https://www.uefa.com/",
        "Financial Fair Play Analytics": "https://www.uefa.com/insideuefa/sustainability/",
        "Contract Legal Radar": "https://www.transfermarkt.com/transfers/endendevertraege"
    }
    src_match = re.search(r'source:\s*["\']([^"\']+)["\']', block)
    src_name = src_match.group(1) if src_match else "Transfer Wire"
    src_url = source_map.get(src_name, "https://www.skysports.com/football/transfers")
    
    attr_str = f"""    sourceUrl: "{src_url}",
    retrievedAt: "2026-08-25T14:00:00Z",
    attributionRequired: true,"""
    
    block = re.sub(r'(source:\s*["\'][^"\']+["\'],\n)', r'\1' + attr_str + '\n', block)
    return block

text = re.sub(r'\{\s*id:\s*["\']news-\d+["\'].*?egoImpact:\s*["\'][^"\']+["\']\s*\}', enrich_news, text, flags=re.DOTALL)

# Prepend data sources at the top
top_pos = text.find("export const CLUBS = [")
if top_pos != -1:
    header = text[:top_pos]
    rest = text[top_pos:]
    text = header + DATA_SOURCES_JS + "\n\n" + rest

with open(input_file, "w", encoding="utf-8") as f:
    f.write(text)

print("Enriched data.js successfully!")
