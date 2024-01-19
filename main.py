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


class UserInputField(UserControl):
    def __init__(self, icon_name, text_hint, hide):
        self.icon_name = icon_name
        self.text_hint = text_hint
        self.hide = hide
        super().__init__()

    def build(self):
        return Container(
            width=320,
            height=40,
            border=border.only(bottom=border.BorderSide(0.5, "white54")),
            content=Row(
                spacing=20,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Icon(
                        name=self.icon_name,
                        size=14,
                        opacity=0.85,
                    ),
                    TextField(
                        border_color='transparent',
                        bgcolor='transparent',
                        height=20,
                        width=200,
                        text_size=12,
                        content_padding=3,
                        cursor_color='white',
                        hint_text=self.text_hint,
                        hint_style=TextStyle(size=11),
                        password=self.hide,
                        on_change=None, # change later...
                        on_blur=None, # also change later...
                ],
            ),
        )

def main(page: Page):
    # dimensions 
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.bgcolor = '#1f262f'

    # "To animate the boxes, we'll need a constant while loop to keep running."
    def animate_boxes():
        # "To animate the boxes, we'll need to create several variables"
        # "We want one box to go clockwise, and the other counter clock"
        clock_wise_rotate = pi / 4
        counter_clock_wise_rotate = -pi * 2

        # "Next we need to get the box instances so we can animate the rotation"
        # "This long line of code is where the red box is in the control list"
        # "This can be simplified by passing in the instance to a dict!"
        red_box = page.controls[0].content.content.controls[1].controls[0].controls[0]
        blue_box = page.controls[0].content.content.controls[1].controls[1].controls[0]

        # "A counter so we can reverse the rotation direction"
        counter = 0
        while True:
            # "We want to rotate 4x before we switch directions"
            if counter >= 0 and counter <= 4:
                red_box.rotate = transform.Rotate(
                    counter_clock_wise_rotate, alignment.center
                )
                blue_box.rotate = transform.Rotate(
                    clock_wise_rotate, alignment.center
                )

                red_box.update()
                blue_box.update()

                clock_wise_rotate += pi / 2
                counter_clock_wise_rotate -= pi / 2
                
                counter += 1
                time.sleep(0.7)

                # "Now we want the boxes to reverse"
            if counter >= 5 and counter <=10:
                # "Make sure to reverese the rotation angles"
                clock_wise_rotate -= pi / 2
                counter_clock_wise_rotate += pi / 2

                red_box.rotate = transform.Rotate(
                    counter_clock_wise_rotate, alignment.center
                )
                blue_box.rotate = transform.Rotate(
                    clock_wise_rotate, alignment.center
                )

                red_box.update()
                blue_box.update()

                counter += 1
                time.sleep(0.7)


            # "Finally we reset the counter back to 0 at 10"
            if counter > 10:
                counter = 0

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
                        Divider(height=40, color='transparent'),
                        Stack(
                            controls=[
                                # "We will pass the animated box class in here"
                                # "recall that the class takes in 3 arguments..."
                                AnimatedBox("#e9665a", None, 0),
                                AnimatedBox("#7df6dd", "#23262a", pi / 4),
                            ]
                        ),
                        Divider(height=20, color='transparent'),
                        # Some text
                        Column(
                            alignment=MainAxisAlignment.CENTER,
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            spacing=5,
                            controls=[
                                Text("Sign In Below", size=22, weight="bold"),
                                Text(
                                    "Advanced Python-Flet UI Concepts",
                                    size=13,
                                    weight="bold",
                                )
                            ]
                        ),
                        Divider(height=20, color='transparent'),
                        # "Next, we have the input fields"
                        UserInputField(
                            icons.PERSON_ROUNDED,
                            "Email",
                            False,
                        ),
                        Divider(height=2, color='transparent'),
                        UserInputField(
                            icons.LOCK_OPEN_ROUNDED, 
                            "Password",
                            True,
                        ),
                    ],
                ),
            ),
        )
    )
    page.update()
    animate_boxes()

if __name__ == "__main__":
    flet.app(target=main)
