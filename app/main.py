import flet as ft 
from flet import *
from login_page import login
from main_page import main_page
#color pallet: E09F7D, EF5D60, 553D36, F9FBB2, CEEC97, #ff7f7f 

def main(page: ft.Page):
    main_page(page)

ft.app(target=main)
