#tạo 1 danh sách rỗng
j=[]
#duyệt các con số từ 2000 tới 3201, nào chia hết cho 7 không bội số 5
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5!=0):
        j.append(str(i))
    print(','.join(j))