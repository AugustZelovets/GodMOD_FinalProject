from django.forms import inlineformset_factory, ModelForm

from .models import *


class ModVersionInline(ModelForm):
    class Meta:
        model = ModVersion
        fields = '__all__'


class ModForm(ModelForm):
    class Meta:
        model = Mod
        fields = '__all__'


ModInlineFormSet = inlineformset_factory(Mod, ModVersion,
                                         form=ModVersionInline,
                                         extra=1,
                                         can_delete=False,
                                         fields='__all__')
