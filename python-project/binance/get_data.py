import pandas as pd
import mplfinance as mpf
from binance.client import Client

client = Client(YOUR_API_KEY, YOUR_API_SECRET)

klines = \
client.get_historical_klines("ETHUSDT",
                            Client.KLINE_INTERVAL_30MINUTE,
                            "15 June, 2021",
                            "15 June, 2022")
column_names = ["Open time", "Open", "High",
               "Low", "Close", "Volume", 
                "Close time", "Quote asset volume",
               "Number of trades", "TB base volume",
               "TB quote volume", "Ignore"]
df = pd.DataFrame(klines, dtype=float, columns=column_names)
df["Open time"] = pd.to_datetime(df["Open time"], unit="ms")
df["Close time"] = pd.to_datetime(df["Close time"], unit="ms")

mpf.plot(df.set_index("Close time").tail(100),
        type="candle",
        style="charles",
        volume=True,
        title="ETHUSDT",
        mav=(10,20,30))