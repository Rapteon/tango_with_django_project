from django import forms
from rango.models import Page, Category


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.

    class Meta:
        # Provide an association between the ModelForm and a model

        model = Category
        fields = ("name",)


class PageForm(forms.ModelForm):
    title = forms.CharField(
        max_length=128, help_text="Please enter the title of the page."
    )
    url = forms.CharField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    def clean(self):
        # self.cleaned_data contains the cleaned data created by Django.
        cleaned_data = self.cleaned_data
        url = cleaned_data.get("url")

        # Cleaning the URL entered by the user, although this doesn't
        # seem to be the right way to fix it.
        if url and not url.startswith("http://"):
            url = f"http://{url}"
            cleaned_data["url"] = url

        # Returning cleaned_data dictionary is necessary for the changes to be applied.
        return cleaned_data

    class Meta:
        # Provide an association between the ModelForm and the Page
        model = Page
        # Specifying the fields we want to include in our form.

        # Add all fields except 'category'.
        exclude = ("category",)
        # You can also include specific fields only
        # using "fields = ('', '', '')"
