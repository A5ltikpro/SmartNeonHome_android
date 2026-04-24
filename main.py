from kivy.app import App
# from kivy.uix.image import Image


class MyApp(App):
    def greet(self):
        # Получаем текст из TextInput по его ID
        name = self.root.ids.user_input.text
        # Меняем текст у Label по его ID
        self.root.ids.output_label.text = f'Привет, {name}!'

class IndexApp(App):
    def build(self):
        local_data_id = self.root.ids.input_text.text
        if local_data_id != '':
            print("True", local_data_id)




if __name__ == '__main__':
    IndexApp().run()