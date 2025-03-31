import reflex as rx
import Tocc.styles.styles as styles
from .components.navbar import navbar
from .components.footer import footer

class State(rx.State):
    pass
    
def index() -> rx.Component:
    return rx.box(
        navbar(),
        footer(),
    )


app = rx.App(
    style=styles.BASE_STYLE
)
app.add_page(index)
