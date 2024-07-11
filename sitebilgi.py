import pyfiglet
import requests


w1 = pyfiglet.figlet_format("W")
w2 = pyfiglet.figlet_format("E")
w3 = pyfiglet.figlet_format("X")
w4 = pyfiglet.figlet_format("Q")
print('\033[1;36m',  w1,w2,w3,w4)


w = """\033[1;32m/—/—/—/—/—/—/—/—/—/—/—/—/
𝐒𝐢𝐭𝐞 𝐁𝐢𝐥𝐠𝐢
/—/—/—/—/—/—/—/—/—/—/—/—/
𝐭.𝐦𝐞/𝐰𝐞𝐱𝐪0 | 𝐭.𝐦𝐞/𝐰𝐞𝐱𝐪0𝐩𝐲𝐭𝐡𝐨𝐧
/—/—/—/—/—/—/—/—/—/—/—/—/"""
print(w)

a = input('𝐒𝐢𝐭𝐞𝐧𝐢𝐧 𝐋𝐢𝐧𝐤𝐢𝐧 𝐆𝐢𝐫:        ')



abe = f"https://tilki.dev/api/site-bilgi?url={a}"

response = requests.get(abe)



dt = response.json()

b = dt['baslık']
a = dt['acıklama']

print(f"𝐚𝐜ı𝐤𝐥𝐚𝐦𝐚; {a}\n𝐛𝐚𝐬𝐥ı𝐤; {b}")
