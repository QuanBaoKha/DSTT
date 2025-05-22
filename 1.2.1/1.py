
danhsach1 = [1.0, 3.0]
danhsach2 = [5.0, 7.0]

danhsach = danhsach1 + danhsach2
print("Kết quả của danhsach1 + danhsach2:", danhsach)

danhsach_gapdoi = 2 * danhsach
print("Kết quả của 2 * danhsach:", danhsach_gapdoi)

print("Kết quả của danhsach * 2:", danhsach * 2)

try:
    print("Kết quả của danhsach / 2:", danhsach / 2)
except TypeError as e:
    print("Lỗi khi thực hiện danhsach / 2:", e)

danhsach_chia2 = [x / 2 for x in danhsach]
print("Kết quả của chia từng phần tử của danhsach cho 2:", danhsach_chia2)
