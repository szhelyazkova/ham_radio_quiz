from django.contrib.auth import get_user_model
from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic as views

from ham_radio_quiz.core.utils import get_categories_names, get_random_question, get_skill_levels
from ham_radio_quiz.examination.core.utils import get_left_questions
from ham_radio_quiz.examination.models import ExamModel, GeneratedQuestionsModel, ExamResultsModel
from ham_radio_quiz.quiz.models import Question, Answer

UserModel = get_user_model()

QUESTIONS_NUMBER = 4
PASS_EXAM_POINTS = int(0.8 * QUESTIONS_NUMBER)


class ExamGenerateView(auth_mixins.LoginRequiredMixin, views.View):

    template_name = 'examination/exam-generate.html'
    model = ExamModel, UserModel
    fields = '__all__'

    level = ''
    user_id = None

    def get(self, request):
        self.user_id = request.user.pk
        self.level = request.GET.get('choice', False)

        exams = GeneratedQuestionsModel.objects.filter(user_generated_id_id=self.user_id).all()
        if exams:
            [exam.delete() for exam in exams]

        is_generated = False

        if self.level:
            exam, is_generated = self._generate_quiz()
            GeneratedQuestionsModel.objects.create(
                user_generated_id_id=self.user_id,
                questions_list=exam,
            )

        context = {
            'is_generated': is_generated,
            'skill_levels': get_skill_levels(),
            'chosen_level': self.level,
            'needed_correct_answers': PASS_EXAM_POINTS,
            'question_number': QUESTIONS_NUMBER,
        }
        return render(request, self.template_name, context)

    def _collect_questions_pk_in_dict_by_categories(self):
        questions_by_category = {}
        categories_names = get_categories_names()
        for name in categories_names:
            questions = Question.objects.filter(category=name).filter(amateur_class=self.level)
            if questions:
                questions_by_category[name] = []
                for question in questions:
                    questions_by_category[name].append(question.pk)
        return questions_by_category

    def _generate_quiz(self):

        questions_counter = 0
        questions_by_category_dict = self._collect_questions_pk_in_dict_by_categories()
        available_questions_number = sum(len(value) for value in questions_by_category_dict.values())
        all_generated_question_id = []

        if available_questions_number < QUESTIONS_NUMBER:
            is_generated = False

        else:
            while questions_counter < QUESTIONS_NUMBER:
                for name in questions_by_category_dict.keys():
                    if questions_counter == QUESTIONS_NUMBER:
                        break
                    if questions_by_category_dict[name]:
                        generated_question_id = get_random_question(name, self.level, questions_by_category_dict[name])
                        all_generated_question_id.append(generated_question_id)
                        questions_counter += 1
                        questions_by_category_dict[name].remove(generated_question_id)

            is_generated = True
        return ','.join(str(x) for x in all_generated_question_id), is_generated


class ExamSolvingView(auth_mixins.LoginRequiredMixin, views.View):
    template_name = 'examination/exam-solving.html'
    model = ExamModel, UserModel, Question

    def get(self, request):
        user_id = request.user.pk
        exam = GeneratedQuestionsModel.objects.filter(user_generated_id_id=user_id).first()
        question, answers, exam = get_left_questions(exam)
        exam.save()

        context = {
            'question': question,
            'answers': answers,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        user_id = request.user.pk
        given_answer = request.POST.get('choice', False)
        question_id = request.POST.get('question')

        ExamModel.objects.create(
            user_test_id=user_id,
            user_test_question_id=question_id,
            user_test_answer_id=given_answer,
        )
        exam = GeneratedQuestionsModel.objects.filter(user_generated_id_id=user_id).first()
        if not exam.questions_list:
            exam.delete()
            return redirect('points exam')
        else:
            question, answers, exam = get_left_questions(exam)
            exam.save()

        context = {
            'question': question,
            'answers': answers,
        }

        return render(request, self.template_name, context)


class ExamPointsView(auth_mixins.LoginRequiredMixin, views.View):

    template_name = 'examination/exam-points.html'
    model = ExamModel, Answer, UserModel

    def get(self, request):
        user_id = request.user.pk
        correct_answers = 0
        wrong_answers = 0

        given_answers = ExamModel.objects.filter(user_test_id=user_id)
        if given_answers:
            for given_answer in given_answers:
                if given_answer.user_test_answer_id:
                    answer = get_object_or_404(Answer, pk=given_answer.user_test_answer_id)
                    if answer.is_correct:
                        correct_answers += 1
                    else:
                        wrong_answers += 1
                given_answer.delete()

            not_answered = QUESTIONS_NUMBER - correct_answers - wrong_answers

            exam_is_passed = True if correct_answers >= PASS_EXAM_POINTS else False
            ExamResultsModel.objects.create(
                user_exam_id=user_id,
                exam_is_passed=exam_is_passed,
                points=correct_answers,
            )
            context = {
                'correct_answers': correct_answers,
                'wrong_answers': wrong_answers,
                'exam_is_passed': exam_is_passed,
                'not_answered': not_answered,
                'needed_correct_answers': PASS_EXAM_POINTS,
            }
        else:
            context = {
                'message': "No results",
            }
        return render(request, self.template_name, context)


class ExamResultsView(auth_mixins.LoginRequiredMixin, views.View):
    template_name = 'examination/exam-result.html'
    model = ExamResultsModel

    def get(self, request, **kwargs):
        user_id = request.user.pk
        results = ExamResultsModel.objects.filter(user_exam=user_id).all()
        context = {
            'results': results,
            'user_id': user_id,
        }
        return render(request, self.template_name, context)
