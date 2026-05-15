def truy_cap_phan_tu(tuple_data):
    firt_element= tuple_data[0]
    last_element= tuple_data[-1]
    return firt_element,last_element
input_tuple= eval(input("Nhập tuple, ví dụ(1,2,3): "))
first,last=truy_cap_phan_tu(input_tuple)
print("Phần tử đầu tiên:", first)
print("Phần tử cuối cùng:", last)