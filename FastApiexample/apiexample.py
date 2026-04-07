import requests
import yfinance as yf
# def get_weather(city: str) -> dict:
#     try:
#         res = requests.get(f"https://wttr.in/{city}?format=j1", timeout=10)
#         data = res.json()
#         current = data["current_condition"][0]
#         return {
#             "city": city,
#             "temperature_C": int(current["temp_C"]),
#             "humidity": int(current["humidity"]),
#             "weather_desc": current["weatherDesc"][0]["value"],
#         }
#     except Exception as e:
#         return {"error": str(e)}
#
# o =get_weather("delhi")
# print(o)

def get_stock_price(symbol: str) -> dict:
    try:
        ticker = yf.Ticker(symbol)
        data = ticker.history(period="1d")
        if data.empty:
            return {"error": f"No data found for {symbol}"}
        latest = round(float(data["Close"].iloc[-1]), 2)
        return {"symbol": symbol.upper(), "latest_close": latest}
    except Exception as e:
        return {"error": str(e)}

a = get_stock_price("AAPL")
print(a)