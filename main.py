from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.utils import platform
import traceback
import sys
import os

# PATH FIX FOR ANDROID NAMESPACE
if platform == 'android':
    sys.path.append(os.path.abspath(os.path.dirname(__file__)))

try:
    from core.render_kernel.abi import RenderABI
    from agents.BaseAgent import BaseAgent
except ImportError as e:
    RenderABI = None
    BaseAgent = None
    print(f"KERNEL_IMPORT_ERROR: {e}")

class FEACUltimateApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical', padding=10)
        
        # HEADER UI
        header = Label(
            text="FEAC ULTIMATE - SOVEREIGN SHELL", 
            size_hint_y=0.1, 
            bold=True, 
            color=(0, 0.8, 1, 1)
        )
        root.add_widget(header)

        if RenderABI and BaseAgent:
            try:
                wg = BaseAgent._world_graph
                manifest = RenderABI.create_manifest("FEAC_MOBILE_PIPELINE", wg)
                
                content = ScrollView()
                log_label = Label(
                    text=f"STATUS: KERNEL LINKED\nNODES: {len(wg.nodes)}\nPIPELINE: {manifest['pipeline']}",
                    size_hint_y=None,
                    halign='left'
                )
                log_label.bind(texture_size=log_label.setter('size'))
                content.add_widget(log_label)
                root.add_widget(content)
            except Exception as e:
                root.add_widget(Label(text=f"KERNEL_EXEC_ERROR: {str(e)}", color=(1, 0, 0, 1)))
        else:
            root.add_widget(Label(text="ERROR: INTERFACE NOT FOUND\nCHECK CORE/ AND AGENTS/ FOLDERS", color=(1, 0.5, 0, 1)))
            
        return root

if __name__ == "__main__":
    FEACUltimateApp().run()
