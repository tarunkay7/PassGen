from random import *
import kivy.uix.textinput
from kivy.app import App
from kivy.core.clipboard import Clipboard
from kivy.core.text import LabelBase

from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout

kivy.require('1.9.0')

LabelBase.register(name="ubuntubold", fn_regular="nunito-bold.ttf")
LabelBase.register(name="nunito", fn_regular="Ubuntu-Bold.ttf")


class Myroot(BoxLayout):

    def __init__(self):
        super(Myroot, self).__init__()

    def generate_number(self):
        text = self.ids.input.text

        try:
            if int(text) <= 25:
                smallletters = [chr(i) for i in range(97, 123)]
                capletters = [chr(i) for i in range(65, 90)]
                numbers = list(range(10))
                special = [chr(i) for i in range(33, 48)]
                lst = smallletters + capletters + numbers + special
                str1 = ""
                self.ids.random_label.text = str1.join([str(choice(lst)) for _ in range(int(text))])
                Clipboard.copy(self.ids.random_label.text)
                Factory.mypopup().open()
                if 5 <= int(text) <= 10:
                    self.ids.pisoot.color = (196 / 255, 94 / 255, 94 / 255)
                    self.ids.pisoot.text = "WEAK"
                elif 10 < int(text) <= 15:
                    self.ids.pisoot.color = (94 / 255, 135 / 255, 196 / 255)
                    self.ids.pisoot.text = "MILDLY STRONG"
                elif 15 < int(text) <= 25:
                    self.ids.pisoot.color = (116 / 255, 196 / 255, 94 / 255)
                    self.ids.pisoot.text = " STRONG"
                else:
                    self.ids.random_label.text = "Please enter a number more than 5"

                    self.ids.pisoot.text = "-"
            else:
                self.ids.pisoot.text = "-"
                self.ids.random_label.text = "INVALID"
        except ValueError:
            self.ids.random_label.text = "Please Enter a Number"


class RandGen(App):

    def build(self):
        self.icon = "smile3.png"
        return Myroot()


randgen = RandGen()
randgen.run()
