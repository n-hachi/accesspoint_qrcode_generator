#!/usr/bin/env python3

import qrcode

print("QRコードを作成します。")
ssid = input("ssidを入力してください。: ")
if len(ssid.strip()) == 0:
    print("ssidが入力されていません。")
    exit()
passwd = input("パスワードを入力してください。: ")
if len(ssid.strip()) == 0:
    print("パスワードが入力されていません。")
    exit()
qrName = input("QRコードの名前を入力してください。: ")
if len(qrName.strip()) == 0:
    print("QRコードが入力されていません。")
    exit()

# # qrコードを作成
formatStr = 'WIFI:S:{};T:WPA;P:{};;'.format(ssid, passwd)
img = qrcode.make(formatStr)
img.save(f"{qrName}.png")
print("QRコードを作成しました。")
