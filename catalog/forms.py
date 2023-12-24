from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('creation_date', 'change_date')

    def clean_name(self):
        dame = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар')
        cleaned_data = self.cleaned_data['name']
        for word in dame:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Please don\'t sell bullshit here')
        return cleaned_data

    def clean_description(self):
        dame = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар')
        cleaned_data = self.cleaned_data['description']
        for word in dame:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Please don\'t sell bullshit here')
        return cleaned_data
