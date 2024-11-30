import flet as ft
def main (page: ft.Page):
    def login(e: ft.ControlEvent):
        #print("Acceso correcto:\n",txt_usuario.value)
        dlg = ft.AlertDialog(
            title=ft.Text ("Fatal Error 404", color="red"),
            actions=[ft.ElevatedButton(
                "Cerrar",
                bgcolor="red",
                on_click=lambda e: page.close(dlg)
            )],
            modal=True
        )
        page.open(dlg)
    
    #pass
    page.window.width = 800
    page.window.height = 600
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.theme_mode = "dark"
    page.title = "Inicio de Sesion"
    page.appbar = ft.AppBar(
        title = ft.Text("Registro", size=40),
        center_title=True,
        bgcolor = "blue"
    )

    txt_usuario = ft.TextField(
        label="Usuario@",
        width=300
    )
    txt_contra = ft.TextField(
        label="Contraseña",
        password=True,
        width=300
    )
    btn_buscar = ft.FilledButton(
        "Buscar",
        icon="search",
        width=150,
        on_click=login
    )

    page.add(txt_usuario)
    page.add(txt_contra)
    page.add(btn_buscar)

    #Atualizar la pagina/ventana/app
    page.update()

#Codigo principal
ft.app (target=main, view=ft.AppView.WEB_BROWSER)