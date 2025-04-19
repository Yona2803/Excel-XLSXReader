import os
import time
import tkinter as tk
import customtkinter as ctk
from PIL import ImageColor, Image, ImageDraw, ImageTk
from Style.UiConfig import ThemeManager, ContentStyles, LayoutSettings

class XLSXReaderApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.theme_manager = ThemeManager()
        window_settings = LayoutSettings.get_window_settings()
        self.title(window_settings["title"])
        self.geometry(window_settings["geometry"])
        self.minsize(*window_settings["minsize"])
        self.resizable(*window_settings["resizable"])
        self.iconbitmap(window_settings["Logo"])

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")


    def on_closing(self):
        """Clean up resources when closing the application"""
        # Destroy the window
        self.destroy()

if __name__ == "__main__":
    app = XLSXReaderApp()
    # Set up proper cleanup when closing the window
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()