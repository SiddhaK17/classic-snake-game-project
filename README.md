# 🐍 Classic Snake Game Project
*A modern reimagining of the timeless Snake arcade classic, this project brings together clean Python programming, interactive graphics with `turtle`, and engaging gameplay mechanics. Built as a part of my Python learning journey, it blends nostalgia with structured, readable, and maintainable code, making it a great demonstration of event driven programming and modular design in Python.*

---

## 📌 Overview
The **Classic Snake Game Project** is a **modern, Python based reimagining** of the legendary Snake game that defined an era of mobile and arcade gaming.  
Built entirely with Python’s native `turtle` graphics module, this project showcases a **clean, modular, and object oriented approach** to game development with smooth gameplay, intelligent collision handling, and persistent high score tracking.

This version retains the nostalgic charm of the original game while integrating **well structured code architecture**, making it an **excellent demonstration of software design principles**.  
It is not just a fun project, it’s a showcase of **OOP mastery, game state management, and file handling** in Python.  

---

## ⚙️ Technologies & Concepts Used
The project incorporates **both programming best practices and real time graphics rendering techniques** to deliver a polished experience:  

- **💻 Programming Language:**  
  Developed in **Python 3.13**, leveraging its simplicity and versatility for game logic.

- **🎨 Graphics Engine:**  
  Built using Python’s built in `turtle` module, enabling smooth and responsive 2D rendering without external dependencies.

- **🏗 Object Oriented Programming (OOP):**  
  Classes are implemented for each game component (`Snake`, `Food`, `Scoreboard`) ensuring **encapsulation, modularity, and reusability**.

- **🧠 Game Logic & State Management:**  
  - Continuous game loop with controlled frame rate using `time.sleep()`.  
  - **Real time collision detection** for snake-to-food, snake-to-wall, and snake-to-self interactions.

- **🗂 File Handling for Data Persistence:**  
  High score stored in `data.txt`, ensuring player achievements are saved across sessions.

- **🖥 Cross Platform Compatibility:**  
  Environment variables (`TCL_LIBRARY` & `TK_LIBRARY`) configured for seamless execution on multiple OS setups.

---

## 🎮 Gameplay Mechanics
The gameplay has been crafted to be **fluid, engaging, and true to the original Snake experience**, with enhanced scoring and reset features:

1. **🔄 Snake Movement**
   - Controlled using **Arrow Keys**:
     - **⬆ Up Arrow** → Moves the snake upward
     - **⬇ Down Arrow** → Moves the snake downward
     - **⬅ Left Arrow** → Moves the snake left
     - **➡ Right Arrow** → Moves the snake right
   - Prevents **180° reverse turns** to maintain logical movement.

2. **🍏 Food Mechanics**
   - Food spawns at **randomized coordinates** within the playable grid.
   - Consuming food increases:
     - Snake length by one segment.
     - Score by **+1 point**.

3. **📊 Scoring System**
   - The **current score** updates dynamically with each food item eaten.
   - **High score** is stored in `data.txt` and loaded on startup.
   - If the current score exceeds the stored high score, it automatically updates.

4. **💥 Collision Handling**
   - **Wall Collision:** Snake resets to starting position, score resets to 0.
   - **Self Collision:** Touching the snake’s own body also triggers a reset.
   - **High Score Persistence:** Even after collisions, the highest score remains saved.

5. **⚡ Game Speed**
   - Balanced timing using `time.sleep()` for smooth, playable difficulty.
   - Designed for responsiveness without overwhelming speed.

---

## 📂 Project Structure

```
classic-snake-game-project/
    ├── main.py         # Entry point – initializes and runs the game loop
    ├── snake.py        # Snake class – handles creation, movement, and growth
    ├── food.py         # Food class – handles random spawning and rendering
    ├── scoreboard.py   # Scoreboard class – manages scoring and high score persistence
    ├── data.txt        # Stores the highest score between game sessions
    └── README.md       # Project documentation
    ├── snake_game_no_highscore.png
    ├── snake_game_with_highscore.png
```

---

### 🚀 How to Run

> ⚠️ Ensure you have **Python 3.10+** installed.

### Prerequisites
- Python 3.10 or above
- Compatible terminal or IDE (e.g., VS Code, PyCharm)

1. Install the required dependencies (if not already present):
   ```bash
   pip install turtle
   ```

2. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/classic-snake-game-project.git
   ```

3. **Navigate to the project folder**
   ```bash
   cd classic-snake-game-project
   ```

> 💡 **Optional – Windows Only:** If you encounter errors related to `TCL_LIBRARY` or `TK_LIBRARY`, ensure that your Python installation's Tcl paths are correctly set using `os.environ` at the beginning of your script:
   ```bash
   import os
   os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python313\tcl\tcl8.6'
   os.environ['TK_LIBRARY'] = r'C:\Program Files\Python313\tcl\tk8.6'
   ```

4. **Run the script**
   ```bash
   python main.py
   ```

---

## 📸 Sample Output  

Below are two snapshots showcasing the **Classic Snake Game** in action, highlighting the scoreboard with different high score states.  

### 🆕 First Launch — No High Score Yet (0)  
When you play for the very first time, the **High Score** will be `0`, waiting to be set.  
This is the perfect moment to claim your first record!  

![Snake Game - High Score 0](snake_game_no_highscore.png)  

---

### 🏆 Gameplay with Saved High Score  
Once you achieve a new high score, it is **automatically saved** and displayed in every future session.  
The scoreboard instantly reflects your achievement, motivating you to keep beating your personal best!  

![Snake Game - High Score Saved](snake_game_with_highscore.png)  

---

💾 **Note:** The high score is stored in the `data.txt` file, ensuring it persists across game sessions even after closing the program. Your high score will keep on updating as you break your own record!!

✨ *Tip:* The **persistent high score feature** ensures your best score is never lost, even after closing the game.  

---

## ✨ Key Highlights  

- **🎮 Immersive Retro Gameplay Experience** – Faithfully recreates the charm of the original Snake game while integrating smooth animations, crisp visuals, and highly responsive controls. Every movement feels fluid, with precise collision mechanics that mimic the classic arcade feel.  

- **📈 Persistent High Score Tracking** – Your top score is automatically saved in the `data.txt` file, ensuring that even after closing the program, your record remains intact. The game instantly reads and updates this file, allowing you to track your progress over time and strive for personal bests.  

- **⚡ Performance Optimized Execution** – Designed with Python’s `turtle` graphics library for lightweight yet visually appealing gameplay. The rendering loop and update intervals are tuned to balance speed and smoothness without causing frame drops or input lag.  

- **🛠 Modular and Scalable Architecture** – Organized into separate, purpose driven modules:
  - `snake.py` – Handles snake creation, movement, and growth mechanics.  
  - `food.py` – Controls random food placement and appearance.  
  - `scoreboard.py` – Manages score tracking, display, and high score persistence.  
  - `main.py` – The central game loop orchestrating all components.  
  This structure makes the code easy to read, debug, and extend with new features.  

- **🎯 Advanced Gameplay Mechanics** – Features realistic boundary collision logic, automatic reset upon losing, and self-collision detection to ensure fair gameplay. Snake growth is visually smooth and food spawning is carefully randomized to avoid overlapping game elements.  

- **🖥 Cross Platform Compatibility** – Works seamlessly on Windows, macOS, and Linux with Python 3.x installed. No additional dependencies are required beyond the standard Python library, making it easy to run anywhere.  

- **🎨 Minimalist Yet Engaging Visual Design** – Simple color schemes and clear on screen text enhance focus on gameplay while maintaining a polished, professional look.  

---

## 📜 Credits  

This project was developed as part of my learning journey through **"100 Days of Code: The Complete Python Pro Bootcamp" by Dr. Angela Yu**. The course provided the foundational concept and guidance for the Snake game, while I worked on implementing the solution, organizing the code, and refining the structure to achieve a clean, modular, and functional final product.  

The inclusion of features such as **persistent high score tracking**, **modular file separation**, and **polished README documentation** were added to enhance both **user experience** and **code readability**, transforming the project into a professional grade demonstration of beginner-to-intermediate Python skills.  

Special acknowledgment to the Python `turtle` graphics library for making the game’s graphical interface possible in a beginner friendly yet powerful way.  
