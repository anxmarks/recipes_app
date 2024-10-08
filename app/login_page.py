import flet as ft 
from flet import *
from flet_core.control_event import ControlEvent
#Please, understand that this is a test

def login(page: ft.Page) -> None:
    page.title = "Welcome, please sign in"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 430
    page.window_height = 850
    page.window_resizable = False

    text_username: TextField = TextField(label='Username', text_align=ft.TextAlign.LEFT, width=200)
    text_password: TextField = TextField(label='Password', text_align=ft.TextAlign.LEFT, width=200, password=True)
    checkbox_signup: Checkbox = Checkbox(label='I understand this is a test', value=False)
    button_submit: ElevatedButton = ElevatedButton(text='Sign up', width=200, disabled=True)

    #check if everything is filled up
    def validate(e: ControlEvent) -> None:
        if all([text_username.value, text_password.value, checkbox_signup.value]):
            button_submit.disabled = False
        else:
            button_submit.disabled = True
        
        page.update()

    def submit(e: ControlEvent) -> None:
        print('Username:', text_username.value)
        print('Password:', text_password.value)

        page.go("/main")

    checkbox_signup.on_change = validate
    text_username.on_change = validate
    text_password.on_change = validate
    button_submit.on_click = submit

    page.add(
        Row(
            controls=[
                Column(
                    [text_username,
                     text_password,
                     checkbox_signup,
                     button_submit]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

#if __name__ == '__main__':
 #   ft.app(target=login)