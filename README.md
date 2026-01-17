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
- [Tips for Best Results](#tips-for-best-results)

## Features

- **Professional GUI Interface**: User-friendly graphical interface built with tkinter
- **Multi-League Support**: Track bets across NFL, NBA, MLB, NHL, Soccer, College Football, Basketball, MMA, and Boxing
- **Dropdown Menus**: Standardized data entry with pre-defined options to prevent errors
- **Soccer League Integration**: Dedicated team selection for 5 major European soccer leagues with full team rosters
- **Automatic Probability Calculation**: Converts decimal odds to implied probability percentages
- **Professional Excel Formatting**: 
  - Color-coded status indicators (Green for Won, Red for Lost, Yellow for Pending, Orange for Partial, Gray for Voided)
  - Currency formatting for bet and payout amounts
  - Auto-fitted column widths
  - Professional header styling with dark blue background and white text
  - Borders on all data cells
- **Timestamp Tracking**: Records exact date and time of each bet entry (YYYY-MM-DD HH:MM:SS format)
- **Comprehensive Data Fields**: 15 columns capturing all essential betting information
- **Form Validation**: GUI validates all inputs before submission with helpful error messages
- **User-Friendly Design**: Clean, intuitive interface for quick bet entry

## Requirements

- Python 3.7 or higher
- openpyxl (for Excel formatting)
- tkinter (usually included with Python)

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

1. **Launch the application**:
   ```bash
   python main.py
   ```

2. **The GUI window will open** with the following sections:
   - **League Selection**: Choose from NFL, NBA, MLB, NHL, Soccer, College Football, College Basketball, MMA, Boxing, or Other
   - **Team Selection**: For Soccer, select the specific league first, then choose teams from dropdown
   - **Bet Details**: Enter description, type, and amount
   - **Odds Input**: Enter decimal odds for both teams
   - **Status**: Mark as Won or Lost
   - **Optional Fields**: Add payout amount and notes

3. **Submit your bet**:
   - Click "Submit Bet" to save your entry to Excel
   - Form validates all required fields before submission
   - Success message confirms the entry was added
   - Click "Clear" to reset the form and enter another bet

4. **View results**:
   - All entries are automatically saved to `weekly_bids.xlsx`
   - Open the file in Excel to view professionally formatted data with color coding and statistics

## Project Structure

```
sports-bid-automation/
├── main.py                 # Entry point - launches the application
├── gui.py                  # BidTrackerGUI class - handles all UI logic
├── data.py                 # Excel operations and odds calculations
├── constants.py            # All dropdown options and team data
├── styles.py               # Excel formatting and styling functions
├── weekly_bids.xlsx        # Generated Excel file with bet data
├── README.md               # This file
└── __pycache__/            # Python cache directory
```

### File Descriptions

- **main.py**: Simple entry point that initializes and runs the GUI
- **gui.py**: Contains the `BidTrackerGUI` class with all UI components, event handlers, and form validation
- **data.py**: Handles Excel file operations (`initialize_file()`, `add_bid_to_excel()`) and odds-to-probability conversion
- **constants.py**: Centralized configuration including leagues, bet types, statuses, and complete soccer team rosters

## Data Fields

| Field | Description | Format | Example |
|-------|-------------|--------|---------|
| Date | Entry date and time | YYYY-MM-DD HH:MM:SS | 2026-01-17 14:35:42 |
| League | Sports league selected | Text | Premier League (England) |
| Team 1 Name | First team in matchup | Text | Real Madrid |
| Team 2 Name | Second team in matchup | Text | Barcelona |
| Bet Description | Specific bet details | Text | Team 1 to win |
| Bet Type | Type of wager | Text | Moneyline, Spread, Over/Under, etc. |
| Bet Amount | Amount wagered | Currency | $50.00 |
| Odds Team 1 | Decimal odds for Team 1 | Decimal | 1.95 |
| Odds Team 2 | Decimal odds for Team 2 | Decimal | 1.85 |
| Implied Prob Team 1 % | Calculated probability for Team 1 | Percentage | 51.28% |
| Implied Prob Team 2 % | Calculated probability for Team 2 | Percentage | 54.05% |
| Sportsbook | Betting platform | Text | DraftKings Sportsbook |
| Status | Bet outcome | Won / Lost | Won |
| Payout Amount | Winnings if applicable | Currency | $97.50 |
| Notes | Additional information | Text | Good odds, high confidence |

## Supported Leagues

### Primary Leagues
- **NFL** - National Football League
- **NBA** - National Basketball Association
- **MLB** - Major League Baseball
- **NHL** - National Hockey League
- **College Football**
- **College Basketball**
- **MMA** - Mixed Martial Arts
- **Boxing**
- **Other** - For any other leagues or sports

### Soccer Leagues (with team selection)
1. **Premier League (England)** - 20 teams
2. **La Liga (Spain)** - 20 teams
3. **Serie A (Italy)** - 20 teams
4. **Bundesliga (Germany)** - 18 teams
5. **Ligue 1 (France)** - 18 teams

## Configuration

### Customizing Options

Edit the configuration in `constants.py`:

- **LEAGUES**: Available sports leagues (currently 10 leagues)
- **BET_TYPES**: Types of bets available (Moneyline, Spread, Over/Under, Parlay, Prop, Teaser, Futures, Tie No Bet)
- **STATUSES**: Bet outcomes (Won, Lost)
- **SOCCER_LEAGUES**: European soccer leagues
- **Team lists**: Soccer teams for each league (PREMIER_LEAGUE_TEAMS, LA_LIGA_TEAMS, SERIE_A_TEAMS, BUNDESLIGA_TEAMS, LIGUE_1_TEAMS)

For GUI logic modifications, edit `gui.py` (BidTrackerGUI class).

For Excel operations, modify functions in `data.py` (convert_odds_to_probability, initialize_file, add_bid_to_excel).

### Excel Styling

Modify `styles.py` to adjust:

- **Header colors and fonts**: Edit `apply_header_style()` function
- **Column widths**: Customize `apply_column_widths()` function
- **Number formatting**: Modify `apply_data_formatting()` function
- **Status color coding**: Update `apply_status_colors()` function
- **Border styles**: Change `apply_borders()` function

## Tips for Best Results

1. **Form Validation**: The GUI validates all required fields before submission - follow error messages for guidance
2. **Consistency**: Use the same bet type and league names each time for better tracking and analysis
3. **Odds Format**: Always enter odds in decimal format (e.g., 1.95, 2.50)
4. **Description**: Be specific in bet descriptions for easy tracking and future reference
5. **Soccer Teams**: When selecting Soccer, first choose the specific league, then select teams from the dropdown
6. **Regular Review**: Check your Excel file regularly to analyze win/loss ratios and refine strategies
7. **Payout Tracking**: Record actual payouts to verify odds calculation accuracy

## License

This project is open source and available for personal use.

## Support

For issues or suggestions, please update the code and test locally before committing changes.
