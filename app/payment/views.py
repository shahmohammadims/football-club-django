from django.http import HttpResponse
from django.shortcuts import redirect , render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Payment

class IndexView(LoginRequiredMixin , TemplateView):
    template_name = 'payment/index.html'
    
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            if self.request.user.debt != 0:
                payment = Payment.objects.create(account=request.user , price=self.request.user.debt)
                payment.items.set(self.request.user.exercises_not_payment)
                payment.save()
                return render(request , 'payment/successfull.html')
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['price'] = self.request.user.debt
        return data