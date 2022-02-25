import vk_api, time,colorama
from colorama import Fore, Back, Style
from vk_api import VkUpload
colorama.init()

priva = [
"""
██████╗░██╗░░██╗░█████╗░████████╗░█████╗░███╗░░██╗░█████╗░██╗░░██╗██████╗░██╗░░░██╗████████╗██╗░░██╗░█████╗░
██╔══██╗██║░░██║██╔══██╗╚══██╔══╝██╔══██╗████╗░██║██╔══██╗██║░██╔╝██╔══██╗██║░░░██║╚══██╔══╝██║░██╔╝██╔══██╗
██████╔╝███████║██║░░██║░░░██║░░░██║░░██║██╔██╗██║███████║█████═╝░██████╔╝██║░░░██║░░░██║░░░█████═╝░███████║
██╔═══╝░██╔══██║██║░░██║░░░██║░░░██║░░██║██║╚████║██╔══██║██╔═██╗░██╔══██╗██║░░░██║░░░██║░░░██╔═██╗░██╔══██║
██║░░░░░██║░░██║╚█████╔╝░░░██║░░░╚█████╔╝██║░╚███║██║░░██║██║░╚██╗██║░░██║╚██████╔╝░░░██║░░░██║░╚██╗██║░░██║
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝
"""
]

opicanya = [
"""
Подписаться на автора в Telegram? (yes/no)
"""
]
print(Fore.GREEN + priva[0])
print(Fore.RED + opicanya[0])
vibor = input('-->')
if vibor == "yes":
    os.system("termux-open-url 'https://t.me/joinchat/RUQ98c7lE_wUXexn'")
elif vibor == "no":
	login1 = input('Введите логин от страницы:')
	password1 = input('Введите пароль от страницы:')
	album = input('Введите ID альбома:')
vk_session = vk_api.VkApi(login=login1, password=password1, app_id='2685278')
vk_session.auth(token_only=True)
vks = vk_session
upload = VkUpload(vk_session)

while True:
	upload.photo(photos="photo.jpg",album_id=album)
