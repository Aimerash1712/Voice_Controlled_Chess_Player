♟️ Voice Controlled Chess Game
A Python-based voice-controlled chess game where you make moves by speaking commands instead. The game uses Speech Recognition for input and Pygame for the graphical chessboard.

✅ Features
Voice-controlled moves (e.g., say E2E4 or C7C6)

Interactive GUI for the chessboard

Move validation using chess rules

Standard chess gameplay

Real-time speech recognition

📂 Project Structure
voice-chess/
|
├── chess.py         # Core game logic: move validation, piece movement
├── gui.py           # Main file to run the game (loads GUI and voice input)
├── images/          # Folder containing chess piece images
└── README.md        # Project documentation

🛠️ Requirements
Python 3.x

Dependencies:

speechrecognition

pygame

pillow

pyaudio (for microphone input)

numpy

⚙️ Installation
1. Download the Files
Download the chess.py and gui.py files and place them in the same folder. Ensure the images folder is also in the same directory.

2. Install the Dependencies
Open your terminal or command prompt and install the required packages by running this command:

pip install speechrecognition pygame pillow pyaudio numpy

▶️ How to Run the Game
Run the gui.py file from your terminal:

python gui.py

🎮 How to Play the Game
Launch the game using the command above.

The chessboard GUI will appear.

Use voice commands in standard chess notation.

Example commands:

E2E4 → Move pawn from E2 to E4

C7C6 → Move pawn from C7 to C6

Speak clearly and wait for the move to process.

Continue until checkmate or draw.
