from django.forms import *
from .models import *
from django import forms


class ProductForm(forms.Form):
    BRAND_LIST = [('Nike', 'Nike'), ('Adides', 'Adides'), ('Jordan', 'Jordan')]
    MADE_LIST = [("USA", 'USA'), ('EU', 'EU')]
    NAME_LIST = [('Nike001', 'Nike001'), ('Adides001', 'Adides001'), ('Jordan001', 'Jordan001')]
    id = forms.CharField(max_length=13, label="รหัสสินค้า", required=True, widget=TextInput(attrs={'size':'15'}))
    name = forms.ChoiceField(label="ชื่อสินค้า", required=True, widget=Select, choices=NAME_LIST)
    brand = forms.ChoiceField(label="ยี่ห้อ", required=True, widget=Select , choices=BRAND_LIST)
    price = forms.FloatField(min_value=1.00, max_value=100000.00, label="ราคาต่อหน่วย", required=True, widget=NumberInput(attrs={'size': '15'}))
    amount = forms.IntegerField(min_value=0, max_value=1000, label="คงเหลือ", required=True, widget=NumberInput(attrs={'size': '15'}))
    made = forms.ChoiceField(label='ผลิตจาก', required=True, widget=RadioSelect, choices=MADE_LIST)

class ProductMForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('pid', 'name', 'brand', 'price', 'net', 'category')
        widgets = {
            'pid': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'net': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'pid': 'รหัสสินค้า',
            'name': 'ชื่อสินค้า',
            'brand': 'ยี้ห้อสินค้า',
            'price': 'ราคาต่อหน่วย',
            'net': 'จำนวนสินค้า',
            'category': 'รหัสสินค้า',
        }
