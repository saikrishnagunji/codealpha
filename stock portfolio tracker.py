import yfinance as yf

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, ticker, shares):
        """Add a stock to the portfolio."""
        if ticker in self.portfolio:
            print(f"{ticker} already exists in the portfolio.")
        else:
            self.portfolio[ticker] = {"shares": shares}
            print(f"Added {ticker}: {shares} shares.")

    def remove_stock(self, ticker):
        """Remove a stock from the portfolio."""
        if ticker in self.portfolio:
            del self.portfolio[ticker]
            print(f"Removed {ticker} from the portfolio.")
        else:
            print(f"{ticker} not found in the portfolio.")

    def fetch_stock_price(self, ticker):
        """Fetch the real-time price of a stock using yfinance."""
        try:
            stock = yf.Ticker(ticker)
            price = stock.history(period="1d")["Close"].i
            return price
        except Exception as e:
            print(f"Error fetching price for {ticker}: {e}")
            return None

    def view_portfolio(self):
        """Display the portfolio summary with real-time stock prices."""
        if not self.portfolio:
            print("Your portfolio is empty.")
            return

        print("\nPortfolio Summary:")
        total_value = 0
        for ticker, details in self.portfolio.items():
            shares = details["shares"]
            price = self.fetch_stock_price(ticker)
            if price is not None:
                value = shares * price
                total_value += value
                print(f"{ticker}: {shares} shares at ${price:.2f} each, Total: ${value:.2f}")
            else:
                print(f"{ticker}: Unable to fetch price.")
        print(f"Total Portfolio Value: ${total_value:.2f}\n")


if __name__ == "__main__":
    portfolio = StockPortfolio()

    while True:
        print("\nOptions:")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            ticker = input("Enter stock ticker: ").upper()
            try:
                shares = int(input("Enter number of shares: "))
                portfolio.add_stock(ticker, shares)
            except ValueError:
                print("Invalid input for shares. Please enter a valid number.")
        elif choice == "2":
            ticker = input("Enter stock ticker: ").upper()
            portfolio.remove_stock(ticker)
        elif choice == "3":
            portfolio.view_portfolio()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
