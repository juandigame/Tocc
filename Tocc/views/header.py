import reflex as rx
from Tocc.styles.styles import Size, Spacing
from Tocc.styles.colors import Color, TextColor

class Spline(rx.Component):
    library = "@splinetool/react-spline"
    lib_dependencies: list[str] = ["@splinetool/runtime@1.5.5"]
    tag = "Spline"
    is_default = True
    scene: rx.Var[str]

    @classmethod
    def spline_demo(cls):
        return cls.create(scene="https://prod.spline.design/1mjBPr5ZXdyYk6ey/scene.splinecode")

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.vstack(
                rx.text("Conoce un poco de nosotros", size="9"),
                rx.vstack(
                    rx.text("Tocc es una empresa dedicada a la creación de experiencias digitales,", size="5"),
                    rx.text("donde la tecnología y el diseño se unen para ofrecer soluciones innovadoras.", size="5"),
                    spacing = "0",
                ),
                rx.link(
                    rx.button(
                        "Conócenos",
                        size="4",
                        bg = Color.PURPLE.value,
                        color="white",
                        width="300px",
                        border="none",
                        box_shadow = "none",
                    ),
                ),
                align_items="center",
                width="60%",  
                bg = Color.LILA.value,
                spacing="4",
                border_radius="10px",
                padding_y=Size.SMALL.value, 
            ), 
            rx.spacer(flex="0.8"),
            rx.box(
                Spline.spline_demo(),
                width="400px",  
                height="400px",
            ),
            width="100%",
            bg = Color.PURPLE.value,
            padding_x=Size.VERY_BIG.value,
            padding_y=Size.SMALL.value,
            align_items="center",
            border_radius="10px",
        ),
        width="100%",
    )