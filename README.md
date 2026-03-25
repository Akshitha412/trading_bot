# 📈 Trading Bot (Binance Spot Testnet)

## 🚀 Overview

This project is a **Command-Line Trading Bot** built using Python that interacts with the Binance Spot Testnet API to place cryptocurrency trades.

The bot allows users to execute **BUY and SELL orders** (MARKET and LIMIT) directly from the terminal and displays real-time order execution details.

---

## 🛠️ Features

* ✅ Place MARKET orders (instant execution)
* ✅ Place LIMIT orders (custom price)
* ✅ Buy and Sell support
* ✅ Real-time order response display
* ✅ CLI-based lightweight interface
* ✅ Error handling and validation

---

## 🧰 Tech Stack

* Python
* Click (CLI handling)
* python-binance (API integration)
* dotenv (environment variables)

---

## 📂 Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py          # Handles Binance API connection
│   ├── orders.py          # Order execution logic
│   ├── logging_config.py  # Logging setup
│   └── validators.py      # Input validation
│
├── cli.py                 # Command-line interface
├── requirements.txt       # Dependencies
├── .env                   # API keys (not shared)
```

---

## ⚙️ Setup Instructions

### 1. Clone or Download Project

```bash
git clone https://github.com/YOUR_USERNAME/trading_bot.git
cd trading_bot
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Configure API Keys

Create a `.env` file in the root folder:

```
API_KEY=your_api_key_here
API_SECRET=your_api_secret_here
```

⚠️ Use keys from Binance Spot Testnet only.

---

## ▶️ Usage

### 🔹 MARKET BUY

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

---

### 🔹 MARKET SELL

```bash
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.01
```

---

### 🔹 LIMIT ORDER

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.01 --price 60000
```

---

## 📊 Example Output

```
====== ORDER SUMMARY ======
Symbol     : BTCUSDT
Side       : BUY
Type       : MARKET
Quantity   : 0.01

====== ORDER RESPONSE ======
Order ID     : 123456
Status       : FILLED
Executed Qty : 0.01
Avg Price    : 71636.62

✅ Order placed successfully!
```

---

## 🔐 Notes

* This project uses Binance Spot Testnet (no real money involved)
* Do not share your API keys publicly
* Replace API keys before running

---

## 💡 Future Improvements

* Add balance checking feature
* Implement automated trading strategies
* Convert CLI to web-based dashboard
* Add trade history tracking

---

## 👨‍💻 Author

Akshitha Y

---

## 📌 Conclusion

This project demonstrates API integration, CLI application design, and real-time data handling in a practical trading environment.
