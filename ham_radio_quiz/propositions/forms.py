from django import forms

from ham_radio_quiz.propositions.models import ProposedQuestionModel


class AddQuestionForm(forms.ModelForm):
    class Meta:
        model = ProposedQuestionModel
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(
                attrs={
                    'placeholder': 'Propose a question',
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data.get('content')

        if len(content) <= 10:
            msg = 'The question is too short.'
            self.add_error('content', msg)


class EditQuestionForm(forms.ModelForm):
    class Meta:
        model = ProposedQuestionModel
        fields = ('content', 'is_approved',)
        widgets = {
            'content': forms.Textarea(),
            'is_approved': forms.TextInput(),
        }

    def __init__(self, *args, **kwargs):
        super(EditQuestionForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = "Proposed question:"
        self.fields['is_approved'].label = "Approved:"
        self.fields['is_approved'].disabled = True

    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data.get('content')
        is_approved = cleaned_data.get('is_approved')

        if is_approved:
            msg = 'The question is approved. You cannot edit it, but you can add a new one.'
            self.add_error('content', msg)
        if len(content) <= 10:
            msg = 'The field cannot be left empty.'
            self.add_error('content', msg)


class DeleteQuestionForm(forms.ModelForm):
    class Meta:
        model = ProposedQuestionModel
        fields = ('content', 'is_approved',)
        widgets = {
            'content': forms.Textarea(),
            'is_approved': forms.TextInput(),
        }

    def __init__(self, *args, **kwargs):
        super(DeleteQuestionForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = "Proposed question:"
        self.fields['is_approved'].label = "Approved:"
        self.fields['is_approved'].disabled = True
        self.fields['content'].disabled = True

    def save(self, commit=True):
        if commit:
            self.instance.delete()
            return self.instance
