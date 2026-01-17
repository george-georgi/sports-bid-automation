import csv
from datetime import datetime

FILE_NAME = "weekly_bids.csv"

# Dropdown options
LEAGUES = ["NFL", "NBA", "MLB", "NHL", "Soccer", "College Football", "College Basketball", "MMA", "Boxing", "Other"]
BET_TYPES = ["Moneyline", "Spread", "Over/Under", "Parlay", "Prop", "Teaser", "Futures"]
SPORTSBOOKS = ["King Draft", "DraftKings", "FanDuel", "BetMGM", "Caesars", "WynnBET", "Draftkings Sportsbook", "Other"]
STATUSES = ["Pending", "Won", "Lost", "Voided", "Partial"]
SOCCER_LEAGUES = ["Premier League (England)", "La Liga (Spain)", "Serie A (Italy)", "Bundesliga (Germany)", "Ligue 1 (France)", "Other"]

def display_menu(options, prompt_text):
    """Display a menu and return the user's selection."""
    print(f"\n{prompt_text}")
    for i, option in enumerate(options, 1):
        print(f"  {i}. {option}")
    while True:
        try:
            choice = int(input("Select option (number): "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print(f"Please enter a number between 1 and {len(options)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def convert_odds_to_probability(odds):
    """Convert decimal odds to implied probability (0-100%)."""
    try:
        odds_float = float(odds)
        if odds_float <= 0:
            return 0
        probability = (1 / odds_float) * 100
        return round(probability, 2)
    except ValueError:
        return None

def initialize_file():
    """Create the CSV with headers if it doesn't exist."""
    try:
        with open(FILE_NAME, "x", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "date",
                "league",
                "team_1_name",
                "team_2_name",
                "bet_description",
                "bet_type",
                "bet_amount",
                "odds_team_1",
                "odds_team_2",
                "implied_prob_team_1",
                "implied_prob_team_2",
                "sportsbook",
                "status",
                "payout_amount",
                "notes"
            ])
            print("Created new weekly_bids.csv file.")
    except FileExistsError:
        pass

def add_bid(league, team_1_name, team_2_name, bet_description, bet_type, bet_amount, odds_team_1, odds_team_2, sportsbook, status="Pending", payout_amount="", notes=""):
    """Append a new bid entry to the CSV."""
    date = datetime.now().strftime("%Y-%m-%d")
    prob_team_1 = convert_odds_to_probability(odds_team_1)
    prob_team_2 = convert_odds_to_probability(odds_team_2)
    
    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            date,
            league,
            team_1_name,
            team_2_name,
            bet_description,
            bet_type,
            bet_amount,
            odds_team_1,
            odds_team_2,
            prob_team_1,
            prob_team_2,
            sportsbook,
            status,
            payout_amount,
            notes
        ])
    print(f"Bid added: {team_1_name} vs {team_2_name} ({bet_description}) - {bet_amount} on {sportsbook}.")

def main():
    initialize_file()

    print("=== Weekly Bid Tracker ===")
    league = display_menu(LEAGUES, "Select League:")
    
    # If Soccer is selected, show soccer leagues submenu
    if league == "Soccer":
        league = display_menu(SOCCER_LEAGUES, "Select Soccer League:")
    
    team_1_name = input("Team 1 name: ")
    team_2_name = input("Team 2 name: ")
    bet_description = input("Bet description: ")
    bet_type = display_menu(BET_TYPES, "Select Bet Type:")
    bet_amount = float(input("Bet amount: $"))
    odds_team_1 = input("Odds for Team 1 (decimal format, e.g., 1.95): ")
    odds_team_2 = input("Odds for Team 2 (decimal format, e.g., 1.95): ")
    sportsbook = display_menu(SPORTSBOOKS, "Select Sportsbook:")
    status = display_menu(STATUSES, "Select Status:")
    payout_amount = input("Payout amount (optional): ")
    notes = input("Notes (optional): ")

    add_bid(league, team_1_name, team_2_name, bet_description, bet_type, bet_amount, odds_team_1, odds_team_2, sportsbook, status, payout_amount, notes)

if __name__ == "__main__":
    main()