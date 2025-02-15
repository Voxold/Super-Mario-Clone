# Super Mario Clone

This is a clone of the classic Super Mario game, implemented in Python. The project is structured with a clear separation of assets and source code, and includes a virtual environment setup for managing dependencies.

## Project Structure

- **assets/**: This directory contains all the images and sound files required for the game.
- **src/**: This directory contains the source code for the game.
  - **game.py**: Contains the main game logic.
  - **platform.py**: Contains the code for the platforms in the game.
  - **player.py**: Contains the code for the player character (Mario).
- **main.py**: The entry point for the game.
- **requirements.txt**: Lists all the dependencies required to run the game.

## Setup Instructions

### 1. Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/voxold/super_mario_clone.git
cd super_mario_clone
```



Create a virtual environment to manage the project dependencies:

```bash
python -m venv venv
```

### 3. Create a Virtual Environment

Activate the virtual environment:

  - On Windows:
    ```bash
    .\venv\Scripts\activate
    ```
    
  - On macOS/Linux:
    ```bash
    source venv/bin/activate
    ```

### 4. Install Dependencies

Install the required dependencies using `pip`:

```bash
  pip install -r requirements.txt
```


### 5. Run the Game

Execute the game by running the `main.py` file:


```bash
  python main.py
```

## Additional Information
Feel free to explore the src/ directory to understand how the game logic is implemented. The assets/ directory is where all the images and sound files are stored, ensuring that the game has the necessary visuals and audio effects to provide an engaging experience.

