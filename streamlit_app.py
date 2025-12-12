import streamlit as st
from openai import OpenAI

# Page configuration
st.set_page_config(page_title="수학 게임 & 퀴즈 챗봇", layout="wide")

# Show title and description.
st.title("🧮 수학 게임 & 퀴즈 챗봇")
st.write(
    "수학 개념을 게임 형식으로 재미있게 학습하세요! "
    "이 앱은 수학 퀴즈, 게임, 문제 풀이를 통해 학생들의 수학적 사고력과 문제 해결 능력을 향상시키도록 설계되었습니다. "
    "사이드바에서 난이도, 주제, AI 모델 설정을 조절하여 맞춤형 학습 경험을 할 수 있습니다."
)

# ===== SIDEBAR CONFIGURATION =====
with st.sidebar:
    st.header("⚙️ 설정")
    
    # API Key input
    openai_api_key = st.text_input("OpenAI API Key", type="password")
    
    # Create collapsible section for game settings
    with st.expander("🎮 게임 설정", expanded=True):
        
        # Difficulty level
        difficulty = st.selectbox(
            "난이도 선택",
            ["초등학교 (1-3학년)", "초등학교 (4-6학년)", "중학교", "고등학교", "대학"],
            index=1,
            help="학습자 수준에 맞는 난이도를 선택하세요."
        )
        
        # Math topic
        math_topic = st.selectbox(
            "주제 선택",
            [
                "덧셈과 뺄셈",
                "곱셈과 나눗셈",
                "분수",
                "소수",
                "기본 기하학",
                "방정식 풀이",
                "함수",
                "확률과 통계",
                "대수",
                "혼합 (모든 주제)"
            ],
            index=9,
            help="학습할 수학 주제를 선택하세요."
        )
        
        # Game type
        game_type = st.radio(
            "게임 형식 선택",
            ["📝 퀴즈 (객관식)", "🎯 문제 풀이", "🏆 챌린지 게임", "💭 개념 설명"],
            help="원하는 게임 형식을 선택하세요."
        )
    
    # Create collapsible section for model settings
    with st.expander("🤖 AI 모델 설정", expanded=False):
        
        # Model selection
        available_models = [
            "gpt-4o",
            "gpt-4-turbo",
            "gpt-4",
            "gpt-3.5-turbo",
        ]
        selected_model = st.selectbox(
            "모델 선택",
            available_models,
            index=0
        )
        
        # Temperature slider
        temperature = st.slider(
            "Temperature",
            min_value=0.0,
            max_value=2.0,
            value=0.7,
            step=0.1,
            help="낮을수록 일관되고 집중된 답변, 높을수록 창의적인 답변"
        )
        
        # Max tokens input
        max_tokens = st.number_input(
            "Max Tokens",
            min_value=100,
            max_value=4096,
            value=2048,
            step=100,
            help="생성할 최대 토큰 수"
        )
    
    # Display current settings
    st.markdown("---")
    st.markdown("**📊 현재 설정:**")
    st.markdown(f"- **난이도**: {difficulty}")
    st.markdown(f"- **주제**: {math_topic}")
    st.markdown(f"- **형식**: {game_type}")
    st.markdown(f"- **AI 모델**: `{selected_model}`")

# ===== MAIN CHAT INTERFACE =====
if not openai_api_key:
    st.info("사이드바에서 OpenAI API 키를 입력해주세요.", icon="🗝️")
else:
    # Create an OpenAI client.
    client = OpenAI(api_key=openai_api_key)

    # Create session state variables
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "game_started" not in st.session_state:
        st.session_state.game_started = False

    # System prompt optimized for math games and quizzes
    system_prompt = f"""당신은 수학 교육 전문가이자 게임 진행자입니다.

학습자 수준: {difficulty}
학습 주제: {math_topic}
게임 형식: {game_type}

당신의 역할:
1. 학생의 수준에 맞는 적절한 난이도의 문제를 제시합니다.
2. 학생의 답변에 대해 즉각적인 피드백을 제공합니다.
3. 정답인 경우 격려하고, 오답인 경우 친절하게 설명합니다.
4. 수학적 개념을 게임과 함께 설명하여 흥미롭게 학습하도록 합니다.
5. 학생의 진행 상황을 추적하고 격려합니다.

응답 형식:
- 문제는 명확하고 이해하기 쉽게 작성합니다.
- 계산 과정을 단계별로 설명합니다.
- 이모지를 사용하여 시각적으로 표현합니다.
- 정답/오답에 따른 재미있는 댓글을 추가합니다."""

    # Display the existing chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Welcome message if no messages yet
    if not st.session_state.messages:
        with st.chat_message("assistant"):
            welcome_msg = f"👋 안녕하세요! {difficulty} 수준의 {math_topic} 학습을 위한 {game_type} 게임을 시작하겠습니다!\n\n첫 번째 문제를 기다려주세요... 또는 어떤 도움이 필요한지 말씀해주세요!"
            st.markdown(welcome_msg)
        st.session_state.messages.append({"role": "assistant", "content": welcome_msg})

    # Create a chat input field
    if prompt := st.chat_input("답변을 입력하거나 '다음 문제' 또는 '처음부터 시작'이라고 입력하세요..."):

        # Store and display the current prompt.
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate a response using the OpenAI API.
        try:
            stream = client.chat.completions.create(
                model=selected_model,
                messages=[
                    {"role": "system", "content": system_prompt}
                ] + [
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                temperature=temperature,
                max_tokens=max_tokens,
                stream=True,
            )

            # Stream the response to the chat
            with st.chat_message("assistant"):
                response = st.write_stream(stream)
            st.session_state.messages.append({"role": "assistant", "content": response})
                except Exception as e:
                    st.error(f"오류 발생: {str(e)}")
    
            # Add reset button
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button("🔄 대화 초기화", key="reset_button"):
                    st.session_state.messages = []
                    st.rerun()
    
            with col2:
                if st.button("📋 사용 팁", key="tips_button"):
                    st.info("""
                    **게임 진행 팁:**
                    - '다음 문제'라고 입력하면 새로운 문제를 받을 수 있습니다.
                    - '처음부터 시작'이라고 입력하면 새로운 게임을 시작합니다.
                    - '설명해줘'라고 입력하면 개념에 대한 상세 설명을 받을 수 있습니다.
                    - 사이드바에서 난이도나 주제를 변경한 후 대화를 계속할 수 있습니다.
                    """)
        except Exception as e:
            st.error(f"오류 발생: {str(e)}")
