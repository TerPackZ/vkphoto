import vk_api, time, colorama
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

token = input('Введите токен: ')
album = input('Введите id альбома: ')
session = vk.Session(access_token=token)
session = vk.Session(access_token=token)
apivk = vk.API(session)
upload = VkUpload(vk_session)

while True:
	upload.photo(photos="photo.jpg",album_id=album)
