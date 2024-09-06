import flet as ft
from flet import *



#color pallet: E09F7D, EF5D60, 553D36, F9FBB2, CEEC97, #ff7f7f 

def main(page: ft.Page):
    #colors
    BG = '#F5E0B7'

    categories_card = Row(
        scroll='auto'
)
    categories = ['Pastries', 'Cakes', 'Candies', 'Snacks']
    for i, category in enumerate(categories):
        categories_card.controls.append(
             Container(
            bgcolor='#E57272', height=110, width=170, border_radius=20, padding=15,
            content=Column(
                controls=[
                    Text('5 Recipes'),
                    Text(category)
                ]
            )
        )
        )
            
        
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
                Container(height=5),
                Image(
                    src=f"app/assets/images/square_logo.png",
                    width=350,
                    height=120,
                ),
                Container(height=5), 
                Text(
                    value='Welcome!',
                    color='#553D36',
                    size=35
                ),
                Text(
                    value='CATEGORIES',
                    color='#553D36'
                ),
                Container(
                    padding=padding.only(top=10, bottom=20),
                    content=categories_card
                ),
                Container(height=20),
                Text("Last Seen")
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
