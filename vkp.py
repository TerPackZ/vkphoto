import vk, vk_api, time, colorama
from colorama import Fore, Back, Style
from vk_api import VkUpload
colorama.init()

banner = """
██╗░░░██╗██╗░░██╗██████╗░██╗░░██╗░█████╗░████████╗░█████╗░
██║░░░██║██║░██╔╝██╔══██╗██║░░██║██╔══██╗╚══██╔══╝██╔══██╗
╚██╗░██╔╝█████═╝░██████╔╝███████║██║░░██║░░░██║░░░██║░░██║
░╚████╔╝░██╔═██╗░██╔═══╝░██╔══██║██║░░██║░░░██║░░░██║░░██║
░░╚██╔╝░░██║░╚██╗██║░░░░░██║░░██║╚█████╔╝░░░██║░░░╚█████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░"""

print(Fore.CYAN + banner)
login = input('Введите логин: ')
password = input('Введите пароль: ')
album = input('Введите id альбома: ')
vk_session = vk_api.VkApi(login=login, password=password, app_id='2685278')
vk_session.auth(token_only=True)
vks = vk_session
upload = VkUpload(vk_session)

while True:
	upload.photo(photos="photo.jpg",album_id=album)
