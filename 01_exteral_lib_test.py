import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Streamlit 타이틀
st.title("Matplotlib Chart in Streamlit")

# 데이터 생성
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Matplotlib를 사용하여 차트 생성
fig, ax = plt.subplots()
ax.plot(x, y, label='Sine Wave')
ax.set_title('Sine Wave Chart')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.legend()

# Streamlit에서 차트 표시
st.pyplot(fig)

# 추가 컨텐츠
st.write("This is a simple sine wave chart created using Matplotlib and displayed in Streamlit.")
