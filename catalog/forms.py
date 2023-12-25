from django import forms

from catalog.models import Product, Version


class FormStyleMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(FormStyleMixin, forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('creation_date', 'change_date', 'created_by')

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


class VersionForm(FormStyleMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["is_current"].widget.attrs.update({"class": "form-check"})

    class Meta:
        model = Version
        fields = '__all__'
