from django import forms
class ArticleForm(forms.ModelForm):
    status = forms.ChoiceField(choices=(('draft', 'Draft'), ('published', 'Published')))