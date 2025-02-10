import tkinter as tk
from ..crawler.collector import KreamCollector
from ..utils.excel import Excel

class KreamHarvesterApp:
    def __init__(self):
        self.collector = KreamCollector()
        self.excel = Excel()
        # GUI 초기화 로직 