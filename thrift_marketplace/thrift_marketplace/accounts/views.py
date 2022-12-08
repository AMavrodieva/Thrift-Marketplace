from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_view, login, get_user_model
from django.urls import reverse_lazy
from django.views import generic as views

from thrift_marketplace.accounts.forms import AppCreateUserForm, AppLoginForm, AppChangeUserForm, AppDeleteUserForm

UserModel = get_user_model()


class AppSignUpUserView(views.CreateView):
    model = UserModel
    template_name = 'accounts/register-page.html'
    form_class = AppCreateUserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


class AppSignInUserView(auth_view.LoginView):
    template_name = 'accounts/login-page.html'
    form_class = AppLoginForm

    def get_success_url(self):
        return reverse_lazy('index')


class AppSignOutUserView(auth_view.LogoutView):
    next_page = reverse_lazy('index')


class HomePageView(LoginRequiredMixin, views.DetailView):
    template_name = 'accounts/profile-home-page.html'
    model = UserModel

    def dispatch(self, request, *args, **kwargs):
        super().dispatch(request, *args, **kwargs)
        if not self.object.pk == request.user.pk:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object

        return context


class AppDetailsUserView(LoginRequiredMixin, views.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel

    def dispatch(self, request, *args, **kwargs):
        super().dispatch(request, *args, **kwargs)
        if not self.object.pk == request.user.pk:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)


class AppEditUserView(LoginRequiredMixin, views.UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = UserModel
    form_class = AppChangeUserForm

    def dispatch(self, request, *args, **kwargs):
        super().dispatch(request, *args, **kwargs)
        if not self.object.pk == request.user.pk:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.object.pk,
        })


@login_required
def delete_user(request, pk):
    user = UserModel(pk=pk)
    if not user.pk == request.user.pk:
        return redirect('index')
    if request.method == "GET":
        form = AppDeleteUserForm(instance=user)
    else:
        form = AppDeleteUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'accounts/profile-delete-page.html', context)

