# Antigravity (안티그래비티) x Gemini 3.0 V3

**Cognitive Airlock (인지 에어락): 안전, 기억, 그리고 시각**

## 1. 프로젝트 목표 (Project Goal)

Antigravity V3는 단순히 코드를 실행하는 것을 넘어, **안전하고(Safe)**, **기억하며(Mnestic)**, **볼 수 있는(Visual)** 시스템을 지향합니다.

*   **Brain (Gemini 3.0 Web)**: 무한한 추론 및 멀티모달(텍스트+이미지) 설계 담당.
*   **Hands (Antigravity Local)**: 생각하는 대로 실행하되, 인간의 통제 하에 둡니다.

## 2. V3 핵심 기능 (Key Features)

### 🛡️ The Airlock (보안 에어락)
Gemini가 위험한 명령어(`rm -rf` 등)를 생성하더라도, 즉시 실행되지 않습니다.
*   **작동 방식**: 명령어 감지 시 **붉은색 경고 패널**이 뜨며 대기합니다.
*   **사용자 승인**: 사용자가 내용을 확인하고 승인해야만 실행됩니다.

### 💎 Context Crystal (기억의 결정체)
채팅이 길어지면 Gemini가 이전 파일 내용을 잊어버리는 문제를 해결합니다.
*   **기능**: 프로젝트 전체 상태를 하나의 XML 블록으로 압축합니다.
*   **사용법**: 스크립트를 실행하여 클립보드에 복사된 내용을 Gemini에게 "기억 복원"용으로 붙여넣습니다.

### 👁️ Vision Bridge (시각 지능)
이제 텍스트뿐만 아니라 이미지도 전송받을 수 있습니다.
*   **기능**: Gemini가 생성한 아키텍처 다이어그램이나 UI 목업(Base64)을 로컬에 이미지 파일(`.png`)로 자동 저장합니다.

## 3. 사용법 (How to Use)

### 1단계: 설치 (Installation)
```powershell
pip install -r requirements.txt
```

### 2단계: 데몬 실행 (Start Daemon)
백그라운드에서 클립보드를 감시합니다.
```powershell
python -m src.main --daemon
```

### 3단계: 워크플로우 (Workflow)
1.  **기억 주입 (필요 시)**:
    ```powershell
    python -c "from src.utils.context_packer import pack_context; print(pack_context('.'))" | clip
    ```
    이 명령어로 복사된 XML을 Gemini에게 주면 프로젝트 구조를 완벽히 이해합니다.
2.  **코드/이미지 생성**: Gemini가 `<file>`, `<cmd>`, `<asset>` 태그를 생성합니다.
3.  **복사 & 실행**: 웹에서 복사(Ctrl+C)하면 로컬에서 감지됩니다.
    *   **코드/이미지**: 자동 저장/실행 대기.
    *   **명령어**: 에어락(경고창) 작동 -> 승인 시 실행.

---
*Created by Google DeepMind's Antigravity Agent.*
