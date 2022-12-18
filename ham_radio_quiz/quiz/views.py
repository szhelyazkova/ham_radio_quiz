from django.core.paginator import Paginator
from django.db.models import Min
from django.views import generic as views
from django.shortcuts import render, get_object_or_404

from ham_radio_quiz.core.utils import get_correct_answer, get_answers, \
    get_categories_names, get_skill_levels, get_random_question
from ham_radio_quiz.quiz.models import Answer, Question


class IndexView(views.View):
    template_name = 'index.html'

    def get(self, request):
        categories_names = get_categories_names()
        context = {
            'categories': categories_names,
        }
        return render(request, self.template_name, context)


class ShowQuestionsByCategoryView(views.DetailView):
    template_name = 'quiz/categories.html'
    model = Question

    def get(self, request, *args, **kwargs):
        chosen_category = kwargs['category']
        questions = Question.objects\
            .filter(category=chosen_category)\
            .order_by('-amateur_class').all()

        paginator = Paginator(questions, 2)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        paginated_questions = paginator.page(page_number)

        context = {
            'chosen_category': chosen_category,
            'questions': paginated_questions,
            'skill_levels': get_skill_levels(),
            'page_obj': page_obj,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        chosen_level = request.POST.get('choice', False)
        chosen_category = kwargs['category']
        not_chosen_categories = [category for category in get_categories_names() if category != chosen_category]

        if chosen_level:
            questions = Question.objects \
                .filter(category=chosen_category) \
                .filter(amateur_class=chosen_level).all()
        else:
            questions = Question.objects \
                .filter(category=chosen_category) \
                .order_by('-amateur_class').all()

        context = {
            'chosen_category': chosen_category,
            'questions': questions,
            'not_chosen_categories': not_chosen_categories,

        }
        return render(request, self.template_name, context)


class ShowAnswersView(views.DetailView):
    template_name = 'quiz/answers.html'

    def get(self, request, *args, **kwargs):
        question_id = kwargs['question_pk']
        answers = get_answers(question_id)
        question = get_object_or_404(Question, pk=question_id)
        correct_answer = get_correct_answer(answers)
        level = question.amateur_class
        category = question.category
        next_question = Question.objects\
            .filter(amateur_class=level)\
            .filter(category=category)\
            .filter(id__gt=question_id)\
            .order_by('pk').first()
        if not next_question:
            next_question_id = Question.objects\
                .filter(amateur_class=level)\
                .filter(category=category)\
                .aggregate(Min('pk'))['pk__min']
            next_question = get_object_or_404(Question, pk=next_question_id)
        context = {
            'question': question,
            'answers': answers,
            'correct_answer': correct_answer,
            'next_question': next_question.pk
        }
        return render(request, self.template_name, context)


class RandomQuestionView(views.View):
    template_name = 'quiz/question.html'

    def get(self, request):
        answers, id_q = self._get_random_question_with_answers()
        if not id_q:
            question = None
        else:
            question = get_object_or_404(Question, pk=id_q)
        context = {
            'question': question,
            'answers': answers,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        given_answer_id = request.POST.get('choice', False)
        correct_answer = ''
        given_answer_is_correct = None
        if given_answer_id:
            correct_answer, given_answer_is_correct, message = \
                self._check_if_answer_is_correct(given_answer_id)
        else:
            message = 'You did not choose an answer!'
        context = {
            'message': message,
            'correct_answer': correct_answer,
            'given_answer_is_correct': given_answer_is_correct,
            'is_answer': True,
            }
        return render(request, self.template_name, context)

    @staticmethod
    def _get_random_question_with_answers():
        random_question_id = get_random_question()
        answers = get_answers(random_question_id)
        return answers, random_question_id

    @staticmethod
    def _check_if_answer_is_correct(given_answer_id):
        answer = get_object_or_404(Answer, pk=given_answer_id)
        correct_answer = ''
        if answer.is_correct:
            given_answer_is_correct = True
            message = 'Your answer is correct!'
        else:
            given_answer_is_correct = False
            current_answers = Answer.objects.filter(question_id=answer.question_id).all()
            correct_answer = get_correct_answer(current_answers)
            message = 'Your answer is not correct. The correct answer is:'

        return correct_answer, given_answer_is_correct, message
