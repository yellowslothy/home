import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime, timedelta

st.set_page_config(layout="wide")
st.title("🌍 글로벌 시가총액 Top 10 기업 - 최근 1년 주가 변화")

top10_tickers = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "NVIDIA": "NVDA",
    "Alphabet (Google)": "GOOGL",
    "Amazon": "AMZN",
    "Meta (Facebook)": "META",
    "Berkshire Hathaway": "BRK-B",
    "Eli Lilly": "LLY",
    "TSMC": "TSM",
    "Tesla": "TSLA"
}

end_date = datetime.today()
start_date = end_date - timedelta(days=365)

@st.cache_data
def load_data():
    data = {}
    for name, ticker in top10_tickers.items():
        df = yf.download(ticker, start=start_date, end=end_date)
        df['Company'] = name
        data[name] = df
    return data

stock_data = load_data()

fig = go.Figure()

for name, df in stock_data.items():
    fig.add_trace(go.Scatter(
        x=df.index,
        y=df['Adj Close'],
        mode='lines',
        name=name
    ))

fig.update_layout(
    title="📈 글로벌 시가총액 Top 10 기업의 최근 1년 주가 변화",
    xaxis_title="날짜",
    yaxis_title="조정 종가 (USD)",
    template="plotly_white",
    hovermode="x unified",
    legend=dict(orientation="h", y=-0.2)
)

st.plotly_chart(fig, use_container_width=True)
