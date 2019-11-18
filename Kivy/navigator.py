from kivy.app import App
from kivy.lang import Builder
from kivymd.theming import ThemeManager

kv=Builder.load_file("application.kv")

#class NavigationDrawer()

class Application(App):
    theme_cls = ThemeManager()

if __name__== "__main__":
    Application.run((Application()))