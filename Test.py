from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty                                          
from kivymd.app import MDApp                                                                        
                                                       
from kivymd.uix.screen import MDScreen                                                              
from kivymd.uix.behaviors import CircularRippleBehavior                                                                                                    

from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image

from kivymd.app import MDApp
from kivymd.uix.behaviors import CircularRippleBehavior                                                                                                   


class Root(MDScreen):                                                                               
    pass                                                                                      

class Test(MDApp):                                                                                  
    def build(self):                                                                                
        # Создаём экземпляр корневого класса                                                        
        root = Root()                                                                               
        self.theme_cls.theme_style = "Dark"  # "Light" Тёмная или Светлая тема                      
        self.theme_cls.primary_palette = 'LightGreen'  # Цвет темы                                  
        self.theme_cls.primary_hue = '400'  # Сочность цвета темы                                   
        return root                                                                                 

class CircularRippleButton(CircularRippleBehavior, ButtonBehavior, Image):
    def __init__(self, **kwargs):
        self.ripple_scale = 0.85
        super().__init__(**kwargs)                                                                                                    
                                                                                                    
Test().run()  # Запуск приложения   