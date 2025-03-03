from django import forms


class MyForm(forms.Form):
    name = forms.CharField(label='Ваше имя', max_length=100, required=True)

    email = forms.EmailField(label='Ваш email', required=False)

    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский'),
    ]
    gender = forms.ChoiceField(label='Ваш пол', choices=GENDER_CHOICES, required=True)

    subscribe = forms.BooleanField(label='Подписаться на рассылку', required=False)

    message = forms.CharField(label='Ваше сообщение', widget=forms.Textarea, required=False)