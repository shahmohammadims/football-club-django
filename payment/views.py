from django.shortcuts import redirect, render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'payment/index.html'
    
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('/')
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['price'] = self.request.POST['price']
        return data