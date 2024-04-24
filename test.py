s = input("Nhập chuỗi của bạn: ")

if "Python" in s:
    s = s.replace("Python", "Java")
    print(s)
else:
    print("Python does not exist in the string!")