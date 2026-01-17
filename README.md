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

- **Professional GUI Interface**: User-friendly graphical interface with tkinter
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
- **Form Validation**: GUI validates all inputs before submission with helpful error messages
- **User-Friendly Design**: Clean, intuitive interface for quick bet entry

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

1. **Launch the application**:
   ```bash
   python main.py
   ```

2. **Enter your bet details** using the intuitive GUI form:
   - Select league from dropdown menu
   - Choose team names (with dropdowns for soccer leagues)
   - Enter bet description and select bet type
   - Input bet amount and odds in decimal format
   - Select status (Won or Lost)
   - Optionally add payout amount and notes

3. **Submit your bet**:
   - Click "Submit Bet" to save your entry
   - Form validates all required fields before submission
   - Success message confirms the entry was added
   - Click "Clear" to reset the form and enter another bet

4. **View results**:
   - All entries are automatically saved to `weekly_bids.xlsx`
   - Open the file in Excel to view professionally formatted data with color coding and statistics

## Project Structure

```
sports-bid-automation/
├── main.py                 # Core CLI application logic
├── gui.py                  # Graphical user interface (recommended)
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
| Team 2 Name | Second team inGUI application with tkinter interface
├── styles.py              # Excel formatting and styling functions
├── weekly_bids.xlsx       # Generated Excel file with bet data
├── README.md              # This file
└── __pycache__/           # Python cache directory | 51.28% |
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

1. **Use the GUI**: The graphical interface is more user-friendly and provides real-time validation
2. **Consistency**: Use the same bet type and league names each time
3. **Odds Format**: Always enter odds in decimal format (e.g., 1.95, 2.50)
4. **Description**: Be specific in bet descriptions for easy tracking
5. **Regular Review**: Check your Excel file regularly to analyze win/loss ratios
6. **Payout Tracking**: Record actual payouts to track accuracy of odds calculations

## License

This project is open source and available for personal use.

## Support

For issues or suggestions, please update the code and test locally before committing changes.
Form Validation**: The GUI validates all required fields before submission - follow error messages for guidance
2. **Consistency**: Use the same bet type and league names each time for better tracking and analysis
3. **Odds Format**: Always enter odds in decimal format (e.g., 1.95, 2.50)
4. **Description**: Be specific in bet descriptions for easy tracking and future reference
5. **Soccer Teams**: When selecting Soccer, first choose the specific league, then select teams from the dropdown
6. **Regular Review**: Check your Excel file regularly to analyze win/loss ratios and refine strategies
7. **Payout Tracking**: Record actual payouts to verify odds calculation accuracy