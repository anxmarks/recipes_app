import flet as ft
from flet import *



#color pallet: E09F7D, EF5D60, 553D36, F9FBB2, CEEC97

def main(page: ft.Page):
    #colors
    BG = '#F5E0B7'

    first_page_contests = Container(
        content=Column(
            controls=[
                Row(alignment = 'SpaceBetween',
                    controls=[
                        Container(content=Icon(
                            icons.MENU)),
                        Row(
                            controls=[
                                Icon(icons.SEARCH),
                                Icon(icons.NOTIFICATIONS_OUTLINED)
                            ]
                        )
                    ]
                ),
                Container(height=20), 
                Text(
                    value='Welcome!',
                    color='#553D36'
                ),
                Text(
                    value='CATEGORIES',
                    color='#553D36'
                ),
                Container(
                    padding=padding.only(top=10, bottom=20)
                )
            ]
        )
    )
    page_1 = Container()
    page_2 = Row(
        controls=[
            Container(
                width=400,
                height=850,
                bgcolor='E09F7D',
                border_radius=35,
                padding=padding.only(top=50, left=20, right=20, bottom=5),
                content=Column(
                    controls=[
                        first_page_contests
                    ]
                )

            )
        ]
    )
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
