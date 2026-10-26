# Deathon Internship Projects

Welcome to my **Deathon Internship Projects** repository! This repository contains Python projects developed during my internship to strengthen my programming, problem-solving, and practical development skills.

## Projects

### Task 1: Hangman Word Guessing Game

A console-based word guessing game where the player guesses a hidden word one letter at a time.

**Features**
- Random word selection
- Maximum of six incorrect attempts
- Tracks previously guessed letters
- Prevents repeated guesses from being penalized
- Displays win or lose messages
- Supports loading words from `words.txt`

**Technologies:** Python, `random`

**Run the project**
```bash
python hangman.py
```

### Task 2: Stock Portfolio Performance Tracker

A Python application that tracks stock holdings and calculates portfolio performance using entered stock details and price data.

**Features**
- Accepts stock ticker symbols, purchase prices, and share quantities
- Calculates investment values and gains or losses
- Processes portfolio information
- Saves a portfolio summary to `portfolio_summary.csv`

**Technologies:** Python, CSV, file handling

**Run the project**
```bash
python portfolio.py
```

*Note: Results depend on the stock prices and data supplied to the program.*

### Task 3: File Organizer

A utility that organizes files into folders based on their file types.

**Features**
- Identifies file extensions
- Sorts files into appropriate folders
- Reduces clutter in a directory

**Technologies:** Python, `os`, `shutil`

**Run the project**
```bash
python file_organizer.py
```

*Test with sample files first and keep a backup of important files.*

### Task 4: Rule-Based Interactive Terminal Assistant

A terminal-based chatbot that responds to greetings and answers internship-related frequently asked questions.

**Features**
- Recognizes common greetings
- Answers internship FAQs using a JSON dataset
- Responds to supported intents such as help and goodbye
- Loads FAQ data from `sample_faq.json`

**Technologies:** Python, JSON, rule-based intent matching

**Run the project**
```bash
python chatbot.py
```

Make sure `sample_faq.json` is in the same directory as `chatbot.py`.

## Project Structure

```text
Deathon-Internship-Projects/
├── hangman.py
├── words.txt
├── portfolio.py
├── file_organizer.py
├── chatbot.py
├── sample_faq.json
└── README.md
```

*The structure above is illustrative. Your actual files may differ depending on how each project is organized.*

## Requirements

- Python 3
- Visual Studio Code or another Python editor
- A terminal or command prompt

## How to Run

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Open the terminal in that folder.
4. Run the Python file for the task you want to try.

## Learning Outcomes

- Python fundamentals and control flow
- Functions and data structures
- File and CSV handling
- JSON data processing
- Basic data analysis and calculations
- Problem-solving and debugging
- Git and GitHub version control

## Author

Python Programming Internship Projects

## Repository

[View the projects on GitHub](https://github.com/Sitha-mounika/hangman-game)
