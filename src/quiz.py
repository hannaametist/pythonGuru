# src/quiz.py
import json
import random
from pathlib import Path


class QuizGame:
    def __init__(self):
        self.score = 0
        self.questions = self._load_questions()
        self.total_questions = len(self.questions)

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

    def run(self):
        print("\nЛаскаво просимо до Python Quiz!")
        print(f"У нас є {self.total_questions} питань для вас.")
        print("Для кожного питання оберіть номер правильної відповіді (1-4)")

        # Stir questions
        random_questions = self.questions.copy()
        random.shuffle(random_questions)

        for i, question in enumerate(random_questions, 1):
            print(f"\nПитання {i} з {self.total_questions}:")
            print(question["question"])

            # Show answer options
            for j, option in enumerate(question["options"], 1):
                print(f"{j}. {option}")

            # Get user answer
            while True:
                try:
                    answer = int(input("\nВаша відповідь (1-4): "))
                    if 1 <= answer <= 4:
                        break
                    print("Будь ласка, введіть число від 1 до 4")
                except ValueError:
                    print("Будь ласка, введіть число!")

            # Check answer
            user_answer = question["options"][answer - 1]
            if user_answer == question["correct_answer"]:
                print("Правильно! ✅")
                self.score += 1
            else:
                print(f"Неправильно! ❌")
                print(f"Правильна відповідь: {question['correct_answer']}")

        # Show result
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
            print("Ух ти! Глибокі знання Python є, асистент гуру! 🌟")
        elif percentage >= 60:
            print("Ну в принципі жити можна! Але є простір для вдосконалення! 📚")
        else:
            print("Оце ти лушпень! Варто приділити більше уваги вивченню Python! 💪")


if __name__ == "__main__":
    game = QuizGame()
    game.run()