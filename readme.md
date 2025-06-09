EchoEd (Echo + Education): -

Your voice echoes back with knowledge.

🧠 AI Tutor for Visually Impaired Students
This project is a voice-interactive AI tutor designed to assist visually impaired learners. 
It combines speech recognition, natural language processing, and text-to-speech technologies to enable an intuitive, hands-free learning experience.

🔍 Features:- 
🎤 Voice Input: Records and transcribes spoken questions using AssemblyAI.
🤖 LLM Integration: Sends queries to a local LLM (like llama3) running via Ollama for intelligent responses.
🔊 Voice Output: Uses pyttsx3 to convert the AI's answers back to speech for the user to hear.
💻 Offline-Friendly: All AI processing happens locally through Ollama — no need for internet-based APIs for answers.

🛠 Tech Stack :- 
1.Python 
2.AssemblyAI (for speech-to-text)
3.Ollama + LLaMA 3 (for NLP/AI processing)
4.pyttsx3 (for text-to-speech)
5.VS Code, virtual environment, and Command Line tools

🚀 How It Works:-
1. The user speaks a question into the microphone.
2. The app transcribes the voice using AssemblyAI.
3. The transcribed text is sent to a locally running LLM (llama3 via Ollama).
4. The AI's reply is read aloud using text-to-speech.
