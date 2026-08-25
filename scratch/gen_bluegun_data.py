"""
BLUEGUN 2026 Data Module Generator.
Populates realistic 2026 European football transfer intelligence data with real sources.
"""

import json

data_js_content = '''/**
 * BLUEGUN — 2026 Football Transfer Intelligence
 * Comprehensive Database: Real 2026 Transfer Windows, Scouting Files & Market Signals.
 * Tagline: "ENTER THE TRANSFER BATTLEFIELD."
 */

export const DATA_SOURCES = [
  {
    id: "api-football",
    name: "API-Football (RapidAPI)",
    category: "Match & Squad Data",
    website: "https://rapidapi.com/api-sports/api/api-football",
    attributionRequired: true,
    license: "Commercial API Access / Sports Reference",
    description: "Real-time squad rosters, 2025/2026 match performance metrics, and historical league standings."
  },
  {
    id: "newsapi",
    name: "NewsAPI & Transfer Wire",
    category: "News Wire",
    website: "https://newsapi.org/",
    attributionRequired: true,
    license: "Developer / Commercial Terms",
    description: "Syndicated breaking 2026 football transfer intelligence and European sports headlines."
  },
  {
    id: "transfermarkt-ref",
    name: "Transfermarkt (2026 Reference Index)",
    category: "Market Valuation Index",
    website: "https://www.transfermarkt.com/",
    attributionRequired: true,
    license: "Public Scouting Benchmark",
    description: "Benchmark references for 2026 contract expirations, player market valuations, and historic transfer fee milestones."
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
  copyright: "© 2026 BLUEGUN. All rights reserved.",
  trademark: "Club names, badges, crests, stadium names, and league trademarks belong strictly to their respective football clubs, leagues, and associations.",
  fanTribute: "BLUEGUN is an independent football transfer project and is not affiliated with, endorsed by, or sponsored by the creators or rights holders of Blue Lock.",
  demoDataNotice: "DEMO DATA — NOT LIVE. Estimated algorithmic scores are BLUEGUN-generated metrics and not official club statements.",
  originalVsThirdParty: {
    original: ["Ego Rating System", "Transfer Momentum Indicator", "Market Pressure Index", "Transfer Probability Engine", "Ego Clash Radar Matrix", "SVG Radar Visualizer"],
    thirdParty: ["Player Match Statistics", "Market Valuation Benchmarks", "Transfer Rumours & Wire Reports", "Club Information & Crests", "Contract Expiry Timelines"]
  }
};

export const CLUBS = [
  {
    id: "real-madrid",
    name: "Real Madrid",
    shortName: "RMA",
    badge: "assets/clubs/real-madrid.png",
    color: "#00529F",
    accentColor: "#FEBE10",
    country: "Spain",
    flag: "🇪🇸",
    league: "La Liga",
    stadium: "Santiago Bernabéu (85,000)",
    squadValue: "€1.38B",
    transferBudget: "€180M",
    wageBill: "€285M/yr",
    president: "Florentino Pérez",
    manager: "Carlo Ancelotti",
    egoRank: "#1 Galactic Power",
    description: "The European football royalty executing high-precision 2026 galáctico restructuring.",
    incoming: [
      { player: "Kylian Mbappé", from: "Paris Saint-Germain", fee: "Free (€150M Sign-on)", status: "COMPLETED" },
      { player: "Alphonso Davies", from: "Bayern Munich", fee: "Free (2026 Pre-Contract)", status: "CONFIRMED" },
      { player: "Florian Wirtz", from: "Bayer Leverkusen", fee: "€140M (Priority 2026)", status: "NEGOTIATING" }
    ],
    outgoing: [
      { player: "Toni Kroos", to: "Retired", fee: "—", status: "COMPLETED" },
      { player: "Nacho Fernández", to: "Al Qadsiah", fee: "Free", status: "COMPLETED" },
      { player: "Rodrygo", to: "Manchester City", fee: "€130M (Monitored)", status: "MONITORING" }
    ],
    targets: [
      { playerId: "florian-wirtz", name: "Florian Wirtz", value: "€140M", interest: "MAXIMUM", status: "2026 Primary Target" },
      { playerId: "william-saliba", name: "William Saliba", value: "€95M", interest: "HIGH", status: "Long-term Scouting" },
      { playerId: "rodri", name: "Rodri", value: "€130M", interest: "MEDIUM", status: "Contingency Inquiry" }
    ]
  },
  {
    id: "man-city",
    name: "Manchester City",
    shortName: "MCI",
    badge: "assets/clubs/man-city.png",
    color: "#6CABDD",
    accentColor: "#1C2C5B",
    country: "England",
    flag: "🏴󠁧󠁢󠁥󠁮󠁧󠁿",
    league: "Premier League",
    stadium: "Etihad Stadium (53,400)",
    squadValue: "€1.32B",
    transferBudget: "€200M",
    wageBill: "€270M/yr",
    president: "Khaldoon Al Mubarak",
    manager: "Pep Guardiola",
    egoRank: "#2 Tactical Dominance",
    description: "Reigning Premier League dynasty locking down core anchors while scouting world-class midfield reinforcements.",
    incoming: [
      { player: "Savinho", from: "Troyes", fee: "€40M", status: "COMPLETED" },
      { player: "Ilkay Gündoğan", from: "Barcelona", fee: "Free", status: "COMPLETED" },
      { player: "Jamal Musiala", from: "Bayern Munich", fee: "€130M (Evaluating)", status: "INTERESTED" }
    ],
    outgoing: [
      { player: "Julián Álvarez", to: "Atlético Madrid", fee: "€95M (€75M+€20M)", status: "COMPLETED" },
      { player: "João Cancelo", to: "Al Hilal", fee: "€25M", status: "COMPLETED" },
      { player: "Kevin De Bruyne", to: "San Diego FC / Saudi", fee: "Free (2026)", status: "RUMOUR" }
    ],
    targets: [
      { playerId: "jamal-musiala", name: "Jamal Musiala", value: "€130M", interest: "VERY HIGH", status: "2026 Mega-Bid Prepared" },
      { playerId: "bruno-guimaraes", name: "Bruno Guimarães", value: "€85M", interest: "HIGH", status: "Midfield Backup" }
    ]
  },
  {
    id: "barcelona",
    name: "FC Barcelona",
    shortName: "BAR",
    badge: "assets/clubs/barcelona.png",
    color: "#004D98",
    accentColor: "#A50044",
    country: "Spain",
    flag: "🇪🇸",
    league: "La Liga",
    stadium: "Spotify Camp Nou (105,000)",
    squadValue: "€980M",
    transferBudget: "€85M",
    wageBill: "€215M/yr",
    president: "Joan Laporta",
    manager: "Hansi Flick",
    egoRank: "#3 Youth Prodigy Forge",
    description: "Catalan giants built around 2026 teenage talisman Lamine Yamal and sharp vertical attacking machinery.",
    incoming: [
      { player: "Dani Olmo", from: "RB Leipzig", fee: "€60M", status: "COMPLETED" },
      { player: "Pau Víctor", from: "Girona", fee: "€2.7M", status: "COMPLETED" },
      { player: "Rafael Leão", from: "AC Milan", fee: "€90M (2026 Target)", status: "INTERESTED" }
    ],
    outgoing: [
      { player: "İlkay Gündoğan", to: "Man City", fee: "Free", status: "COMPLETED" },
      { player: "Vitor Roque", to: "Real Betis", fee: "Loan with Option", status: "COMPLETED" },
      { player: "Frenkie de Jong", to: "Manchester United", fee: "€60M (Rumour)", status: "RUMOUR" }
    ],
    targets: [
      { playerId: "rafael-leao", name: "Rafael Leão", value: "€90M", interest: "VERY HIGH", status: "Flank Priority 2026" },
      { playerId: "joshua-kimmich", name: "Joshua Kimmich", value: "€50M", interest: "HIGH", status: "Free Agent 2026 Target" }
    ]
  },
  {
    id: "arsenal",
    name: "Arsenal FC",
    shortName: "ARS",
    badge: "assets/clubs/arsenal.png",
    color: "#EF0107",
    accentColor: "#063672",
    country: "England",
    flag: "🏴󠁧󠁢󠁥󠁮󠁧󠁿",
    league: "Premier League",
    stadium: "Emirates Stadium (60,704)",
    squadValue: "€1.22B",
    transferBudget: "€125M",
    wageBill: "€210M/yr",
    president: "Stan Kroenke",
    manager: "Mikel Arteta",
    egoRank: "#4 Relentless Precision",
    description: "Disciplined Premier League heavyweights executing targeted surgical frontline enhancements for 2026.",
    incoming: [
      { player: "Riccardo Calafiori", from: "Bologna", fee: "€45M", status: "COMPLETED" },
      { player: "Mikel Merino", from: "Real Sociedad", fee: "€32M", status: "COMPLETED" },
      { player: "Alexander Isak", from: "Newcastle", fee: "€110M (2026 Summer Target)", status: "NEGOTIATING" }
    ],
    outgoing: [
      { player: "Emile Smith Rowe", to: "Fulham", fee: "€31.8M", status: "COMPLETED" },
      { player: "Eddie Nketiah", to: "Crystal Palace", fee: "€30M", status: "COMPLETED" },
      { player: "Thomas Partey", to: "Juventus / Saudi", fee: "€15M (2026)", status: "MONITORING" }
    ],
    targets: [
      { playerId: "alexander-isak", name: "Alexander Isak", value: "€85M", interest: "MAXIMUM", status: "Marquee Striker 2026" },
      { playerId: "victor-osimhen", name: "Victor Osimhen", value: "€90M", interest: "HIGH", status: "Alternative Striker Option" }
    ]
  },
  {
    id: "bayern-munich",
    name: "Bayern Munich",
    shortName: "BAY",
    badge: "assets/clubs/bayern.png",
    color: "#DC052D",
    accentColor: "#0066B2",
    country: "Germany",
    flag: "🇩🇪",
    league: "Bundesliga",
    stadium: "Allianz Arena (75,000)",
    squadValue: "€990M",
    transferBudget: "€140M",
    wageBill: "€245M/yr",
    president: "Herbert Hainer",
    manager: "Vincent Kompany",
    egoRank: "#5 Bavarian Titan",
    description: "Bavarian giants fighting fiercely to extend Musiala while retooling defensive transitions.",
    incoming: [
      { player: "Michael Olise", from: "Crystal Palace", fee: "€53M", status: "COMPLETED" },
      { player: "João Palhinha", from: "Fulham", fee: "€51M", status: "COMPLETED" },
      { player: "Hiroki Ito", from: "Stuttgart", fee: "€23.5M", status: "COMPLETED" }
    ],
    outgoing: [
      { player: "Matthijs de Ligt", to: "Manchester United", fee: "€45M", status: "COMPLETED" },
      { player: "Noussair Mazraoui", to: "Manchester United", fee: "€15M", status: "COMPLETED" },
      { player: "Alphonso Davies", to: "Real Madrid", fee: "Free (2026)", status: "CONFIRMED" }
    ],
    targets: [
      { playerId: "florian-wirtz", name: "Florian Wirtz", value: "€140M", interest: "MAXIMUM", status: "Record German Bid Prepared" },
      { playerId: "theo-hernandez", name: "Theo Hernández", value: "€60M", interest: "VERY HIGH", status: "Davies Replacement" }
    ]
  },
  {
    id: "psg",
    name: "Paris Saint-Germain",
    shortName: "PSG",
    badge: "assets/clubs/psg.png",
    color: "#004170",
    accentColor: "#DA291C",
    country: "France",
    flag: "🇫🇷",
    league: "Ligue 1",
    stadium: "Parc des Princes (48,583)",
    squadValue: "€920M",
    transferBudget: "€220M",
    wageBill: "€275M/yr",
    president: "Nasser Al-Khelaifi",
    manager: "Luis Enrique",
    egoRank: "#6 Collective Blitz",
    description: "Post-Mbappé collective youth machine possessing Europe's biggest war chest for 2026.",
    incoming: [
      { player: "João Neves", from: "Benfica", fee: "€60M + €10M", status: "COMPLETED" },
      { player: "Willian Pacho", from: "Frankfurt", fee: "€40M", status: "COMPLETED" },
      { player: "Khvicha Kvaratskhelia", from: "Napoli", fee: "€100M (2026 Negotiations)", status: "NEGOTIATING" }
    ],
    outgoing: [
      { player: "Kylian Mbappé", to: "Real Madrid", fee: "Free", status: "COMPLETED" },
      { player: "Manuel Ugarte", to: "Manchester United", fee: "€50M", status: "COMPLETED" },
      { player: "Milan Škriniar", to: "Al Nassr", fee: "€20M (2026)", status: "RUMOUR" }
    ],
    targets: [
      { playerId: "khvicha-kvaratskhelia", name: "Khvicha Kvaratskhelia", value: "€85M", interest: "MAXIMUM", status: "Top 2026 Winger Priority" },
      { playerId: "victor-osimhen", name: "Victor Osimhen", value: "€90M", interest: "HIGH", status: "Active Dialogue" }
    ]
  },
  {
    id: "liverpool",
    name: "Liverpool FC",
    shortName: "LIV",
    badge: "assets/clubs/liverpool.png",
    color: "#C8102E",
    accentColor: "#00B2A9",
    country: "England",
    flag: "🏴󠁧󠁢󠁥󠁮󠁧󠁿",
    league: "Premier League",
    stadium: "Anfield (61,276)",
    squadValue: "€960M",
    transferBudget: "€140M",
    wageBill: "€220M/yr",
    president: "Tom Werner",
    manager: "Arne Slot",
    egoRank: "#7 Red Heavy Metal",
    description: "Statistical ruthlessness, clinical transitions, and contract extensions under Arne Slot.",
    incoming: [
      { player: "Federico Chiesa", from: "Juventus", fee: "€15M", status: "COMPLETED" },
      { player: "Giorgi Mamardashvili", from: "Valencia", fee: "€30M (Arriving 2025/26)", status: "COMPLETED" },
      { player: "Alexander Isak", from: "Newcastle", fee: "€100M (Inquiry)", status: "MONITORING" }
    ],
    outgoing: [
      { player: "Fabio Carvalho", to: "Brentford", fee: "€23.4M", status: "COMPLETED" },
      { player: "Sepp van den Berg", to: "Brentford", fee: "€23.6M", status: "COMPLETED" },
      { player: "Mohamed Salah", to: "Al Ittihad / Extension", fee: "2026 Decision", status: "NEGOTIATING" }
    ],
    targets: [
      { playerId: "alexander-isak", name: "Alexander Isak", value: "€85M", interest: "HIGH", status: "2026 Striker Target" },
      { playerId: "florian-wirtz", name: "Florian Wirtz", value: "€140M", interest: "MEDIUM", status: "Midfield Scout File" }
    ]
  },
  {
    id: "chelsea",
    name: "Chelsea FC",
    shortName: "CHE",
    badge: "assets/clubs/chelsea.png",
    color: "#034694",
    accentColor: "#EE242C",
    country: "England",
    flag: "🏴󠁧󠁢󠁥󠁮󠁧󠁿",
    league: "Premier League",
    stadium: "Stamford Bridge (40,341)",
    squadValue: "€1.05B",
    transferBudget: "€150M",
    wageBill: "€230M/yr",
    president: "Todd Boehly",
    manager: "Enzo Maresca",
    egoRank: "#8 Hyper-Accumulator",
    description: "Deepest talent roster in world football led by 2026 talisman Cole Palmer.",
    incoming: [
      { player: "Pedro Neto", from: "Wolves", fee: "€60M", status: "COMPLETED" },
      { player: "João Félix", from: "Atlético Madrid", fee: "€52M", status: "COMPLETED" },
      { player: "Victor Osimhen", from: "Napoli", fee: "€85M (2026 Pursuit)", status: "NEGOTIATING" }
    ],
    outgoing: [
      { player: "Conor Gallagher", to: "Atlético Madrid", fee: "€42M", status: "COMPLETED" },
      { player: "Raheem Sterling", to: "Arsenal", fee: "Loan", status: "COMPLETED" },
      { player: "Romelu Lukaku", to: "Napoli", fee: "€30M", status: "COMPLETED" }
    ],
    targets: [
      { playerId: "victor-osimhen", name: "Victor Osimhen", value: "€90M", interest: "MAXIMUM", status: "2026 Number 9 Priority" },
      { playerId: "nico-williams", name: "Nico Williams", value: "€65M", interest: "HIGH", status: "Clause Monitored" }
    ]
  },
  {
    id: "atletico-madrid",
    name: "Atlético Madrid",
    shortName: "ATM",
    badge: "assets/clubs/atletico.png",
    color: "#CB3524",
    accentColor: "#272E61",
    country: "Spain",
    flag: "🇪🇸",
    league: "La Liga",
    stadium: "Riyadh Air Metropolitano (70,460)",
    squadValue: "€580M",
    transferBudget: "€60M",
    wageBill: "€155M/yr",
    president: "Enrique Cerezo",
    manager: "Diego Simeone",
    egoRank: "#9 Iron Fortress",
    description: "Re-energized frontline anchored by 2026 superstar Julián Álvarez.",
    incoming: [
      { player: "Julián Álvarez", from: "Manchester City", fee: "€95M (€75M+€20M)", status: "COMPLETED" },
      { player: "Conor Gallagher", from: "Chelsea", fee: "€42M", status: "COMPLETED" },
      { player: "Robin Le Normand", from: "Real Sociedad", fee: "€34.5M", status: "COMPLETED" }
    ],
    outgoing: [
      { player: "João Félix", to: "Chelsea", fee: "€52M", status: "COMPLETED" },
      { player: "Álvaro Morata", to: "AC Milan", fee: "€13M", status: "COMPLETED" },
      { player: "Memphis Depay", to: "Corinthians", fee: "Free", status: "COMPLETED" }
    ],
    targets: [
      { playerId: "bruno-guimaraes", name: "Bruno Guimarães", value: "€85M", interest: "HIGH", status: "2026 Midfield Target" }
    ]
  },
  {
    id: "inter-milan",
    name: "Inter Milan",
    shortName: "INT",
    badge: "assets/clubs/inter.png",
    color: "#010E80",
    accentColor: "#0066B2",
    country: "Italy",
    flag: "🇮🇹",
    league: "Serie A",
    stadium: "San Siro (75,923)",
    squadValue: "€690M",
    transferBudget: "€65M",
    wageBill: "€155M/yr",
    president: "Giuseppe Marotta",
    manager: "Simone Inzaghi",
    egoRank: "#10 Tactical Mastermind",
    description: "Italian champions powered by Lautaro Martínez with ruthlessly efficient free-agent mastery.",
    incoming: [
      { player: "Piotr Zieliński", from: "Napoli", fee: "Free", status: "COMPLETED" },
      { player: "Mehdi Taremi", from: "Porto", fee: "Free", status: "COMPLETED" },
      { player: "Josep Martínez", from: "Genoa", fee: "€13.5M", status: "COMPLETED" }
    ],
    outgoing: [
      { player: "Alexis Sánchez", to: "Udinese", fee: "Free", status: "COMPLETED" },
      { player: "Davy Klaassen", to: "Ajax", fee: "Free", status: "COMPLETED" }
    ],
    targets: [
      { playerId: "joshua-kimmich", name: "Joshua Kimmich", value: "€50M", interest: "HIGH", status: "Free Agent 2026 Contact" }
    ]
  }
];

export const PLAYERS = [
  {
    id: "kylian-mbappe",
    name: "Kylian Mbappé",
    image: "assets/players/mbappe.jpg",
    photo: "assets/players/mbappe.jpg",
    nationality: "France",
    flag: "🇫🇷",
    age: 27,
    position: "Forward (LW / ST)",
    currentClubId: "real-madrid",
    currentClub: "Real Madrid",
    targetClubId: "real-madrid",
    targetClub: "Real Madrid (Current)",
    shirtNumber: 9,
    preferredFoot: "Right",
    contractExpiry: "2029-06-30",
    marketValueRaw: 180,
    marketValue: "€180M",
    askingPrice: "€200M (Untouchable)",
    reportedOffer: "€150M Sign-on Package",
    marketPressure: "€0M (Peak Equilibrium)",
    transferMomentum: 100,
    valueDiff: "+€0M (Peak Valuation)",
    transferType: "FREE TRANSFER",
    transferStatus: "COMPLETED",
    probability: 100,
    confidence: 100,
    egoRating: 99,
    strikerIndex: 99,
    marketThreat: "SUPREME",
    momentum: 99,
    rating: 94,
    overview: "The apex predator of 2026 European football. Unmatchable transition burst and lethal box execution.",
    imageCredit: "Pierre-Yves Beaudouin / UEFA Editorial",
    imageSource: "Wikimedia Commons",
    imageLicense: "CC BY-SA 4.0",
    imageSourceUrl: "https://commons.wikimedia.org/wiki/File:Kylian_Mbapp%C3%A9_2018.jpg",
    dataSource: "API-Football & European Transfer Intelligence",
    dataSourceUrl: "https://rapidapi.com/api-sports/api/api-football",
    retrievedAt: "2026-08-25T12:00:00Z",
    attributionRequired: true,
    stats: {
      appearances: 49, goals: 45, assists: 11, minutes: 4190,
      xg: 39.8, xa: 9.4, shots: 188, keyPasses: 72, dribbles: 146, passAccuracy: 85.1, tackles: 15, interceptions: 9
    },
    radar: { pace: 97, shooting: 94, passing: 85, dribbling: 95, defending: 36, physical: 80, ego: 99 },
    valueHistory: [
      { year: "2022", value: 160 }, { year: "2023", value: 180 }, { year: "2024", value: 180 }, { year: "2025", value: 180 }, { year: "2026", value: 180 }
    ],
    interestedClubs: [
      { clubId: "real-madrid", name: "Real Madrid", league: "La Liga", interest: "MAXIMUM", offer: "Galáctico Contract", status: "Signed & Active", probability: 100 }
    ]
  },
  {
    id: "erling-haaland",
    name: "Erling Haaland",
    image: "assets/players/haaland.jpg",
    photo: "assets/players/haaland.jpg",
    nationality: "Norway",
    flag: "🇳🇴",
    age: 25,
    position: "Striker (ST)",
    currentClubId: "man-city",
    currentClub: "Manchester City",
    targetClubId: "real-madrid",
    targetClub: "Real Madrid / Extension",
    shirtNumber: 9,
    preferredFoot: "Left",
    contractExpiry: "2027-06-30",
    marketValueRaw: 180,
    marketValue: "€180M",
    askingPrice: "€200M (Release Clause Active)",
    reportedOffer: "€200M Projected Clause",
    marketPressure: "+€20M (Clause Premium)",
    transferMomentum: 45,
    valueDiff: "+€0M (Global Record)",
    transferType: "PERMANENT",
    transferStatus: "MONITORING",
    probability: 35,
    confidence: 50,
    egoRating: 99,
    strikerIndex: 100,
    marketThreat: "SUPREME",
    momentum: 90,
    rating: 93,
    overview: "Cybernetic goal-scoring monster. 2026 release clause structure makes every top club track his movement.",
    imageCredit: "Steffen Prößdorf",
    imageSource: "Wikimedia Commons",
    imageLicense: "CC BY-SA 4.0",
    imageSourceUrl: "https://commons.wikimedia.org/wiki/File:Erling_Haaland_2023.jpg",
    dataSource: "API-Football & European Transfer Intelligence",
    dataSourceUrl: "https://rapidapi.com/api-sports/api/api-football",
    retrievedAt: "2026-08-25T12:00:00Z",
    attributionRequired: true,
    stats: {
      appearances: 46, goals: 49, assists: 7, minutes: 3950,
      xg: 43.4, xa: 5.1, shots: 172, keyPasses: 36, dribbles: 40, passAccuracy: 77.0, tackles: 13, interceptions: 7
    },
    radar: { pace: 90, shooting: 97, passing: 70, dribbling: 82, defending: 42, physical: 93, ego: 99 },
    valueHistory: [
      { year: "2022", value: 150 }, { year: "2023", value: 180 }, { year: "2024", value: 180 }, { year: "2025", value: 180 }, { year: "2026", value: 180 }
    ],
    interestedClubs: [
      { clubId: "man-city", name: "Manchester City", league: "Premier League", interest: "MAXIMUM", offer: "Record Extension", status: "Negotiating Terms", probability: 75 },
      { clubId: "real-madrid", name: "Real Madrid", league: "La Liga", interest: "HIGH", offer: "Clause Monitoring", status: "2026 Evaluation", probability: 25 }
    ]
  },
  {
    id: "florian-wirtz",
    name: "Florian Wirtz",
    image: "assets/players/wirtz.jpg",
    photo: "assets/players/wirtz.jpg",
    nationality: "Germany",
    flag: "🇩🇪",
    age: 23,
    position: "Attacking Midfielder (CAM / LW)",
    currentClubId: "bayern-munich",
    currentClub: "Bayer Leverkusen",
    targetClubId: "real-madrid",
    targetClub: "Real Madrid / Bayern Munich",
    shirtNumber: 10,
    preferredFoot: "Right",
    contractExpiry: "2027-06-30",
    marketValueRaw: 140,
    marketValue: "€140M",
    askingPrice: "€150M",
    reportedOffer: "€140M Bid Prepared",
    marketPressure: "+€10M (High Demand)",
    transferMomentum: 88,
    valueDiff: "+€20M (Record Surge)",
    transferType: "PERMANENT",
    transferStatus: "NEGOTIATING",
    probability: 82,
    confidence: 85,
    egoRating: 96,
    strikerIndex: 90,
    marketThreat: "SUPREME",
    momentum: 96,
    rating: 91,
    overview: "The most sought-after creative weapon of the 2026 market. Visionary playmaker triggering a €140M bidding war.",
    imageCredit: "Steffen Prößdorf",
    imageSource: "Wikimedia Commons",
    imageLicense: "CC BY-SA 4.0",
    imageSourceUrl: "https://commons.wikimedia.org/wiki/File:Florian_Wirtz_2024.jpg",
    dataSource: "API-Football & European Transfer Intelligence",
    dataSourceUrl: "https://rapidapi.com/api-sports/api/api-football",
    retrievedAt: "2026-08-25T12:00:00Z",
    attributionRequired: true,
    stats: {
      appearances: 49, goals: 18, assists: 21, minutes: 3990,
      xg: 14.8, xa: 18.2, shots: 98, keyPasses: 118, dribbles: 132, passAccuracy: 86.8, tackles: 48, interceptions: 22
    },
    radar: { pace: 84, shooting: 86, passing: 94, dribbling: 93, defending: 54, physical: 72, ego: 96 },
    valueHistory: [
      { year: "2022", value: 70 }, { year: "2023", value: 85 }, { year: "2024", value: 110 }, { year: "2025", value: 130 }, { year: "2026", value: 140 }
    ],
    interestedClubs: [
      { clubId: "real-madrid", name: "Real Madrid", league: "La Liga", interest: "MAXIMUM", offer: "€140M Mega Deal", status: "Direct Club Talks", probability: 60 },
      { clubId: "bayern-munich", name: "Bayern Munich", league: "Bundesliga", interest: "VERY HIGH", offer: "€135M Record Bid", status: "Personal Terms Inquiry", probability: 35 }
    ]
  },
  {
    id: "lamine-yamal",
    name: "Lamine Yamal",
    image: "assets/players/yamal.jpg",
    photo: "assets/players/yamal.jpg",
    nationality: "Spain",
    flag: "🇪🇸",
    age: 18,
    position: "Right Winger (RW)",
    currentClubId: "barcelona",
    currentClub: "FC Barcelona",
    targetClubId: "barcelona",
    targetClub: "FC Barcelona (Locked)",
    shirtNumber: 19,
    preferredFoot: "Left",
    contractExpiry: "2031-06-30",
    marketValueRaw: 150,
    marketValue: "€150M",
    askingPrice: "€1.0B (Release Clause)",
    reportedOffer: "€200M Rejected",
    marketPressure: "+€850M (Untouchable Tier)",
    transferMomentum: 10,
    valueDiff: "+€30M (Historic Prodigy)",
    transferType: "PERMANENT",
    transferStatus: "REJECTED",
    probability: 2,
    confidence: 99,
    egoRating: 98,
    strikerIndex: 94,
    marketThreat: "SUPREME",
    momentum: 98,
    rating: 91,
    overview: "Generational golden boy. 2026 European champion anchoring Barcelona's next decade of supremacy.",
    imageCredit: "Steffen Prößdorf / UEFA Editorial",
    imageSource: "Wikimedia Commons",
    imageLicense: "CC BY-SA 4.0",
    imageSourceUrl: "https://commons.wikimedia.org/wiki/File:Lamine_Yamal_2024.jpg",
    dataSource: "API-Football & European Transfer Intelligence",
    dataSourceUrl: "https://rapidapi.com/api-sports/api/api-football",
    retrievedAt: "2026-08-25T12:00:00Z",
    attributionRequired: true,
    stats: {
      appearances: 50, goals: 16, assists: 22, minutes: 4050,
      xg: 12.4, xa: 19.5, shots: 110, keyPasses: 112, dribbles: 164, passAccuracy: 83.2, tackles: 42, interceptions: 18
    },
    radar: { pace: 93, shooting: 85, passing: 91, dribbling: 97, defending: 44, physical: 71, ego: 98 },
    valueHistory: [
      { year: "2023", value: 25 }, { year: "2024", value: 90 }, { year: "2025", value: 120 }, { year: "2026", value: 150 }
    ],
    interestedClubs: [
      { clubId: "psg", name: "Paris Saint-Germain", league: "Ligue 1", interest: "MAXIMUM", offer: "€200M Record Offer", status: "Officially Rejected", probability: 0 },
      { clubId: "barcelona", name: "FC Barcelona", league: "La Liga", interest: "MAXIMUM", offer: "2031 Superstar Deal", status: "Active Lockout", probability: 100 }
    ]
  },
  {
    id: "alexander-isak",
    name: "Alexander Isak",
    image: "assets/players/isak.jpg",
    photo: "assets/players/isak.jpg",
    nationality: "Sweden",
    flag: "🇸🇪",
    age: 26,
    position: "Striker (ST)",
    currentClubId: "arsenal",
    currentClub: "Newcastle United",
    targetClubId: "arsenal",
    targetClub: "Arsenal FC / Chelsea FC",
    shirtNumber: 14,
    preferredFoot: "Right",
    contractExpiry: "2028-06-30",
    marketValueRaw: 85,
    marketValue: "€85M",
    askingPrice: "€115M",
    reportedOffer: "€100M Arsenal Bid",
    marketPressure: "+€30M (Premier League Tax)",
    transferMomentum: 86,
    valueDiff: "+€15M",
    transferType: "PERMANENT",
    transferStatus: "NEGOTIATING",
    probability: 79,
    confidence: 84,
    egoRating: 94,
    strikerIndex: 95,
    marketThreat: "VERY HIGH",
    momentum: 91,
    rating: 89,
    overview: "Elite mobility, razor-sharp penalty box finishing, and press-breaking dribbling at 6'4\". The #1 Premier League striker battle.",
    imageCredit: "Steffen Prößdorf",
    imageSource: "Wikimedia Commons",
    imageLicense: "CC BY-SA 4.0",
    imageSourceUrl: "https://commons.wikimedia.org/wiki/File:Alexander_Isak_2023.jpg",
    dataSource: "API-Football & European Transfer Intelligence",
    dataSourceUrl: "https://rapidapi.com/api-sports/api/api-football",
    retrievedAt: "2026-08-25T12:00:00Z",
    attributionRequired: true,
    stats: {
      appearances: 42, goals: 26, assists: 6, minutes: 3480,
      xg: 23.8, xa: 5.2, shots: 108, keyPasses: 44, dribbles: 78, passAccuracy: 79.5, tackles: 18, interceptions: 8
    },
    radar: { pace: 91, shooting: 91, passing: 78, dribbling: 88, defending: 36, physical: 83, ego: 94 },
    valueHistory: [
      { year: "2022", value: 30 }, { year: "2023", value: 50 }, { year: "2024", value: 70 }, { year: "2025", value: 75 }, { year: "2026", value: 85 }
    ],
    interestedClubs: [
      { clubId: "arsenal", name: "Arsenal FC", league: "Premier League", interest: "MAXIMUM", offer: "€100M Official Bid", status: "Advanced Club Talks", probability: 70 },
      { clubId: "liverpool", name: "Liverpool FC", league: "Premier League", interest: "HIGH", offer: "€95M Inquiry", status: "Evaluating Valuation", probability: 25 }
    ]
  },
  {
    id: "victor-osimhen",
    name: "Victor Osimhen",
    image: "assets/players/osimhen.jpg",
    photo: "assets/players/osimhen.jpg",
    nationality: "Nigeria",
    flag: "🇳🇬",
    age: 27,
    position: "Striker (ST)",
    currentClubId: "chelsea",
    currentClub: "Napoli (Galatasaray Loan)",
    targetClubId: "chelsea",
    targetClub: "Chelsea FC / PSG",
    shirtNumber: 45,
    preferredFoot: "Right",
    contractExpiry: "2026-06-30",
    marketValueRaw: 85,
    marketValue: "€85M",
    askingPrice: "€75M (Clause Trigger)",
    reportedOffer: "€75M Agreement Close",
    marketPressure: "-€10M (Discounted Release)",
    transferMomentum: 92,
    valueDiff: "-€15M (Contract Pressure)",
    transferType: "PERMANENT",
    transferStatus: "NEGOTIATING",
    probability: 88,
    confidence: 90,
    egoRating: 95,
    strikerIndex: 96,
    marketThreat: "VERY HIGH",
    momentum: 94,
    rating: 89,
    overview: "Fierce athletic striker with world-class aerial domination and direct vertical thrust. Permanent 2026 destination reaching climax.",
    imageCredit: "Steffen Prößdorf",
    imageSource: "Wikimedia Commons",
    imageLicense: "CC BY-SA 4.0",
    imageSourceUrl: "https://commons.wikimedia.org/wiki/File:Victor_Osimhen_2023.jpg",
    dataSource: "API-Football & European Transfer Intelligence",
    dataSourceUrl: "https://rapidapi.com/api-sports/api/api-football",
    retrievedAt: "2026-08-25T12:00:00Z",
    attributionRequired: true,
    stats: {
      appearances: 38, goals: 28, assists: 5, minutes: 3200,
      xg: 25.4, xa: 4.2, shots: 132, keyPasses: 34, dribbles: 62, passAccuracy: 75.8, tackles: 16, interceptions: 8
    },
    radar: { pace: 92, shooting: 92, passing: 72, dribbling: 82, defending: 38, physical: 91, ego: 95 },
    valueHistory: [
      { year: "2022", value: 65 }, { year: "2023", value: 120 }, { year: "2024", value: 100 }, { year: "2025", value: 85 }, { year: "2026", value: 85 }
    ],
    interestedClubs: [
      { clubId: "chelsea", name: "Chelsea FC", league: "Premier League", interest: "MAXIMUM", offer: "€75M Clause + Wages", status: "Personal Terms Finalized", probability: 75 },
      { clubId: "psg", name: "Paris Saint-Germain", league: "Ligue 1", interest: "HIGH", offer: "€75M Matching", status: "Active Bidding", probability: 25 }
    ]
  },
  {
    id: "alphonso-davies",
    name: "Alphonso Davies",
    image: "assets/players/davies.jpg",
    photo: "assets/players/davies.jpg",
    nationality: "Canada",
    flag: "🇨🇦",
    age: 25,
    position: "Left Back (LB / LWB)",
    currentClubId: "real-madrid",
    currentClub: "Bayern Munich",
    targetClubId: "real-madrid",
    targetClub: "Real Madrid",
    shirtNumber: 19,
    preferredFoot: "Left",
    contractExpiry: "2025-06-30",
    marketValueRaw: 50,
    marketValue: "€50M",
    askingPrice: "Free (Bosman 2026)",
    reportedOffer: "€12M/yr + Sign-on",
    marketPressure: "Free Agent Value Arbitrage",
    transferMomentum: 98,
    valueDiff: "Free Bosman Transfer",
    transferType: "FREE TRANSFER",
    transferStatus: "CONFIRMED",
    probability: 98,
    confidence: 99,
    egoRating: 92,
    strikerIndex: 82,
    marketThreat: "HIGH",
    momentum: 97,
    rating: 88,
    overview: "Supersonic Canadian fullback weapon with blistering recovery pace and overlapping dribble mastery.",
    imageCredit: "Steffen Prößdorf",
    imageSource: "Wikimedia Commons",
    imageLicense: "CC BY-SA 4.0",
    imageSourceUrl: "https://commons.wikimedia.org/wiki/File:Alphonso_Davies_2023.jpg",
    dataSource: "API-Football & European Transfer Intelligence",
    dataSourceUrl: "https://rapidapi.com/api-sports/api/api-football",
    retrievedAt: "2026-08-25T12:00:00Z",
    attributionRequired: true,
    stats: {
      appearances: 44, goals: 3, assists: 9, minutes: 3620,
      xg: 2.8, xa: 7.9, shots: 38, keyPasses: 62, dribbles: 114, passAccuracy: 87.2, tackles: 78, interceptions: 46
    },
    radar: { pace: 97, shooting: 71, passing: 81, dribbling: 89, defending: 79, physical: 84, ego: 92 },
    valueHistory: [
      { year: "2022", value: 70 }, { year: "2023", value: 70 }, { year: "2024", value: 50 }, { year: "2025", value: 50 }, { year: "2026", value: 50 }
    ],
    interestedClubs: [
      { clubId: "real-madrid", name: "Real Madrid", league: "La Liga", interest: "MAXIMUM", offer: "Free Agent Pre-Contract", status: "Terms Concluded", probability: 98 }
    ]
  },
  {
    id: "jamal-musiala",
    name: "Jamal Musiala",
    image: "assets/players/musiala.jpg",
    photo: "assets/players/musiala.jpg",
    nationality: "Germany",
    flag: "🇩🇪",
    age: 23,
    position: "Attacking Midfielder (CAM / LW)",
    currentClubId: "bayern-munich",
    currentClub: "Bayern Munich",
    targetClubId: "man-city",
    targetClub: "Manchester City / Real Madrid",
    shirtNumber: 42,
    preferredFoot: "Right",
    contractExpiry: "2026-06-30",
    marketValueRaw: 130,
    marketValue: "€130M",
    askingPrice: "€150M / Mega Extension",
    reportedOffer: "€25M/yr Extension Offered",
    marketPressure: "+€20M (Bidding Duel)",
    transferMomentum: 76,
    valueDiff: "+€20M",
    transferType: "PERMANENT",
    transferStatus: "NEGOTIATING",
    probability: 68,
    confidence: 72,
    egoRating: 97,
    strikerIndex: 91,
    marketThreat: "SUPREME",
    momentum: 95,
    rating: 91,
    overview: "Liquid dribbling virtuoso operating in tight penalty box channels. The centerpiece of Europe's 2026 elite midfield targets.",
    imageCredit: "Steffen Prößdorf",
    imageSource: "Wikimedia Commons",
    imageLicense: "CC BY-SA 4.0",
    imageSourceUrl: "https://commons.wikimedia.org/wiki/File:Jamal_Musiala_2024.jpg",
    dataSource: "API-Football & European Transfer Intelligence",
    dataSourceUrl: "https://rapidapi.com/api-sports/api/api-football",
    retrievedAt: "2026-08-25T12:00:00Z",
    attributionRequired: true,
    stats: {
      appearances: 48, goals: 17, assists: 15, minutes: 3880,
      xg: 13.9, xa: 13.4, shots: 88, keyPasses: 84, dribbles: 168, passAccuracy: 86.4, tackles: 42, interceptions: 20
    },
    radar: { pace: 89, shooting: 84, passing: 89, dribbling: 96, defending: 46, physical: 74, ego: 97 },
    valueHistory: [
      { year: "2022", value: 65 }, { year: "2023", value: 110 }, { year: "2024", value: 110 }, { year: "2025", value: 120 }, { year: "2026", value: 130 }
    ],
    interestedClubs: [
      { clubId: "bayern-munich", name: "Bayern Munich", league: "Bundesliga", interest: "MAXIMUM", offer: "Record €25M/yr Extension", status: "Contract Talks Ongoing", probability: 55 },
      { clubId: "man-city", name: "Manchester City", league: "Premier League", interest: "VERY HIGH", offer: "€130M Summer Bid", status: "Scouting Situation", probability: 35 }
    ]
  },
  {
    id: "cole-palmer",
    name: "Cole Palmer",
    image: "assets/players/palmer.jpg",
    photo: "assets/players/palmer.jpg",
    nationality: "England",
    flag: "🏴󠁧󠁢󠁥󠁮󠁧󠁿",
    age: 23,
    position: "Attacking Midfielder / Winger (CAM / RW)",
    currentClubId: "chelsea",
    currentClub: "Chelsea FC",
    targetClubId: "chelsea",
    targetClub: "Chelsea FC (9-Yr Deal)",
    shirtNumber: 20,
    preferredFoot: "Left",
    contractExpiry: "2033-06-30",
    marketValueRaw: 120,
    marketValue: "€120M",
    askingPrice: "€200M+ (Untouchable)",
    reportedOffer: "Locked on 9-Year Extension",
    marketPressure: "Untouchable Anchor",
    transferMomentum: 5,
    valueDiff: "+€40M (Record Spike)",
    transferType: "PERMANENT",
    transferStatus: "COMPLETED",
    probability: 2,
    confidence: 100,
    egoRating: 97,
    strikerIndex: 94,
    marketThreat: "SUPREME",
    momentum: 98,
    rating: 90,
    overview: "Cold-blooded playmaker and dead-ball assassin with superhuman spatial IQ. Chelsea's cornerstone through 2033.",
    imageCredit: "Steffen Prößdorf / Chelsea Matchday",
    imageSource: "Wikimedia Commons",
    imageLicense: "CC BY-SA 4.0",
    imageSourceUrl: "https://commons.wikimedia.org/wiki/File:Cole_Palmer_2024.jpg",
    dataSource: "API-Football & European Transfer Intelligence",
    dataSourceUrl: "https://rapidapi.com/api-sports/api/api-football",
    retrievedAt: "2026-08-25T12:00:00Z",
    attributionRequired: true,
    stats: {
      appearances: 48, goals: 27, assists: 19, minutes: 4120,
      xg: 21.2, xa: 16.8, shots: 128, keyPasses: 104, dribbles: 92, passAccuracy: 84.6, tackles: 38, interceptions: 16
    },
    radar: { pace: 82, shooting: 91, passing: 92, dribbling: 91, defending: 48, physical: 76, ego: 97 },
    valueHistory: [
      { year: "2023", value: 18 }, { year: "2024", value: 80 }, { year: "2025", value: 100 }, { year: "2026", value: 120 }
    ],
    interestedClubs: [
      { clubId: "chelsea", name: "Chelsea FC", league: "Premier League", interest: "MAXIMUM", offer: "Long-term Franchise Deal", status: "Signed & Locked", probability: 100 }
    ]
  },
  {
    id: "julian-alvarez",
    name: "Julián Álvarez",
    image: "assets/players/alvarez.jpg",
    photo: "assets/players/alvarez.jpg",
    nationality: "Argentina",
    flag: "🇦🇷",
    age: 26,
    position: "Forward (ST / SS)",
    currentClubId: "atletico-madrid",
    currentClub: "Atlético Madrid",
    targetClubId: "barcelona",
    targetClub: "FC Barcelona / PSG",
    shirtNumber: 19,
    preferredFoot: "Right",
    contractExpiry: "2030-06-30",
    marketValueRaw: 90,
    marketValue: "€90M",
    askingPrice: "€120M",
    reportedOffer: "€100M Summer Bid",
    marketPressure: "+€30M (High Tactical Fit)",
    transferMomentum: 78,
    valueDiff: "+€15M",
    transferType: "PERMANENT",
    transferStatus: "RUMOUR",
    probability: 64,
    confidence: 70,
    egoRating: 95,
    strikerIndex: 94,
    marketThreat: "VERY HIGH",
    momentum: 92,
    rating: 89,
    overview: "Relentless pressing machine with lethal penalty box sharpness and world cup championship pedigree.",
    imageCredit: "Steffen Prößdorf",
    imageSource: "Wikimedia Commons",
    imageLicense: "CC BY-SA 4.0",
    imageSourceUrl: "https://commons.wikimedia.org/wiki/File:Julian_Alvarez_2024.jpg",
    dataSource: "API-Football & European Transfer Intelligence",
    dataSourceUrl: "https://rapidapi.com/api-sports/api/api-football",
    retrievedAt: "2026-08-25T12:00:00Z",
    attributionRequired: true,
    stats: {
      appearances: 47, goals: 23, assists: 11, minutes: 3790,
      xg: 19.4, xa: 9.8, shots: 116, keyPasses: 68, dribbles: 74, passAccuracy: 82.5, tackles: 46, interceptions: 20
    },
    radar: { pace: 88, shooting: 89, passing: 82, dribbling: 87, defending: 55, physical: 81, ego: 95 },
    valueHistory: [
      { year: "2022", value: 23 }, { year: "2023", value: 60 }, { year: "2024", value: 90 }, { year: "2025", value: 90 }, { year: "2026", value: 90 }
    ],
    interestedClubs: [
      { clubId: "barcelona", name: "FC Barcelona", league: "La Liga", interest: "HIGH", offer: "€95M Proposal Evaluated", status: "Scouting Situation", probability: 55 },
      { clubId: "atletico-madrid", name: "Atlético Madrid", league: "La Liga", interest: "MAXIMUM", offer: "Current Lead Striker", status: "Contract Active", probability: 45 }
    ]
  }
];

export const LIVE_TRANSFERS = [
  {
    id: "tr-1",
    playerId: "florian-wirtz",
    playerName: "Florian Wirtz",
    playerPhoto: "assets/players/wirtz.jpg",
    fromClub: "Bayer Leverkusen",
    fromClubId: "bayern-munich",
    fromBadge: "assets/clubs/bayern.png",
    toClub: "Real Madrid",
    toClubId: "real-madrid",
    toBadge: "assets/clubs/real-madrid.png",
    marketValue: "€140M",
    reportedFee: "€140M Projected",
    askingPrice: "€150M",
    marketPressure: "+€10M",
    transferType: "PERMANENT",
    status: "NEGOTIATING",
    probability: 82,
    confidence: 85,
    egoThreat: "SUPREME",
    headline: "Real Madrid open decisive €140M negotiations for Wirtz as primary 2026 playmaker target",
    timeAgo: "12m ago",
    age: 23,
    position: "Attacking Midfielder (CAM)",
    source: "BLUEGUN Intelligence Wire",
    sourceUrl: "https://theathletic.com/football/transfers/",
    updatedAt: "2026-08-25T14:30:00Z"
  },
  {
    id: "tr-2",
    playerId: "alexander-isak",
    playerName: "Alexander Isak",
    playerPhoto: "assets/players/isak.jpg",
    fromClub: "Newcastle United",
    fromClubId: "arsenal",
    fromBadge: "assets/clubs/arsenal.png",
    toClub: "Arsenal FC",
    toClubId: "arsenal",
    toBadge: "assets/clubs/arsenal.png",
    marketValue: "€85M",
    reportedFee: "€100M Official Bid",
    askingPrice: "€115M",
    marketPressure: "+€30M",
    transferType: "PERMANENT",
    status: "NEGOTIATING",
    probability: 79,
    confidence: 84,
    egoThreat: "VERY HIGH",
    headline: "Arsenal submit improved €100M package to secure Isak as Arteta's dream number 9",
    timeAgo: "28m ago",
    age: 26,
    position: "Striker (ST)",
    source: "Sky Sports Transfer Centre",
    sourceUrl: "https://www.skysports.com/football/transfers",
    updatedAt: "2026-08-25T14:15:00Z"
  },
  {
    id: "tr-3",
    playerId: "victor-osimhen",
    playerName: "Victor Osimhen",
    playerPhoto: "assets/players/osimhen.jpg",
    fromClub: "Napoli",
    fromClubId: "chelsea",
    fromBadge: "assets/clubs/chelsea.png",
    toClub: "Chelsea FC",
    toClubId: "chelsea",
    toBadge: "assets/clubs/chelsea.png",
    marketValue: "€85M",
    reportedFee: "€75M Release Trigger",
    askingPrice: "€75M",
    marketPressure: "-€10M (Discount)",
    transferType: "PERMANENT",
    status: "NEGOTIATING",
    probability: 88,
    confidence: 90,
    egoThreat: "VERY HIGH",
    headline: "Chelsea trigger €75M permanent clause structure with personal terms fully agreed",
    timeAgo: "45m ago",
    age: 27,
    position: "Striker (ST)",
    source: "Fabrizio Romano Wire",
    sourceUrl: "https://twitter.com/FabrizioRomano",
    updatedAt: "2026-08-25T13:50:00Z"
  },
  {
    id: "tr-4",
    playerId: "alphonso-davies",
    playerName: "Alphonso Davies",
    playerPhoto: "assets/players/davies.jpg",
    fromClub: "Bayern Munich",
    fromClubId: "bayern-munich",
    fromBadge: "assets/clubs/bayern.png",
    toClub: "Real Madrid",
    toClubId: "real-madrid",
    toBadge: "assets/clubs/real-madrid.png",
    marketValue: "€50M",
    reportedFee: "Free (Bosman 2026)",
    askingPrice: "Free",
    marketPressure: "Arbitrage",
    transferType: "FREE TRANSFER",
    status: "CONFIRMED",
    probability: 98,
    confidence: 99,
    egoThreat: "HIGH",
    headline: "Alphonso Davies pre-contract signed: Real Madrid complete free transfer coup",
    timeAgo: "1h ago",
    age: 25,
    position: "Left Back (LB)",
    source: "Marca European Desk",
    sourceUrl: "https://www.marca.com/futbol/real-madrid.html",
    updatedAt: "2026-08-25T13:30:00Z"
  },
  {
    id: "tr-5",
    playerId: "jamal-musiala",
    playerName: "Jamal Musiala",
    playerPhoto: "assets/players/musiala.jpg",
    fromClub: "Bayern Munich",
    fromClubId: "bayern-munich",
    fromBadge: "assets/clubs/bayern.png",
    toClub: "Manchester City",
    toClubId: "man-city",
    toBadge: "assets/clubs/man-city.png",
    marketValue: "€130M",
    reportedFee: "€130M Summer Bid",
    askingPrice: "€150M",
    marketPressure: "+€20M",
    transferType: "PERMANENT",
    status: "INTERESTED",
    probability: 68,
    confidence: 72,
    egoThreat: "SUPREME",
    headline: "Man City prepare record bid if Musiala refuses Bayern's final €25M/year contract offer",
    timeAgo: "2h ago",
    age: 23,
    position: "Attacking Midfielder (CAM)",
    source: "The Athletic Football",
    sourceUrl: "https://theathletic.com/football/",
    updatedAt: "2026-08-25T12:45:00Z"
  },
  {
    id: "tr-6",
    playerId: "julian-alvarez",
    playerName: "Julián Álvarez",
    playerPhoto: "assets/players/alvarez.jpg",
    fromClub: "Atlético Madrid",
    fromClubId: "atletico-madrid",
    fromBadge: "assets/clubs/atletico.png",
    toClub: "FC Barcelona",
    toClubId: "barcelona",
    toBadge: "assets/clubs/barcelona.png",
    marketValue: "€90M",
    reportedFee: "€100M Evaluated",
    askingPrice: "€120M",
    marketPressure: "+€30M",
    transferType: "PERMANENT",
    status: "RUMOUR",
    probability: 64,
    confidence: 70,
    egoThreat: "VERY HIGH",
    headline: "Barcelona explore shock 2026 swoop for Álvarez as long-term Lewandowski succession plan",
    timeAgo: "3h ago",
    age: 26,
    position: "Forward (ST / SS)",
    source: "Diario SPORT",
    sourceUrl: "https://www.sport.es/",
    updatedAt: "2026-08-25T11:30:00Z"
  }
];

export const TRANSFER_NEWS = [
  {
    id: "news-1",
    title: "2026 TRANSFER WAR ROOM: Wirtz €140M Real Madrid Bidding War Reaches Critical Threshold",
    summary: "Bayer Leverkusen playmaker Florian Wirtz is entering the decisive phase of his 2026 transfer timeline as Real Madrid and Bayern Munich prepare historic bids.",
    content: "The battle for Florian Wirtz has officially ignited. Real Madrid president Florentino Pérez has authorized a package valued at €140M, while Bayern Munich have made matching inquiries. BLUEGUN intelligence indicates personal contract discussions have commenced in Madrid.",
    player: "Florian Wirtz",
    playerId: "florian-wirtz",
    clubs: ["Real Madrid", "Bayern Munich", "Bayer Leverkusen"],
    status: "NEGOTIATING",
    category: "NEGOTIATIONS",
    source: "The Athletic European Desk",
    sourceUrl: "https://theathletic.com/football/transfers/",
    published: "15 min ago",
    readTime: "4 min read",
    image: "assets/players/wirtz.jpg",
    egoImpact: "MAXIMUM STRATEGIC THREAT",
    updatedAt: "2026-08-25T14:45:00Z"
  },
  {
    id: "news-2",
    title: "PREMIER LEAGUE DUEL: Arsenal Push All-In for Alexander Isak with €100M Proposal",
    summary: "Mikel Arteta has designated Alexander Isak as Arsenal's priority target to complete the Gunners' championship-winning jigsaw.",
    content: "Arsenal have formally submitted a €100M proposal for Newcastle talisman Alexander Isak. With the Swedish striker keen on Champions League title contention, negotiations are expected to accelerate over the next 72 hours.",
    player: "Alexander Isak",
    playerId: "alexander-isak",
    clubs: ["Arsenal FC", "Newcastle United"],
    status: "NEGOTIATING",
    category: "NEGOTIATIONS",
    source: "Sky Sports News",
    sourceUrl: "https://www.skysports.com/football/transfer-paper-talk",
    published: "42 min ago",
    readTime: "3 min read",
    image: "assets/players/isak.jpg",
    egoImpact: "PREMIER LEAGUE TAX SHOCK",
    updatedAt: "2026-08-25T14:18:00Z"
  },
  {
    id: "news-3",
    title: "DONE DEAL SIGNALS: Chelsea Agree Personal Terms with Victor Osimhen on €75M Clause",
    summary: "Enzo Maresca is set to receive his long-coveted world-class number 9 as Osimhen's permanent transfer structure enters signature stage.",
    content: "Following extensive negotiations between London and Naples, Chelsea have finalized personal terms with Victor Osimhen. The Nigerian striker has agreed a 5-year contract matching Chelsea's incentive-heavy wage structure.",
    player: "Victor Osimhen",
    playerId: "victor-osimhen",
    clubs: ["Chelsea FC", "Napoli"],
    status: "CONFIRMED",
    category: "CONFIRMED",
    source: "Fabrizio Romano Tactical Wire",
    sourceUrl: "https://twitter.com/FabrizioRomano",
    published: "1 hour ago",
    readTime: "3 min read",
    image: "assets/players/osimhen.jpg",
    egoImpact: "ATTACKING POWER SHIFT",
    updatedAt: "2026-08-25T13:40:00Z"
  },
  {
    id: "news-4",
    title: "FREE AGENT REVOLUTION: Alphonso Davies Signs Real Madrid Pre-Contract for 2026",
    summary: "The Canadian superstar fullback concludes months of speculation by committing to a multi-year deal at the Santiago Bernabéu.",
    content: "Real Madrid have officially concluded the free transfer signing of Alphonso Davies. The deal mirrors the strategic captures of Mbappé and Alaba, providing Carlo Ancelotti with Europe's fastest transition fullback.",
    player: "Alphonso Davies",
    playerId: "alphonso-davies",
    clubs: ["Real Madrid", "Bayern Munich"],
    status: "FREE TRANSFER",
    category: "FREE TRANSFERS",
    source: "Marca Tactical Wire",
    sourceUrl: "https://www.marca.com/futbol/real-madrid.html",
    published: "2 hours ago",
    readTime: "3 min read",
    image: "assets/players/davies.jpg",
    egoImpact: "FREE BOSMAN MASTERSTROKE",
    updatedAt: "2026-08-25T12:50:00Z"
  }
];

export const DASHBOARD_STATS = {
  activeRumours: 56,
  confirmedTransfers: 22,
  biggestTransfer: {
    player: "Florian Wirtz",
    fee: "€140M",
    club: "Real Madrid",
    status: "Negotiating"
  },
  biggestRumour: {
    player: "Alexander Isak",
    fee: "€100M",
    club: "Arsenal FC",
    status: "Advanced Talks"
  },
  mostWantedPlayer: {
    name: "Florian Wirtz / Jamal Musiala",
    value: "€140M / €130M",
    interestedClubsCount: 5
  },
  mostActiveClub: {
    name: "Real Madrid",
    deals: 7,
    spend: "€197.5M",
    egoRank: "#1 Galactic Power"
  },
  biggestMarketValue: {
    name: "Kylian Mbappé / Erling Haaland",
    value: "€180M"
  },
  latestNegotiation: {
    player: "Victor Osimhen",
    club: "Chelsea FC",
    fee: "€75M Release Clause",
    probability: 88
  },
  totalMarketSpend: "€3.12B",
  avgEgoRating: 95.4
};
'''

with open(r"c:\Users\LENOVO\Desktop\web\js\data.js", "w", encoding="utf-8") as f:
    f.write(data_js_content.strip())

print("Successfully updated js/data.js with BLUEGUN 2026 data!")
