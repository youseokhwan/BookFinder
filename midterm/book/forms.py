from django import forms


class BookSearchForm(forms.Form):
    keyword = forms.CharField(label='Keyword')
