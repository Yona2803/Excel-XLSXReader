from customtkinter import CTkImage
from PIL import Image
import os


class ThemeManager:
    # def __init__(self, ):
    #     # self.is_dark_mode = is_dark_mode

    def define_colors(self):
        self.primaryColor = "#242424"
        self.secondaryColor = "#2F2F2F"
        self.tertiaryColor_ON = "#4CD951"
        self.tertiaryColor_OFF = "#D94C4E"
        self.font_Main = "#C8C8C8"
        self.font_Secondary = "#D0D0D0"
        self.font_Tertiary = "#F9F7FF"
        self.base_bg = "#8265FC"
        self.hover_bg = "#B562E7"
        self.active_bg = "#424242"
        self.code_font = "#939DA7"
        self.code_bg = "#1F2831"

    @staticmethod
    def Icons(name):
        path = f"Assets/Icons/{name}.png"
        if os.path.exists(path):
            return {"icon": CTkImage(Image.open(path), size=(16, 16))}


class ContentStyles:
    @staticmethod
    def get_Main_Title(text):
        return {
            "text": text,
            "font": ("Jura", 24),
            "justify": "center",
        }


class LayoutSettings:
    @staticmethod
    def get_Text_layout():
        return [
            ("How can I help you today?", "Main"),
            ("Message Lamsa-Ai...", "Secondary"),
        ]

    @staticmethod
    def get_window_settings():
        return {
            "title": "Excel XLSX-Reader",
            "geometry": "850x550",
            "minsize": (640, 320),
            "resizable": (True, True),
            "Logo": os.path.abspath("Assets/Logo/Logo.ico"),
        }
