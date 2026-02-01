from django.shortcuts import render, get_object_or_404
from .models import HoSo, DuAn, ThanhTich

# 1. Hàm xử lý trang chủ (Home)
def home(request):
    profile = HoSo.objects.first() 
    projects = DuAn.objects.all()
    achievements = ThanhTich.objects.all()
    
    # Biến bên trái (chuỗi) là tên bạn sẽ dùng ngoài file HTML
    # Biến bên phải là dữ liệu vừa lấy ở trên
    context = {
        'nguoi_dung': profile,
        'danh_sach_du_an': projects,
        'danh_sach_thanh_tich': achievements,
    }

    # ---TRẢ VỀ GIAO DIỆN ---
    return render(request, 'cv/home.html', context)


# 2. Hàm xem chi tiết một dự án (Project Detail)
def project_detail(request, project_id):
    du_an = get_object_or_404(DuAn, pk=project_id)
    
    context = {
        'du_an': du_an
    }
    
    return render(request, 'cv/project_detail.html', context)