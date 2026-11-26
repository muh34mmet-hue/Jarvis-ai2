from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (0.02, 0.04, 0.12, 1)

class JarvisApp(App):
    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=25,
            spacing=20
        )

        self.title_label = Label(
            text="[b]J.A.R.V.I.S[/b]\nSistem çevrimiçi",
            markup=True,
            font_size=28
        )

        self.output = Label(
            text="Merhaba efendim. Komutunuzu bekliyorum.",
            font_size=18
        )

        self.input = TextInput(
            hint_text="Jarvis'e bir şey sor...",
            size_hint_y=None,
            height=55,
            multiline=False
        )

        button = Button(
            text="GÖNDER",
            size_hint_y=None,
            height=55,
            background_color=(0, 0.4, 1, 1)
        )
        button.bind(on_press=self.respond)

        layout.add_widget(self.title_label)
        layout.add_widget(self.output)
        layout.add_widget(self.input)
        layout.add_widget(button)

        return layout

    def respond(self, instance):
        command = self.input.text.lower().strip()

        if "merhaba" in command:
            answer = "Merhaba efendim. Size nasıl yardımcı olabilirim?"
        elif "adın" in command:
            answer = "Ben JARVIS, kişisel asistanınız."
        elif "nasılsın" in command:
            answer = "Sistemlerim sorunsuz çalışıyor efendim."
        elif "saat" in command:
            from datetime import datetime
            answer = "Saat: " + datetime.now().strftime("%H:%M")
        elif "tarih" in command:
            from datetime import datetime
            answer = "Tarih: " + datetime.now().strftime("%d.%m.%Y")
        else:
            answer = "Bu komutu henüz öğrenmedim efendim."

        self.output.text = answer
        self.input.text = ""

if __name__ == "__main__":
    JarvisApp().run()
