# Space War Game 🚀

> **A fast-paced, retro-style 2-player local spaceship shooter built with Python and Pygame.**

---

## 1. Overview
**Space War Game** is a competitive 1v1 arcade shooter where two players battle it out on a single screen. Piloting custom spaceships, players must dodge incoming fire while trying to deplete their opponent's health. The game features smooth movement, sound effects, and a simple but addictive gameplay loop.

**Why it exists**: This project serves as a fun demonstration of game development concepts using Python's `pygame` library, organized with a professional, scalable architecture.

**Main Technologies**:
*   **Python**: Core programming language.
*   **Pygame**: Library for game development (graphics, sound, input).

---

## 2. Key Features
*   **Local Multiplayer**: Two players can play simultaneously on the same keyboard.
*   **Health System**: Each player starts with 5 health points.
*   **Sound Effects**: Immersive audio for shooting and impacts.
*   **Win Detection**: Automatic game-over state announcing the winner (Red or Yellow).
*   **Optimized Performance**: Runs smoothly at 60 FPS.
*   **Modular Codebase**: Clean separation of concerns (Entities, Systems, UI).

---

## 3. Architecture Overview
The project has been refactored into a modern, modular structure to ensure scalability and maintainability.

### **Folder Structure**
```
War_Game_py/
├── assets/          # Raw asset files (images, sounds)
├── docs/            # Documentation and visual assets
│   └── images/      # Screenshots
├── src/             # Source Code
│   ├── core/        # Core game loop and initialization
│   ├── entities/    # Game objects (Spaceship, Bullet)
│   ├── managers/    # Resource management (AssetManager)
│   ├── systems/     # Logic systems (Collision)
│   ├── ui/          # Rendering and interface
│   └── config.py    # Global constants and configuration
├── main.py          # Application entry point
└── README.md        # Project documentation
```

### **Core Components**
*   **`src/core/game.py`**: The heart of the application. It manages the game loop, events, and component coordination.
*   **`src/entities/`**: Contains the `Spaceship` class, encapsulating state (position, health, bullets) and movement logic.
*   **`src/systems/collision.py`**: Handles the physics of bullet impacts.
*   **`src/managers/asset_manager.py`**: A singleton handles loading and providing access to images and sounds, ensuring resources are loaded once.
*   **`src/ui/renderer.py`**: Decouples the drawing logic from the game state, handling all screen updates.

---

## 4. Requirements
### **Hardware**
*   **CPU**: Any modern dual-core processor.
*   **RAM**: 2GB+ recommended.
*   **Graphics**: Integrated graphics or better.
*   **Audio**: Speakers or headphones.

### **Software**
*   **OS**: Windows 10/11, macOS, or Linux.
*   **Python**: Version 3.6 or higher.
*   **Dependencies**: `pygame`.

---

## 5. Installation Instructions

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/Start-Tech-Academy/War_Game_py.git
cd War_Game_py
```

### **Step 2: Install Python**
Ensure Python is installed:
```bash
python --version
```

### **Step 3: Install Dependencies**
```bash
pip install pygame
```

---

## 6. Usage Guide

### **Launch the Game**
Run the main script from the root directory:
```bash
python main.py
```

### **Gameplay Controls**
| Feature | **Yellow Spaceship (Left)** | **Red Spaceship (Right)** |
| :--- | :--- | :--- |
| **Movement** | `W`, `A`, `S`, `D` Keys | `↑`, `↓`, `←`, `→` Arrow Keys |
| **Shoot** | `Left Ctrl` | `Right Ctrl` |
| **Health** | Displayed on Top-Left | Displayed on Top-Right |

**Objective**: Shoot your opponent 5 times to win!

![Game Screenshot](./docs/images/Screenshot%20from%202023-08-19%2011-23-05.png)

---

## 7. Configuration Options
Game constants can be easily adjusted in `src/config.py`:

| Variable | Default | Description |
| :--- | :--- | :--- |
| `WIDTH`, `HEIGHT` | `1200`, `600` | Resolution of the game window. |
| `FPS` | `60` | Target frames per second. |
| `VEL` | `5` | Spaceship speed. |
| `MAX_BULLETS` | `4` | Max bullets per player. |

---

## 8. Testing
To verify the installation and code integrity:

1.  **Launch the game**: `python main.py`
2.  **Check Console**: Ensure no "Asset not found" warnings appear.
3.  **Play**: Test movement and shooting for both players.

---

## 9. Contributing
Contributions are welcome! Please follow the folder structure conventions when adding new features.

1.  **Logic**: Place new logic in `src/systems/` or `src/core/`.
2.  **Entities**: New game objects go in `src/entities/`.
3.  **Assets**: Add new files to `assets/` and register them in `src/managers/asset_manager.py`.

---

## 10. License
Distributed under the **MIT License**.

---

## 11. Credits
*   **Developer**: Yossef (yossefsabry66@gmail.com) - forked from yossefsabry/War_Game_py
*   **Refactoring**: Updated to modular architecture by Antigravity.
