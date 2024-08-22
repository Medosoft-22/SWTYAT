from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import vlc
import webbrowser

class AudioPlayerApp(App):
    def build(self):
        self.player = vlc.MediaPlayer()
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # إدخال القيمة
        self.value_input = TextInput(size_hint_y=None, height=40, multiline=False)
        layout.add_widget(Label(text=": أدخل القيمة", size_hint_y=None, height=40))
        layout.add_widget(self.value_input)

        # زر التشغيل
        play_button = Button(text="تشغيل", size_hint_y=None, height=50)
        play_button.bind(on_press=self.play_audio)
        layout.add_widget(play_button)

        # زر الإيقاف
        stop_button = Button(text="إيقاف", size_hint_y=None, height=50)
        stop_button.bind(on_press=self.stop_audio)
        layout.add_widget(stop_button)

        # معلومات المطور
        developer_label = Label(text="تطوير: أدهم حمدي", size_hint_y=None, height=40)
        layout.add_widget(developer_label)

        # رابط الفيسبوك
        facebook_button = Button(text="جروب كل حاجه في الدش", size_hint_y=None, height=50)
        facebook_button.bind(on_press=self.open_facebook)
        layout.add_widget(facebook_button)

        return layout

    def play_audio(self, instance):
        value = self.value_input.text
        url_map = {
            "adham1": "http://goradio.top/Orange-Audio1/mpegts?token=rNqboJ0-GFlkr2",
            "adham2": "http://goradio.top/Orange-Audio2/mpegts?token=rNqboJ0-GFlkr2",
            "adham3": "http://goradio.top/Orange-Audio3/mpegts?token=rNqboJ0-GFlkr2",
            "adham4": "http://goradio.top/Orange-Audio4/mpegts?token=rNqboJ0-GFlkr2"
        }
        url = url_map.get(value)
        if url:
            self.player.set_media(vlc.Media(url))
            self.player.play()
        else:
            print("قيمة غير صحيحة")

    def stop_audio(self, instance):
        self.player.stop()

    def open_facebook(self, instance):
        webbrowser.open("https://www.facebook.com/groups/adhamsat/")

if __name__ == '__main__':
    AudioPlayerApp().run()
