from django.contrib import admin
from .models import HoSo, DuAn, ThanhTich

# Đăng ký các model để chúng hiện ra trong trang Admin
admin.site.register(HoSo)
admin.site.register(DuAn)
admin.site.register(ThanhTich)