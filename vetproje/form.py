from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import hayvan_tanitimi, musteriler, musteri_hayvaniliskisi


class hayvan_form(forms.ModelForm):
    hayvan_tur = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'hayvan_tur',
        'placeholder': 'Hayvan Türünü Giriniz...',
        'style': 'margin-top:10px;margin-left:70px;font-size:14px;width:250px;height:39px;border-radius:7px;border:solid 2.3px'}))

    hayvan_cins = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'hayvan_cins',
        'placeholder': 'Hayvan Cinsini Giriniz...',
        'style': 'margin-top:10px;margin-left:70px;font-size:14px;width:250px;height:39px;border-radius:7px;border:solid 2.3px'}))

    hayvan_isim = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'hayvan_isim',
        'placeholder': 'Hayvan İsimini Giriniz...',
        'style': 'margin-top:10px;margin-left:70px;font-size:14px;width:250px;height:39px;border-radius:7px;border:solid 2.3px'}))

    hayvan_yas = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'hayvan_yas',
        'placeholder': 'Hayvan Yaşını Giriniz...',
        'style': 'margin-top:10px;margin-left:70px;font-size:14px;width:250px;height:39px;border-radius:7px;border'
                 ':solid 2.3px'}))

    hayvan_aciklama = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'name': 'hayvan_aciklama',
        'placeholder': 'Açıklama Giriniz...',
        'style': 'margin-top:20px;font-size:14px;margin-left:70px;width:250px;height:90px;border-radius:7px;border'
                 ':solid 2.3px;'}))

    class Meta:
        model = hayvan_tanitimi
        fields = '__all__'


class musteri_form(forms.ModelForm):
    musteri_adisoyadi = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'hayvan_yas',
        'placeholder': 'Müşterinin İsmini Giriniz...',
        'style': 'margin-top:10px;margin-left:70px;font-size:14px;width:250px;height:39px;border-radius:7px;border'
                 ':solid 2.3px'}))
    musteri_eposta = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'e_mail',
        'placeholder': 'Müşterinin E-posta Adresini Giriniz...',
        'style': 'margin-top:10px;margin-left:70px;font-size:14px;width:250px;height:39px;border-radius:7px;border'
                 ':solid 2.3px'}))
    musteri_telefon = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'hayvan_yas',
        'placeholder': 'Müşterinin Telefon Numarasını Giriniz...',
        'style': 'margin-top:10px;margin-left:70px;font-size:14px;width:250px;height:39px;border-radius:7px;border'
                 ':solid 2.3px'}))
    musteri_adres = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'name': 'hayvan_aciklama',
        'placeholder': 'Müşterinin Adresini Giriniz...',
        'style': 'margin-top:15px;font-size:14px;margin-left:70px;width:250px;height:90px;border-radius:7px;border'
                 ':solid 2.3px;'}))

    class Meta:
        model = musteriler
        fields = '__all__'


class atama_yap(forms.ModelForm):
    hayvan_adivecinsi = forms.ModelChoiceField(label="Hayvan Seçimi", queryset=hayvan_tanitimi.objects.all(),
                                               widget=forms.Select(attrs={
                                                   'class': 'form-control',
                                                   'name': 'hayvan_adivecinsi',
                                                   'style': 'margin-top:10px;font-size:14px;margin-left:40px;width:250px;height:39px;border-radius:7px;border'
                                                            ':solid 2.3px;font-size:17px'}))

    musteri_adisoyadi = forms.ModelChoiceField(label="Müşteri Seçimi", queryset=musteriler.objects.all(),
                                               widget=forms.Select(attrs={
                                                   'class': 'form-control',
                                                   'name': 'musteri_adisoyadi',
                                                   'style': 'margin-top:10px;font-size:14px;margin-left:40px;width:250px;height:39px;border-radius:7px;border'
                                                            ':solid 2.3px;font-size:17px'}))

    class Meta:
        model = musteri_hayvaniliskisi
        fields = '__all__'


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(label="Username", required=True, max_length=30,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'name': 'username',
                                   'placeholder': 'Kullanıcı adınız...',
                                   'style': 'font-family: "Segoe UI Semibold";margin-left:-220px;width:330px;height:40px;border-radius:5px;background-color:#eaeaea'}))
    password = forms.CharField(label="Password", required=True, max_length=30,
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'name': 'password',
                                   'placeholder': 'Parolanız...',
                                   'style': 'font-family: "Segoe UI Semibold";margin-left:-220px;width:330px;height:40px;border-radius:5px;background-color:#eaeaea'}))
