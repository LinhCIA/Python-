class NhanVien:

    def __init__(self, fullname, age, salary) -> None:
        self.hoten = fullname
        self.tuoi = age
        self.luong = salary
    def __str__(self) -> str:
        message = '[Họ và tên:'+str(self.hoten)+';Tuổi:'+str(self.tuoi)+';Mức lương:'+str(self.luong)+']'
        return message
# ThanhLinh

    def __gt__(self, obj):
        return (self.tuoi > obj.tuoi)

    def __getattr__(self, obj):
        return (self.tuoi >= obj.tuoi)

    def __lt__(self, obj):
        return (self.tuoi < obj.tuoi)

    def __le__(self, obj):
        return (self.tuoi <= obj.tuoi)

    def __eq__(self, obj):
        return (self.tuoi == obj.tuoi)