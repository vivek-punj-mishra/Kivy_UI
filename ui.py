from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
import sqlite3

#Define our different screens
class LoginWindow(Screen):
    pass
class NotifyWindow(Screen):
    pass

class RewardsWindow(Screen):
    pass


class MailWindow(Screen):
    pass

class ChatWindow(Screen):
    pass

class PayWindow(Screen):
    pass

class SearchWindow(Screen):
    pass

class GamesWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass


class UiApp(MDApp):
    dialog = None
    
    def verify(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        conn = sqlite3.connect('first_db.db')

        #Create A Cursor
        c = conn.cursor()
                                                    
        c.execute("SELECT * FROM customers;")

        user = self.root.ids["user"].text
        pswd = self.root.ids["password"].text

        c.execute('SELECT * from customers WHERE name ="%s" AND password="%s"' % (user, pswd))
        if c.fetchall():
            self.manager.current = "user"
        #Clear the input box
        #self.root.ids.user.text=''
        #self.root.ids.password.text = ''

        #Show alert dailog
        if not self.dialog:
                # create dialog
                self.dialog = MDDialog(
                    title="Log In",
                    text=f"Welcome {self.root.ids.user.text}!",
                    buttons=[
                        MDFlatButton(
                            text="Ok", text_color=self.theme_cls.primary_color,
                            on_release=self.close
                        ),
                    ],
                )
        # open and display dialog
        self.dialog.open()

    def close(self, instance):
        # close dialog
        self.dialog.dismiss()    

    def clear(self):
        self.root.ids.welcome_label.text = "WELCOME"
        self.root.ids.user.text = ""
        self.root.ids.password.text = ""
    def builder(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('ui.kv')
        
UiApp().run()
