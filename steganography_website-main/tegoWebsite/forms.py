from django import forms


class HideTextForm(forms.Form):
    image = forms.ImageField()
    text = forms.CharField(widget=forms.Textarea)
