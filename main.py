from kivy.app import App
from kivy.uix.label import Label
from agents.render_kernel_bridge import render_headless
import logging

class NeoEngineApp(App):
    def build(self):
        try:
            result = render_headless(
                pipeline="deferred_pbr_sovereign", 
                passes=["gbuffer", "lighting", "post"]
            )
            return Label(
                text=f"NEOENGINE ONLINE\nStatus: {result['mode']}\nPipeline: {result['pipeline']}\nGraph: VALID",
                halign='center', font_size='14sp'
            )
        except Exception as e:
            return Label(text=f"KERNEL ERROR: {str(e)}", color=(1,0,0,1))

if __name__ == "__main__":
    NeoEngineApp().run()
