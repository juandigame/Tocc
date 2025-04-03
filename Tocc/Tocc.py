import reflex as rx
import Tocc.styles.styles as styles
from .components.navbar import navbar
from .components.footer import footer
from Tocc.styles.styles import Size
from Tocc.views.header import header
from Tocc.views.form import form


class State(rx.State):
    pass
    
def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                bg=styles.Color.MORADO_CLARO.value,
                width="100%",
                padding_x=Size.DEFAULT.value,
                padding_y=Size.DEFAULT.value,
            )
        ),
        footer(),
    )

def contactanos() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                form(),
                bg=styles.Color.MORADO_CLARO.value,
                width="100%",
                padding_x=Size.DEFAULT.value,
                padding_y=Size.DEFAULT.value,
            )
        ),
        footer(),
    )

def servicios() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                bg=styles.Color.MORADO_CLARO.value,
                width="100%",
                padding_x=Size.DEFAULT.value,
                padding_y=Size.DEFAULT.value,
            )
        ),
        footer(),
    )

def nosotros() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                bg=styles.Color.MORADO_CLARO.value,
                width="100%",
                padding_x=Size.DEFAULT.value,
                padding_y=Size.DEFAULT.value,
            )
        ),
        footer(),
    )


app = rx.App(
    style=styles.BASE_STYLE,
)
app.add_page(index, title="TOCC TECHNOLOGY", description="Soluciones al instante, tecnología sin límites.")
app.add_page(contactanos, title="Contáctanos", description="Contáctanos para más información.")
app.add_page(servicios, title="Servicios", description="Servicios que ofrecemos.")
app.add_page(nosotros, title="Nosotros", description="¿Quiénes somos?")