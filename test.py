import streamlit as st

st.markdown("""
    <style>
    * {font-family: "Comic Sans MS", cursive; }
    .stApp {background-color: lightblue;}
    </style>
    """, unsafe_allow_html=True)

st.title("증상별 처방/팁 안내 앱")

symptoms = ["현재 느끼는 증상을 선택하세요", "두통", "복통", "기침", "발열", "근육통", "콧물", "목통증"]
selected = st.selectbox("현재 느끼는 증상을 선택하세요 🩺", symptoms)

if selected == "현재 느끼는 증상을 선택하세요":
    st.stop()

if selected == "두통":
    st.write("🧠 두통")
    st.write("⚠️ 병원 방문 권장" )
    st.write("효과가 있는 약: 아세트아미노펜, 이부프로펜 등")
    st.write("증상 완화 방법: 충분한 수분 섭취, 조용한 곳에서 휴식")
elif selected == "복통":
    st.write("🤢 복통")
    st.write("⚠️ 병원 방문 권장" )
    st.write("효과가 있는 약: 제산제, 소화제")
    st.write("증상 완화 방법: 자극적인 음식 피하기, 따뜻한 물 마시기")
elif selected == "기침":
    st.write("🤧 기침")
    st.write("⚠️ 병원 방문 권장" )
    st.write("효과가 있는 약: 메틸에페드린(판콜에이), 데쿠스트씨럽")
    st.write("증상 완화 방법: 따뜻한 꿀물 마시기, 수분 유지")
elif selected == "발열":
    st.write("🤒 발열")
    st.write("⚠️ 병원 방문 권장" )
    st.write("효과가 있는 약: 타이레놀, 펜잘")
    st.write("증상 완화 방법: 미지근한 물로 몸 닦기, 충분한 수분 섭취")
elif selected == "근육통":
    st.write("💪 근육통")
    st.write("⚠️ 병원 방문 권장" )
    st.write("효과가 있는 약: 아스피린, 이부프로펜(애드빌)")
    st.write("증상 완화 방법: 스트레칭, 온찜질")
elif selected == "콧물":
    st.write("🤧 콧물")
    st.write("⚠️ 병원 방문 권장" )
    st.write("효과가 있는 약: 코대원포르테, 알러지캡슐")
    st.write("증상 완화 방법: 따뜻한 수분 섭취, 실내 습도 유지")
elif selected == "목통증":
    st.write("😷 목통증")
    st.write("⚠️ 병원 방문 권장" )
    st.write("효과가 있는 약: 트라스트 목캔디, 레스콜")
    st.write("증상 완화 방법: 따뜻한 차 마시기, 휴식")
    st.write("효과가 있는 약: 해열제")
    st.write("증상 완화 방법: 미지근한 물로 몸 닦기, 충분한 수분 섭취")
