from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model, login

from ham_radio_quiz.accounts.forms import UserCreateForm, UserBaseForm

UserModel = get_user_model()


class SignUpView(views.CreateView):
    template_name = 'accounts/user-create.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if self.object:
            login(request, self.object)
        return response


class SignInView(auth_views.LoginView):
    template_name = 'accounts/user-login.html'


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


class UserDetailsView(LoginRequiredMixin, views.DetailView):
    template_name = 'accounts/user-details.html'
    model = UserModel


class UserEditView(LoginRequiredMixin, views.UpdateView):
    template_name = 'accounts/user-edit.html'
    model = UserModel
    form_class = UserBaseForm

    def get_success_url(self):
        return reverse('user details', kwargs={'pk': self.kwargs['pk']})


class UserDeleteView(views.DeleteView):
    template_name = 'accounts/user-delete.html'
    model = UserModel

    def post(self, request, *args, **kwargs):
        k = request.POST
        if 'cancel' in request.POST:
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(UserDeleteView, self).post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('user details', kwargs={'pk': self.kwargs['pk']})
