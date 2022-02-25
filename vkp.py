import vk_api, time,colorama
import os
import sys
from colorama import Fore, Back, Style
from vk_api import VkUpload
colorama.init()

priva = [
"""
██╗░░░██╗██╗░░██╗██████╗░██╗░░██╗░█████╗░████████╗░█████╗░
██║░░░██║██║░██╔╝██╔══██╗██║░░██║██╔══██╗╚══██╔══╝██╔══██╗
╚██╗░██╔╝█████═╝░██████╔╝███████║██║░░██║░░░██║░░░██║░░██║
░╚████╔╝░██╔═██╗░██╔═══╝░██╔══██║██║░░██║░░░██║░░░██║░░██║
░░╚██╔╝░░██║░╚██╗██║░░░░░██║░░██║╚█████╔╝░░░██║░░░╚█████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░
"""
]

opicanya = [
"""
Подписаться на автора в Telegram? (yes/no)
"""
]
print(Fore.CYAN + priva[0])
print(Fore.CYAN + opicanya[0])
choose = input('--> ')
if choose == "yes":
	os.system("termux-open-url 'https://t.me/TerPackZ'")
	login1 = input('Введите логин: ')
	password1 = input('Введите пароль: ')
	album = input('Введите id альбома: ')
elif choose == "no":
	login1 = input('Введите логин: ')
	password1 = input('Введите пароль: ')
	album = input('Введите id альбома: ')
vk_session = vk_api.VkApi(login=login1, password=password1, app_id='2685278')
vk_session.auth(token_only=True)
vks = vk_session
upload = VkUpload(vk_session)

while True:
	upload.photo(photos="photo.jpg",album_id=album)
