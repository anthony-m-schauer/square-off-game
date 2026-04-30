# Square Off Game

**Square Off Game** is a small interactive browser game built with Streamlit. The player draws a rectangle and tries to make it as close to a perfect square as possible.

The game is simple: click **BEGIN**, drag to draw a rectangle, wait until the status says **READY**, then submit your shape and see how close you were to a perfect square.

---

## Live App

Add your Streamlit app link here after deployment:

```text
https://square-off-game.streamlit.app
```

---

## Project Overview

The goal of this project was to create a clean, lightweight web game using Python and Streamlit, while also using custom HTML, CSS, and JavaScript for the actual drawing interaction.

Streamlit handles the app structure and deployment, while the embedded browser component handles the canvas-based game logic.

---

## How the Game Works

1. The user clicks **BEGIN**.
2. The user clicks and drags inside the play area to draw a rectangle.
3. The rectangle must be large enough before it can be submitted.
4. Once the drawn shape reaches the minimum required area, the status changes from **TOO SMALL** to **READY**.
5. When the user releases the mouse, a confirmation box appears.
6. After submitting, the game calculates how close the rectangle is to a perfect square.
7. The final score is shown as a percentage, and the top five scores are tracked on the leaderboard for the current session.

---

## Scoring Logic

The score is based on how close the drawn rectangle is to a square.

The larger side of the rectangle is treated as the correct side length for the target square. The smaller side is treated as the user's attempt to match that square.

```text
score = smaller_side / larger_side * 100
```

A perfect square receives a score of:

```text
100.00%
```

Example:

```text
larger side = 400
smaller side = 320

score = 320 / 400 * 100
score = 80.00%
```

---

## Features

- Interactive click-and-drag rectangle drawing
- Minimum area requirement before submission
- Visual **TOO SMALL** and **READY** status indicator
- Score shown to two decimal places
- Animated circular percentage result display
- Color-coded score result
- Current-session leaderboard with top five scores
- Simple, clean visual design
- Built as a deployable Streamlit web app

---

## Tech Stack

- Python
- Streamlit
- HTML
- CSS
- JavaScript
- Canvas API

---

## Project Structure

```text
square-off-game/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Running the App Locally

First, clone the repository or open the project folder.

Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Run the app:

```powershell
streamlit run app.py
```

The app should open locally at:

```text
http://localhost:8501
```

---

## Deployment

This app is designed to deploy through Streamlit Community Cloud.

Deployment settings:

```text
Repository: square-off-game
Branch: main
Main file path: app.py
```

The app only requires Streamlit as a dependency, listed in `requirements.txt`.

---

## Notes

The leaderboard tracks scores only during the current running browser session. Refreshing the page or restarting the app clears the leaderboard.

This project was created as a small interactive game and Streamlit deployment exercise.

---

## Future Improvements

Possible future additions:

- Persistent leaderboard storage
- Clear leaderboard button
- Best score highlight
- Round counter
- Mobile/touch support
- Difficulty modes
- Timer-based challenge mode
- More polished visual effects after scoring

---

## Author

Created by **Anthony Schauer**.
