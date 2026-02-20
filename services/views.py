from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Service, Review, Profile
from .forms import UserUpdateForm, ProfileUpdateForm

# === 1. HOME (Wajib ada biar gak error 'views has no attribute index') ===
def index(request):
    banners = Service.objects.filter(is_banner=True)[:3]
    category = request.GET.get('cat')
    services = Service.objects.all()
    
    if category:
        services = services.filter(category=category)

    return render(request, 'index.html', {
        'services': services,
        'banners': banners,
        'selected_cat': category
    })

# === 2. DETAIL SERVICE ===
def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        if user_name and rating and comment:
            Review.objects.create(service=service, user_name=user_name, rating=rating, comment=comment)
            messages.success(request, 'Review terkirim!')
            return redirect('service_detail', pk=pk)

    reviews = service.reviews.all().order_by('-created_at')
    # Ambil rekomendasi (exclude yang sedang dibuka)
    related_services = Service.objects.filter(category=service.category).exclude(pk=pk)[:3]
    
    return render(request, 'service_detail.html', {
        'service': service, 
        'reviews': reviews,
        'related_services': related_services
    })

# === 3. REGISTER ===
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Akun {username} jadi! Silakan login.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# === 4. DASHBOARD (Anti-Crash Logic) ===
@login_required
def dashboard(request):
    # Cek Profil (Buat baru kalau belum ada biar gak error kuning)
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Data berhasil diupdate!')
            return redirect('dashboard')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'dashboard.html', {'u_form': u_form, 'p_form': p_form})
