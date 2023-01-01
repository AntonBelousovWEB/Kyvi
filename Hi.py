from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from plyer import gyroscope, vibrator

from kivy.clock import Clock

class MyBox(BoxLayout):    
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=10, spacing=10, **kwargs)       
        self.label = Label(text = '0', font_size = '30sp')
        self.add_widget(self.label)
        gyroscope.enable()
        Clock.schedule_interval(self.run_acceleration, 0.1)
        
     
    def run_acceleration(self, *args):
        print(gyroscope.rotation)
        try:
            if (gyroscope.rotation[0] >0.5 or
                gyroscope.rotation[0] < -0.5 or
                gyroscope.rotation[1] > 0.5 or
                gyroscope.rotation[1] < -0.5 or
                gyroscope.rotation[2] > 0.5 or
                gyroscope.rotation[2] < -0.5):
                iter = int(self.label.text)
                self.label.text = str(iter + 1)
                vibrator.vibrate(0.05)
        except:
            pass
    

class MyApp(App):
    def build(self):
        return MyBox()


app = MyApp()
app.run()
