import csv
from datetime import datetime
from pathlib import Path

CSV_FILE = Path("portfolio_summary.csv")


def get_positive_number(message):
    while True:
        try:
            number = float(input(message))
            if number > 0:
                return number
            print("Enter a number greater than zero.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    print("\n=== Stock Portfolio Performance Tracker ===")
    print("Enter stock prices manually for this version.\n")

    stocks = []

    while True:
        ticker = input("Stock ticker (e.g., AAPL): ").strip().upper()

        if not ticker:
            print("Ticker cannot be empty.")
            continue

        buy_price = get_positive_number("Purchase price per share: ")
        quantity = get_positive_number("Number of shares: ")
        current_price = get_positive_number("Current price per share: ")

        invested = buy_price * quantity
        current_value = current_price * quantity
        profit_loss = current_value - invested
        profit_percent = profit_loss / invested * 100

        stocks.append({
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "ticker": ticker,
            "buy_price": buy_price,
            "quantity": quantity,
            "current_price": current_price,
            "invested": round(invested, 2),
            "current_value": round(current_value, 2),
            "profit_loss": round(profit_loss, 2),
            "profit_percent": round(profit_percent, 2)
        })

        again = input("Add another stock? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            break

    print("\n========== PORTFOLIO REPORT ==========")
    total_invested = sum(s["invested"] for s in stocks)
    total_value = sum(s["current_value"] for s in stocks)

    for stock in stocks:
        print(
            f'{stock["ticker"]}: '
            f'Invested={stock["invested"]:.2f}, '
            f'Current Value={stock["current_value"]:.2f}, '
            f'Profit/Loss={stock["profit_loss"]:.2f} '
            f'({stock["profit_percent"]:.2f}%)'
        )

    total_profit = total_value - total_invested
    total_percent = total_profit / total_invested * 100

    print("--------------------------------------")
    print(f"Total Investment: {total_invested:.2f}")
    print(f"Current Value:    {total_value:.2f}")
    print(f"Total Profit/Loss: {total_profit:.2f}")
    print(f"Overall Return:    {total_percent:.2f}%")

    columns = [
        "date", "ticker", "buy_price", "quantity", "current_price",
        "invested", "current_value", "profit_loss", "profit_percent"
    ]

    file_exists = CSV_FILE.exists() and CSV_FILE.stat().st_size > 0

    with CSV_FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        if not file_exists:
            writer.writeheader()
        writer.writerows(stocks)

    print(f"\nReport saved to: {CSV_FILE.resolve()}")


if __name__ == "__main__":
    main()
