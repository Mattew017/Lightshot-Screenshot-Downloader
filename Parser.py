import tkinter as tk
import os
import tkinter.filedialog as fd
import Downloader


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.count_of_images = 0
        self.path_to_save = os.getcwd()

        self.btn_dir = tk.Button(self, text="Выбрать папку", command=self.choose_directory)
        self.lbl = tk.Label(self, text="Введите количество картинок:")
        self.btn_start = tk.Button(self, text="Старт", command=self.start_downloading)
        self.text = tk.Entry(self)
        self.btn_count = tk.Button(self, text="OK", command=self.input_count)

        self.lbl.pack()
        self.text.pack()
        self.btn_count.pack()
        self.btn_dir.pack()
        self.btn_start.pack()

    def input_count(self):
        try:
            self.count_of_images = int(self.text.get())
            self.lbl['text']= f"Будет скачано {self.count_of_images} картинок"
        except BaseException as error:
            self.lbl['text']= "Неправильный ввод! Число должно быть натуральным!\nВведите количество картинок:"

    def start_downloading(self):
        downloader = Downloader.LightLoader(self.count_of_images, self.path_to_save)
        downloader.run()

    def choose_directory(self):
        directory = fd.askdirectory(title="Открыть папку", initialdir="/")
        if directory:
            self.path_to_save = directory


if __name__ == "__main__":
    app = App()
    app.mainloop()
