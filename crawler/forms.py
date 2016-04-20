from django import forms

class KeywordForm(forms.Form):
    keyword = forms.CharField(max_length=100, widget=forms.TextInput)
    def test(self):
        pass
