import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from functools import partial

class Test(toga.App):

    def f(self, widget, f_var):
        print(f_var.value)

    def fg(self, widget, f_var, g_var):
        print(f_var.value, g_var.value)

    def startup(self):

        self.f_var = 'my param f'
        self.font_size = 20
        main_box = toga.Box(style=Pack(direction=COLUMN))

        f_lbl = toga.Label("Label f()", style=Pack(font_size=self.font_size)) #____________________________
        f_box = toga.Box(style=Pack(direction=ROW,))
        f_box.add(f_lbl)
        self.f_input = toga.TextInput(value="f_input", style=Pack(flex=1, font_size=self.font_size))
        f_box.add(self.f_input)
        f_btn = toga.Button('Function f', on_press=partial(self.f,   f_var=self.f_input))
        #f_btn = toga.Button('Function fg', on_press=partial(self.fg, f_var=self.f_input, g_var=self.g_input))
        f_btn.style.update(font_size=self.font_size, color='red')
        f_box.add(f_btn)

        g_lbl = toga.Label("Label fg()", style=Pack(font_size=self.font_size)) #___________________________
        g_box = toga.Box(style=Pack(direction=ROW))
        g_box.add(g_lbl)
        self.g_input = toga.TextInput(value="g_input", style=Pack(flex=1, font_size=self.font_size))
        g_box.add(self.g_input)
        g_btn = toga.Button('Function fg', on_press=partial(self.fg, f_var=self.f_input, g_var=self.g_input))
        g_btn.style.update(font_size=self.font_size, color='green')
        g_box.add(g_btn)


        main_box.add(f_box)
        main_box.add(g_box)

        self.main_window = toga.MainWindow(title=self.formal_name, size=(410, 110))
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return Test()
'''
f_input
f_input g_var_lbl
'''
