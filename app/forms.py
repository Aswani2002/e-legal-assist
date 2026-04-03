import re
from django import forms

class DynamicTemplateForm(forms.Form):

    def __init__(self, template_content, *args, **kwargs):
        super().__init__(*args, **kwargs)

        tags = re.findall(r"{{(.*?)}}", template_content)
        unique_tags = set(tags)

        for tag in unique_tags:
            self.fields[tag] = forms.CharField(
                label=tag.replace("_", " ").title(),
                widget=forms.TextInput(attrs={'class': 'form-control'}),
                required=False
            )
