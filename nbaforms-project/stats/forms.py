from django import forms
from .models import Player, Stat

# --------------------------- Form: Version A ---------------------------
# class StatForm(forms.Form):
    # --------------------------- Various Widgets ---------------------------
    # player = forms.CharField(label='Player', max_length=100, widget=forms.PasswordInput)
    # player = forms.CharField(label='Player', max_length=100, widget=forms.Textarea)
    # stats = forms.MultipleChoiceField(choices=[('Points', 'Points'), 
    #                                             ('FG%', 'FG%'),
    #                                             ('3P%', '3P%'),
    #                                             ('Assists', 'Assists'),
    #                                             ('Rebounds', 'Rebounds')],
    #                                             widget=forms.CheckboxSelectMultiple)

    # player = forms.CharField(label='Player', max_length=100)
    # stat   = forms.ChoiceField(label='Stat', choices=[('Points', 'Points'), 
    #                                                   ('FG%', 'FG%'),
    #                                                   ('3P%', '3P%'),
    #                                                   ('Assists', 'Assists'),
    #                                                   ('Rebounds', 'Rebounds')
    #                                                  ])

# --------------------------- Form: Version B ---------------------------
class StatForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ['player', 'stat']
        labels = {'player':'Player'}

        # --------------------------- Various Widgets ---------------------------
        # widgets = {'player':forms.Textarea}
        # widgets = {'stat':forms.CheckboxSelectMultiple}

        # --------------------------- Various Fiels ---------------------------
        # email = forms.EmailField()
        # url = forms.URLField()

class MultipleStatsForms(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=20)
