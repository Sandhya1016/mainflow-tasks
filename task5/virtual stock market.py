import random
class StockMarketSimulator:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.portfolio = {}
    def buy_stock(self, stock, price, shares):
        cost = price * shares
        if cost <= self.balance:
            self.balance -= cost
            if stock in self.portfolio:
                self.portfolio[stock] += shares
            else:
                self.portfolio[stock] = shares
            print(f'Bought {shares} shares of {stock} at ${price:.2f} each.')
        else:
            print('Insufficient balance.')

    def sell_stock(self, stock, price, shares):
        if stock in self.portfolio and self.portfolio[stock] >= shares:
            revenue = price * shares
            self.balance += revenue
            self.portfolio[stock] -= shares
            if self.portfolio[stock] == 0:
                del self.portfolio[stock]
            print(f'Sold {shares} shares of {stock} at ${price:.2f} each.')
        else:
            print('Insufficient shares.')

    def get_portfolio_value(self, stock_prices):
        total_value = self.balance
        for stock, shares in self.portfolio.items():
            if stock in stock_prices:
                total_value += shares * stock_prices[stock]
        return total_value
simulator = StockMarketSimulator(initial_balance=1000)
stock_prices = {
    'AAPL': random.uniform(100, 150),
    'GOOGL': random.uniform(1200, 1300),
    'TSLA': random.uniform(600, 700),
}

simulator.buy_stock('AAPL', stock_prices['AAPL'], 5)
simulator.sell_stock('AAPL', stock_prices['AAPL'], 2)

portfolio_value = simulator.get_portfolio_value(stock_prices)
print(f'Total portfolio value: ${portfolio_value:.2f}')
