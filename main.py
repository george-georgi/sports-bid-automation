import csv
from datetime import datetime

FILE_NAME = "weekly_bids.csv"

def initialize_file():
    """Create the CSV with headers if it doesn't exist."""
    try:
        with open(FILE_NAME, "x", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "program", "bid_amount", "notes"])
            print("Created new weekly_bids.csv file.")
    except FileExistsError:
        pass  # File already exists

def add_bid(program, bid_amount, notes=""):
    """Append a new bid entry to the CSV."""
    date = datetime.now().strftime("%Y-%m-%d")
    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, program, bid_amount, notes])
    print(f"Bid added for {program}.")

def main():
    initialize_file()

    print("=== Weekly Bid Tracker ===")
    program = input("Program name: ")
    bid_amount = float(input("Bid amount: "))
    notes = input("Notes (optional): ")

    add_bid(program, bid_amount, notes)

if __name__ == "__main__":
    main()