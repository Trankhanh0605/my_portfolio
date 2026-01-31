from django.shortcuts import render, get_object_or_404
from .models import HoSo, DuAn, ThanhTich

# 1. Hàm xử lý trang chủ (Home)
def home(request):
    # --- BƯỚC 1: LẤY DỮ LIỆU TỪ DATABASE ---
    
    # Lấy thông tin cá nhân (chỉ lấy người đầu tiên tìm thấy)
    # Dùng .first() để tránh lỗi nếu lỡ tay chưa tạo hồ sơ nào
    profile = HoSo.objects.first() 
    
    # Lấy toàn bộ danh sách dự án
    projects = DuAn.objects.all()
    
    # Lấy toàn bộ thành tích (đã được sắp xếp theo ngày nhờ class Meta trong models)
    achievements = ThanhTich.objects.all()

    # --- BƯỚC 2: ĐÓNG GÓI DỮ LIỆU (CONTEXT) ---
    # Biến bên trái (chuỗi) là tên bạn sẽ dùng ngoài file HTML
    # Biến bên phải là dữ liệu vừa lấy ở trên
    context = {
        'nguoi_dung': profile,
        'danh_sach_du_an': projects,
        'danh_sach_thanh_tich': achievements,
    }

    # --- BƯỚC 3: TRẢ VỀ GIAO DIỆN ---
    return render(request, 'cv/home.html', context)


# 2. Hàm xem chi tiết một dự án (Project Detail)
def project_detail(request, project_id):
    # Hàm get_object_or_404 rất hay:
    # Nếu tìm thấy dự án có id = project_id -> Lấy dữ liệu
    # Nếu không tìm thấy (ví dụ gõ bừa id=9999) -> Tự động báo lỗi 404 "Page Not Found"
    du_an = get_object_or_404(DuAn, pk=project_id)
    
    context = {
        'du_an': du_an
    }
    
    return render(request, 'cv/project_detail.html', context)