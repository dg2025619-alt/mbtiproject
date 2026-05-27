import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="MBTI 동물 갤러리 추천",
    page_icon="📸",
    layout="centered"
)

# 2. MBTI별 고화질 동물 사진 및 데이터
mbti_animal = {
    "INTJ": {
        "name": "부엉이 (Owl)",
        "image": "https://images.unsplash.com/photo-1509248961158-e54f6934749c?w=800",
        "credit": "Photo by Vincent van Zalingen on Unsplash",
        "description": "밤하늘의 고요한 지배자, 부엉이입니다. 혼자만의 시간을 소중히 여기며, 깊이 있고 날카로운 통찰력으로 주변을 분석하는 이성적인 당신과 꼭 닮았습니다.",
        "traits": ["🎯 날카로운 통찰력", "🧠 깊은 분석력", "🛡️ 독립적인 성향"],
        "color": "#2C3E50"
    },
    "INTP": {
        "name": "해달 (Sea Otter)",
        "image": "https://images.unsplash.com/photo-1615813967485-a41dfed6a48a?w=800",
        "credit": "Photo by Kedar Gadge on Unsplash",
        "description": "도구를 사용하고 생각을 멈추지 않는 영리한 해달입니다. 세상에 대한 끝없는 호기심을 가지고 자신만의 방식으로 문제를 창의적으로 해결하는 타입입니다.",
        "traits": ["🔍 무한한 호기심", "💡 창의적 발상", "🧩 논리적 탐구"],
        "color": "#7F8C8D"
    },
    "ENTJ": {
        "name": "사자 (Lion)",
        "image": "https://images.unsplash.com/photo-1614027164847-1b2809eb7b9b?w=800",
        "credit": "Photo by Samuel Scrimshaw on Unsplash",
        "description": "드넓은 초원을 당당하게 이끄는 사자입니다. 타고난 카리스마와 결단력으로 목표를 정하면 무리를 이끌고 거침없이 돌진하는 타고난 리더입니다.",
        "traits": ["👑 타고난 리더십", "🔥 강력한 결단력", "💪 목표 지향성"],
        "color": "#D35400"
    },
    "ENTP": {
        "name": "붉은여우 (Red Fox)",
        "image": "https://images.unsplash.com/photo-1513836279014-a89f7a76ae86?w=800",
        "credit": "Photo by Ray Hennessy on Unsplash",
        "description": "영리하고 눈치 빠른 붉은여우입니다. 늘 흥미진진한 도전을 즐기며, 임기응변이 뛰어나고 상식을 뒤흔드는 기발한 아이디어로 주변을 놀라게 합니다.",
        "traits": ["⚡ 임기응변", "🎨 기발한 아이디어", "🚀 모험과 도전"],
        "color": "#E67E22"
    },
    "INFJ": {
        "name": "회색늑대 (Gray Wolf)",
        "image": "https://images.unsplash.com/photo-1590424753858-3b4d1ec6473f?w=800",
        "credit": "Photo by Thomas Bonometti on Unsplash",
        "description": "무리를 수호하는 고고하고 신비로운 회색늑대입니다. 겉으로는 조용해 보이지만 강한 신념을 품고 있으며, 타인의 아픔을 깊이 헤아리는 공감 능력을 갖췄습니다.",
        "traits": ["👁️ 깊은 공감력", "📜 굳건한 신념", "🌙 신비로운 통찰"],
        "color": "#34495E"
    },
    "INFP": {
        "name": "사슴 (Deer)",
        "image": "https://images.unsplash.com/photo-1507608869274-d3177c8bb4c7?w=800",
        "credit": "Photo by S&B Vonlanthen on Unsplash",
        "description": "깊은 안개 속 숲속의 아름다운 사슴입니다. 순수하고 섬세한 감수성을 지니고 있으며, 마음속에 자신만의 조화롭고 아름다운 이상적인 세계를 꿈꾸는 예술가입니다.",
        "traits": ["🌸 섬세한 감수성", "🌿 평화주의", "✨ 이상주의"],
        "color": "#27AE60"
    },
    "ENFJ": {
        "name": "돌고래 (Dolphin)",
        "image": "https://images.unsplash.com/photo-1570481662006-a3a1374699e8?w=800",
        "credit": "Photo by Ishan @seefromthesky on Unsplash",
        "description": "바다를 누비며 동료들을 보살피는 다정한 돌고래입니다. 타인의 성장을 격려하고 도와주는 것에 보람을 느끼며, 긍정적인 에너지를 널리 퍼뜨리는 따뜻한 교사형입니다.",
        "traits": ["🤝 따뜻한 배려", "☀️ 긍정 에너지", "🌟 공동체 의식"],
        "color": "#2980B9"
    },
    "ENFP": {
        "name": "골든 리트리버 (Golden Retriever)",
        "image": "https://images.unsplash.com/photo-1552053831-71594a27632d?w=800",
        "credit": "Photo by Autri Taheri on Unsplash",
        "description": "보는 사람마저 웃음 짓게 만드는 친근한 리트리버입니다. 새로운 사람들과 소통하는 것을 진심으로 즐기며, 자유롭고 열정적으로 세상을 탐색하는 에너자이저입니다.",
        "traits": ["🎉 엄청난 친화력", "💛 넘치는 에너지", "🐾 자유로운 영혼"],
        "color": "#F1C40F"
    },
    "ISTJ": {
        "name": "바다거북 (Sea Turtle)",
        "image": "https://images.unsplash.com/photo-1559583985-c80d8ad9b29f?w=800",
        "credit": "Photo by Randall Ruiz on Unsplash",
        "description": "수천 킬로미터의 바다를 묵묵히 헤엄쳐 가는 신중한 바다거북입니다. 맡은 바 책임을 다하며, 약속을 반드시 지키는 성실하고 신뢰감 주는 사회의 소금 같은 존재입니다.",
        "traits": ["🛡️ 한결같은 성실성", "📋 신중한 계획", "💎 깊은 책임감"],
        "color": "#16A085"
    },
    "ISFJ": {
        "name": "토끼 (Rabbit)",
        "image": "https://images.unsplash.com/photo-1585110396000-c9ffd4e4b308?w=800",
        "credit": "Photo by Gary Bendig on Unsplash",
        "description": "숲 풀밭 위의 다정하고 따뜻한 토끼입니다. 조용하지만 주위 사람들의 세밀한 요구를 눈치채고 세심하게 보살펴주며, 가정적이고 헌신적인 수호자 타입입니다.",
        "traits": ["💗 세심한 배려", "🏡 헌신적인 수호", "🕊️ 온화한 태도"],
        "color": "#E84393"
    },
    "ESTJ": {
        "name": "시베리아 호랑이 (Tiger)",
        "image": "https://images.unsplash.com/photo-1504470695779-75300268aa0e?w=800",
        "credit": "Photo by Waldemar Brandt on Unsplash",
        "description": "질서와 법칙을 준수하는 엄격하고 강인한 호랑이입니다. 체계적이고 조직적인 환경을 선호하며, 약속과 기한을 엄격히 지키며 일을 효율적으로 완수하는 해결사입니다.",
        "traits": ["⚔️ 확실한 실행력", "👔 조직 관리", "🎯 체계적인 설계"],
        "color": "#D35400"
    },
    "ESFJ": {
        "name": "꿀벌 (Honeybee)",
        "image": "https://images.unsplash.com/photo-1473081556163-2a17de81fc97?w=800",
        "credit": "Photo by Boris Smokrovic on Unsplash",
        "description": "서로 소통하며 완벽한 사회를 이뤄가는 부지런한 꿀벌입니다. 주변 사람들의 감정에 매우 민감하고, 모임의 분위기를 화기애애하게 돋우는 사교적인 매력의 소유자입니다.",
        "traits": ["🍯 높은 친화력", "🤝 협동과 헌신", "🌟 세심한 눈썰미"],
        "color": "#F39C12"
    },
    "ISTP": {
        "name": "고양이 (Cat)",
        "image": "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=800",
        "credit": "Photo by Paul Hanaoka on Unsplash",
        "description": "자유롭고 시크한 매력의 고양이입니다. 조용히 관찰하는 것을 즐기며 상황 판단이 매우 빠르고 유연합니다. 도구를 다루거나 실용적인 일을 뚝딱 해내는 재주꾼입니다.",
        "traits": ["😎 쿨한 독립심", "🔧 뛰어난 현실 적응력", "🧭 조용한 관찰력"],
        "color": "#7F8C8D"
    },
    "ISFP": {
        "name": "코알라 (Koala)",
        "image": "https://images.unsplash.com/photo-1525382455947-f319bc05fb35?w=800",
        "credit": "Photo by David Clode on Unsplash",
        "description": "유칼립투스 나무 위에서 평화롭게 쉬는 온화한 코알라입니다. 다른 사람의 의견을 잘 수용하며 갈등을 싫어합니다. 삶의 여유와 예술적 감성을 즐길 줄 압니다.",
        "traits": ["🎨 뛰어난 예술 감성", "🌿 평화롭고 유연함", "🏡 다정한 따뜻함"],
        "color": "#95A5A6"
    },
    "ESTP": {
        "name": "치타 (Cheetah)",
        "image": "https://images.unsplash.com/photo-1602491453979-04da9d486245?w=800",
        "credit": "Photo by Gerhard Crous on Unsplash",
        "description": "눈앞의 순간을 가장 역동적으로 즐기는 날렵한 치타입니다. 복잡한 이론보다는 직접 몸으로 부딪치며 즉각적인 문제를 효율적으로 해결하는 뛰어난 행동가입니다.",
        "traits": ["⚡ 신속한 판단력", "🔥 거침없는 행동력", "🎯 위기 극복 능력"],
        "color": "#E67E22"
    },
    "ESFP": {
        "name": "앵무새 (Parrot)",
        "image": "https://images.unsplash.com/photo-1552728089-57bdde30beb3?w=800",
        "credit": "Photo by Sharad Bhat on Unsplash",
        "description": "화려한 깃털을 뽐내며 숲을 밝히는 유쾌한 앵무새입니다. 늘 긍정적이고 유머러스하여 주변 사람들을 유쾌하게 만들며, 스포트라이트를 즐길 줄 아는 축제형 인물입니다.",
        "traits": ["🌈 밝고 유머러스함", "🎤 타고난 스타성", "🎈 끊임없는 낙천성"],
        "color": "#E74C3C"
    }
}

# 3. 웹앱 상단 레이아웃
st.markdown("<h1 style='text-align: center; color: #2C3E50;'>📸 MBTI 와일드 포토 갤러리</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #7F8C8D;'>당신의 MBTI 성향과 가장 조화를 이루는 야생동물 사진을 매칭해 드립니다.</p>", unsafe_allow_html=True)
st.markdown("---")

st.markdown("### 🧬 성향 테스트")
st.write("본인의 MBTI 지표를 차례대로 선택해 주세요.")

# 4. 성향 지표 선택 영역
col1, col2 = st.columns(2)
with col1:
    ei = st.radio("🌿 **에너지 방향성 (E / I)**", ["E (외향형) - 외부와의 교류", "I (내향형) - 내부 성찰과 조용함"])
    sn = st.radio("👁️ **정보 인식 방식 (S / N)**", ["S (감각지각) - 실제 경험과 사실", "N (직관지각) - 가능성과 의미 탐색"])
with col2:
    tf = st.radio("⚖️ **판단 및 의사결정 (T / F)**", ["T (사고형) - 논리적 인과 분석", "F (감정형) - 인간관계와 가치 판단"])
    jp = st.radio("📅 **생활 패턴 양식 (J / P)**", ["J (판단형) - 체계와 철저한 계획", "P (인식형) - 자율성과 즉흥적인 대처"])

mbti_result = ei[0] + sn[0] + tf[0] + jp[0]

st.markdown("---")
st.markdown(f"<h3 style='text-align: center;'>선택하신 MBTI: <strong style='color: #2980B9;'>{mbti_result}</strong></h3>", unsafe_allow_html=True)

# 5. 결과 확인 버튼
if st.button("🖼️ 매칭 동물 사진 불러오기", use_container_width=True):
    data = mbti_animal[mbti_result]
    
    st.balloons()
    
    st.markdown("### 🔍 분석 결과")
    st.image(data['image'], caption=data['credit'], use_container_width=True)
    st.markdown(f"<h2 style='color: {data['color']};'>{data['name']}</h2>", unsafe_allow_html=True)
    st.info(data['description'])
    
    st.markdown("#### ✨ 핵심 공통 성향")
    cols = st.columns(3)
    for i, trait in enumerate(data['traits']):
        with cols[i]:
            st.markdown(f"""
            <div style="background-color: #F8F9FA; border-left: 4px solid {data['color']}; padding: 10px; border-radius: 4px; text-align: center;">
                <p style="margin: 0; font-weight: bold; font-size: 14px; color: #333;">{trait}</p>
            </div>
            """, unsafe_allow_html=True)
            
    with st.expander("🖼️ 추가 분석: 이 동물과의 연결 고리"):
        st.write(f"- **대표 테마 컬러**: `<span style='color:{data['color']}; font-weight:bold;'>{data['color']}</span>`", unsafe_allow_html=True)
        st.write("- **관찰 시 추천 음악**: 클래식 또는 자연의 소리 🎧")
        st.write(f"- **매칭 의미**: {data['name']}의 야생 생존 방식과 당신의 사회적 적응 메커니즘은 매우 긴밀하게 닮아 있습니다.")

st.markdown("---")
st.markdown("<p style='text-align: center; color: #BDC3C7; font-size: 12px;'>© 2026 DangGok High School Python Projects | 📸 Images powered by Unsplash License</p>", unsafe_allow_html=True)
