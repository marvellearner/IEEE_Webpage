from django.shortcuts import render
from django.views.generic import View
from .models import Register
from .forms import Submit


# Create your views here.
def home(request):
    return render(request , 'register/home.html' , {})
class FormView(View):
    form_class = Submit
    template = "register/form.html"

    def get(self, request):
        form = self.form_class(None)
        context = {'form': form}
        return render(request, self.template, context)

    def post(self, request):
        form = self.form_class(request.POST)
        context = {'form': form,}
        if form.is_valid():
            obj = Register()
            obj.Name = form.cleaned_data['Name']
            obj.Email = form.cleaned_data['Email']
            obj.Mobile_number = form.cleaned_data['Mobile_number']
            obj.Address = form.cleaned_data['Address']
            obj.College = form.cleaned_data['College']
            obj.IEEE_mem_no = form.cleaned_data['IEEE_mem_no']
            obj.save()
            context = {
                'form': form,
                'message': "Thank You for Registering",
            }

        return render(request, self.template, context)
