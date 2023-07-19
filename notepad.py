from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import filedialog
from collections import deque


class Window:
    def __init__(self, master):
        self.master = master
        #self.master.option_add("*Font", "Verdana 9")
        self.master.option_add('*tearOff', FALSE)
        # ----------
        self.stack = deque(maxlen=10)
        self.stackcursor = 0
        # ----------
        self.T1 = Text(self.master, font='consolas 12', width=725, height=450)
        self.T1.pack(fill=BOTH)
        # ----------

        self.menu = Menu(self.master)
        self.menu_file = Menu(self.menu)
        self.menu_edit = Menu(self.menu)
        # ----------

        self.menu.add_cascade(menu=self.menu_file, label='File')
        self.menu.add_cascade(menu=self.menu_edit, label='Edit')

        self.menu_file.add_command(label='Open', command=self.open_file)
        self.menu_file.add_command(label='Save', command=self.save)


        self.menu_change_font_size = Menu(self.menu_edit)
        self.menu_change_font_family = Menu(self.menu_edit)
        self.menu_change_font_style = Menu(self.menu_edit)
        self.menu_change_font_color = Menu(self.menu_edit)

        self.menu_edit.add_cascade(menu=self.menu_change_font_size, label='Font size')
        self.menu_edit.add_cascade(menu=self.menu_change_font_family, label='Font family')
        self.menu_edit.add_cascade(menu=self.menu_change_font_style, label='Font style')
        self.menu_edit.add_command(label="Font color", command=self.change_font_color)

        global actual_font
        global actual_size
        global actual_style

        actual_font = 'consolas'
        actual_size = '12'
        actual_style = 'normal'

        self.menu_change_font_size.add_command(label='10', command=lambda: self.change_font_size('10'))
        self.menu_change_font_size.add_command(label='12', command=lambda: self.change_font_size('12'))
        self.menu_change_font_size.add_command(label='14', command=lambda: self.change_font_size('14'))
        self.menu_change_font_size.add_command(label='16', command=lambda: self.change_font_size('16'))
        self.menu_change_font_size.add_command(label='18', command=lambda: self.change_font_size('18'))
        self.menu_change_font_size.add_command(label='20', command=lambda: self.change_font_size('20'))
        self.menu_change_font_size.add_command(label='22', command=lambda: self.change_font_size('22'))
        self.menu_change_font_size.add_command(label='24', command=lambda: self.change_font_size('24'))
        self.menu_change_font_size.add_command(label='26', command=lambda: self.change_font_size('26'))
        self.menu_change_font_size.add_command(label='28', command=lambda: self.change_font_size('28'))
        self.menu_change_font_size.add_command(label='30', command=lambda: self.change_font_size('30'))
        self.menu_change_font_size.add_command(label='32', command=lambda: self.change_font_size('32'))
        self.menu_change_font_size.add_command(label='34', command=lambda: self.change_font_size('34'))
        self.menu_change_font_size.add_command(label='36', command=lambda: self.change_font_size('36'))
        self.menu_change_font_size.add_command(label='38', command=lambda: self.change_font_size('38'))
        self.menu_change_font_size.add_command(label='40', command=lambda: self.change_font_size('40'))

        # ----------

        self.menu_change_font_family.add_command(label='Arial', command=lambda: self.change_font_family('arial'))
        self.menu_change_font_family.add_command(label='Impact', command=lambda: self.change_font_family('impact'))
        self.menu_change_font_family.add_command(label='Georgia', command=lambda: self.change_font_family('georgia'))
        self.menu_change_font_family.add_command(label='Consolas', command=lambda: self.change_font_family('consolas'))
        self.menu_change_font_family.add_command(label='Courier', command=lambda: self.change_font_family('courier'))
        self.menu_change_font_family.add_command(label='Dinengschrift',
                                                 command=lambda: self.change_font_family('dinengschrift'))

        # ----------

        self.menu_change_font_style.add_command(label='Normal', command=lambda: self.change_font_style('normal'))
        self.menu_change_font_style.add_command(label='Bold', command=lambda: self.change_font_style('bold'))

        # ----------
        self.menu.add_command(label='Clear', command=self.clear)
        self.menu.add_command(label='Undo', command=self.undo)
        self.menu.add_command(label='Redo', command=self.redo)

        # ----------
        self.menu_theme = Menu(self.menu)
        self.menu.add_cascade(menu=self.menu_theme, label='Themes')

        self.menu_theme.add_command(label='Custom solid', command= self.change_theme_custom)
        self.menu_theme.add_command(label='Default', command=lambda: self.change_theme('white', 'black'))
        self.menu_theme.add_command(label='Exagerated blue', command=lambda: self.change_theme('blue', 'white'))
        self.menu_theme.add_command(label='Night mode', command=lambda: self.change_theme('grey', 'white'))
        self.menu_theme.add_command(label='Matrix', command=lambda: self.change_theme('green', 'black'))
        self.menu_theme.add_command(label='Blood (it sucks)', command=lambda: self.change_theme('red', 'white'))

        # ----------
        self.menu.add_command(label='About', command=self.about)

        # ----------
        self.master.config(menu=self.menu)

    def save(self):
        save_as = filedialog.asksaveasfilename(title='Save file', initialdir='D:\Diogo\Documents',
                                                 defaultextension='.txt')
        text_output = self.T1.get('0.0', 'end')
        with open(f'{save_as}', 'w') as f:
            f.write(str(text_output))

        global file_name
        file_name = str(save_as)
        app_title()

    def change_font_size(self, size):
        global actual_size
        actual_size = size
        self.T1.config(font=(f'{actual_font} {actual_size}'))

    def change_font_family(self, font):
        global actual_font
        actual_font = font
        self.T1.config(font=f'{actual_font}')

    def change_font_style(self, weight):
        global actual_style
        actual_style = weight
        self.T1.config(font=(f'{actual_font} {actual_size} {actual_style}'))

    def change_font_color(self):
        color = askcolor(color=None)
        self.T1.config(fg=color[1])


    def open_file(self):
        file_opened = filedialog.askopenfile(title='Open file', initialdir='D:\Diogo\Documents',
                                                 filetypes=(("txt", "*.txt"), ("HTML", "*.html")),
                                                 defaultextension='.txt')

        text_from_opened = str(file_opened.read())
        self.T1.delete('0.0', 'end')
        self.T1.insert('0.0', text_from_opened)
        global file_name
        file_name = file_opened.name
        app_title()

    def clear(self):
        self.T1.delete('1.0', END)

    def stackify(self):
        self.stack.append(self.T1.get('1.0', 'end - 1c'))
        if self.stackcursor < 9: self.stackcursor += 1

    def undo(self):
        if self.stackcursor != 0:
            self.clear()
            if self.stackcursor > 0: self.stackcursor -= 1
            self.T1.insert('0.0', self.stack[self.stackcursor])

    def redo(self):
        if len(self.stack) > self.stackcursor + 1:
            self.clear()
            if self.stackcursor < 9: self.stackcursor += 1
            self.T1.insert('0.0', self.stack[self.stackcursor])

    def change_theme(self, bg, fg):
        self.T1.config(foreground=fg, background=bg)
        self.menu_file.config(foreground=fg, background=bg)
        self.menu_edit.config(foreground=fg, background=bg)
        self.menu_change_font_family.config(foreground=fg, background=bg)
        self.menu_change_font_size.config(foreground=fg, background=bg)
        self.menu_theme.config(foreground=fg, background=bg)
        self.menu_change_font_style.config(foreground=fg, background=bg)

    def change_theme_custom(self):
        bg_color = askcolor(color=None)
        fg_color = askcolor(color="Black")
        self.T1.config(background=bg_color[1], fg=fg_color[1])
        self.menu_file.config(background=bg_color[1], fg=fg_color[1])
        self.menu_edit.config(background=bg_color[1], fg=fg_color[1])
        self.menu_change_font_color.config(background=bg_color[1], fg=fg_color[1])
        self.menu_change_font_size.config(background=bg_color[1], fg=fg_color[1])
        self.menu_change_font_style.config(background=bg_color[1], fg=fg_color[1])
        self.menu_change_font_family.config(background=bg_color[1], fg=fg_color[1])
        self.menu_theme.config(background=bg_color[1], fg=fg_color[1])


    def about(self):
        about_window = Toplevel(self.master)
        about_window.geometry('250x350')
        about_window.title('About')
        about_window.iconbitmap(r"src/notepad_icon.ico")
        about_window.resizable(width=False, height=False)

        T1_content = self.T1.get('0.0', 'end')

        if T1_content.__contains__('oi diogo, vim falar com você.'):
            self.T1.delete('0.0', 'end')
            self.T1.insert('0.0',
                           'Easter egg\nEspero que esteja bem!, como recompensa, toma aqui um pedaço: !3>|cF\nSomos capazes? honestamente, não sei. independente de como você estiver, te desejo toda a sorte, confio muito em ti.')

        Label(about_window, text='Notepad made in Python\nwith TKinter GUI\nver. 1.0', font=('Courier 14 bold')).pack(
            ipady=10)
        Label(about_window, text='Kodachi\n26/06/2023').pack(ipady=10, ipadx=10, fill=X)


root = Tk()


root.iconbitmap(r"src/notepad_icon.ico")
root.geometry('725x450')
root.resizable(width=True, height=True)
window = Window(root)
root.bind('<Key>', lambda event: window.stackify())

def app_title():
    if "file_name" in globals():
        root.title(f"{file_name} - Notepad")
    else:
        root.title("Untitled - Notepad")

root.title("Untitled - Notepad")
root.mainloop()
