import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.image(src="/logo_negro.png"),
            rx.text("TOCC",),
            rx.text("TECHNOLOGY")
        )
    )