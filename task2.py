import csv
from datetime import datetime

# Hardcoded stock prices (in USD)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 145,
    "MSFT": 410
}


def show_available_stocks():
    print("\nAvailable stocks:")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol}: ${price}")


def get_portfolio():
    """Collect stock symbol + quantity pairs from the user."""
    portfolio = {}

    print("\nEnter your stock holdings one at a time.")
    print("Type 'done' as the stock symbol when you're finished.\n")

    while True:
        try:
            symbol = input("Stock symbol (or 'done'): ").strip().upper()
        except EOFError:
            print("\nNo input detected. Stopping entry here.")
            break

        if symbol == "DONE":
            break

        if symbol == "":
            print("Please enter a stock symbol.")
            continue

        if symbol not in STOCK_PRICES:
            print(f"'{symbol}' is not in the price list. Try one of: "
                  + ", ".join(STOCK_PRICES.keys()))
            continue

        try:
            qty_input = input(f"Quantity of {symbol}: ").strip()
        except EOFError:
            print("\nNo input detected. Stopping entry here.")
            break

        if not qty_input.isdigit() or int(qty_input) <= 0:
            print("Please enter a positive whole number for quantity.")
            continue

        quantity = int(qty_input)

        if symbol in portfolio:
            portfolio[symbol] += quantity
        else:
            portfolio[symbol] = quantity

        print(f"Added {quantity} share(s) of {symbol}.\n")

    return portfolio


def calculate_totals(portfolio):
    """Return a list of (symbol, quantity, price, value) rows and the grand total."""
    rows = []
    grand_total = 0

    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        grand_total += value
        rows.append((symbol, quantity, price, value))

    return rows, grand_total


def display_summary(rows, grand_total):
    print("\n" + "=" * 45)
    print("PORTFOLIO SUMMARY")
    print("=" * 45)
    print(f"{'Symbol':<8}{'Qty':<8}{'Price':<10}{'Value':<10}")
    print("-" * 45)

    for symbol, quantity, price, value in rows:
        print(f"{symbol:<8}{quantity:<8}${price:<9}${value:<9}")

    print("-" * 45)
    print(f"TOTAL INVESTMENT: ${grand_total}")
    print("=" * 45)


def save_to_txt(rows, grand_total, filename="portfolio_summary.txt"):
    with open(filename, "w") as f:
        f.write("STOCK PORTFOLIO SUMMARY\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 45 + "\n")
        f.write(f"{'Symbol':<8}{'Qty':<8}{'Price':<10}{'Value':<10}\n")
        f.write("-" * 45 + "\n")
        for symbol, quantity, price, value in rows:
            f.write(f"{symbol:<8}{quantity:<8}${price:<9}${value:<9}\n")
        f.write("-" * 45 + "\n")
        f.write(f"TOTAL INVESTMENT: ${grand_total}\n")
    print(f"Saved summary to {filename}")


def save_to_csv(rows, grand_total, filename="portfolio_summary.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Symbol", "Quantity", "Price", "Value"])
        for symbol, quantity, price, value in rows:
            writer.writerow([symbol, quantity, price, value])
        writer.writerow([])
        writer.writerow(["", "", "TOTAL", grand_total])
    print(f"Saved summary to {filename}")


def main():
    print("=== Stock Portfolio Tracker ===")
    show_available_stocks()

    portfolio = get_portfolio()

    if not portfolio:
        print("\nNo stocks entered. Exiting.")
        return

    rows, grand_total = calculate_totals(portfolio)
    display_summary(rows, grand_total)

    try:
        choice = input("\nSave summary to a file? (txt/csv/no): ").strip().lower()
    except EOFError:
        choice = "no"

    if choice == "txt":
        save_to_txt(rows, grand_total)
    elif choice == "csv":
        save_to_csv(rows, grand_total)
    else:
        print("Summary not saved.")


if __name__ == "__main__":
    main()