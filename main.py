import os
import sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.utils import platform

# Path Fix for Local Modules
if platform == 'android':
    sys.path.append(os.path.abspath(os.path.dirname(__file__)))

class FEACShell(App):
    def build(self):
        root = BoxLayout(orientation='vertical', padding=10)
        
        try:
            from core.render_kernel.abi import RenderABI
            from agents.BaseAgent import BaseAgent
            
            # Jika berhasil load
            status_text = "[color=00ff00]KERNEL LINKED[/color]\nREADY FOR SOVEREIGN COMMAND"
        except ImportError as e:
            # Jika gagal load (Standard Jujur)
            status_text = f"[color=ff0000]KERNEL MISSING[/color]\nError: {str(e)}"

        root.add_widget(Label(
            text=f"FEAC ULTIMATE SHELL\n\n{status_text}",
            markup=True,
            halign='center'
        ))
        return root

if __name__ == "__main__":
    FEACShell().run()
