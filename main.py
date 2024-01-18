import flet
from flet import *
import time 
from math import pi


class AnimatedBox(UserControl):
    def __init__(self, border_color, bg_color, rotate_angle):
        # "Create isntances for each paramter"
        self.border_color = border_color
        self.bg_color = bg_color
        self.rotate_angle = rotate_angle
        super().__init__()
    def build(self):
        # "We'll need to boxes that differe in rotation, color, and bgcolor. These will be passed as arguments whes the class is called"

        return Container(
            width=48,
            height=48,
            border=border.all(2.5, self.border_color),
            bgcolor=self.bg_color,
            border_radius=2,
            rotate=transform.Rotate(self.rotate_angle, alignment.center),
            animate_rotation=animation.Animation(700, "easeInOut"),
        )

def main(page: Page):
    # dimensions 
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.bgcolor = '#1f262f'

    # main page controls
    page.add(
        Card(
            width=408,
            height=612,
            elevation=15,
            content=Container(
                bgcolor="#23262a",
                border_radius=6,
                content=Column(
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        # add main controls here
                         
                    ]
                )
            )
        )
    )
    page.update()

if __name__ == "__main__":
    flet.app(target=main)
