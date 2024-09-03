import flet as ft
from flet import *

BG = '#F5E0B7'

#color pallet: E09F7D, EF5D60, 553D36, F9FBB2, CEEC97

page_1 = Container()
page_2 = Row()


def main(page: ft.Page):
    container = Container(
        width=400, 
        height=850,
        bgcolor=BG,
        border_radius=35,
        content=Stack(
            controls=[
                page_1,
                page_2

            ]
        )
    )
    page.add(container)


ft.app(main)
