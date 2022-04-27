from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from .forms import UserForm


class UserUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'user_update.html'
    form_class = UserForm
    login_url = '/admin/'
    redirect_field_name = 'user_update'
#    raise_exception = False


    def get_object(self, **kwargs):
        return self.request.user

