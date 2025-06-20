
# 🕹️ Pong Game (Python Turtle Edition)

This is a classic **Pong** game built using Python's `turtle` graphics library. The game features two-player paddle controls, bouncing ball mechanics, and real-time scoring. Sound effects are added using the `winsound` module for an enhanced arcade feel.

---

## 🧠 Game Overview

* Two players control paddles on each side of the screen.
* The objective is to bounce the ball back and forth.
* If the opponent misses the ball, you score a point.
* First to a target score (or play endlessly!) wins.

---

## 🖥️ Requirements

* Python 3.x
* Windows OS (required for `winsound`)
* `.wav` sound files: `bounce.wav` and `bounce2.wav` (must be in the same directory as the script)

Install dependencies:

```bash
pip install PythonTurtle
```

---

## ▶️ How to Run

1. Save the code to a file, e.g., `pong_game.py`
2. Ensure you have `bounce.wav` and `bounce2.wav` in the same folder.
3. Open a terminal or command prompt.
4. Run the script:

```bash
python pong_game.py
```

---

## 🎮 Controls

### Player A (Left Paddle):

* 🔼 `W` – Move Up
* 🔽 `S` – Move Down

### Player B (Right Paddle):

* 🔼 `↑ Arrow` – Move Up
* 🔽 `↓ Arrow` – Move Down

---

## 🎨 Features

* Real-time paddle and ball movement
* Edge-bound paddle logic to prevent going off-screen
* Collision detection with sound feedback
* Live score tracking using Turtle's `write` method
* Fullscreen game area with customizable colors

---

## 🧩 Code Structure

* **Turtle Setup**: Initializes screen, paddles, and ball
* **Functions**: Handles paddle movement
* **Game Loop**: Continuously updates game state and checks for collisions
* **Sound**: Uses `winsound` for bounce effects

---

## 🛠️ To-Do / Enhancements

* Add game-over condition when a player reaches a score limit
* Add a restart/new game menu
* Add AI paddle for single-player mode
* Add pause functionality
* Cross-platform sound support (replace `winsound`)

---

## 📁 Assets

Include these `.wav` files in your project folder:

* `bounce.wav` – Sound for wall bounce
* `bounce2.wav` – Sound for paddle bounce

