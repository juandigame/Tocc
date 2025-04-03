import reflex as rx
from Tocc.styles.styles import Size, Spacing
from Tocc.styles.colors import Color, TextColor

class FormState(rx.State):

    @rx.event
    def submit(self, form_data):
        return rx.toast(form_data)

def form() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.text("Contáctanos", size="8", font_weight="bold"),
            rx.form(
                rx.vstack(
                    rx.input(placeholder="Nombre", name="name"),
                    rx.input(placeholder="Correo electrónico", name="email"),
                    #rx.textarea(placeholder="Mensaje", name="message"),
                    rx.button("Enviar", 
                              type_="submit", 
                              bg=Color.LILA.value, 
                              color=TextColor.LIGHT.value, 
                              size="4", 
                              padding_x=Size.DEFAULT.value, 
                              padding_y=Size.DEFAULT.value),
                ),
                on_submit=FormState.submit,
            ),
            padding=Size.DEFAULT.value,
            spacing=Spacing.SMALL.value,
        ),
        width="100%",
        padding=Size.DEFAULT.value,
        border_radius=Size.SMALL.value,
        box_shadow=Color.PURPLE.value,
        bg=Color.LILA.value,
    )