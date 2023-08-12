from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

class UserInterface(GridLayout):
    '''
    A class to design the graphic interface:
    - construct layout grids
    - add widgets to grids
    - attach methods to widgets
    '''
    def __init__(self, **kwargs):
        super(UserInterface, self).__init__(**kwargs)
        # set fixed window size
        Window.size = (700, 600)
        
        # window *main grid layout) settings
        self.cols = 1
        self.spacing = 20 # vertical spacing
        self.size_hint = (0.6, 0.7)
        self.pos_hint = {"center_x": 0.5, "center_y":0.5}
        
        # create additional grid layout for a,b,c inputs and their labels
        self.inputs = GridLayout()
        # set inputs columns to 6 while the rest of the window remains with only 1
        self.inputs.cols = 6 

        # add image widgets
        self.add_widget(Image(source="assets/diagram.png"))
        self.add_widget(Image(source="assets/logo.png"))

        # add label widget
        self.message = Label(
                        text= "please enter 2 triangle sides lengths to get the 3rd",
                        font_size= 25,
                        color= '#FFFFFF',
                        halign="center"
                        )
        self.add_widget(self.message)
        
        # START: INPUTS GRID WIDGETS
        #############################

        # create input widgets
        self.label_a = Label(
                        text= "a",
                        font_size= 25,
                        color= '#FFFFFF'
                        )

        self.input_a = TextInput(
                    multiline= False,
                    font_size= 25,
                    padding= [20,35],
                    halign="center",
                    input_type="number",
                    input_filter="float"
                    )

        self.label_b = Label(
                        text= "b",
                        font_size= 25,
                        color= '#FFFFFF'
                        )

        self.input_b = TextInput(
                    multiline= False,
                    font_size= 25,
                    padding= [20,35],
                    halign="center",
                    input_type="number",
                    input_filter="float"
                    )

        self.label_c = Label(
                        text= "c",
                        font_size= 25,
                        color= '#FFFFFF'
                        )

        self.input_c = TextInput(
                    multiline= False,
                    font_size= 25,
                    padding= [20,35],
                    halign="center",
                    input_type="number",
                    input_filter="float"
                    )

        # add inputs to inputs grid
        self.inputs.add_widget(self.label_a)
        self.inputs.add_widget(self.input_a)
        self.inputs.add_widget(self.label_b)
        self.inputs.add_widget(self.input_b)
        self.inputs.add_widget(self.label_c)
        self.inputs.add_widget(self.input_c)

        # add inputs grid to window
        self.add_widget(self.inputs)

        # END: INPUTS GRID WIDGETS
        #############################
        
        # submit button widget
        self.button = Button(
                      text= "SUBMIT",
                      bold= True,
                      background_color ='#00FFCE',
                      )
        self.button.bind(on_press=self.callback)
        self.add_widget(self.button)

    def callback(self, this_button):
        '''
        a method executed each time the submit button is pressed
        '''
        # get result dictionary
        output = self.pythagorean()
        # fetch dictionary key
        key = list(output.keys())[0]

        # display value on the UI
        self.message.text = str(output[key])

    def pythagorean(self):
        a = self.input_a.text # leg
        b = self.input_b.text #leg
        c = self.input_c.text # hypotenuse

        if a == "" and b!="" and c!="":
            # find a
            b = float(b)
            c = float(c)
            a = (c**2 - b**2)**(1/2)
            return {"a": a}

        elif b == "" and a!="" and c!="":
            # find b
            a = float(a)
            c = float(c)
            b = (c**2-a**2)**(1/2)
            return {"b": b}

        elif c == "" and a!="" and b!="":
            # find c
            a = float(a)
            b = float(b)
            c = (a**2+b**2)**(1/2)   
            return {"c": c}

        elif a=="" and b=="" and c=="":
            # 0 arguments provided
            return {"error": "oops! no input was recieved! please enter 2 side lengths to get the 3rd!"}

        elif (a=="" and b=="" and c!="") or (a=="" and c=="" and b!="") or (b=="" and c=="" and a!=""):
            return {"error": "please enter one more side length to get the third!"}

        elif a!="" and b!="" and c!="":
            return {"error": "if you already know ALL sides then you don't need me!"}
        
        else:
            return {"error": "an unexpected error has occured. please try again"}

class Pythagorean(App):
    '''
    a class that builds the app based on the design of class::UserInterface
    '''
    def build(self):
        return UserInterface()

if __name__ == "__main__":
    Pythagorean().run()