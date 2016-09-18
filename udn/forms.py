from django import forms
from django.forms import ModelForm
from udn.models import Participants


class ParticipantForm(forms.ModelForm):
    def clean_name(self):
        clean_name = self.cleaned_data['name']
        if not clean_name:
            raise forms.ValidationError("You have forgotten to add a Name")
        return clean_name

    class Meta:
        model = Participants
        exclude = ['review']


class ReviewForm(ModelForm):
    review = forms.ChoiceField(widget=forms.Select(attrs={"onChange": 'submit()'}), label='',
                               choices=Participants.REVIEW_CHOICES, required=False)

    def clean_review(self):
        review = self.cleaned_data['review']
        if review:
            review = dict(Participants.REVIEW_CHOICES).get(review)
        return review

    class Meta:
        model = Participants
        fields = ['review']
