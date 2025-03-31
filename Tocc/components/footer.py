import reflex as rx
import datetime
from Tocc.styles.styles import Size, Spacing
from Tocc.styles.colors import Color, TextColor

def footer() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.vstack(
                rx.text("TOCC TECHNOLOGY", size="4"),
                rx.text("Soluciones al instante, tecnología sin límites.", size="4"),
                rx.hstack(
                    rx.link(rx.icon(tag="facebook", size=20), href="https://facebook.com", is_external=True),
                    rx.link(rx.icon(tag="instagram", size=20), href="https://instagram.com", is_external=True),
                    spacing="4",
                ),
                spacing="2",
                align="start", 
            ),
            rx.vstack(
                rx.text("¿Tienes dudas?", size="4"),
                rx.vstack(
                    rx.hstack(
                        rx.icon(tag="mail", size=20),
                        rx.text("toccthecnology@gmail.com", size="4"),
                    ),
                    rx.hstack(
                        rx.icon(tag="phone", size=20),
                        rx.text("31455555555", size="4"),
                    ),
                    spacing="1",
                ),
                spacing="2",
                align="start",  
            ),
            rx.spacer(), 
            border_bottom="1px solid rgba(247, 247, 247, 0.2)",
            width="100%",
            padding_y=Size.DEFAULT.value,
        ),
        rx.box(
            f"© {datetime.datetime.now().year} TOCC TECHNOLOGY.",
            rx.text("Todos los derechos reservados.", size="4"),
            padding_y=Size.SMALL.value,  
            align="center",
        ),
        align="center",
        padding_bottom=Size.VERY_BIG.value,
        padding_x=Size.BIG.value,
        padding_y=Size.ZERO.value,
        spacing=Spacing.ZERO.value,
        color=TextColor.LIGHT.value,
        bg=Color.LILA.value,
    )