from ham_radio_quiz.core.utils import get_answers
from ham_radio_quiz.quiz.models import Question


def get_left_questions(exam):

    question_ids_queue = exam.questions_list.strip('[]').split(',')
    question_id = int(question_ids_queue.pop(0).strip())
    answers = get_answers(question_id)
    question = Question.objects.filter(pk=question_id).get()
    exam.questions_list = ','.join(str(x) for x in question_ids_queue)
    return question, answers, exam
