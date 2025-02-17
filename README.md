# Professional Crypto Backtesting Framework 🚀

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Backtests](https://img.shields.io/badge/backtests-passing-brightgreen)](https://github.com/yourusername/crypto-backtesting/actions)

An institutional-grade backtesting system featuring multiple strategies, advanced analytics, and professional risk management for cryptocurrency markets.

## 🌟 Key Features

### Strategy Engine
- Dual SMA crossover system (50/200 periods)
- Multiple timeframe support (1m - 1D)
- Adaptive position sizing algorithms
- Short/long position capabilities

### Risk Management
- Dynamic stop-loss/take-profit levels
- Volatility-adjusted position sizing
- Realistic exchange fee modeling
- Slippage and liquidity simulation

### Analytics Suite
- Comprehensive performance metrics
- Walk-forward optimization
- Monte Carlo simulations
- Interactive HTML reports
- Equity curve analysis

### Quick Start 🚀
Clone repository

```bash
git clone https://github.com/yourusername/crypto-backtesting.git
cd crypto-backtesting
```
Install requirements
```bash
pip install -r requirements.txt
```
## 🧠 Strategy Overview

### Logic Diagram
```mermaid
graph TD
    A[Price Data] --> B{SMA Calculation}
    B --> C[50-period SMA]
    B --> D[200-period SMA]
    C --> E{Crossover Detection}
    D --> E
    E -->|Golden Cross| F[Long Entry]
    E -->|Death Cross| G[Short Entry]
    F --> H[TP/SL Management]
    G --> H
    H --> I[Position Closing]

