# cv/urls.py
from django.urls import path
from . import views  # Import file views từ thư mục hiện tại

urlpatterns = [
    # 1. Trang chủ (Homepage)
    # path('', ...): Chuỗi rỗng nghĩa là trang chủ (vd: 127.0.0.1:8000)
    path('', views.home, name='home'),

    # 2. Trang chi tiết dự án (Ví dụ mở rộng)
    # <int:pk> là ID của dự án (số nguyên). VD: project/1, project/5
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
]