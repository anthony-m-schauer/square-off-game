"""
Square Off Game
Author: Anthony Schauer

Overview:
    A Streamlit game where the player draws a rectangle and tries to make it
    as close to a perfect square as possible.

Game Rules:
    - Click BEGIN to start.
    - Click and drag inside the play area to draw a rectangle.
    - The rectangle must cover at least 1/6 of the play area.
    - While the rectangle is too small, the top status says TOO SMALL.
    - Once the rectangle is large enough, the top status says READY.
    - When the user releases the mouse while READY, a confirmation box appears.
    - The score is based on how close the rectangle's area is to the perfect
      square area using the larger side as the correct square side.
"""

import streamlit as st
import streamlit.components.v1 as components


##### Step One: Streamlit Page Setup #####

st.set_page_config(
    page_title="Square Off Game",
    page_icon="⬛",
    layout="wide",
)

st.markdown(
    """
    <style>
        .block-container {
            padding-top: 0.25rem;
            padding-bottom: 0.25rem;
            max-width: 1550px;
        }

        header[data-testid="stHeader"] {
            height: 2rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


##### Step Two: Game HTML, CSS, and JavaScript #####

game_code = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">

<style>
    html, body {
        margin: 0;
        padding: 0;
        background: transparent;
        font-family: Arial, sans-serif;
        overflow: hidden;
    }

    .full-wrapper {
        width: 100%;
        max-width: 1480px;
        margin: 0 auto;
        padding-top: 56px;
        box-sizing: border-box;
    }

    .game-header {
        width: 100%;
        background: #2f3742;
        border: 3px solid #222222;
        border-radius: 16px;
        padding: 26px 24px 22px 24px;
        box-sizing: border-box;
        margin-bottom: 18px;
    }

    .main-title {
        color: #ffffff;
        text-align: center;
        font-size: 40px;
        font-weight: 900;
        line-height: 1.25;
        margin: 0 0 10px 0;
        padding: 0;
    }

    .subtitle {
        color: #ffffff;
        text-align: center;
        font-size: 17px;
        line-height: 1.35;
        margin: 0;
    }

    .app-shell {
        width: 100%;
        display: flex;
        gap: 20px;
        align-items: stretch;
        box-sizing: border-box;
    }

    .leaderboard-panel {
        width: 265px;
        background: #ffffff;
        border: 3px solid #222222;
        border-radius: 16px;
        overflow: hidden;
        display: flex;
        flex-direction: column;
        flex-shrink: 0;
        min-height: 705px;
    }

    .leaderboard-header {
        background: #e8e8e8;
        border-bottom: 3px solid #222222;
        text-align: center;
        font-size: 22px;
        font-weight: bold;
        padding: 18px 10px;
        color: #222222;
    }

    .leaderboard-subheader {
        font-size: 13px;
        color: #666666;
        text-align: center;
        padding: 12px 8px 8px 8px;
    }

    .leaderboard-list {
        padding: 14px 16px 18px 16px;
        display: flex;
        flex-direction: column;
        gap: 11px;
        flex: 1;
        box-sizing: border-box;
    }

    .leaderboard-item {
        border: 2px solid #222222;
        border-radius: 11px;
        background: #f8f8f8;
        padding: 13px 14px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 16px;
        font-weight: bold;
        color: #222222;
    }

    .leaderboard-rank {
        color: #555555;
    }

    .leaderboard-score {
        color: #1f5fa8;
    }

    .leaderboard-empty {
        border: 2px dashed #bbbbbb;
        border-radius: 11px;
        background: #fcfcfc;
        padding: 20px 14px;
        text-align: center;
        font-size: 14px;
        color: #777777;
        line-height: 1.45;
    }

    .game-shell {
        flex: 1;
        background: #ffffff;
        border: 3px solid #222222;
        box-sizing: border-box;
        border-radius: 16px;
        overflow: hidden;
        min-height: 705px;
    }

    .top-box {
        height: 80px;
        background: #ececec;
        border-bottom: 3px solid #222222;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 0 18px;
        box-sizing: border-box;
    }

    .top-center-group {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 16px;
        flex-wrap: nowrap;
    }

    .status-pill {
        min-width: 165px;
        text-align: center;
        font-size: 19px;
        font-weight: bold;
        letter-spacing: 0.5px;
        padding: 12px 18px;
        border-radius: 9px;
        border: 2px solid #222222;
    }

    .status-start {
        color: #222222;
        background: #ffffff;
    }

    .status-small {
        color: #a40016;
        background: #ffe1e1;
    }

    .status-ready {
        color: #0b7a20;
        background: #ddffdf;
    }

    .button {
        font-size: 15px;
        font-weight: bold;
        padding: 11px 17px;
        border: 2px solid #222222;
        border-radius: 9px;
        background: #ffffff;
        color: #222222;
        cursor: pointer;
    }

    .button:hover {
        background: #eeeeee;
    }

    .chip {
        font-size: 14px;
        font-weight: bold;
        color: #1f1f1f;
        background: #dbe9ff;
        border: 2px solid #222222;
        border-radius: 999px;
        padding: 10px 15px;
        white-space: nowrap;
    }

    .chip-alt {
        background: #fff3c9;
    }

    .play-area {
        position: relative;
        width: 100%;
        height: 590px;
        background: #f7f7f2;
        overflow: hidden;
    }

    canvas {
        display: block;
        width: 100%;
        height: 100%;
        background: transparent;
        cursor: crosshair;
    }

    .corner-design {
        position: absolute;
        right: 22px;
        bottom: 20px;
        display: flex;
        align-items: center;
        gap: 12px;
        color: #777777;
        font-size: 14px;
        font-weight: bold;
        pointer-events: none;
        opacity: 0.95;
    }

    .target-square {
        width: 44px;
        height: 44px;
        border: 3px solid #1f5fa8;
        background: rgba(31, 95, 168, 0.12);
        box-sizing: border-box;
    }

    .mini-legend {
        position: absolute;
        left: 20px;
        bottom: 18px;
        display: flex;
        gap: 10px;
        pointer-events: none;
    }

    .legend-item {
        font-size: 13px;
        color: #333333;
        background: rgba(255, 255, 255, 0.95);
        border: 1px solid #bbbbbb;
        border-radius: 999px;
        padding: 7px 11px;
    }

    .decor-top-left {
        position: absolute;
        left: 22px;
        top: 20px;
        display: flex;
        gap: 8px;
        pointer-events: none;
        opacity: 0.55;
    }

    .decor-square {
        width: 15px;
        height: 15px;
        border: 2px solid #222222;
        background: #f5f5f5;
    }

    .decor-square.blue {
        background: #dbe9ff;
    }

    .decor-square.gold {
        background: #fff3c9;
    }

    .decor-square.green {
        background: #ddffdf;
    }

    .center-layer {
        position: absolute;
        inset: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        pointer-events: none;
    }

    .popup {
        background: #ffffff;
        border: 3px solid #222222;
        border-radius: 14px;
        padding: 30px 42px;
        text-align: center;
        box-shadow: 0 12px 26px rgba(0, 0, 0, 0.23);
        pointer-events: auto;
        min-width: 300px;
    }

    .popup h2 {
        margin-top: 0;
        margin-bottom: 17px;
        font-size: 29px;
    }

    .popup p {
        font-size: 16px;
        color: #333333;
        margin: 12px 0 0 0;
    }

    .button-row {
        display: flex;
        justify-content: center;
        gap: 14px;
        margin-top: 12px;
    }

    .hidden {
        display: none;
    }

    .score-circle {
        width: 210px;
        height: 210px;
        border-radius: 50%;
        border: 3px solid #222222;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 10px auto 14px auto;
        background: conic-gradient(from -90deg, #dddddd 0deg 360deg);
    }

    .score-inner {
        width: 142px;
        height: 142px;
        border-radius: 50%;
        background: #ffffff;
        border: 2px solid #222222;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 31px;
        font-weight: bold;
    }

    .score-details {
        font-size: 15px;
        color: #333333;
        line-height: 1.5;
    }

    .restart-late {
        margin-top: 14px;
    }

    .bottom-design {
        height: 34px;
        background: #f8f8f8;
        border-top: 3px solid #222222;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 12px;
    }

    .dot {
        width: 11px;
        height: 11px;
        border-radius: 50%;
        border: 1px solid #222222;
        background: #dbe9ff;
    }

    .dot.gold {
        background: #fff3c9;
    }

    .dot.green {
        background: #ddffdf;
    }

    .dot.red {
        background: #ffe1e1;
    }

    .bottom-text {
        font-size: 13px;
        font-weight: bold;
        color: #555555;
        letter-spacing: 0.3px;
    }
</style>
</head>

<body>

<div class="full-wrapper">

    <div class="game-header">
        <h1 class="main-title">Square Off Game</h1>
        <p class="subtitle">Draw a rectangle. Make it as close to a perfect square as possible.</p>
    </div>

    <div class="app-shell">

        <div class="leaderboard-panel">
            <div class="leaderboard-header">Leaderboard</div>
            <div class="leaderboard-subheader">Top 5 scores this session</div>
            <div id="leaderboardList" class="leaderboard-list">
                <div class="leaderboard-empty">
                    No scores yet.<br>
                    Play a round to set the board.
                </div>
            </div>
        </div>

        <div class="game-shell">

            <div class="top-box">
                <div class="top-center-group">
                    <div id="statusText" class="status-pill status-start">PRESS BEGIN</div>
                    <button class="button" onclick="restartGame()">RESTART</button>
                    <div class="chip">One Drag Only</div>
                    <div class="chip chip-alt">Ready Turns Green</div>
                </div>
            </div>

            <div id="playArea" class="play-area">
                <canvas id="gameCanvas"></canvas>

                <div class="decor-top-left">
                    <div class="decor-square blue"></div>
                    <div class="decor-square gold"></div>
                    <div class="decor-square green"></div>
                </div>

                <div class="mini-legend">
                    <div class="legend-item">Trust your eye</div>
                    <div class="legend-item">Aim for symmetry</div>
                </div>

                <div class="corner-design">
                    <span>Square target</span>
                    <div class="target-square"></div>
                </div>

                <div id="beginLayer" class="center-layer">
                    <div class="popup">
                        <h2>Square Off</h2>
                        <button class="button" onclick="beginGame()">BEGIN</button>
                        <p>Click, drag, release, then submit.</p>
                    </div>
                </div>

                <div id="readyLayer" class="center-layer hidden">
                    <div class="popup">
                        <h2>READY?</h2>
                        <div class="button-row">
                            <button class="button" onclick="submitRectangle()">SUBMIT</button>
                            <button class="button" onclick="restartGame()">RESTART</button>
                        </div>
                    </div>
                </div>

                <div id="calculatingLayer" class="center-layer hidden">
                    <div class="popup">
                        <h2>Calculating...</h2>
                        <p>Checking how close your shape is to a perfect square.</p>
                    </div>
                </div>

                <div id="resultLayer" class="center-layer hidden">
                    <div class="popup">
                        <h2>Your Score</h2>

                        <div id="scoreCircle" class="score-circle">
                            <div id="scoreInner" class="score-inner">0.00%</div>
                        </div>

                        <div id="scoreDetails" class="score-details"></div>

                        <div id="restartLate" class="restart-late hidden">
                            <button class="button" onclick="restartGame()">RESTART</button>
                        </div>
                    </div>
                </div>
            </div>

            <div class="bottom-design">
                <div class="dot"></div>
                <div class="dot gold"></div>
                <div class="bottom-text">Square Off</div>
                <div class="dot green"></div>
                <div class="dot red"></div>
            </div>

        </div>

    </div>

</div>

<script>
    const canvas = document.getElementById("gameCanvas");
    const ctx = canvas.getContext("2d");

    const playArea = document.getElementById("playArea");
    const statusText = document.getElementById("statusText");

    const beginLayer = document.getElementById("beginLayer");
    const readyLayer = document.getElementById("readyLayer");
    const calculatingLayer = document.getElementById("calculatingLayer");
    const resultLayer = document.getElementById("resultLayer");
    const restartLate = document.getElementById("restartLate");

    const scoreCircle = document.getElementById("scoreCircle");
    const scoreInner = document.getElementById("scoreInner");
    const scoreDetails = document.getElementById("scoreDetails");

    const leaderboardList = document.getElementById("leaderboardList");

    let gameStarted = false;
    let isDragging = false;

    let startX = 0;
    let startY = 0;
    let currentX = 0;
    let currentY = 0;

    let finalRectangle = null;
    let isReady = false;

    let leaderboardScores = [];


    function resizeCanvas() {
        const rect = playArea.getBoundingClientRect();
        const ratio = window.devicePixelRatio || 1;

        canvas.width = rect.width * ratio;
        canvas.height = rect.height * ratio;

        ctx.setTransform(ratio, 0, 0, ratio, 0, 0);

        redrawCanvas();
    }


    function getMousePosition(event) {
        const rect = canvas.getBoundingClientRect();

        return {
            x: event.clientX - rect.left,
            y: event.clientY - rect.top
        };
    }


    function getPlayAreaInfo() {
        const rect = canvas.getBoundingClientRect();

        return {
            width: rect.width,
            height: rect.height,
            area: rect.width * rect.height,
            minimumArea: (rect.width * rect.height) / 6
        };
    }


    function normalizeRectangle(x1, y1, x2, y2) {
        return {
            x: Math.min(x1, x2),
            y: Math.min(y1, y2),
            width: Math.abs(x2 - x1),
            height: Math.abs(y2 - y1)
        };
    }


    function setStatusStart() {
        statusText.textContent = "PRESS BEGIN";
        statusText.className = "status-pill status-start";
    }


    function setStatusTooSmall() {
        statusText.textContent = "TOO SMALL";
        statusText.className = "status-pill status-small";
    }


    function setStatusReady() {
        statusText.textContent = "READY";
        statusText.className = "status-pill status-ready";
    }


    function updateReadiness(rectangle) {
        const play = getPlayAreaInfo();
        const rectangleArea = rectangle.width * rectangle.height;

        if (rectangleArea >= play.minimumArea) {
            isReady = true;
            setStatusReady();
        } else {
            isReady = false;
            setStatusTooSmall();
        }
    }


    function clearCanvas() {
        const rect = canvas.getBoundingClientRect();
        ctx.clearRect(0, 0, rect.width, rect.height);

        if (gameStarted) {
            drawGuideText();
        }
    }


    function drawGuideText() {
        const rect = canvas.getBoundingClientRect();

        ctx.save();
        ctx.fillStyle = "#777777";
        ctx.font = "16px Arial";
        ctx.textAlign = "center";
        ctx.fillText("Click and drag to draw your rectangle", rect.width / 2, 34);
        ctx.restore();
    }


    function drawRectangle(rectangle) {
        clearCanvas();

        ctx.save();
        ctx.fillStyle = "rgba(45, 105, 180, 0.20)";
        ctx.strokeStyle = "#1f5fa8";
        ctx.lineWidth = 3;

        ctx.fillRect(rectangle.x, rectangle.y, rectangle.width, rectangle.height);
        ctx.strokeRect(rectangle.x, rectangle.y, rectangle.width, rectangle.height);

        ctx.restore();
    }


    function redrawCanvas() {
        if (finalRectangle) {
            drawRectangle(finalRectangle);
        } else {
            clearCanvas();
        }
    }


    function beginGame() {
        gameStarted = true;
        isDragging = false;
        finalRectangle = null;
        isReady = false;

        beginLayer.classList.add("hidden");
        readyLayer.classList.add("hidden");
        calculatingLayer.classList.add("hidden");
        resultLayer.classList.add("hidden");
        restartLate.classList.add("hidden");

        setStatusTooSmall();
        clearCanvas();
    }


    function restartGame() {
        gameStarted = false;
        isDragging = false;
        finalRectangle = null;
        isReady = false;

        beginLayer.classList.remove("hidden");
        readyLayer.classList.add("hidden");
        calculatingLayer.classList.add("hidden");
        resultLayer.classList.add("hidden");
        restartLate.classList.add("hidden");

        setStatusStart();
        clearCanvas();
    }


    function updateLeaderboard(score) {
        leaderboardScores.push(score);
        leaderboardScores.sort(function(a, b) {
            return b - a;
        });
        leaderboardScores = leaderboardScores.slice(0, 5);
        renderLeaderboard();
    }


    function renderLeaderboard() {
        if (leaderboardScores.length === 0) {
            leaderboardList.innerHTML = `
                <div class="leaderboard-empty">
                    No scores yet.<br>
                    Play a round to set the board.
                </div>
            `;
            return;
        }

        let html = "";

        leaderboardScores.forEach(function(score, index) {
            html += `
                <div class="leaderboard-item">
                    <span class="leaderboard-rank">#${index + 1}</span>
                    <span class="leaderboard-score">${score.toFixed(2)}%</span>
                </div>
            `;
        });

        leaderboardList.innerHTML = html;
    }


    canvas.addEventListener("mousedown", function(event) {
        if (!gameStarted) {
            return;
        }

        if (!readyLayer.classList.contains("hidden")) {
            return;
        }

        isDragging = true;

        const position = getMousePosition(event);

        startX = position.x;
        startY = position.y;
        currentX = position.x;
        currentY = position.y;

        finalRectangle = null;
        readyLayer.classList.add("hidden");

        const rectangle = normalizeRectangle(startX, startY, currentX, currentY);
        drawRectangle(rectangle);
        updateReadiness(rectangle);
    });


    canvas.addEventListener("mousemove", function(event) {
        if (!gameStarted || !isDragging) {
            return;
        }

        const position = getMousePosition(event);

        currentX = position.x;
        currentY = position.y;

        const rectangle = normalizeRectangle(startX, startY, currentX, currentY);

        finalRectangle = rectangle;

        drawRectangle(rectangle);
        updateReadiness(rectangle);
    });


    canvas.addEventListener("mouseup", function(event) {
        if (!gameStarted || !isDragging) {
            return;
        }

        isDragging = false;

        const position = getMousePosition(event);

        currentX = position.x;
        currentY = position.y;

        const rectangle = normalizeRectangle(startX, startY, currentX, currentY);

        finalRectangle = rectangle;

        drawRectangle(rectangle);
        updateReadiness(rectangle);

        if (isReady) {
            readyLayer.classList.remove("hidden");
        }
    });


    canvas.addEventListener("mouseleave", function() {
        if (!gameStarted || !isDragging) {
            return;
        }

        isDragging = false;

        if (finalRectangle) {
            drawRectangle(finalRectangle);
            updateReadiness(finalRectangle);

            if (isReady) {
                readyLayer.classList.remove("hidden");
            }
        }
    });


    function submitRectangle() {
        if (!finalRectangle || !isReady) {
            return;
        }

        readyLayer.classList.add("hidden");
        calculatingLayer.classList.remove("hidden");

        setTimeout(function() {
            calculatingLayer.classList.add("hidden");
            showScore();
        }, 2000);
    }


    function getScoreColor(score) {
        if (score >= 90) {
            return "#0b7a20";
        }

        if (score >= 80) {
            return "#d4b000";
        }

        if (score >= 70) {
            return "#d96b00";
        }

        return "#b00020";
    }


    function getScoreMessage(score) {
        if (score >= 98) {
            return "Almost perfect.";
        }

        if (score >= 90) {
            return "Excellent square feel.";
        }

        if (score >= 80) {
            return "Very solid attempt.";
        }

        if (score >= 70) {
            return "Pretty close.";
        }

        if (score >= 60) {
            return "A bit off, but not bad.";
        }

        return "Give it another shot.";
    }


    function showScore() {
        const width = finalRectangle.width;
        const height = finalRectangle.height;

        const largerSide = Math.max(width, height);
        const userRectangleArea = width * height;
        const targetSquareArea = largerSide * largerSide;

        let score = 0;

        if (targetSquareArea > 0) {
            score = (userRectangleArea / targetSquareArea) * 100;
        }

        const scoreDisplay = score.toFixed(2);
        const scoreColor = getScoreColor(score);
        const fillDegrees = (score / 100) * 360;

        scoreCircle.style.background =
            "conic-gradient(from -90deg, " +
            scoreColor +
            " 0deg " +
            fillDegrees +
            "deg, #dddddd " +
            fillDegrees +
            "deg 360deg)";

        scoreInner.textContent = scoreDisplay + "%";
        scoreInner.style.color = scoreColor;

        scoreDetails.innerHTML =
            getScoreMessage(score) + "<br>" +
            "Can you make it even closer next round?";

        updateLeaderboard(score);

        resultLayer.classList.remove("hidden");

        setTimeout(function() {
            restartLate.classList.remove("hidden");
        }, 5000);
    }


    window.addEventListener("resize", resizeCanvas);

    resizeCanvas();
    renderLeaderboard();
    restartGame();
</script>

</body>
</html>
"""


##### Step Three: Render Game #####

components.html(game_code, height=920)