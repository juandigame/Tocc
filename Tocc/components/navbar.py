import reflex as rx
import Tocc.styles.styles as styles
from Tocc.styles.styles import Size
from Tocc.styles.colors import Color

def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.image(src="/logo.png", 
                     width="80px", 
                     height="auto", 
                     alt="TOCC TECHNOLOGY"
                     ),
        ),
        position="sticky",
        bg=Color.DARK.value,
        border_bottom="1px solid rgba(247, 247, 247, 0.2)",
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="9999",
        top="0"
    )