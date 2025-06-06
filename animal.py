import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title('동물 생장 시뮬레이터')

initial_size = st.slider('초기 크기를 선택하세요 (단위: cm)', 1, 100, 10)
growth_rate = st.slider('성장 속도를 선택하세요 (단위: cm/년)', 1, 10, 2)
years = st.slider('몇 년 동안 성장할지 선택하세요', 1, 100, 10)

def growth_simulation(initial_size, growth_rate, years):
    time = np.arange(0, years + 1)
    sizes = initial_size + growth_rate * time
    return time, sizes

time, sizes = growth_simulation(initial_size, growth_rate, years)

st.write(f"초기 크기: {initial_size} cm, 성장 속도: {growth_rate} cm/년")
st.line_chart(sizes)

st.write(f"{years}년 후의 크기: {sizes[-1]:.2f} cm")

st.write("""
이 시뮬레이터는 입력한 초기 크기와 성장 속도에 따라 동물의 크기가 시간이 지남에 따라 어떻게 변하는지를 보여줍니다.
자세한 생리학적 모델링이나 다른 변수들은 고려하지 않은 간단한 모델입니다.
""")
