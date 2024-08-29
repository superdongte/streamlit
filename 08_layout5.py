import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import streamlit.components.v1 as components

# 한글 폰트 설정
font_path = 'C:\\Windows\\Fonts\\malgun.ttf'  # 필요한 폰트 파일 경로
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

# 페이지 레이아웃 설정
st.set_page_config(
    page_title="알파시티 대시보드",
    layout="wide",
)

# CSS 스타일 적용을 위한 HTML 템플릿
html_template = """
<!DOCTYPE html>		
<html lang="ko">	
<head>				
    <meta charset="UTF-8"> 
    <title>layout 적용</title> 
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
</head>
<body> 

<div class='header'><h2>알파시티 대시보드</h2></div>
<div class='section'>
    <h3>오늘의 인기아이템</h3>
    {table_html}
</div>
<div class='section'>
    <h3>시계열 분석</h3>
    <div>{timeseries_plot}</div>
</div>
<div class='section'>
    <h3>매출 현황</h3>
    <div>{sales_plot}</div>
</div>
<div class='footer'><h4>대경 ICT 산업협회</h4></div>

</body>
</html>
"""

# 인기 아이템 데이터
data = {
    "순위": [1, 2, 3, 4, 5, 6, 7],
    "아이템명": ["아이템1", "아이템2", "아이템3", "아이템4", "아이템5", "아이템6", "아이템7"],
    "등록폭": ["+2", "-", "-2", "+4", "+1", "-1", "+5"]
}
df = pd.DataFrame(data)

# HTML 테이블 생성
def generate_table(dataframe):
    table_html = """
    <table>
        <thead>
            <tr>
                <th>순위</th>
                <th>아이템명</th>
                <th>등록폭</th>
            </tr>
        </thead>
        <tbody>
    """
    for _, row in dataframe.iterrows():
        table_html += f"""
        <tr>
            <td>{row['순위']}</td>
            <td>{row['아이템명']}</td>
            <td>{row['등록폭']}</td>
        </tr>
        """
    table_html += """
        </tbody>
    </table>
    """
    return table_html

# 인기 아이템 테이블 생성
table_html = generate_table(df)

# 시계열 분석 그래프 생성
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [4, 3, 2, 5], label='아이템1')
ax.plot([1, 2, 3, 4], [3, 4, 1, 2], label='아이템2')
ax.plot([1, 2, 3, 4], [2, 3, 3, 4], label='아이템3')
ax.set_xlabel('기간')
ax.set_ylabel('수치')
ax.set_title('시계열 분석')
ax.legend()
# 그래프를 HTML로 변환
timeseries_plot = st.pyplot(fig, clear_figure=True)

# 매출 현황 파이차트 생성
labels = '1분기', '2분기', '3분기', '4분기'
sizes = [35, 25, 20, 20]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# 파이차트를 HTML로 변환
sales_plot = st.pyplot(fig1, clear_figure=True)

# 전체 HTML 페이지 생성
html_contents = html_template.format(table_html=table_html, timeseries_plot=timeseries_plot, sales_plot=sales_plot)

# HTML 콘텐츠를 Streamlit 앱에 렌더링
components.html(html_contents, height=1200)
