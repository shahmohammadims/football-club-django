from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class ProfileView(TemplateView):
    template_name = 'account/profile.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('account:login')
        if not request.user.view_profile:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)