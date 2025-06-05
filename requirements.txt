folium
streamlit.folium
import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime, timedelta

# 1. 글로벌 시가총액 상위 10개 기업 티커
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

st.set_page_config(layout="wide")
st.title("🌎 글로벌 시가총액 Top 10 기업 - 최근 1년 주가 변화")

# 2. 기간 설정 (최근 1년)
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

# 3. 데이터 수집
@st.cache_data
def fetch_data(tickers):
    data = {}
    for name, ticker in tickers.items():
        df = yf.download(ticker, start=start_date, end=end_date)
        df['Company'] = name
        data[name] = df
    return data

stock_data = fetch_data(top10_tickers)

# 4. Plotly 그래프 생성
fig = go.Figure()

for name, df in stock_data.items():
    fig.add_trace(go.Scatter(
        x=df.index,
        y=df['Adj Close'],
        mode='lines',
        name=name
    ))

fig.update_layout(
    title="📈 최근 1년간 글로벌 시가총액 Top 10 기업의 주가 변화",
    xaxis_title="날짜",
    yaxis_title="주가 (USD)",
    template="plotly_white",
    hovermode="x unified"
)

st.plotly_chart(fig, use_container_width=True)
