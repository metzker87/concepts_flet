import flet
from flet import *
import time 
from math import pi


class SignInButton(UserControl):
    def __init__(self, btn_name):
        self.btn_name = btn_name
        super().__init__()
    def build(self):
        return Container(
            content=ElevatedButton(
                content=Text(
                    self.btn_name,
                    size=13,
                    weight='bold',
                ),
                style=ButtonStyle(
                    shape={
                        "": RoundedRectangleBorder(radius=8),
                    },
                    color={
                        "": "black",
                    },
                    bgcolor={
                        "": "#7df6dd"
                    },
                ),
                height=42,
                width=320,
            ),
        )


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
    # "Before getting the email extensions, we need to create a paramter in order to select which input field will generate this functionality. The email field will do so, but the password will not."
    # "Here's one way to set up the logic"

    def __init__(self, icon_name, text_hint, hide, function_emails:bool, function_check:bool):
        self.icon_name = icon_name
        self.text_hint = text_hint
        self.hide = hide
        self.function_emails = function_emails
        self.function_check = function_check
        super().__init__()


    # function to fill in email extension
    def return_email_prefix(self, e):
        email = self.controls[0].content.controls[1].value
        if e.control.data in email:
            pass
        else:
            self.controls[0].content.controls[1].value += e.control.data
            self.controls[0].content.controls[2].offset = transform.Offset(0.5, 0)
            self.controls[0].content.controls[2].opacity = 0
            self.update()


    # Generating the email extension when the user starts typing in his/her email
    def prefix_email_containers(self):
        email_labels = ["@gmail.com", "@outlook.com"]
        label_title = ["GMAIL", "MAIL"]
        __ = Row(
            spacing=1,
            alignment=MainAxisAlignment.END,
        )
        for index, label in enumerate(email_labels):
            # "We will append a container for each email server"
            __.controls.append(
                Container(
                    width=45,
                    height=30,
                    alignment=alignment.center,
                    data=label,
                    on_click=lambda e: self.return_email_prefix(e), # change later
                    content=Text(
                        label_title[index],
                        size=9,
                        weight='bold',
                    ),
                ),
            )
        return Row(
            vertical_alignment=CrossAxisAlignment.CENTER,
            alignment=MainAxisAlignment.END,
            spacing=2,
            opacity=0, # change to 0
            animate_opacity=200,
            offset=transform.Offset(0.35, 0),
            animate_offset=animation.Animation(400, 'decelerate'),
            controls=[__]
        )
    

    # 

    # "Now we can do one to simulate a green OK check mark."
    # "This can be used during status OK authentication"
    def off_focus_input_check(self):
        return Container(
            opacity=0,
            offset=transform.Offset(0, 0),
            animate=200,
            border_radius=6,
            width=18,
            height=18,
            alignment=alignment.center,
            content=Checkbox(
                fill_color="#7df6dd",
                check_color="black",
                disabled=True,
            ),
        )


    def get_prefix_emails(self, e):
        # "Now in the class instance below, we passed a true for the email and a false for the password"
        # "Now we can check these booleans here and aonly animate the emails for the true parameters."
        if self.function_emails: # so if the instance has this as True
            # get the email value
            email = self.controls[0].content.controls[1].value
            # check if user is typing
            if e.data:
                if "@gmail.com" in email or "@outlook.com" in email:
                    # if these names as in the field already, remove the extensions
                    self.controls[0].content.controls[2].offset = transform.Offset(0, 0)
                    self.controls[0].content.controls[2].opacity = 0
                    self.update()
                else:
                    # if the above strings are in the field
                    #  we can animate the extensions visible
                    self.controls[0].content.controls[2].offset = transform.Offset(-0.15, 0)
                    self.controls[0].content.controls[2].opacity = 1
                    self.update()
            else:
                self.controls[0].content.controls[2].offset = transform.Offset(0.5, 0)
                self.controls[0].content.controls[2].opacity = 0
                self.update()
        else: # "heref, since the password instance we created has this set to false, the code won't generate the extensions."
            pass


    # "In order to simulate the green checks, we need to follow the same logic as the email extensions"
    # "First we need to see which fields will have this property"
    def get_green_check(self, e):
        if self.function_check:
            email = self.controls[0].content.controls[1].value
            password = self.controls[0].content.controls[1].password
            if email:
                if "@gmail.com" in email or "@outlook.com" in email or password:
                    time.sleep(0.5)
                    self.controls[0].content.controls[3].offset = transform.Offset(-2, 0)
                    self.controls[0].content.controls[3].opacity = 1
                    self.update()
                    time.sleep(0.2)
                    self.controls[0].content.controls[3].content.value = True
                    time.sleep(0.1)
                    self.update()
                else:
                    self.controls[0].content.controls[3].offset = transform.Offset(0, 0)
                    self.controls[0].content.controls[3].opacity = 0
                    self.update()
        else:
            pass


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
                        on_change=lambda e: self.get_prefix_emails(
                            e
                        ),
                        on_blur=lambda e: self.get_green_check(e), # also change later...
                    ),
                    # "We are gonna display the items here..."
                    # "in hindsight, these could also be done using a SATCK() widget, but either method works"
                    self.prefix_email_containers(),
                    self.off_focus_input_check(),
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
                            True,
                            True,
                        ),
                        Divider(height=2, color='transparent'),
                        UserInputField(
                            icons.LOCK_OPEN_ROUNDED, 
                            "Password",
                            True,
                            False,
                            True,
                        ),
                        Divider(height=2, color='transparent'),
                        Row(
                            width=320,
                            alignment=MainAxisAlignment.END,
                            controls=[
                                Text('Forgot Password?', size=8.5),
                            ],
                        ),
                        Divider(height=45, color='transparent'),
                        # button for sign in 
                        SignInButton('Sign In'),
                        Divider(height=45, color='transparent'),
                        Text(
                            'Footer text goes in here.',
                            size=10,
                            color='white54',
                        ),
                    ],
                ),
            ),
        )
    )
    page.update()
    animate_boxes()

if __name__ == "__main__":
    # Configure my local server to use port 5000 for the web browser view
    flet.app(target=main, view=flet.AppView.WEB_BROWSER, port=5000)
