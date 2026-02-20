from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# === 1. MODEL SERVICES (Jasa) ===
class Service(models.Model):
    CATEGORY_CHOICES = [
        ('OS', 'Instalasi & Perbaikan OS'),
        ('GAME', 'Instalasi Game'),
        ('SOSMED', 'Jasa Followers'),
    ]

    title = models.CharField(max_length=200, verbose_name="Nama Jasa")
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, verbose_name="Kategori")
    description = models.TextField(verbose_name="Deskripsi Lengkap")
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="Harga (Rp)")
    
    # Kolom Gambar & Banner
    image = models.ImageField(upload_to='service_images/', blank=True, null=True, verbose_name="Upload Gambar Banner")
    is_banner = models.BooleanField(default=False, verbose_name="Jadikan Banner Slider")

    def __str__(self):
        return self.title

# === 2. MODEL REVIEW (Ulasan) ===
class Review(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='reviews')
    user_name = models.CharField(max_length=100, verbose_name="Nama User")
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], verbose_name="Bintang (1-5)")
    comment = models.TextField(verbose_name="Komentar")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} - {self.service.title}"

# === 3. MODEL SETTINGS (Pengaturan Web) ===
class SiteSettings(models.Model):
    site_name = models.CharField(max_length=100, default="Nexus IT", verbose_name="Nama Website")
    whatsapp_number = models.CharField(max_length=20, help_text="Gunakan format 628xxx (tanpa + atau 0 di depan)", verbose_name="No WhatsApp Admin")
    instagram_url = models.URLField(blank=True, null=True, verbose_name="Link Instagram")
    address = models.TextField(blank=True, null=True, verbose_name="Alamat Toko")
    
    # Singleton Pattern (Biar data cuma satu)
    def save(self, *args, **kwargs):
        if not self.pk and SiteSettings.objects.exists():
            return SiteSettings.objects.first().save(*args, **kwargs)
        return super(SiteSettings, self).save(*args, **kwargs)

    # --- BAGIAN INI YANG TADI ERROR ---
    def __str__(self):
        return self.site_name  # <--- SEKARANG UDAH BENER (Panggil site_name, bukan user_name)
    
    class Meta:
        verbose_name = "Pengaturan Website"
        verbose_name_plural = "Pengaturan Website"


# ===4. MODEL PROFILE (Member Area) ===
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'

# === SIGNAL (Otomatis bikin profil pas user daftar) ===
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()