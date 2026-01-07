from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from core.render_kernel.abi import RenderABI
from agents.BaseAgent import BaseAgent

class SovereignApp(App):
    def build(self):
        wg = BaseAgent._world_graph
        
        # Trigger event awal sebagai tanda boot
        BaseAgent.emit_kernel_event("SovereignSystem", "BOOT", {"status": "SUCCESS"})
        
        manifest = RenderABI.create_manifest("SOVEREIGN_DEBUG_PIPELINE", wg)
        
        root = BoxLayout(orientation='vertical', padding=10)
        header = Label(text="NEOENGINE KERNEL v1.1", size_hint_y=0.1, bold=True, color=(0, 1, 0, 1))
        
        content = ScrollView()
        log_label = Label(
            text=f"PIPELINE: {manifest['pipeline']}\n"
                 f"NODES IN GRAPH: {manifest['world_state']['nodes']}\n"
                 f"LATEST SNAPSHOT:\n{manifest['graph_snapshot']}",
            size_hint_y=None,
            halign='left',
            valign='top'
        )
        log_label.bind(texture_size=log_label.setter('size'))
        
        content.add_widget(log_label)
        root.add_widget(header)
        root.add_widget(content)
        
        return root

if __name__ == "__main__":
    SovereignApp().run()
