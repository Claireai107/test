import streamlit as st
import pandas as pd


import os
print("현재 위치:", os.getcwd())


st.title("심부전 분석")
st.write("👈메뉴를 선택하세요")



import streamlit as st, pandas as pd
st.title("📊데이터")

df = pd.read_csv("heart_failure.csv")
st.dataframe(df)






# st.title("건강 데이터 탐험기")
# st.write("이 앱은")


# name = st.text_input("이름을 입력하세요")

# if name:
#     st.write(f"반갑습니다/{name}님! 함께 시작해요.")
# else:
#     st.info("위에 이름을 입력하면 인사를 드릴게요.")
    
    
    
df = pd.read_csv("heart_failure.csv")
st.subheader("환자 데이터")
st.dataframe(df.head())

st.metric(
    label="전체 환자 수",
    value=f"{len(df)}명",
    delta="299건 수집")



st.dataframe(df.head(10))
avg = df['age'].mean()
st.metric("평균 나이 ", f"{avg:.1f}세")





age_max = st.slider(
    "최대 나이 ", 40, 95,70)

filtered = df[df['age'] <= age_max]
st.write(f"{len(filtered)}명이 조건에 맞아요")
st.dataframe(filtered)





choice = st.selectbox(
    "성별 ", ["남성", "여성"])
    
code = 1 if choice == "남성 " else 0
result = df[df['sex'] == 1]
st.write(f"{len(result)}명")

st.dataframe(result)







import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots()
ax.hist(df['age'], bins=20,
        color='#5BAFB8')
ax.set_xlabel("나이")
ax.set_ylabel("환자 수")

st.pyplot(fig)






counts = df['DEATH_EVENT'].value_counts().sort_index()


fig, ax = plt.subplots()
ax.bar(['생존', '사망'], counts, color=['#02C39A', '#E63946'])


ax.set_title("생존 vs 사망 환자 수")
ax.set_ylabel("환자 수")


st.pyplot(fig)







# st.sidebar.header("필터")
# age = st.sidebar.slider("최대 나이",
#                         40, 95, 70)
# df = df[df['age'] <= age]




# c1, c2 = st.columns(2)
# c1.metric("환자 수 ", len(df))
# c2.metric("평균 나이 ", f"{df.age.mean():.0f}")






# # 사이드바 슬라이더
# age = st.sidebar.slider("최대 나이", 40, 95, 95)

# # 필터링
# df = df[df['age'] <= age]

# # 탭 생성
# tab1, tab2 = st.tabs(["표 보기", "차트 보기"])


# with tab1:
#     st.dataframe(df)


# with tab2:
#     fig, ax = plt.subplots()
#     ax.hist(df['age'], bins=20, color='#5BAFB8')
#     ax.set_title("나이 분포")
#     ax.set_xlabel("나이")
#     ax.set_ylabel("인원 수")
#     st.pyplot(fig)
    
    
    
    