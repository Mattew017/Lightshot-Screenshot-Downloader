import tkinter as tk
import tkinter.filedialog as fd
import Downloader 


class App(tk.Tk):
    is_started = False
    def __init__(self):
        super().__init__()
        btn_dir = tk.Button(self, text="Выбрать папку", command=self.choose_directory)
        btn_dir.pack(padx=60, pady=10)
        btn_start = tk.Button(self, text= "Старт", command = self.start_downloading)
        btn_start.pack(padx=10, pady=10)

    def start_downloading(self):
        if not self.is_started:
            downloader = Downloader.LightLoader(10, path_to_save)
            downloader.run()
            self.is_started = True

    def choose_directory(self):
        directory = fd.askdirectory(title="Открыть папку", initialdir="/")
        if directory:
            global path_to_save
            path_to_save = directory

if __name__ == "__main__":
    app = App()
    app.mainloop()
    
