import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 한글 폰트 설정
font_path = 'C:\\Windows\\Fonts\\malgun.ttf'  # 필요한 폰트 파일 경로
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

# 페이지 레이아웃 설정
st.set_page_config(
    page_title="알파시티 대시보드",
    layout="wide",
)

# 스타일 적용을 위한 CSS
st.markdown("""
    <style>
        .header, .footer {
            text-align: center; 
            padding: 10px; 
        }
        .header {
            background-color: lightblue; 
        }
        .footer {
            background-color: lightgray;
            position: fixed; 
            bottom: 0; 
            width: 100%;
        }
        .section {
            background-color: #f0f0f0; 
            padding: 20px;
            margin: 10px 0;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: center;
            background-color: #f8f9fa;
        }
        th {
            background-color: #dddddd;
        }
    </style>
""", unsafe_allow_html=True)

# 헤더
st.markdown("<div class='header'><h2>알파시티 대시보드</h2></div>", unsafe_allow_html=True)

# 인기 아이템 데이터
data = {
    "순위": [1, 2, 3, 4, 5, 6, 7],
    "아이템명": ["아이템1", "아이템2", "아이템3", "아이템4", "아이템5", "아이템6", "아이템7"],
    "등록폭": ["+2", "-", "-2", "+4", "+1", "-1", "+5"]
}
df = pd.DataFrame(data)

# 본문 레이아웃
col1, col2, col3 = st.columns([1, 2, 1])

# 왼쪽 사이드바
with col1:
    st.markdown("<div class='section'><h3>오늘의 인기아이템</h3>", unsafe_allow_html=True)
    st.table(df)
    st.markdown("</div>", unsafe_allow_html=True)

# 가운데 컨텐츠
with col2:
    st.markdown("<div class='section'><h3>시계열 분석</h3>", unsafe_allow_html=True)

    # 시계열 분석 그래프
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [4, 3, 2, 5], label='아이템1')
    ax.plot([1, 2, 3, 4], [3, 4, 1, 2], label='아이템2')
    ax.plot([1, 2, 3, 4], [2, 3, 3, 4], label='아이템3')
    ax.set_xlabel('기간')
    ax.set_ylabel('수치')
    ax.set_title('시계열 분석')
    ax.legend()
    st.pyplot(fig)

    st.markdown("</div>", unsafe_allow_html=True)

# 오른쪽 사이드바
with col3:
    st.markdown("<div class='section'><h3>매출 현황</h3>", unsafe_allow_html=True)

    # 매출 현황 파이차트
    labels = '1분기', '2분기', '3분기', '4분기'
    sizes = [35, 25, 20, 20]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)

    st.markdown("</div>", unsafe_allow_html=True)

# 푸터
st.markdown("<div class='footer'><h4>대경 ICT 산업협회</h4></div>", unsafe_allow_html=True)
