from django import forms


class ProductCreateForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea())
    price = forms.IntegerField(min_value=1)


class ReviewCreateForm(forms.Form):
    text = forms.CharField(max_length=255)