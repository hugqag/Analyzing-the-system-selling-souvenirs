# Ma
# Ten
# Gioi tinh
# sdt
# Dia chi
# Dia diem du lich
# Noi o
# Gia

def Nhap(n):
    ma = "HK" + str(n)
    ten = input("Nhap ten khach: ")
    gioi_tinh = int(input("Nhap gioi tinh (1: Nam /0: Nu): "))
    sdt = input("Nhap so dien thoai lien he: ")
    noi_o = input("Nhap dia chi: ")
    dia_diem_den = input("Nhap diem den: ")
    dat_phong = int(input("Ban co muon dat phong (1: Yes /0: No)?"))
    gia = int(input("Nhap gia dich vu: "))
    print("Ma khach cua ban la: " + ma)
    return [ma, ten, gioi_tinh, sdt, noi_o, dia_diem_den, dat_phong, gia]


def Xuat(khach):
    if khach[2] == 1:
        xung_ho = "Anh"
    else:
        xung_ho = "Chi"
    print(f"Ma khach {khach[0]}")
    print(f"{xung_ho} {khach[1]} dang ky tour du lich {khach[5]}")
    print(
        f"Thong tin lien lac:\nSDT: {khach[3]}\nDia chi thuong chu: {khach[4]}")
    print(
        f"Thong tin khac: \nDat phong: {'Co' if khach[6] == 1 else 'Khong'} \nGia dich vu: {khach[7]} 000 VND")


def CapNhat(khach):
    if khach[2] == "Nam":
        xung_ho = "Anh"
    else:
        xung_ho = "Chi"
    print(f"Ma khach {khach[0]}")
    print(f"{xung_ho} {khach[1]} dang ky tour du lich {khach[5]}")
    khach[3] = input("Nhap so dien thoai lien he: ")
    khach[4] = input("Nhap dia chi: ")
    khach[6] = int(input("Ban co muon dat phong (1: Yes /0: No)?"))


def IndexOfFirst(DSKhach, ma):
    for i in range(len(DSKhach)):
        if DSKhach[i][0] == ma:
            return i
    return -1


def Push(DSKhach):
    print("Them thong tin khach")
    khach = Nhap(len(DSKhach) + 1)
    DSKhach.append(khach)


def Update(DSKhach):
    ma = input("Nhap ma khach: ")
    index = IndexOfFirst(DSKhach, ma)
    if index == -1:
        print("Khong thay ma khach trong danh sach")
    else:
        CapNhat(DSKhach[index])
        print("Da cap nhat thong tin khach. Thong tin moi:\n")
        Xuat(DSKhach[index])


def Search(DSKhach):
    ma = input("Nhap ma khach: ")
    index = IndexOfFirst(DSKhach, ma)
    if index == -1:
        print("Khong thay ma khach trong danh sach")
    else:
        Xuat(DSKhach[index])


def Remove(DSKhach):
    ma = input("Nhap ma khach: ")
    index = IndexOfFirst(DSKhach, ma)
    if index == -1:
        print("Khong thay ma khach trong danh sach")
    else:
        DSKhach.remove(DSKhach[index])
        print("Da xoa thong tin khach khoi danh sach")


def NhapDuLieu(duong_dan):
    DSKhach = []
    try:
        with open(duong_dan) as du_lieu:
            for i in du_lieu:
                khach = i.strip().split(';')
                DSKhach.append(khach)

    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Permission denied")
    except Exception as e:
        print("An error occurred:", e)

    return DSKhach


def XuLy(DSKhach):
    print("\n____________________________")
    print("\n\tChuc nang\n")
    print("1. Nhap thong tin hanh khach")
    print("2. Tim kiem thong tin hanh khach")
    print("3. Sua thong tin hanh khach")
    print("4. Xoa thong tin hanh khach")
    print("5. Thoat")
    chuc_nang = int(input("Chuc nang: "))
    print("\n____________________________\n")
    if chuc_nang == 1:
        Push(DSKhach)
    elif chuc_nang == 2:
        Search(DSKhach)
    elif chuc_nang == 3:
        Update(DSKhach)
    elif chuc_nang == 4:
        Remove(DSKhach)
    elif chuc_nang == 5:
        return False
    else:
        print("Chuc nang khong hop le")
    return True


def Main():
    DSKhach = NhapDuLieu("input.txt")
    continue_ = True
    while continue_:
        continue_ = XuLy(DSKhach)
    print("Ket thuc")


Main()
