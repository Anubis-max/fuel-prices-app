import kivy
import requests
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

class MyGrid(BoxLayout, FloatLayout):
    pass

class MyApp(App):
    def build(self):
        Window.clearcolor = (0.113, 0.122, 0.129, 1)

        response =  requests.get('https://tool.orlen.pl/api/wholesalefuelprices')

        if response.status_code == 200:
            data = response.json()
            pb95_value = data[0]['value']
            diesel_value = data[2]['value']

            root = MyGrid()
            pb95_label = root.ids.pb95
            pb95_label.text = str(round((pb95_value / 1000) * (1 + 0.26), 2))

            diesel_label = root.ids.diesel
            diesel_label.text = str(round((diesel_value / 1000) * (1 + 0.26), 2))

            pb98_label = root.ids.pb98
            pb98_label.text = str(round((pb95_value / 1000) * (1 + 0.26) + 0.60, 2))

            diesel2_label = root.ids.diesel2
            diesel2_label.text = str(round((diesel_value / 1000) * (1 + 0.26), 2) + 0.20)


            pb95_label_tax = root.ids.pb95_tax
            pb95_label_tax.text = str(round((pb95_value / 1000), 2))

            diesel_label_tax = root.ids.diesel_tax
            diesel_label_tax.text = str(round((diesel_value / 1000), 2))

            pb98_label_tax = root.ids.pb98_tax
            pb98_label_tax.text = str(round((pb95_value / 1000) + 0.60, 2))

            diesel2_label_tax = root.ids.diesel2_tax
            diesel2_label_tax.text = str(round((diesel_value / 1000) + 0.20, 2))

        return root
    
if __name__ == "__main__":
    MyApp().run()
