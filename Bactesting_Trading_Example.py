import pandas as pd
from time import sleep
import ta
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA, GOOG
from helper import get_tickers_usdt, klines, klines_extended

# Strategy parameters
tp = 0.04  # 4% take profit
sl = 0.02  # 2% stop loss
sma_short = 50
sma_long = 200

# Timeframe and interval
timeframe = '1h'
interval = 90  # days

def sma(df, period):
    return ta.trend.SMAIndicator(pd.Series(df), window=period).sma_indicator()

class SMACrossover(Strategy):
    # Optimizable parameters
    short_period = sma_short
    long_period = sma_long
    
    def init(self):
        # Calculate indicators
        close = self.data.Close
        self.sma_short = self.I(sma, close, self.short_period)
        self.sma_long = self.I(sma, close, self.long_period)

    def next(self):
        price = self.data.Close[-1]
        
        # Bullish crossover
        if crossover(self.sma_short, self.sma_long):
            if not self.position:
                self.buy(size=0.05,  # 5% of equity
                         tp=price * (1 + tp),
                         sl=price * (1 - sl))
        
        # Bearish crossover
        elif crossover(self.sma_long, self.sma_short):
            if self.position:
                self.position.close()

# Example usage
symbol = 'BTCUSDT'
kl = klines_extended(symbol, timeframe, interval)

bt = Backtest(kl, SMACrossover, 
             cash=1000, 
             margin=1/10, 
             commission=0.00075)

stats = bt.run()
print(stats)
bt.plot()