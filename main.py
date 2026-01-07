import logging
import traceback
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from core.render_kernel.abi import RenderABI

logging.basicConfig(level=logging.DEBUG)

class SovereignApp(App):
    def build(self):
        try:
            # Simulasi Pemanggilan Kernel Render
            # Ini adalah tahap FASE 1: Mengunci Kernel
            manifest = RenderABI.create_manifest(
                pipeline_name="deferred_pbr_sovereign",
                passes=["gbuffer", "lighting", "shadow_map", "post_process"]
            )
            
            layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
            
            title = Label(text="NEOENGINE KERNEL ONLINE", font_size='24sp', bold=True, color=(0, 1, 0, 1))
            status = Label(text=f"ABI Status: {manifest['status']}\nPipeline: {manifest['pipeline']}", 
                          halign='center', font_size='14sp')
            metrics = Label(text=f"Integrity: {manifest['metrics']['node_integrity']}\nVisual Adapter: WAITING", 
                           color=(0.7, 0.7, 0.7, 1), font_size='12sp')
            
            layout.add_widget(title)
            layout.add_widget(status)
            layout.add_widget(metrics)
            
            return layout
            
        except Exception as e:
            error_msg = f"KERNEL PANIC:\n{str(e)}\n\n{traceback.format_exc()}"
            logging.error(error_msg)
            return Label(text=error_msg, color=(1, 0, 0, 1), font_size='10sp')

if __name__ == "__main__":
    SovereignApp().run()
