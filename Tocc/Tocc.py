import reflex as rx
import Tocc.styles.styles as styles
from .components.navbar import navbar
from .components.footer import footer
from Tocc.styles.styles import Size
from Tocc.views.header import header


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


app = rx.App(
    style=styles.BASE_STYLE
)
app.add_page(index)
