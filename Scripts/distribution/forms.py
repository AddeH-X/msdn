from django import forms

from .models import Hospital,M_material

class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['name','address']
        labels = {'name':'name','address':'address'}


class M_materialForm(forms.ModelForm):
    class Meta:
        model = M_material
        fields = ['name','need_num','urgency']
        labels = {'name':'supplies_name'}
