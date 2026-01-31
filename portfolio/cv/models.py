from django.db import models

# 1. Bảng Thông Tin Cá Nhân (Chỉ nên có 1 bản ghi duy nhất)
class HoSo(models.Model):
    ten_hien_thi = models.CharField(max_length=100, help_text="ten cua ban")
    nghe_nghiep = models.CharField(max_length=100, help_text="Ví dụ: Backend Developer")
    gioi_thieu = models.TextField(help_text="Đoạn văn giới thiệu bản thân ngắn gọn")
    avatar = models.ImageField(upload_to='profile_pics/') # Cần cài thư viện Pillow
    file_cv = models.FileField(upload_to='cv_files/', blank=True, help_text="File PDF CV để người xem tải về")
    link_github = models.URLField(blank=True)
    link_linkedin = models.URLField(blank=True)

    def __str__(self):
        return self.ten_hien_thi

# 2. Bảng Dự Án (Showcase các sản phẩm đã làm)
class DuAn(models.Model):
    ten_du_an = models.CharField(max_length=200)
    anh_mo_ta = models.ImageField(upload_to='projects/')
    mo_ta_ngan = models.CharField(max_length=250) # Hiện ở trang chủ
    noi_dung_chi_tiet = models.TextField()        # Hiện khi bấm vào xem chi tiết
    cong_nghe_su_dung = models.CharField(max_length=200, help_text="Ví dụ: Python, Django, ReactJS")
    link_demo = models.URLField(blank=True, help_text="Link web chạy thực tế")
    link_source_code = models.URLField(blank=True, help_text="Link Github")
    
    def __str__(self):
        return self.ten_du_an

# 3. Bảng Thành Tích (Cái bạn đang muốn khoe)
class ThanhTich(models.Model):
    tieu_de = models.CharField(max_length=200, verbose_name="Tên thành tích/Chứng chỉ")
    to_chuc_cap = models.CharField(max_length=200, verbose_name="Nơi cấp", help_text="Ví dụ: Coursera, Google, Đại học Bách Khoa")
    ngay_nhan = models.DateField()
    mo_ta = models.TextField(blank=True, help_text="Mô tả kỹ hơn về độ khó của chứng chỉ này")
    hinh_anh_chung_nhan = models.ImageField(upload_to='certificates/', blank=True)
    
    # Meta class dùng để cấu hình phụ cho Model
    class Meta:
        ordering = ['-ngay_nhan'] # Dấu trừ (-) nghĩa là sắp xếp giảm dần (mới nhất lên đầu)
        verbose_name_plural = "Các Thành Tích"

    def __str__(self):
        return self.tieu_de