from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.clock import Clock
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import OneLineListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFillRoundFlatButton, MDRectangleFlatIconButton
import webbrowser
from kivymd.uix.pickers import MDDatePicker, MDTimePicker



class Info(MDFloatLayout):
    Builder.load_file('add_event.kv')


class Ticketfy(MDApp):
    dialog = None
    def build(self):
        self.theme_cls.primary_palette = "Red"
        
        global sm
        sm = ScreenManager()
        sm.add_widget(Builder.load_file("welcome.kv"))
        sm.add_widget(Builder.load_file("load.kv"))   
        sm.add_widget(Builder.load_file("home.kv"))
        sm.add_widget(Builder.load_file("bank.kv"))
        sm.add_widget(Builder.load_file("account.kv"))
        sm.add_widget(Builder.load_file("eventhome.kv"))
        sm.add_widget(Builder.load_file("cart.kv"))
        sm.add_widget(Builder.load_file("ticket.kv"))  
        sm.add_widget(Builder.load_file("notify.kv"))
        sm.add_widget(Builder.load_file("service.kv"))
        sm.add_widget(Builder.load_file("login.kv"))
        sm.add_widget(Builder.load_file("signup.kv"))
        return sm
    
    def on_start(self):
        Clock.schedule_once(self.load, 4)


    def load(self, *args):
        sm.current = "load"
    
    def open_link(self, url):
        webbrowser.open(url)
        

    def date_picker(self):
        date_dialog = MDDatePicker()

        #date_dialog.bind(on_save = self.on_save)
        date_dialog.open()
        

    def time_picker(self):
        date_dialog = MDTimePicker()
        #date_dialog.bind(on_save = self.on_save)
        date_dialog.open()


    def open_dialog_box(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Add Event",
                type="custom",
                content_cls=Info(),
                buttons = {
                    MDRectangleFlatIconButton(text='Cancel', on_release = self.submit),
                    MDFillRoundFlatButton(text='Submit', on_release = self.submit)
                },
                on_dismiss=self.reset_dialog
            )
        self.dialog.open()

    def reset_dialog(self, *args):
        self.dialog = None


    def submit(self, *args):
        self.dialog.dismiss(force=True)
 
    


    

if __name__ == "__main__":
    Ticketfy().run()

