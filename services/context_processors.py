from .models import SiteSettings

def global_settings(request):
    # Ambil data pertama dari database
    settings = SiteSettings.objects.first()
    return {'global_settings': settings}
