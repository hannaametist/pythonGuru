# src/quiz.py
import json
import random
import requests
from pathlib import Path


class QuizGame:
    def __init__(self):
        self.score = 0
        self.questions = self._load_questions()
        self.total_questions = len(self.questions)
        self.api_url = "https://opentdb.com/api.php"

    def _load_questions(self):
        # Get absolute path to the dir with data
        current_dir = Path(__file__).parent.parent
        file_path = current_dir / 'data' / 'quiz_questions.json'

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data["questions"]
        except FileNotFoundError:
            print(f"Error: File not found: {file_path}")
            exit(1)
        except json.JSONDecodeError:
            print("Error: Wrong file format (need JSON)")
            exit(1)

    def _fetch_api_questions(self, amount=5):
        # Fetch additional questions from the Open Trivia Database API
        params = {
            "amount": amount,
            "category": 18,  # Computer Science category
            "type": "multiple",
            "difficulty": "medium"
        }

        try:
            response = requests.get(self.api_url, params=params)
            response.raise_for_status()
            data = response.json()

            if data["response_code"] == 0:
                new_questions = []
                for q in data["results"]:
                    # Format API questions to match our structure
                    options = q["incorrect_answers"] + [q["correct_answer"]]
                    random.shuffle(options)
                    new_questions.append({
                        "question": q["question"],
                        "options": options,
                        "correct_answer": q["correct_answer"]
                    })
                print(f"\nУспішно завантажено {len(new_questions)} нових питань!")
                return new_questions
            else:
                print("Error: Failed to fetch questions from API")
                return []

        except requests.RequestException as e:
            print(f"Error: API connection failed: {e}")
            return []

    def run(self):
        print("\nЛаскаво просимо до Python Quiz!")
        print("\nОберіть режим гри:")
        print("1. Локальні питання")
        print("2. Онлайн питання")
        print("3. Змішаний режим")

        while True:
            try:
                mode = int(input("\nВаш вибір (1-3): "))
                if 1 <= mode <= 3:
                    break
                print("Будь ласка, введіть число від 1 до 3")
            except ValueError:
                print("Будь ласка, введіть число!")

        # Handle game mode selection
        if mode == 2:
            api_questions = self._fetch_api_questions()
            if api_questions:
                self.questions = api_questions
                self.total_questions = len(self.questions)
        elif mode == 3:
            api_questions = self._fetch_api_questions()
            if api_questions:
                self.questions.extend(api_questions)
                self.total_questions = len(self.questions)

        print(f"\nУ нас є {self.total_questions} питань для вас.")
        print("Для кожного питання оберіть номер правильної відповіді (1-4)")

        # Create a copy and shuffle questions for randomization
        random_questions = self.questions.copy()
        random.shuffle(random_questions)

        for i, question in enumerate(random_questions, 1):
            print(f"\nПитання {i} з {self.total_questions}:")
            print(question["question"])

            # Display answer options
            for j, option in enumerate(question["options"], 1):
                print(f"{j}. {option}")

            # Get and validate user input
            while True:
                try:
                    answer = int(input("\nВаша відповідь (1-4): "))
                    if 1 <= answer <= 4:
                        break
                    print("Будь ласка, введіть число від 1 до 4")
                except ValueError:
                    print("Будь ласка, введіть число!")

            # Evaluate user's answer
            user_answer = question["options"][answer - 1]
            if user_answer == question["correct_answer"]:
                print("Правильно! ✅")
                self.score += 1
            else:
                print(f"Неправильно! ❌")
                print(f"Правильна відповідь: {question['correct_answer']}")

        # Display final results
        self.show_results()

    def show_results(self):
        print("\n=== Результати гри ===")
        print(f"Правильних відповідей: {self.score} з {self.total_questions}")
        percentage = (self.score / self.total_questions) * 100
        print(f"Відсоток правильних відповідей: {percentage:.1f}%")

        # Оцінка результату
        if percentage == 100:
            print("Браво! Ну ти справжній Python-гуру! 🏆")
        elif percentage >= 80:
            print("Ух ти! Глибокі знання є, вважаємо тебе асистентом гуру! 🌟")
        elif percentage >= 60:
            print("Ну в принципі жити можна! Але є простір для вдосконалення! 📚")
        else:
            print("Оце ти лушпень! Варто приділити більше уваги навчанню! 💪")


if __name__ == "__main__":
    game = QuizGame()
    game.run()