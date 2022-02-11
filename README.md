# Veteriner Yönetim Paneli

Öncelikle biz VetDjango adında bir django projesi başlatmalıyız.

Konsolumuza ***django-admin startproject VetDjango*** yazıyoruz.Aardından ise bir adet app oluşturmalıyız.

Konsolumuzu tekrardan açıp ***py manage.py startapp vetproje*** yazıyoruz.

> Bu kısımda ise github'ımda yer alan dosyaları indirip gerekli olan yerlere tek tek kopyala yapıştır yapıyoruz. Örneğin sizde oluşan VetDjango klasöründeki urls.py harici çoğu şey
sizdekinde sabit kalmalı sadece url.py dosyası oraya eklenmelidir.

### ***Dosya dosya kopyalama işlemi yapmalıyız***


## Setting Kısmı Düzenleme


Öncelikle Installed_Apps yerine vetprojeyi yani oluşturduğumuz app dosyasını eklemeyi unutmuyoruz.


LANGUAGE_CODE = 'tr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

LOGIN_URL = 'login'

LOGIN_REDIRECT_URL = "dashboard"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' **

Setting kısımındaki alanlara yukarıda yazan kodu yazıyoruz


Gerekli dosyaları kopyaladıktan sonra proje açmaya hazır hale gelir.

Konsola ** py manage.py runserver ** yazıp projemizi kullanmaya başlayabiliriz.
