class SinhVien: #LE THANHLINH 
  def __init__(self,fullname,age,score):
    self.hoten = fullname
    self.namsinh= age
    self.dtb = score
  #dung de in gia tri cua doi tuong ra man hing
  def __str__(self):
    message ='[hoten:'+ str(self.hoten)+';nam sinh:'+str(self.namsinh)+';dtb:'+str(self.dtb)+']'
    return message
  #Dung de so sanh
  def __gt__(self, obj):
    return(self.dtb > obj.dtb)
  def __getattr__(self, obj):
    return(self.dtb >= obj.dtb)
  def __lt__(self, obj):
    return(self.dtb < obj.dtb)
  def __le__(self, obj):
    return(self.dtb <= obj.dtb)
  def __eq__(self, obj):
    return(self.dtb == obj.dtb)