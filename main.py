import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="MBTI 포켓몬 추천기",
    page_icon="⚡",
    layout="centered"
)

# MBTI별 포켓몬 데이터
mbti_pokemon = {
    "INTJ": {
        "name": "뮤츠",
        "emoji": "🧠🔮",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png",
        "description": "전략적이고 지적인 당신! 강력한 사이코 능력으로 모든 것을 계획하고 실행하는 천재형 포켓몬이에요.",
        "traits": ["🎯 전략가", "🔮 지적임", "💎 카리스마"]
    },
    "INTP": {
        "name": "후딘",
        "emoji": "🧙‍♂️📚",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/65.png",
        "description": "호기심 많고 분석적인 당신! IQ 5000의 후딘처럼 끊임없이 생각하고 탐구하는 타입이에요.",
        "traits": ["🤔 분석적", "📖 학구적", "✨ 창의적"]
    },
    "ENTJ": {
        "name": "리자몽",
        "emoji": "🔥👑",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png",
        "description": "타고난 리더! 불꽃처럼 강렬한 카리스마로 사람들을 이끄는 당신에게 딱이에요!",
        "traits": ["👑 리더십", "🔥 열정적", "💪 강인함"]
    },
    "ENTP": {
        "name": "겟핸보숭",
        "emoji": "🐵💡",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/424.png",
        "description": "재치있고 아이디어가 넘치는 당신! 장난기 가득하고 영리한 겟핸보숭이 찰떡!",
        "traits": ["💡 창의력", "🎭 재치", "🚀 도전정신"]
    },
    "INFJ": {
        "name": "루카리오",
        "emoji": "🥋✨",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/448.png",
        "description": "직관력이 뛰어난 당신! 파동을 읽어내는 루카리오처럼 사람의 마음을 잘 헤아려요.",
        "traits": ["🔮 직관력", "💙 공감능력", "⚔️ 정의감"]
    },
    "INFP": {
        "name": "이브이",
        "emoji": "🌸💕",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png",
        "description": "다양한 가능성을 가진 당신! 무한한 진화 가능성을 품은 이브이처럼 순수하고 따뜻해요.",
        "traits": ["🌈 가능성", "💖 따뜻함", "🎨 감성적"]
    },
    "ENFJ": {
        "name": "님피아",
        "emoji": "🎀💝",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/700.png",
        "description": "사람들을 사랑으로 이끄는 당신! 리본으로 마음을 연결하는 님피아가 딱이에요!",
        "traits": ["💕 다정함", "🌟 카리스마", "🤝 친화력"]
    },
    "ENFP": {
        "name": "피카츄",
        "emoji": "⚡💛",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png",
        "description": "에너지 넘치는 당신! 모두에게 사랑받는 피카츄처럼 밝고 긍정적인 매력의 소유자!",
        "traits": ["⚡ 활발함", "😊 긍정적", "🎉 사교적"]
    },
    "ISTJ": {
        "name": "거북왕",
        "emoji": "🐢🛡️",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/9.png",
        "description": "신뢰감 가는 당신! 든든하고 책임감 강한 거북왕처럼 믿음직스러운 타입이에요.",
        "traits": ["🛡️ 신중함", "📋 책임감", "💎 성실함"]
    },
    "ISFJ": {
        "name": "이상해꽃",
        "emoji": "🌺🌿",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/3.png",
        "description": "따뜻하게 보살피는 당신! 등에 핀 꽃으로 주변을 평화롭게 만드는 이상해꽃이 어울려요.",
        "traits": ["🌸 헌신적", "💚 배려심", "🕊️ 평화로움"]
    },
    "ESTJ": {
        "name": "한카리아스",
        "emoji": "🦈⚔️",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/445.png",
        "description": "강력한 추진력의 당신! 목표를 향해 돌진하는 한카리아스처럼 결단력 있는 리더!",
        "traits": ["⚔️ 결단력", "🎯 추진력", "👔 리더십"]
    },
    "ESFJ": {
        "name": "푸린",
        "emoji": "🎤💗",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/39.png",
        "description": "사람들을 즐겁게 하는 당신! 노래로 모두를 행복하게 하는 푸린처럼 사랑스러워요!",
        "traits": ["🎵 사교적", "💕 다정함", "🌟 인기쟁이"]
    },
    "ISTP": {
        "name": "갸라도스",
        "emoji": "🐉🌊",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/130.png",
        "description": "쿨하고 독립적인 당신! 평소엔 조용하지만 한번 움직이면 강력한 갸라도스 스타일!",
        "traits": ["🌊 독립적", "⚡ 카리스마", "🔧 실용적"]
    },
    "ISFP": {
        "name": "이브이(샤미드)",
        "emoji": "💧🎨",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/134.png",
        "description": "감성 충만한 예술가! 우아하고 신비로운 샤미드처럼 섬세한 매력의 소유자예요.",
        "traits": ["🎨 예술적", "💫 감성적", "🌙 신비로움"]
    },
    "ESTP": {
        "name": "루가루암",
        "emoji": "🐺🌙",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/745.png",
        "description": "행동파인 당신! 본능적이고 모험을 즐기는 루가루암처럼 거침없는 매력!",
        "traits": ["🔥 모험심", "⚡ 행동력", "💪 자신감"]
    },
    "ESFP": {
        "name": "마릴",
        "emoji": "💙🎈",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/183.png",
        "description": "분위기 메이커! 통통 튀는 마릴처럼 어디서나 사랑받는 귀여운 매력의 소유자!",
        "traits": ["🎉 활발함", "💖 매력적", "🎈 자유로움"]
    }
}

# 타이틀
st.markdown("<h1 style='text-align: center;'>⚡ MBTI 포켓몬 추천기 🎮</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>당신의 MBTI에 어울리는 포켓몬을 찾아드려요! 🔍✨</h4>", unsafe_allow_html=True)
st.markdown("---")

# 소개 문구
st.markdown("""
### 🌟 사용 방법
1️⃣ 아래에서 당신의 **MBTI**를 선택하세요! 🎯  
2️⃣ **추천 받기** 버튼을 눌러보세요! 🚀  
3️⃣ 당신에게 딱 맞는 포켓몬을 만나보세요! 💖
""")

st.markdown("---")

# MBTI 선택
col1, col2 = st.columns(2)
with col1:
    ei = st.radio("🌟 **E vs I**", ["E (외향) 🎉", "I (내향) 🌙"])
    sn = st.radio("🔍 **S vs N**", ["S (감각) 🌳", "N (직관) ✨"])
with col2:
    tf = st.radio("💭 **T vs F**", ["T (사고) 🧠", "F (감정) 💖"])
    jp = st.radio("📅 **J vs P**", ["J (계획) 📋", "P (즉흥) 🎲"])

# MBTI 조합
mbti = ei[0] + sn[0] + tf[0] + jp[0]

st.markdown("---")
st.markdown(f"<h3 style='text-align: center;'>당신의 MBTI: <span style='color: #FF6B6B;'>{mbti}</span> 🎊</h3>", unsafe_allow_html=True)

# 추천 버튼
if st.button("🎁 내 포켓몬 추천 받기! 🎁", use_container_width=True):
    pokemon = mbti_pokemon[mbti]
    
    st.balloons()
    
    st.markdown("---")
    st.markdown(f"<h2 style='text-align: center;'>🎉 두구두구두구... 🥁</h2>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align: center; color: #FF6B6B;'>{pokemon['emoji']} {pokemon['name']} {pokemon['emoji']}</h1>", unsafe_allow_html=True)
    
    # 포켓몬 이미지
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(pokemon['image'], use_container_width=True)
    
    # 설명
    st.markdown(f"### 💬 {pokemon['name']}는 이런 포켓몬이에요!")
    st.info(pokemon['description'])
    
    # 특징
    st.markdown("### ✨ 당신과 닮은 특징")
    cols = st.columns(3)
    for i, trait in enumerate(pokemon['traits']):
        with cols[i]:
            st.success(trait)
    
    st.markdown("---")
    st.markdown("<h4 style='text-align: center;'>🌈 당신과 포켓몬의 만남을 응원해요! 🎊</h4>", unsafe_allow_html=True)

# 푸터
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Made with 💖 by 당곡고 | 🎮 Gotta Catch 'Em All!</p>", unsafe_allow_html=True)
