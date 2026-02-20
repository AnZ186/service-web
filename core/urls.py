from django.contrib import admin
from django.urls import path, include
from django.conf import settings             # <--- Wajib ada
from django.conf.urls.static import static   # <--- Wajib ada

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('services.urls')),
]

# === BAGIAN INI YANG BIKIN GAMBAR MUNCUL ===
# Kalau DEBUG=True (Mode Termux), izinkan akses ke folder Media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
