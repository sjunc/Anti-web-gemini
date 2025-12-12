# Anti-web-gemini
이 프로젝트는 에이전트 코딩 툴, Antigravity를 통한 프로젝트에 대한 완성도를 높이고 토큰 사용량을 적게 사용하기 위해서 고려되었습니다.  
방식은 Antigravity의 자체 토큰은 오로지 에이전트 및 개발자의 기능에 집중시키고 웹에서 Thinking mode를 통해 에셋(이미지/영상), 계획, 조사(최신 동향, 논문)를 활용하는 방식입니다.   
현재 웹의 토큰이 훨씬 크며 자동화를 할 수 있다면 매우 활용성이 높은 상태입니다. 
## 목표
이를 우린 명세하고 작성하여 똑똑하게 질문하기, 가져오기, 작성하기 등의 명세와 단순히 에이전트에 의존하는 것보다 함수를 활용해서 더 줄이는 방법입니다.   
## 언어
python 3.8  이상 버전  
데이터 XML 방식  
## 계획 
### Phase 1: The Architect (인지 및 설계 단계)"코드를 작성하기 전에, 완벽한 정신적 모델(Mental Model)을 수립한다."  
1.1 Intent Decoupling (요구사항 해체 및 재조립)  
- Input: 사용자의 불명확한 요구사항.  
- Action: 바로 코딩하지 않고, Socratic Questioning을 수행하여 숨겨진 의도와 기술적 제약을 파악합니다.   
- Goal: "무엇을 만들까?"가 아니라 "왜, 그리고 어떻게 작동해야 하는가?"를 정의.    
1.2 Deep Research & Knowledge Sync (지식 공백 메우기)  
- Protocol: LLM의 지식 차단 시점(Cutoff)을 인정하고, Deep Research 툴을 강제 실행합니다.  
- Target:최신 라이브러리 버전 (Deprecation 방지)  
- Best Practices (2024-2025 SOTA 패턴)하드웨어 호환성 체크 Differentiation: 단순 검색이 아니라, 검색 결과를 바탕으로 **"현재 시점의 기술 스택 호환성 매트릭스"**를 작성합니다.  
1.3 Visual Blueprinting (멀티모달 설계)  
- Concept: 텍스트로만 설계하지 않습니다. Gemini의 이미지 생성 기능을 활용해 **청사진(Blueprint)**을 그립니다.  
- Action:DB Schema ERD 생성UI Wireframe/Mockup 이미지 생성System Architecture Diagram 생성  
- Loop: 생성된 이미지를 Gemini가 다시 Vision으로 분석하여 코드 구조가 이미지와 일치하는지 "자가 검증(Self-Correction)" 합니다.  
### Phase 2: The Engineer (구조화 및 사고 단계)"토큰 효율성을 극대화하기 위해 영어로 사고하고 구조를 잡는다."  
2.1 English-First Internal Monologue (토큰 절감 전략)    
- Rule: 모든 내부 사고 과정(Thinking Process), 주석(Comments), 변수명, 커밋 메시지는 반드시 영어로 작성합니다.  
- Reason: 한글 대비 토큰 소모량을 30~50% 절감하고, LLM의 학습 데이터 분포상 영어로 추론할 때 논리적 정합성이 더 높습니다. (사용자 최종 출력만 한국어로 변환)  
2.2 Structural Jsonification (데이터 구조화)  
  Action: 파일 트리를 텍스트로 나열하지 않고, JSON 또는 XML 형태로 완벽하게 구조화하여 출력합니다.  
  Example:{    
  "project_root": {    
    "src": { "main.py": "...", "utils.py": "..." },    
    "tests": { "test_main.py": "..." },    
    "docs": { "README.md": "..." }    
  }    
}    
Benefit: Antigravity가 파싱하기 가장 쉬운 형태로 전달하여 에러율 0% 도전.  
### Phase 3: The Executor (실행 및 반복 단계)"Antigravity를 통해 물리적 세계에 개입하고 피드백을 받는다."   
3.1 Atomic Execution Loop (원자적 실행)단순 반복이 아닌, TDD (Test Driven Development) 기반의 루프를 돕니다.  
- Test First: 기능 구현 전, 실패하는 테스트 코드를 먼저 작성 (Gemini).   
- Implementation: 테스트를 통과하기 위한 최소한의 코드 작성 (Gemini).  
- Run: Antigravity가 로컬에서 실행.Verification: 테스트 통과 여부 확인.  
3.2 Dynamic Asset Generation (에셋 즉시 생성)   
- Trigger: 코딩 중 Placeholder 이미지가 필요하거나, 아이콘이 필요할 때.  
- Action: 즉시 이미지 생성 도구를 호출하여 에셋을 만들고, 로컬 경로에 저장하도록 지시.  
3.3 Error Context Compression (에러 처리 최적화)  
- Problem: 에러 로그 전체를 붙여넣으면 토큰 낭비 발생.  
- Solution: Antigravity가 에러의 핵심 스택 트레이스(Stack Trace)만 요약(Digest)하여 Gemini에게 전달.  
### Phase 4: The Auditor (최종 검증 및 회고) 
4.1 Final Polish작성된 코드를 Black이나 Prettier 같은 포맷터로 정리하고, Docstring이 누락된 곳을 채웁니다.  
4.2 User Presentation최종 결과물은 한국어로 요약하여 보고하되, 기술적인 상세 내용은 영어 원문을 유지하여 정확성을 보장합니다.Summary of Logic Flowgraph TD  
    User[User Request] --> Intent[Intent Analysis (Socratic)]   
    Intent --> Research[Deep Research (SOTA/Docs)]  
    Research --> Visual[Visual Blueprinting (Image Gen)]  
    Visual --> VisionCheck[Self-Correction via Vision]  
    VisionCheck --> EnglishPlan[English Structural Planning (JSON)]  
    EnglishPlan --> Loop{Execution Loop}  
      
    Loop --> TestGen[Write Fail Test]  
    TestGen --> CodeGen[Write Code]  
    CodeGen --> Antigravity[Local Execution (Antigravity)]  
    Antigravity --> Result[Pass/Fail?]  
      
    Result -- Fail --> LogCompress[Compress Error Log]  
    LogCompress --> CodeGen  
      
    Result -- Pass --> Asset[Asset Gen (If needed)]  
    Asset --> Next[Next Feature]  
      
    Next --> Loop  
    Loop -- Complete --> Polish[Final Polish & Korean Summary]  
  
### 예상되는 문제점 
antigravity와 웹의 입출력이 매끄럽게 연결되지 않고 복사, 붙여넣기에 의존한다면 안 쓰니만 못 할 만큼 느리고 토큰 사용량에서 감소 또한 없을 것입니다.  
# Log
프로젝트를 수행하면서 문제점들이 몇가지 발견되었습니다.  
GEMINI가 google에서 제작한 antigravity라도 bot으로 감지하며 extension을 통해서 이용할 수 없게 설정되어 있었습니다.   
그래서 스크립팅 및 크롤링을 활용하려고 했으나 또 하나의 문제점은 google 정책상 자동 스크립팅 및 스크랩은 수행하면 계정이 정지될 수 있습니다.  
다른 방법으로 시도하기로 했습니다. 문제점을 해결하기 위해서 완전 agent를 통해서 권한을 넘기는 것이었습니다. mcp를 만들기도 했지만 gemini의 html script 부분을 매번 변경해서 한번 짠 코드가 소용없어진다는 문제와 결국 이를 막았다는 것은 이부분 또한 회색지대에 가까웠다는 문제점이 존재했습니다. 더 큰 문제는 내 권한을 모두 넘겨준다는 불안감과 마우스와 키보드를 치는 방식이여서 속도가 매우 느렸다는 문제가 존재했습니다.   
그 다음 부분은 크롬 익스텐션을 새로 만들어서 폴더 내로 보내는 방법이었습니다. 하지만 이부분은 원활하지 않고 이미지 전달에서의 문제가 발생했습니다.  
또 새롭게 시도한 방법은 Gems를 가지고 전체 프로젝트를 총괄하는 프로토콜을 만들고 이를 클립보드를 통해서 전달하는 방법이었습니다.  
현재 합법적이고 기능면에서의 합의점은 찾았다고 생각은 하고 있지만 프로젝트를 수행함에 있어서나 다른 사람들에게 제공할 방법에 있어서는 매우 부족하다고 느끼고 있습니다. 그리고 antigravity의 기능 자체가 상당부분 줄어서 테스터로 전락한 것이 아닌가하는 생각이 들어서 아쉬움이 남습니다.   
  












