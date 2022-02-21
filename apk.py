from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import AsyncImage
from kivy.uix.textinput import TextInput

vodochkaL, viskarL, romL, budget, per,money = 0,0,0,0,0,0
tipbuhla = ''
class Application(App):
    def persons(self,instance):
        self.label.text = "Что ж, давайте начнем\nвведите количество персон"
        self.grid.remove_widget(self.but)
        self.inp = TextInput()
        self.subm = Button(text = "submit",on_press = self.money)
        self.grid.add_widget(self.inp)
        self.grid.add_widget(self.subm)

    def build(self):
        self.grid = GridLayout(cols = 1,spacing = 10)
        self.but = Button(text = "Начать!",font_size = 30, background_color = "cyan",on_press = self.persons)
        self.label = Label(text = "Добро пожаловать в мастерскую настроения!\nГотовы сделать выбор?",font_size = 30)

        self.grid.add_widget(self.label)
        self.grid.add_widget(self.but)
        return self.grid
    def money(self,obj):
        global per
        per = float(self.inp.text)
        self.grid.remove_widget(self.subm)
        self.label.text = "Хорошо, а каков бюджет?"
        self.subm = Button(text="submit", on_press=self.choice)
        self.grid.add_widget(self.subm)
    def choice(self,obj):
        global budget,money
        budget = float(self.inp.text)
        money = float(self.inp.text)
        self.label.text = "Бутылку какого напитка вы берете?"
        self.grid.remove_widget(self.inp)
        self.grid.remove_widget(self.subm)
        self.vodochka = Button(text = "Водочка!",font_size = 30, background_color = "cyan",on_press = self.vodochka1)
        self.whisky = Button(text="Вискарик!", font_size=30, background_color="cyan", on_press=self.viskarik)
        self.rom = Button(text="Ром!", font_size=30, background_color="cyan", on_press=self.rome)
        self.nothing = Button(text="Больше ничего не нужно, спасибо!", font_size=30, background_color="cyan", on_press=self.nothing1)

        self.grid.add_widget(self.vodochka)
        self.grid.add_widget(self.whisky)
        self.grid.add_widget(self.rom)
        self.grid.add_widget(self.nothing)
    def vodochka1(self,obj):
        global case
        case = 1
        self.label.text = "Выбираем водочку!"
        self.grid.remove_widget(self.vodochka)
        self.grid.remove_widget(self.whisky)
        self.grid.remove_widget(self.rom)
        self.grid.remove_widget(self.nothing)
        self.inp = TextInput(text = "Введите объем водочки")
        self.inp1 = TextInput(text="Введите цену водочки")
        self.inp2 = TextInput(text="Введите кол-во бутылок")
        self.subm = Button(text="Выбрано!", font_size=30, background_color="cyan", on_press=self.choice1)
        self.grid.add_widget(self.inp)
        self.grid.add_widget(self.inp1)
        self.grid.add_widget(self.inp2)
        self.grid.add_widget(self.subm)
    def viskarik(self,obj):
        global case
        case = 2
        self.label.text = "Выбираем вискарик!"
        self.grid.remove_widget(self.vodochka)
        self.grid.remove_widget(self.whisky)
        self.grid.remove_widget(self.rom)
        self.grid.remove_widget(self.nothing)
        self.inp = TextInput(text = "Введите объем вискарика")
        self.inp1 = TextInput(text="Введите цену вискарика")
        self.inp2 = TextInput(text="Введите кол-во вискарика")
        self.subm = Button(text="Выбрано!", font_size=30, background_color="cyan", on_press=self.choice1)
        self.grid.add_widget(self.inp)
        self.grid.add_widget(self.inp1)
        self.grid.add_widget(self.inp2)
        self.grid.add_widget(self.subm)
    def rome(self,obj):
        global case
        case = 3
        self.label.text = "Выбираем ром!"
        self.grid.remove_widget(self.vodochka)
        self.grid.remove_widget(self.whisky)
        self.grid.remove_widget(self.rom)
        self.grid.remove_widget(self.nothing)
        self.inp = TextInput(text = "Введите объем, Рома")
        self.inp1 = TextInput(text="Введите цену, Рома")
        self.inp2 = TextInput(text="Введите кол-во, Рома")
        self.subm = Button(text="Выбрано!", font_size=30, background_color="cyan", on_press=self.choice1)
        self.grid.add_widget(self.inp)
        self.grid.add_widget(self.inp1)
        self.grid.add_widget(self.inp2)
        self.grid.add_widget(self.subm)
    def choice1(self,obj):
        if not self.inp.text.isdigit()or not self.inp1.text.isdigit() or not self.inp2.text.isdigit():
            return self.bruh()
        global case,vodochkaL,romL,viskarL
        if case == 1:
            vodochkaL += float(self.inp.text)*float(self.inp2.text)
        elif case == 2:
            viskarL += float(self.inp.text)*float(self.inp2.text)
        elif case == 3:
            romL += float(self.inp.text)*float(self.inp2.text)
        self.label.text = "Бутылку какого напитка вы берете?"
        self.grid.remove_widget(self.inp)
        self.grid.remove_widget(self.inp1)
        self.grid.remove_widget(self.inp2)
        self.grid.remove_widget(self.subm)
        self.vodochka = Button(text="Водочка!", font_size=30, background_color="cyan", on_press=self.vodochka1)
        self.whisky = Button(text="Вискарик!", font_size=30, background_color="cyan", on_press=self.viskarik)
        self.rom = Button(text="Ром!", font_size=30, background_color="cyan", on_press=self.rome)
        self.nothing = Button(text="Больше ничего не нужно, спасибо!", font_size=30, background_color="cyan", on_press=self.nothing1)

        self.grid.add_widget(self.vodochka)
        self.grid.add_widget(self.whisky)
        self.grid.add_widget(self.rom)
        self.grid.add_widget(self.nothing)
    def nothing1(self,obj):
        self.label.text = "Выберите дальнейшее действие"
        self.grid.remove_widget(self.vodochka)
        self.grid.remove_widget(self.whisky)
        self.grid.remove_widget(self.rom)
        self.grid.remove_widget(self.nothing)
        self.results = Button(text="Показать результаты", font_size=30, background_color="cyan", on_press=self.results1)
        self.add = Button(text="Добавить товары", font_size=30, background_color="cyan", on_press=self.add1)
        self.rerun = Button(text="Запустить программу заново", font_size=30, background_color="cyan", on_press=self.rerun1)
        self.grid.add_widget(self.results)
        self.grid.add_widget(self.add)
        self.grid.add_widget(self.rerun)
    def rerun1(self,obj):
        self.grid.remove_widget(self.results)
        self.grid.remove_widget(self.add)
        self.grid.remove_widget(self.rerun)
        global vodochkaL, viskarL, romL, budget, per, money
        vodochkaL, viskarL, romL, budget, per, money = 0,0,0,0,0,0
        self.label.text = "В этот раз будьте внимательнее, все получится!\nвведите количество персон?"
        self.grid.remove_widget(self.but)
        self.inp = TextInput()
        self.subm = Button(text="submit", on_press=self.money)
        self.grid.add_widget(self.inp)
        self.grid.add_widget(self.subm)
    def add1(self,obj):
        self.grid.remove_widget(self.results)
        self.grid.remove_widget(self.add)
        self.grid.remove_widget(self.rerun)
        self.label.text = "Бутылку какого напитка вы берете?"
        self.vodochka = Button(text="Водочка!", font_size=30, background_color="cyan", on_press=self.vodochka1)
        self.whisky = Button(text="Вискарик!", font_size=30, background_color="cyan", on_press=self.viskarik)
        self.rom = Button(text="Ром!", font_size=30, background_color="cyan", on_press=self.rome)
        self.nothing = Button(text="Больше ничего не нужно, спасибо!", font_size=30, background_color="cyan",
                              on_press=self.nothing1)
        self.grid.add_widget(self.vodochka)
        self.grid.add_widget(self.whisky)
        self.grid.add_widget(self.rom)
        self.grid.add_widget(self.nothing)
    def bruh(self):
        self.label.text = "Ты пидор!\nвведи нормальные данные!"
    def results1(self,obj):
        self.grid.remove_widget(self.results)
        self.grid.remove_widget(self.add)
        self.grid.remove_widget(self.rerun)
        str1 = str(money)
        str2 = str(vodochkaL)
        str3 = str(viskarL)
        str4 = str(romL)
        str5 = str((vodochkaL+viskarL+romL)/per)
        self.label.text = "Что ж, у вас осталось "+str1+" рублей\nВы купили\n"+str2+" литров водочки\n"+str3+" литров вискарика\n"+str4+" литров рома\n"+\
                          "по моим расчетам у вас "+str5+" литров на человека"

        aimg = AsyncImage(source='https://i.ytimg.com/vi/xw6e4v8k4eU/maxresdefault.jpg')
        self.grid.add_widget(aimg)

if __name__ == "__main__":
    Application().run()