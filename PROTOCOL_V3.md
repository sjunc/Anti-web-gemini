# Antigravity V3: The Cognitive Airlock

**Theme**: Safety, Vision, and Infinite Context.

## 1. The Core Problem with V2
V2 is efficient but "blind."
*   **Dangerous**: The Daemon executes clipboard contents automatically. If Gemini hallucinates `rm -rf /`, we have no safety net.
*   **Amnesiac**: As the chat thread grows, Gemini loses track of earlier files. We need a way to "rehydrate" its memory.
*   **Text-Only**: It cannot handle the visual blueprints (images) we discussed in the strategy.

## 2. V3 Feature Set

### 2.1 The Airlock (Safety UI)
*   **What**: A lightweight TUI (Terminal User Interface) or GUI popup.
*   **Function**: When the Daemon detects a `<cmd>` tag in the clipboard, it pauses.
*   **Action**: User hits `[Enter]` to Approve or `[Esc]` to Reject.
*   **Goal**: "Human-in-the-Loop" security without friction.

### 2.2 Context Crystal (Memory Management)
*   **What**: A script (`context_packer.py`) that serializes the entire project into a single XML block.
*   **Usage**: When starting a new thread or when Gemini gets confused, run this script and paste the output.
*   **Prompt**: "Restore project state from this block. Enter Thinking Mode."

### 2.3 The Vision Bridge
*   **What**: Protocol for handling Base64 images from Gemini.
*   **Tag**: `<asset type="image" path="assets/blueprint.png">{base64_string}</asset>`
*   **Action**: Antigravity decodes the string and saves the .png file automatically.

### 2.4 Deep Research Sync
*   **What**: Automatic environment dumping.
*   **Action**: A command that runs `pip freeze` or `npm list` and formats it as JSON to the clipboard.

## 3. Implementation Priorities
1.  **Priority Alpha**: Context Crystal (Solves the immediate "Context Amnesia" issue).
2.  **Priority Beta**: The Airlock (Security).
3.  **Priority Gamma**: Vision Bridge (Multimodal).

*Roadmap approved for immediate execution.*
