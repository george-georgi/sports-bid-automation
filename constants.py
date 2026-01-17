# Dropdown options
LEAGUES = ["NFL", "NBA", "MLB", "NHL", "Soccer", "College Football", "College Basketball", "MMA", "Boxing", "Other"]
BET_TYPES = ["Moneyline", "Spread", "Over/Under", "Parlay", "Prop", "Teaser", "Futures", "Tie No Bet"]
STATUSES = ["Won", "Lost"]
SOCCER_LEAGUES = ["Premier League (England)", "La Liga (Spain)", "Serie A (Italy)", "Bundesliga (Germany)", "Ligue 1 (France)", "Other"]

# Soccer teams by league
PREMIER_LEAGUE_TEAMS = ["Arsenal", "Aston Villa", "Bournemouth", "Brentford", "Brighton", "Chelsea", "Crystal Palace", "Everton", "Fulham", "Ipswich Town", "Leicester City", "Liverpool", "Manchester City", "Manchester United", "Newcastle United", "Nottingham Forest", "Southampton", "Tottenham", "West Ham", "Wolverhampton"]

LA_LIGA_TEAMS = ["Real Madrid", "Barcelona", "Atlético Madrid", "Real Sociedad", "Villarreal", "Athletic Bilbao", "Girona", "Real Betis", "Valencia", "Sevilla", "Las Palmas", "Getafe", "Rayo Vallecano", "Osasuna", "Real Valladolid", "Celta Vigo", "Leganés", "Alavés", "Mallorca", "Huesca"]

SERIE_A_TEAMS = ["Juventus", "Inter", "AC Milan", "Roma", "Lazio", "Napoli", "Atalanta", "Fiorentina", "Torino", "Sassuolo", "Sampdoria", "Monza", "Udinese", "Salernitana", "Frosinone", "Lecce", "Verona", "Como", "Cagliari", "Empoli"]

BUNDESLIGA_TEAMS = ["Bayern Munich", "Borussia Dortmund", "RB Leipzig", "Bayer Leverkusen", "Stuttgart", "Union Berlin", "Borussia Mönchengladbach", "Wolfsburg", "Eintracht Frankfurt", "Mainz", "Hoffenheim", "SC Freiburg", "Cologne", "Augsburg", "VfB Bochum", "Holstein Kiel", "St. Pauli", "Heidenheim"]

LIGUE_1_TEAMS = ["PSG", "Marseille", "Monaco", "Lyon", "Lille", "Lens", "Nice", "Rennes", "Nantes", "Toulouse", "Strasbourg", "Brest", "Saint-Étienne", "Montpellier", "Angers", "Le Havre", "Lorient", "Reims"]

SOCCER_TEAMS_MAP = {
    "Premier League (England)": PREMIER_LEAGUE_TEAMS,
    "La Liga (Spain)": LA_LIGA_TEAMS,
    "Serie A (Italy)": SERIE_A_TEAMS,
    "Bundesliga (Germany)": BUNDESLIGA_TEAMS,
    "Ligue 1 (France)": LIGUE_1_TEAMS,
}

FILE_NAME = "weekly_bids.xlsx"
