import flet
from flet import *
import time 
from math import pi

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
