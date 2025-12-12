# 🧮 수학 게임 & 퀴즈 챗봇

수학 개념을 게임 형식으로 재미있게 학습할 수 있는 AI 기반 대화형 교육 앱입니다.
학생들의 수학적 사고력과 문제 해결 능력을 향상시키는 데 도움이 됩니다.

## 주요 기능

### 🎮 맞춤형 게임 설정
- **난이도 선택**: 초등학교부터 대학 수준까지 5단계 선택 가능
- **주제 선택**: 덧셈, 곱셈, 분수, 방정식, 함수 등 10가지 주제
- **게임 형식**: 퀴즈, 문제 풀이, 챌린지 게임, 개념 설명 중 선택

### 🤖 AI 기반 맞춤형 학습
- **다양한 모델 지원**: GPT-4o, GPT-4-turbo, GPT-4, GPT-3.5-turbo 중 선택
- **실시간 피드백**: 답변에 대한 즉각적인 피드백과 설명 제공
- **단계별 학습**: 수학적 개념을 쉽고 재미있게 설명

### ⚙️ 고급 설정
- **Temperature 조절**: 답변의 창의성 정도 조절 (0.0 ~ 2.0)
- **Max Tokens 설정**: 답변의 길이 조절
- **시스템 프롬프트 커스터마이징**: AI 동작 방식 자유롭게 설정

## 사용 방법

### 1. 설치
\`\`\`
$ pip install -r requirements.txt
\`\`\`

### 2. 앱 실행
\`\`\`
$ streamlit run streamlit_app.py
\`\`\`

### 3. 게임 시작
1. OpenAI API 키를 사이드바에 입력합니다
2. 난이도, 주제, 게임 형식을 선택합니다
3. AI 모델과 파라미터를 설정합니다
4. 채팅창에서 게임을 시작합니다!

## 팁

- **다음 문제**: '다음 문제'라고 입력하면 새로운 문제를 받을 수 있습니다
- **처음부터 시작**: '처음부터 시작'이라고 입력하면 새로운 게임을 시작합니다
- **설명 요청**: '설명해줘'라고 입력하면 개념에 대한 상세 설명을 받습니다
- **설정 변경**: 언제든지 사이드바에서 난이도, 주제, 모델을 변경할 수 있습니다

## 필수 요구사항

- Python 3.8 이상
- OpenAI API 키 ([여기서 획득](https://platform.openai.com/account/api-keys))
- Streamlit 1.28 이상
- OpenAI Python 라이브러리

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://chatbot-template.streamlit.app/)

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```
