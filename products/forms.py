from django import forms

from .models import Product

class ProductForm (forms.ModelForm):

    #overriding the definition of title, description in the class meta.
    title = forms.CharField(
                    label = '',
                    widget = forms.TextInput(attrs ={"placeholder": "Your Title"}))
    description = forms.CharField(
                        required = False,
                        widget = forms.Textarea(
                            attrs = {
                                "placeholder": "Your Desc",
                                "class": "new-class_name two",
                                "id": "my-id-for-textarea",
                                "rows" : 20,
                                "colums": 100
                            }
                        ))
    price = forms.DecimalField(initial = 50)

    class Meta:
        model=Product
        fields = ['title',
                  'description',
                  'price' ,
                  'summary']

    def clean_title(self, *args, **kwargs): #clean_<my_field>
        title = self.cleaned_data.get("title")
        if not "X" in title:
            raise forms.ValidationError ("Not a valid Title; Must Contain 'X'")
        return title




class RawProductForm (forms.Form):
    title = forms.CharField(label = '', widget = forms.TextInput(attrs ={"placeholder": "Your Title"}))  #textfield not possible; charfield
    description = forms.CharField(
                        required = False,
                        widget = forms.Textarea(
                            attrs = {
                                "placeholder": "Your Desc",
                                "class": "new-class_name two",
                                "id": "my-id-for-textarea",
                                "rows" : 20,
                                "colums": 100
                            }
                        ))
    price = forms.DecimalField(initial = 50)
