import flet as ft
 
adele = "https://github.com/marcosrod12/Software-Development-Projects/blob/main/Adele%20-%20Set%20Fire%20To%20The%20Rain%20(Live%20at%20The%20Royal%20Albert%20Hall).mp3?raw=True"
aventura = "https://github.com/marcosrod12/Software-Development-Projects/blob/main/Dile%20al%20Amor.mp3?raw=true"
juanes = "https://github.com/marcosrod12/Software-Development-Projects/blob/main/Juanes%20-%20Para%20Tu%20Amor%20(Official%20Music%20Video).mp3?raw=true"
karolg = "https://github.com/marcosrod12/Software-Development-Projects/blob/main/KAROL%20G%20-%20Mercurio%20(Visualizer).mp3?raw=true"
romeo_santos = "https://github.com/marcosrod12/Software-Development-Projects/blob/main/Romeo%20Santos%20-%20Eres%20M%C3%ADa.mp3?raw=true"
 
def main(page: ft.Page):
    page.title = "El Real Music Player"
 
    super_cancion_numero_1 = ft.Audio(
        src=adele,
        autoplay=False,
    )
    page.overlay.append(super_cancion_numero_1)
 
    super_cancion_numero_2 = ft.Audio(
        src=aventura,
        autoplay=False,
    )
    page.overlay.append(super_cancion_numero_2)
 
    super_cancion_numero_3 = ft.Audio(
        src=juanes,
        autoplay=False,
    )
    page.overlay.append(super_cancion_numero_3)
 
    super_cancion_numero_4 = ft.Audio(
        src=karolg,
        autoplay=False,
    )
    page.overlay.append(super_cancion_numero_4)
 
    super_cancion_numero_5 = ft.Audio(
        src=romeo_santos,
        autoplay=False,
    )
    page.overlay.append(super_cancion_numero_5)
 
    def yes_click(e):
        page.window_destroy()  
 
    
    page.add(
        ft.ElevatedButton("Cancion 1", on_click=lambda _: super_cancion_numero_1.play()),
        ft.ElevatedButton("Cancion 2", on_click=lambda _: super_cancion_numero_2.play()),
        ft.ElevatedButton("Cancion 3", on_click=lambda _: super_cancion_numero_3.play()),
        ft.ElevatedButton("Cancion 4", on_click=lambda _: super_cancion_numero_4.play()),
        ft.ElevatedButton("Cancion 5", on_click=lambda _: super_cancion_numero_5.play()),
        ft.ElevatedButton("Salir de la App", color="red", on_click=yes_click)
    )
 
ft.app(target=main)