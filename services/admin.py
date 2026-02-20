from django.contrib import admin
from django.utils.html import format_html
from django.contrib.humanize.templatetags.humanize import intcomma
from .models import Service, Review, SiteSettings

# 1. ADMIN SERVICES
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'title', 'category_badge', 'formatted_price', 'is_banner', 'total_reviews')
    list_editable = ('is_banner',)  # Centang banner langsung dari luar
    list_filter = ('category', 'is_banner')
    search_fields = ('title', 'description')
    list_per_page = 10

    # Thumbnail Foto Kecil
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 8px;" />', obj.image.url)
        return "-"
    image_preview.short_description = 'Foto'

    # Badge Kategori Warna-warni
    def category_badge(self, obj):
        colors = {
            'OS': 'info',
            'GAME': 'success',
            'SOSMED': 'warning',
        }
        color = colors.get(obj.category, 'secondary')
        return format_html('<span class="badge badge-{}">{}</span>', color, obj.get_category_display())
    category_badge.short_description = 'Kategori'

    # Format Harga Rupiah
    def formatted_price(self, obj):
        return f"Rp {intcomma(obj.price)}"
    formatted_price.short_description = 'Harga'

    # Hitung Jumlah Review
    def total_reviews(self, obj):
        return f"{obj.reviews.count()} Ulasan"

# 2. ADMIN REVIEW (Ini yang tadi error)
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'service', 'rating_stars', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('user_name', 'comment', 'service__title')
    readonly_fields = ('created_at',)

    # Fungsi Bintang ⭐ (Pastikan ini ada!)
    def rating_stars(self, obj):
        return "⭐" * obj.rating
    rating_stars.short_description = 'Rating'

# 3. ADMIN SETTINGS (Fitur Baru)
@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    # Biar gak bisa nambah lebih dari 1 setting
    def has_add_permission(self, request):
        if SiteSettings.objects.exists():
            return False
        return True

    # Biar gak bisa dihapus
    def has_delete_permission(self, request, obj=None):
        return False
