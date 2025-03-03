from django.shortcuts import render
from .forms import MyForm


def main_view(request):
    return render(request, 'authorization/main_page.html')


def my_form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            data = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'gender': form.cleaned_data['gender'],
                'subscribe': form.cleaned_data['subscribe'],
                'message': form.cleaned_data['message'],
            }
            return render(request, 'authorization/my_form.html', {'form': form, 'data': data})
    else:
        form = MyForm()

    return render(request, 'authorization/my_form.html', {'form': form})