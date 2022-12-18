import random

from ham_radio_quiz.quiz.models import Answer, Category, AmateurSkills, Question


def get_correct_answer(current_answers):
    current_correct_answer = ''
    for current_answer in current_answers:
        if current_answer.is_correct:
            current_correct_answer = current_answer.content
            break
    return current_correct_answer


def get_answers(q_id):
    answers = Answer.objects.filter(question_id=q_id).all()
    return answers


def get_categories_names():
    categories = Category.choices()
    categories_names = [category[0] for category in categories]
    return categories_names


def get_skill_levels():
    skills = AmateurSkills.choices()
    skill_levels = [skill[0] for skill in skills]
    return skill_levels


def get_random_question(category_name=None, level=None, questions_id_list=None):
    if category_name:
        questions = Question.objects.filter(amateur_class=level).filter(category=category_name)
    else:
        questions = Question.objects.all()
    if not questions:
        return None
    if not questions_id_list:
        questions_id_list = []
        for question in questions:
            questions_id_list.append(question.pk)
    random_question_id = random.choice(questions_id_list)
    return random_question_id
