# ♟️ Voice-Controlled Chess

A simple Python chess game you can play with your voice. Make moves by speaking standard chess notation (e.g., `c6c7`, `3637`).

---

## 🚀 How to Run

1. **Download the Files**

   * `chess.py`
   * `gui.py`
   * `images/` (folder with chess piece images)

   Keep all these in the **same folder**.

2. **Install Dependencies**

   ```bash
   pip install pygame SpeechRecognition pyaudio python-chess
   ```

   > Typical dependencies include `pygame`, `speechrecognition`, `pyaudio`, `chess`.

3. **Run the Game**

   ```bash
   python gui.py
   ```

---

## 🎮 How to Play

1. **Launch the Game** – Run `python gui.py`.
2. **Speak Your Move** – Use legal voice commands such as:

   * `c6c7`
   * `3637`
3. **Speak Clearly** – For accurate speech recognition, reduce background noise and speak at a steady pace.
4. **Continue Playing** – Play proceeds until **checkmate**, **stalemate**, or **draw**.

---

## 🗣️ Supported Speech Patterns

* **Coordinate moves**: `c6c7`, `3637`

> The game currently supports coordinate-style input for voice commands.

---

## ⚙️ Requirements

* **Python** 3.9+
* **Audio Input**: A working microphone
* **Libraries** (typical):

  * `SpeechRecognition`
  * `PyAudio` *(on some systems you may need system-level install: e.g., `brew install portaudio` on macOS)*
  * `pygame`
  * `python-chess`

---

## 🔧 Troubleshooting

* **Microphone not detected**: Ensure OS mic permissions are enabled for your terminal/app.
* **`PyAudio` install fails**: Install PortAudio first (e.g., `brew install portaudio` on macOS, `sudo apt-get install portaudio19-dev` on Debian/Ubuntu), then `pip install pyaudio`.
* **Moves not recognized**: Speak slowly, try different phrasing, or type the move if your GUI supports manual input.

---


## 🙌 Acknowledgements

* Built with ❤️ using Python and open-source libraries.

---

## 👤 Author

**Amey Somvanshi**
IIT Roorkee
