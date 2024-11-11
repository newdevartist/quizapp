python
import random

class Quiz:
    def __init__(self):
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
                "answer": "C"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
                "answer": "B"
            },
            {
                "question": "Who wrote 'To Kill a Mockingbird'?",
                "options": ["A) Harper Lee", "B) Mark Twain", "C) J.K. Rowling", "D) Ernest Hemingway"],
                "answer": "A"
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
                "answer": "D"
            },
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["A) Au", "B) Ag", "C) Pb", "D) Fe"],
                "answer": "A"
            }
        ]
        self.score = 0
        self.total_questions = len(self.questions)

    def ask_question(self, question_data):
        print(question_data["question"])
        for option in question_data["options"]:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        return answer

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("Correct!\n")
            self.score += 1
        else:
            print(f"Wrong! The correct answer was {correct_answer}.\n")

    def review_answers(self, user_answers):
        print("\nReview your answers:")
        for i, question_data in enumerate(self.questions):
            print(f"{question_data['question']}")
            print(f"Your answer: {user_answers[i]}")
            print(f"Correct answer: {question_data['answer']}\n")

    def start_quiz(self):
        user_answers = []
        random.shuffle(self.questions)

        for question in self.questions:
            user_answer = self.ask_question(question)
            user_answers.append(user_answer)
            self.check_answer(user_answer, question["answer"])

        print(f"Quiz finished! Your score: {self.score}/{self.total_questions}")
        self.review_answers(user_answers)

def main():
    quiz_app = Quiz()
    while True:
        quiz_app.start_quiz()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()