# Python Quiz Game 🐍

A simple console quiz application to test your Python knowledge.

## Description

This quiz game helps you test and improve your Python programming knowledge through interactive questions. Questions cover various Python topics including syntax, data types, functions, and basic concepts.

## Features

- Multiple choice questions about Python
- Randomized question order
- Immediate feedback on answers
- Score tracking
- Final results with percentage and assessment
- Easy to add new questions

## Project Structure

```
pythonGuru/
├── src/
│   ├── __init__.py
│   └── quiz.py
└── data/
    └── quiz_questions.json
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/hannaametist/pythonGuru.git
cd pythonGuru
```

## How to Run

```bash
python3 src/quiz.py
```

## Adding New Questions

New questions can be added to `data/quiz_questions.json` in the following format:
```json
{
    "question": "Your question here?",
    "options": [
        "Option 1",
        "Option 2",
        "Option 3",
        "Option 4"
    ],
    "correct_answer": "Option 1"
}
```

## Author

- Hanna Ametist

## License

This project is open source and available under the MIT License.