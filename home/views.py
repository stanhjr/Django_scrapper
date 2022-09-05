from django.shortcuts import render
from django.views.generic import TemplateView


class LoginPage(TemplateView):
    template_name = 'login.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     context['page'] = 'settings'

        # receive_news_initial = self.request.user.receive_news
        # receive_activity_initial = self.request.user.receive_activity
        # context['email_settings_form'] = EmailSettingsForm(
        #     receive_news_initial=receive_news_initial,
        #     receive_activity_initial=receive_activity_initial)
        #
        # context['password_change_form'] = CustomPasswordChangeForm(
        #     self.request.user)

        # return context
