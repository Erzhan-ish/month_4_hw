from django import forms
from . import models, paser_kinoogo

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('kinoogo', 'kinoogo'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)
    class Meta:
        fields = [
            'media_type'
        ]
    def parser_data(self):
        if self.data['media_type'] == 'kinoogo':
            kinoogo_file = paser_kinoogo.parsing()
            for i in kinoogo_file:
                models.KinoogoModel.objects.create(**i)