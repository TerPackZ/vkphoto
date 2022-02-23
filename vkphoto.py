import vk, vk_api, time,colorama
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
api = vk.API(session)
vks = vk_session
upload = VkUpload(vk_session)

while True:
	upload.photo(photos="photo.jpg",album_id=album)
