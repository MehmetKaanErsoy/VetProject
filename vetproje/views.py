from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .form import UserLoginForm, hayvan_form, musteri_form, atama_yap
from .models import hayvan_tanitimi, musteriler, musteri_hayvaniliskisi
# Create your views here.
from vetproje.form import UserLoginForm
from django.contrib import messages
from django.db.models import Q


@login_required()
def admin_login(request):
    form = UserLoginForm(request.POST)
    if form.is_valid():
        username = User.objects.get('username', False)
        password = User.objects.get('password', False)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
    return render(request, 'admin_login.html', {"form": form})


@login_required()
def dashboard(request):
    return render(request,'dashboard.html',{})


@login_required()
def cikis(request):
    logout(request)
    return redirect('login')


@login_required()
def dashboard(request):
    data_hayvan = hayvan_tanitimi.objects.all()
    data_musteri = musteriler.objects.all()
    data_sahipli = musteriler.objects.all()
    return render(request, 'dashboard.html',
                  {'data_hayvan': data_hayvan, 'data_musteri': data_musteri, 'data_sahipli': data_sahipli})


@login_required()
def hayvan_ekle(request):
    form = hayvan_form()
    if request.method == "POST":
        form = hayvan_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Başarı ile kayıt işlemi yapıldı.")
            redirect('hayvanekle')
        else:
            form = hayvan_form()
            messages.error(request, "Kayıt işlemi Başarısız.")
    else:
        form = hayvan_form()
    return render(request, 'hayvan_ekle.html', {'form': form})


@login_required()
def hayvan_musteriara(request):
    data = musteri_hayvaniliskisi.objects.all()
    search_post = request.GET.get('q')
    if search_post:
        data = musteri_hayvaniliskisi.objects.filter(
            Q(hayvan_adivecinsi__hayvan_isim__icontains=search_post) & Q(
                musteri_adisoyadi__musteri_adisoyadi__icontains=search_post))
    else:
        data = hayvan_tanitimi.objects.all()
    return render(request, 'sahiplendirilenler_listesi.html', {'data': data})


@login_required()
def hayvan_listele(request):
    data = hayvan_tanitimi.objects.all()
    arama_q = request.GET.get('q')
    if arama_q:
        data = hayvan_tanitimi.objects.filter(Q(hayvan_isim__icontains=arama_q))
    else:
        data = hayvan_tanitimi.objects.all()
    return render(request, 'hayvan_listele.html', {'data': data})


@login_required()
def hayvan_sil(request, id):
    hayvan_tanitimi.objects.filter(id=id).delete()
    return redirect('hayvanlistele')


@login_required()
def musteri_ekle(request):
    form = musteri_form()
    e_mail = request.POST.get('e_mail', False)
    if request.method == "POST":
        form = musteri_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Başarı ile kayıt işlemi yapıldı...")
        else:
            messages.error(request, "Kayıt İşlemi Başarısız. Mail adresinizi Kontrol Ediniz...")
    else:
        form = musteri_form()
    return render(request, 'musteri_ekle.html', {'form': form})


@login_required()
def musteri_listele(request):
    data = musteriler.objects.all()
    q = request.GET.get('q')
    if q:
        data = musteriler.objects.filter(Q(musteri_adisoyadi__icontains=q))
    else:
        data = musteriler.objects.all()
    return render(request, 'musteri_listele.html', {'data': data})


@login_required()
def musteri_sil(request, id):
    musteriler.objects.filter(id=id).delete()
    return redirect('musterilistele')


@login_required()
def atamayap(request):
    form = atama_yap()
    hayvan_adivecinsi_id = request.POST.get('hayvan_adivecinsi', False)
    musteri_adisoyadi_id = request.POST.get('musteri_adisoyadi', False)
    data = musteri_hayvaniliskisi.objects.filter(hayvan_adivecinsi=hayvan_adivecinsi_id).exists()
    if request.method == "POST":
        form = atama_yap(request.POST)
        if form.is_valid():
            if data:
                messages.error(request, 'Seçilen hayvan sahiplendirilmiş.')
                return redirect('atamayap')
            else:
                musteri_hayvaniliskisi.objects.create(musteri_adisoyadi_id=musteri_adisoyadi_id,
                                                      hayvan_adivecinsi_id=hayvan_adivecinsi_id)
                messages.success(request, "Başarı ile hayvan sahiplendirildi.")
                return redirect('atamaliste')
        else:
            messages.error(request, "Hata ile karşılaşıldı")
    else:
        form = atama_yap()
    return render(request, 'atama_yap.html', {'form': form})


@login_required()
def atama_listele(request):
    data = musteri_hayvaniliskisi.objects.all()
    return render(request, 'sahiplendirilenler_listesi.html', {'data': data})


@login_required()
def atama_sil(request, id):
    musteri_hayvaniliskisi.objects.filter(id=id).delete()
    messages.success(request, "Başarı ile silme işlemi gerçekleşti.")
    return redirect('atamaliste')


@login_required()
def hayvan_incele(request, id):
    data = hayvan_tanitimi.objects.get(id=id)
    hayvan_tur = data.hayvan_tur
    hayvan_cins = data.hayvan_cins
    hayvan_isim = data.hayvan_isim
    hayvan_yas = data.hayvan_yas
    hayvan_aciklama = data.hayvan_aciklama
    hayvan_id = data.id

    data_sorgu = musteri_hayvaniliskisi.objects.filter(hayvan_adivecinsi=hayvan_id).exists()
    return render(request, 'hayvan_incele.html',
                  {'hayvan_tur': hayvan_tur, 'hayvan_cins': hayvan_cins, 'hayvan_isim': hayvan_isim,
                   'hayvan_yas': hayvan_yas, 'hayvan_aciklama': hayvan_aciklama, 'data_sorgu': data_sorgu})


@login_required()
def musteri_incele(request, id):
    data = musteriler.objects.get(id=id)
    musteri_adisoyadi = data.musteri_adisoyadi
    musteri_eposta = data.musteri_eposta
    musteri_telefon = data.musteri_telefon
    musteri_adres = data.musteri_adres
    musteri_id = data.id

    data_sorgu = musteri_hayvaniliskisi.objects.filter(musteri_adisoyadi=musteri_id).exists()
    data_sayac = musteri_hayvaniliskisi.objects.filter(musteri_adisoyadi=musteri_id).count()
    print(data_sayac)

    return render(request, 'musteri_incele.html',
                  {'musteri_adisoyadi': musteri_adisoyadi, 'musteri_eposta': musteri_eposta,
                   'musteri_telefon': musteri_telefon, 'musteri_adres': musteri_adres, 'data_sorgu': data_sorgu,
                   'sayac': data_sayac})


@login_required()
def atama_incele(request, id):
    data = musteri_hayvaniliskisi.objects.get(id=id)
    musteri_adisoyadi = data.musteri_adisoyadi
    hayvan = data.hayvan_adivecinsi

    return render(request, 'sahipli_incele.html', {'data': data})


@login_required()
def hayvan_guncelle(request, id):
    if request.method == "POST":
        hayvan_tur = request.POST.get('hayvan_tur', False)
        hayvan_cins = request.POST.get('hayvan_cins', False)
        hayvan_isim = request.POST.get('hayvan_isim', False)
        hayvan_yas = request.POST.get('hayvan_yas', False)
        hayvan_aciklama = request.POST.get('hayvan_aciklama', False)
        hayvan_tanitimi.objects.filter(id=id).update(hayvan_tur=hayvan_tur, hayvan_cins=hayvan_cins,
                                                     hayvan_isim=hayvan_isim, hayvan_yas=hayvan_yas,
                                                     hayvan_aciklama=hayvan_aciklama)
        messages.info(request, 'Değişiklikler başarı ile kayıt edildi')

    data = hayvan_tanitimi.objects.get(id=id)
    return render(request, 'hayvan_guncelle.html', {'data': data})


@login_required()
def musteriguncelle(request, id):
    if request.method == "POST":
        musteri_adisoyadi = request.POST.get('musteri_adisoyadi', False)
        musteri_eposta = request.POST.get('musteri_eposta', False)
        musteri_telefon = request.POST.get('musteri_telefon', False)
        musteri_adres = request.POST.get('musteri_adres', False)

        musteriler.objects.filter(id=id).update(musteri_adisoyadi=musteri_adisoyadi, musteri_eposta=musteri_eposta,
                                                musteri_telefon=musteri_telefon, musteri_adres=musteri_adres)
        messages.info(request, "Değişiklikler başarı ile kayıt edildi")

    data = musteriler.objects.get(id=id)
    return render(request, 'musteri_guncelle.html', {'data': data})
