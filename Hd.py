import requests

l = """——————————————————————————————
𝐇𝐞𝐚𝐝𝐞𝐫𝐬 𝐂𝐞𝐤𝐦𝐞
——————————————————————————————
𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦> 𝐭.𝐦𝐞/𝐰𝐞𝐱𝐪0 / 𝐭.𝐦𝐞/𝐰𝐞𝐱𝐪0𝐩𝐲𝐭𝐡𝐨𝐧 |
——————————————————————————————
"""
print("\033[97m", l)

time.sleep(1)


s = input("\x1b[1;36m𝐒𝐢𝐭𝐞𝐧𝐢𝐧 𝐋𝐢𝐧𝐤𝐢𝐧𝐢 𝐠𝐢𝐫 > ")


ape = f'https://api.hackertarget.com/httpheaders/?q={s}'

response = requests.get(ape)

d = response.text

print(f"𝐇𝐞𝐚𝐝𝐞𝐫𝐬 𝐜𝐞𝐤𝐢𝐥𝐝𝐢\n{d}")
