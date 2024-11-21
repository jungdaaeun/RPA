import qrcode

name = input("이름을 입력하시오 : ")
studentcode = input("학번을 입력하시오 : ")
major = input("전공울 입력하시오 : ")

qr_data = f"{name} {studentcode} {major}"
qr_img = qrcode.make(qr_data)

save_path = 'my_info_data.png'
qr_img.save(save_path)