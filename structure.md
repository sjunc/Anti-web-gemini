# Antigravity Project Structure

이 문서는 프로젝트의 파일 구조와 각 모듈의 역할을 설명합니다.

## 📂 Project Root (`vibe/`)

*   **`GEMINI.md` / `PROTOCOL_V3.md`**: 안티그래비티 V3 프로토콜(Cognitive Airlock)의 정의 문서입니다.
*   **`README.md`**: 프로젝트의 개요 및 사용법 (한국어).
*   **`requirements.txt`**: 파이썬 의존성 목록.

## 📂 Source Code (`src/`)

핵심 로직이 포함된 디렉토리입니다.

*   **`main.py`**: 프로그램의 진입점(Entry Point). 데몬 모드 실행을 담당합니다.
*   **`daemon.py`**: **[V2]** 클립보드 감시자. XML 파싱을 트리거하는 백그라운드 프로세스입니다.
*   **`parser.py`**: **[V3 업데이트]** `<file>`, `<cmd>` 외에 **`<asset>`(이미지)** 태그 파싱을 지원합니다.
*   **`executor.py`**: **[V3 업데이트]** 실행 담당. **Airlock(보안 패널)** UI 및 이미지 디코딩/저장 로직이 추가되었습니다.
*   **`utils/compressor.py`**: **[V2]** 에러 로그 압축 유틸리티.
*   **`utils/context_packer.py`**: **[V3 신규]** **Context Crystal**. 프로젝트 전체 파일을 하나의 XML로 직렬화하여 Gemini의 기억력을 보존합니다.

## 📂 Tests (`tests/`)

TDD(Test Driven Development) 기반 테스트 코드입니다.

*   **`test_daemon.py`**: 클립보드 감시 로직 테스트.
*   **`test_compressor.py`**: 에러 압축 로직 테스트.
*   **`test_packer.py`**: **[V3]** 컨텍스트 패킹 로직 테스트.
*   **`test_vision.py`**: **[V3]** 이미지 자산(Base64) 처리 로직 테스트.
