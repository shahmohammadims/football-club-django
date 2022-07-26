from django.shortcuts import redirect
from django.views.generic import TemplateView
from exercise.models import Category

class ProfileView(TemplateView):
    template_name = 'account/profile.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('account:login')
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['category_list'] = Category.objects.all()
        return data