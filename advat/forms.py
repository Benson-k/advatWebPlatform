from advat.choices import *
from datetimewidget.widgets import DateWidget
from django import forms
from .models import Post




class PostForm(forms.ModelForm):

    class Meta:
        model = Post

        location = forms.ChoiceField(choices = LOCATIONS, label="", initial='', widget=forms.Select(), required=True)
        category = forms.ChoiceField(choices = CATEGORIES, label="", initial='', widget=forms.Select(), required=True)
        widgets = {

            'start_date': DateWidget(attrs={'id':"start_date"}, usel10n = True, ),
            'end_date': DateWidget(attrs={'id':"end_date"}, usel10n = True, )
        }
        fields = ('sale_title', 'sale_description','category', 'start_date','end_date','location', 'address','banner')

