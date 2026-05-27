import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="MBTI 동물 추천기",
    page_icon="🐾",
    layout="centered"
)

# MBTI별 동물 데이터
mbti_animal = {
    "INTJ": {
        "name": "부엉이",
        "emoji": "🦉",
        "image": "https://images.unsplash.com/photo-1543549790-8b5f4a028cfb?w=600",
        "description": "지혜롭고 통찰력 있는 당신! 밤하늘의 현자, 부엉이처럼 깊이 있는 사고를 가진 전략가예요.",
        "traits": ["🧠 지혜로움", "🌙 통찰력", "🎯 전략가"],
        "color": "#4A4E69"
    },
    "INTP": {
        "name": "수달",
        "emoji": "🦦",
        "image": "https://images.unsplash.com/photo-1606937295547-bc0f668595c0?w=600",
        "description": "호기심 가득한 탐구자! 끊임없이 도구를 다루며 실험하는 영리한 수달과 닮았어요.",
        "traits": ["🔍 호기심", "💡 창의력", "🧩 분석력"],
        "color": "#8B7355"
    },
    "ENTJ": {
        "name": "사자",
        "emoji": "🦁",
        "image": "https://images.unsplash.com/photo-1546182990-dffeafbe841d?w=600",
        "description": "타고난 리더! 정글의 왕 사자처럼 카리스마 넘치고 무리를 이끄는 당신!",
        "traits": ["👑 리더십", "🔥 카리스마", "💪 추진력"],
        "color": "#D4A574"
    },
    "ENTP": {
        "name": "여우",
        "emoji": "🦊",
        "image": "https://images.unsplash.com/photo-1474511320723-9a56873867b5?w=600",
        "description": "재치 넘치는 아이디어 뱅크! 영리하고 재빠른 여우처럼 톡톡 튀는 매력의 소유자!",
        "traits": ["🎭 재치", "💡 아이디어", "🚀 도전정신"],
        "color": "#E07856"
    },
    "INFJ": {
        "name": "늑대",
        "emoji": "🐺",
        "image": "https://images.unsplash.com/photo-1564349683136-77e08dba1ef7?w=600",
        "description": "신비롭고 깊은 영혼! 무리를 소중히 여기며 강한 직관을 가진 늑대와 닮았어요.",
        "traits": ["🌙 직관력", "💙 신비로움", "🛡️ 충성심"],
        "color": "#6B7280"
    },
    "INFP": {
        "name": "사슴",
        "emoji": "🦌",
        "image": "https://images.unsplash.com/photo-1484406566174-9da000fda645?w=600",
        "description": "순수하고 감성 충만한 당신! 숲속의 우아한 사슴처럼 따뜻하고 꿈이 많아요.",
        "traits": ["🌸 순수함", "💖 감성적", "✨ 이상주의"],
        "color": "#C9A87C"
    },
    "ENFJ": {
        "name": "돌고래",
        "emoji": "🐬",
        "image": "https://images.unsplash.com/photo-1607153333879-c174d265f1d2?w=600",
        "description": "사람들을 행복하게 하는 마법사! 친절하고 사교적인 돌고래처럼 모두의 친구!",
        "traits": ["💕 다정함", "🌟 카리스마", "🤝 공감능력"],
        "color": "#5BA3D0"
    },
    "ENFP": {
        "name": "강아지",
        "emoji": "🐶",
        "image": "https://images.unsplash.com/photo-1543466835-00a7907e9de1?w=600",
        "description": "에너지 폭발! 모두를 사랑하고 사랑받는 강아지처럼 밝고 사랑스러운 당신!",
        "traits": ["☀️ 활발함", "💛 긍정적", "🎉 사교적"],
        "color": "#F4B860"
    },
    "ISTJ": {
        "name": "거북이",
        "emoji": "🐢",
        "image": "https://images.unsplash.com/photo-1437622368342-7a3d73a34c8f?w=600",
        "description": "믿음직한 든든이! 천천히 그러나 확실하게 나아가는 거북이처럼 성실한 당신!",
        "traits": ["🛡️ 신중함", "📋 책임감", "💎 성실함"],
        "color": "#6B8E5A"
    },
    "ISFJ": {
        "name": "토끼",
        "emoji": "🐰",
        "image": "https://images.unsplash.com/photo-1535241749838-299277b6305f?w=600",
        "description": "따뜻하고 다정한 보호자! 가족과 친구를 소중히 여기는 사랑스러운 토끼와 닮았어요.",
        "traits": ["🌸 헌신적", "💗 배려심", "🕊️ 온화함"],
        "color": "#F5C5C5"
    },
    "ESTJ": {
        "name": "호랑이",
        "emoji": "🐯",
        "image": "https://images.unsplash.com/photo-1561731216-c3a4d99437d5?w=600",
        "description": "강인한 통솔자! 위풍당당한 호랑이처럼 목표를 향해 거침없이 나아가는 리더!",
        "traits": ["⚔️ 결단력", "🎯 추진력", "👔 통솔력"],
        "color": "#E89B4F"
    },
    "ESFJ": {
        "name": "꿀벌",
        "emoji": "🐝",
        "image": "https://images.unsplash.com/photo-1568526381923-caf3fd520382?w=600",
        "description": "공동체의 활력소! 부지런하고 협동심 강한 꿀벌처럼 모두를 챙기는 인기쟁이!",
        "traits": ["🍯 사교적", "💕 협동심", "🌟 인기쟁이"],
        "color": "#F4C430"
    },
    "ISTP": {
        "name": "고양이",
        "emoji": "🐱",
        "image": "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=600",
        "description": "쿨하고 독립적인 매력! 자유로운 영혼의 고양이처럼 신비롭고 손재주 좋은 당신!",
        "traits": ["🌙 독립적", "🔧 손재주", "😎 시크함"],
        "color": "#8B7BA8"
    },
    "ISFP": {
        "name": "판다",
        "emoji": "🐼",
        "image": "https://images.unsplash.com/photo-1566826377583-5b909bf4ed72?w=600",
        "description": "조용하지만 매력 폭발! 평화롭고 예술적인 감성을 지닌 사랑스러운 판다와 닮았어요.",
        "traits": ["🎨 예술적", "💫 감성적", "🌿 평화로움"],
        "color": "#A8A8A8"
    },
    "ESTP": {
        "name": "치타",
        "emoji": "🐆",
        "image": "https://images.unsplash.com/photo-1551972873-b7e8754e8e26?w=600",
        "description": "스릴을 즐기는 모험가! 빠르고 역동적인 치타처럼 짜릿한 순간을 사랑하는 당신!",
        "traits": ["⚡ 행동력", "🔥 모험심", "💪 자신감"],
        "color": "#D4943E"
    },
    "ESFP": {
        "name": "앵무새",
        "emoji": "🦜",
        "image": "https://images.unsplash.com/photo-1552728089-57bdde30beb3?w=600",
        "description": "분위기 메이커! 화려하고 흥 많은 앵무새처럼 어디서나 빛나는 인싸 매력의 소유자!",
        "traits": ["🎉 활발함", "🌈 화려함", "🎤 자유로움"],
        "color": "#FF6B6B"
    }
}

# 타이틀
st.markdown("<h1 style='text-align: center;'>🐾 MBTI 동물 추천기 🌟</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>당신의 MBTI에 어울리는 동물 친구를 찾아드려요! 🔍✨</h4>", unsafe_allow_html=True)
st.markdown("---")

# 소개 문구
st.markdown("""
### 🌈 사용 방법
1️⃣ 아래에서 당신의 **MBTI**를 선택해주세요! 🎯  
2️⃣ **추천 받기** 버튼을 눌러보세요! 🚀  
3️⃣ 당신과 꼭 닮은 동물 친구를 만나보세요! 💖
""")

st.markdown("---")

# MBTI 선택
st.markdown("### 🎨 당신의 MBTI를 알려주세요!")

col1, col2 = st.columns(2)
with col1:
    ei = st.radio("🌟 **에너지 방향**", ["E (외향) 🎉", "I (내향) 🌙"])
    sn = st.radio("🔍 **인식 기능**", ["S (감각) 🌳", "N (직관) ✨"])
with col2:
    tf = st.radio("💭 **판단 기능**", ["T (사고) 🧠", "F (감정) 💖"])
    jp = st.radio("📅 **생활 양식**", ["J (계획) 📋", "P (즉흥) 🎲"])

# MBTI 조합
mbti = ei[0] + sn[0] + tf[0] + jp[0]

st.markdown("---")
st.markdown(f"<h3 style='text-align: center;'>당신의 MBTI: <span style='color: #FF6B6B;'>✨ {mbti} ✨</span></h3>", unsafe_allow_html=True)

# 추천 버튼
if st.button("🎁 내 동물 친구 만나러 가기! 🎁", use_container_width=True):
    animal = mbti_animal[mbti]
    
    st.balloons()
    
    st.markdown("---")
    st.markdown(f"<h2 style='text-align: center;'>🥁 두구두구두구... 🎊</h2>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align: center; color: {animal['color']};'>{animal['emoji']} {animal['name']} {animal['emoji']}</h1>", unsafe_allow_html=True)
    
    # 동물 이미지
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.image(animal['image'], use_container_width=True)
    
    # 설명
    st.markdown(f"### 💬 {animal['name']}는 이런 친구예요!")
    st.info(animal['description'])
    
    # 특징
    st.markdown("### ✨ 당신과 닮은 특징")
    cols = st.columns(3)
    for i, trait in enumerate(animal['traits']):
        with cols[i]:
            st.success(trait)
    
    # 응원 메시지
    st.markdown("---")
    st.markdown(f"<h4 style='text-align: center;'>🌈 {animal['emoji']} {animal['name']}같은 당신, 오늘도 빛나세요! ✨</h4>", unsafe_allow_html=True)
    
    # 재미 요소
    with st.expander("🎁 보너스! 우리의 케미는?"):
        st.markdown(f"""
        - 🍀 **행운의 색**: {animal['color']}  
        - 💝 **나의 매력 포인트**: {animal['traits'][0]}  
        - 🌟 **오늘의 한마디**: "{animal['name']}처럼 자연스러운 당신이 가장 멋져요!" 
        """)

# 푸터
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Made with 💖 by 당곡고 | 🐾 모든 동물 친구들과 함께해요!</p>", unsafe_allow_html=True)
