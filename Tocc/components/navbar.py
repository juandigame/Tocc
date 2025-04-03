import reflex as rx
import Tocc.styles.styles as styles
from Tocc.styles.styles import Size
from Tocc.styles.colors import Color

def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.image(src="/logo.png", 
                     width="50px", 
                     height="auto", 
                     alt="TOCC TECHNOLOGY",
                     ),
            href="/",
        ),
        rx.spacer(),
        rx.hstack(
            rx.link(rx.text("Servicios", size="6", font_weight="bold"), href="/servicios"),
            rx.link(rx.text("Nosotros", size="6", font_weight="bold"), href="/nosotros"),
            rx.link(rx.text("Contactanos", size="6", font_weight="bold"), href="/contactanos"),
            spacing="6",
        ),
        position="sticky",
        bg=Color.LILA.value,
        border_bottom="1px solid rgba(247, 247, 247, 0.2)",
        padding_x=Size.VERY_BIG.value,
        padding_y=Size.DEFAULT.value,
        align="center",    
        z_index="999",
        top="0"
    )