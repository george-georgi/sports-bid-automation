# Sports Bid Automation Tracker

A comprehensive Python-based application for tracking and managing sports bets across multiple leagues with professional Excel formatting and analytics.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Data Fields](#data-fields)
- [Supported Leagues](#supported-leagues)
- [Configuration](#configuration)

## Features

- **Multi-League Support**: Track bets across NFL, NBA, MLB, NHL, Soccer, College Football, Basketball, MMA, and Boxing
- **Dropdown Menus**: Standardized data entry with pre-defined options to prevent errors
- **Soccer League Integration**: Dedicated team selection for 5 major European soccer leagues
- **Automatic Probability Calculation**: Converts decimal odds to implied probability percentages
- **Professional Excel Formatting**: 
  - Color-coded status indicators (Green for Won, Red for Lost)
  - Currency formatting for bet and payout amounts
  - Auto-fitted column widths
  - Professional header styling with borders
- **Timestamp Tracking**: Records exact date and time of each bet entry
- **Comprehensive Data Fields**: 15 columns capturing all essential betting information

## Requirements

- Python 3.7 or higher
- openpyxl (for Excel formatting)

## Installation

1. **Clone the repository** (or download the files):
   ```bash
   git clone <repository-url>
   cd sports-bid-automation
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install openpyxl
   ```

## Usage

1. **Run the application**:
   ```bash
   python main.py
   ```

2. **Follow the prompts**:
   - Select league from dropdown menu
   - If Soccer is selected, choose the specific league and teams
   - Enter bet details (description, type, amount)
   - Input odds in decimal format (e.g., 1.95)
   - Select status (Won or Lost)
   - Add optional payout amount and notes

3. **View results**:
   - All entries are saved to `weekly_bids.xlsx`
   - Open the file in Excel to view professionally formatted data

## Project Structure

```
sports-bid-automation/
├── main.py                 # Core application logic
├── styles.py              # Excel formatting and styling functions
├── weekly_bids.xlsx       # Generated Excel file with bet data
├── .gitignore             # Git ignore configuration
├── README.md              # This file
└── .venv/                 # Virtual environment (optional)
```

## Data Fields

| Field | Description | Example |
|-------|-------------|---------|
| Date | Entry date and time | 2026-01-17 14:35:42 |
| League | Sports league | Premier League (England) |
| Team 1 Name | First team in matchup | Real Madrid |
| Team 2 Name | Second team in matchup | Barcelona |
| Bet Description | Specific bet details | Team 1 to win |
| Bet Type | Type of wager | Moneyline, Spread, Over/Under, etc. |
| Bet Amount | Amount wagered | $50.00 |
| Odds Team 1 | Decimal odds for Team 1 | 1.95 |
| Odds Team 2 | Decimal odds for Team 2 | 1.85 |
| Implied Prob Team 1 % | Calculated probability for Team 1 | 51.28% |
| Implied Prob Team 2 % | Calculated probability for Team 2 | 54.05% |
| Sportsbook | Betting platform | DraftKings Sportsbook |
| Status | Bet outcome | Won, Lost |
| Payout Amount | Winnings if applicable | $97.50 |
| Notes | Additional information | Good odds, high confidence |

## Supported Leagues

### Primary Leagues
- NFL (National Football League)
- NBA (National Basketball Association)
- MLB (Major League Baseball)
- NHL (National Hockey League)
- College Football
- College Basketball
- MMA (Mixed Martial Arts)
- Boxing

### Soccer Leagues (with team selection)
1. **Premier League (England)** - 20 teams
2. **La Liga (Spain)** - 20 teams
3. **Serie A (Italy)** - 20 teams
4. **Bundesliga (Germany)** - 18 teams
5. **Ligue 1 (France)** - 18 teams

## Configuration

### Customizing Options

Edit the list variables in `main.py` to customize:

- **LEAGUES**: Available sports leagues
- **BET_TYPES**: Types of bets you use
- **STATUSES**: Bet outcomes
- **SOCCER_LEAGUES**: European soccer leagues
- **Team lists**: Soccer teams for each league

### Excel Styling

Modify `styles.py` to adjust:

- Header colors and fonts
- Column widths
- Number formatting
- Status color coding
- Border styles

## Tips for Best Results

1. **Consistency**: Use the same bet type and league names each time
2. **Odds Format**: Always enter odds in decimal format (e.g., 1.95, 2.50)
3. **Description**: Be specific in bet descriptions for easy tracking
4. **Regular Review**: Check your Excel file regularly to analyze win/loss ratios
5. **Payout Tracking**: Record actual payouts to track accuracy of odds calculations

## License

This project is open source and available for personal use.

## Support

For issues or suggestions, please update the code and test locally before committing changes.
