import kivy
kivy.require('2.3.0')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, RoundedRectangle, Line
from kivy.metrics import dp, sp
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.lang import Builder
import json

# Color palette
COLORS = {
    'bg_dark': get_color_from_hex('#1A1A2E'),
    'card_bg': get_color_from_hex('#16213E'),
    'accent_blue': get_color_from_hex('#00D4FF'),
    'accent_orange': get_color_from_hex('#FF6B35'),
    'accent_green': get_color_from_hex('#00E676'),
    'white': get_color_from_hex('#FFFFFF'),
    'light_gray': get_color_from_hex('#B0B0B0'),
    'mid_gray': get_color_from_hex('#808080'),
    'soft_white': get_color_from_hex('#E0E0E0'),
}

# Q&A Data
QA_PAIRS = [
    {
        "num": 1,
        "q_hi": "आप घर पर AC क्यों चलाते हैं?",
        "q_en": "Why do you run AC at home?",
        "a_hi": "बहुत गर्मी है, इसलिए AC चलाता हूँ।",
        "a_en": "It's very hot, so I run the AC.",
    },
    {
        "num": 2,
        "q_hi": "आप कल जल्दी क्यों सोएंगे?",
        "q_en": "Why will you sleep early tomorrow?",
        "a_hi": "मुझे कल जल्दी उठना है, इसलिए मैं जल्दी सोऊंगा।",
        "a_en": "I have to wake up early tomorrow, so I will sleep early.",
    },
    {
        "num": 3,
        "q_hi": "आपकी माँ बाजार क्यों नहीं जाती?",
        "q_en": "Why doesn't your mother go to the market?",
        "a_hi": "बारिश हो रही है, इसलिए वह बाजार नहीं जाती।",
        "a_en": "It's raining, so she doesn't go to the market.",
    },
    {
        "num": 4,
        "q_hi": "आप कल पाइप ठीक क्यों करवाएंगे?",
        "q_en": "Why will you get the pipe repaired tomorrow?",
        "a_hi": "पानी टपक रहा है, इसलिए उसे ठीक करवाऊंगा।",
        "a_en": "Water is leaking, so I will get it repaired.",
    },
    {
        "num": 5,
        "q_hi": "आप घर पर ज्यादा लाइटें क्यों जलाते हैं?",
        "q_en": "Why do you turn on more lights at home?",
        "a_hi": "अंधेरा हो गया है, इसलिए लाइटें जलाता हूँ।",
        "a_en": "It has become dark, so I turn on the lights.",
    },
    {
        "num": 6,
        "q_hi": "आप कल खाना ऑर्डर क्यों करेंगे?",
        "q_en": "Why will you order food tomorrow?",
        "a_hi": "घर पर कोई नहीं है, इसलिए ऑर्डर करूंगा।",
        "a_en": "No one is at home, so I will order food.",
    },
    {
        "num": 7,
        "q_hi": "आप दरवाजा क्यों बंद करते हैं?",
        "q_en": "Why do you close the door?",
        "a_hi": "बहुत शोर है, इसलिए दरवाजा बंद करता हूँ।",
        "a_en": "There's too much noise, so I close the door.",
    },
    {
        "num": 8,
        "q_hi": "आप कल घर साफ क्यों करेंगे?",
        "q_en": "Why will you clean the house tomorrow?",
        "a_hi": "मेहमान आ रहे हैं, इसलिए साफ करूंगा।",
        "a_en": "Guests are coming, so I will clean.",
    },
    {
        "num": 9,
        "q_hi": "आप पंखा क्यों चलाते हैं?",
        "q_en": "Why do you run the fan?",
        "a_hi": "हवा नहीं है, इसलिए पंखा चलाता हूँ।",
        "a_en": "There's no breeze, so I run the fan.",
    },
    {
        "num": 10,
        "q_hi": "आप कल नया फर्नीचर क्यों खरीदेंगे?",
        "q_en": "Why will you buy new furniture tomorrow?",
        "a_hi": "पुराना टूट गया है, इसलिए नया खरीदूंगा।",
        "a_en": "The old one is broken, so I will buy new.",
    },
]

Builder.load_string('''
<ColoredBox@BoxLayout>:
    bg_color: 1, 1, 1, 1
    canvas.before:
        Color:
            rgba: self.bg_color
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(16), dp(16), dp(16), dp(16)]

<CustomButton@Button>:
    background_normal: ''
    background_color: 0, 0, 0, 0
    canvas.before:
        Color:
            rgba: self.bg_color if hasattr(self, 'bg_color') else (0, 0.83, 1, 1)
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(12), dp(12), dp(12), dp(12)]
    color: 1, 1, 1, 1
    font_size: sp(16)
    bold: True
    size_hint_y: None
    height: dp(50)

<ArrowWidget@Widget>:
    arrow_color: 1, 0.42, 0.21, 1
    canvas:
        Color:
            rgba: self.arrow_color
        Triangle:
            points: self.center_x - dp(30), self.center_y, self.center_x + dp(30), self.center_y, self.center_x, self.center_y + dp(20)
        Rectangle:
            pos: self.center_x - dp(30), self.center_y - dp(5)
            size: dp(60), dp(10)

<QACard@ColoredBox>:
    orientation: 'vertical'
    padding: dp(20)
    spacing: dp(12)
    bg_color: 0.086, 0.129, 0.243, 1
    size_hint_y: None
    height: self.minimum_height

<TitleScreen@Screen>:
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: 0.102, 0.102, 0.18, 1
            Rectangle:
                pos: self.pos
                size: self.size
        Widget:
            size_hint_y: 0.15
        Label:
            text: 'Pattern 8'
            font_size: sp(48)
            bold: True
            color: 0, 0.83, 1, 1
            size_hint_y: None
            height: dp(80)
            font_name: 'Roboto-Thin'
        Label:
            text: 'So / That\\'s why + Result'
            font_size: sp(32)
            color: 1, 1, 1, 1
            size_hint_y: None
            height: dp(60)
            font_name: 'Roboto-Light'
        Widget:
            size_hint_y: 0.05
        Canvas:
            Color:
                rgba: 0, 0.83, 1, 1
            Line:
                points: self.center_x - dp(100), self.center_y, self.center_x + dp(100), self.center_y
                width: dp(3)
            size_hint_y: None
            height: dp(10)
        Widget:
            size_hint_y: 0.05
        Label:
            text: 'Category 1: Home & Family'
            font_size: sp(24)
            color: 0.69, 0.69, 0.69, 1
            size_hint_y: None
            height: dp(40)
        Label:
            text: 'Present & Future Tense Mix'
            font_size: sp(20)
            color: 0.5, 0.5, 0.5, 1
            size_hint_y: None
            height: dp(35)
        Widget:
            size_hint_y: 0.15
        CustomButton:
            text: 'Start Learning'
            bg_color: 1, 0.42, 0.21, 1
            size_hint_x: 0.6
            pos_hint: {'center_x': 0.5}
            on_press: root.manager.transition = SlideTransition(direction='left'); root.manager.current = 'category'
        Widget:
            size_hint_y: 0.1

<CategoryScreen@Screen>:
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: 0.102, 0.102, 0.18, 1
            Rectangle:
                pos: self.pos
                size: self.size
        BoxLayout:
            size_hint_y: None
            height: dp(80)
            padding: dp(20)
            Label:
                text: 'Category 1: Home & Family'
                font_size: sp(28)
                bold: True
                color: 0, 0.83, 1, 1
                halign: 'left'
                valign: 'middle'
                text_size: self.size
            CustomButton:
                text: 'Back'
                size_hint_x: None
                width: dp(100)
                bg_color: 0.5, 0.5, 0.5, 1
                on_press: root.manager.transition = SlideTransition(direction='right'); root.manager.current = 'title'
        BoxLayout:
            orientation: 'horizontal'
            spacing: dp(16)
            padding: dp(20)
            size_hint_y: 0.45
            QACard:
                orientation: 'vertical'
                Label:
                    text: 'Pattern Structure'
                    font_size: sp(22)
                    bold: True
                    color: 0, 0.83, 1, 1
                    size_hint_y: None
                    height: dp(40)
                    halign: 'left'
                    text_size: self.width, None
                Label:
                    text: 'Question: Why...?\\nAnswer: Reason, so/that\\'s why Result.\\n\\nHindi: कारण, इसलिए/इसलिए परिणाम।'
                    font_size: sp(16)
                    color: 0.878, 0.878, 0.878, 1
                    halign: 'left'
                    valign: 'top'
                    text_size: self.width, None
                    size_hint_y: None
                    height: self.texture_size[1] + dp(20)
            QACard:
                orientation: 'vertical'
                Label:
                    text: 'Key Connectors'
                    font_size: sp(22)
                    bold: True
                    color: 1, 0.42, 0.21, 1
                    size_hint_y: None
                    height: dp(40)
                    halign: 'left'
                    text_size: self.width, None
                Label:
                    text: '• so\\n• that\\'s why\\n• इसलिए\\n• इसीलिए\\n\\nUsed to show cause → effect'
                    font_size: sp(16)
                    color: 0.878, 0.878, 0.878, 1
                    halign: 'left'
                    valign: 'top'
                    text_size: self.width, None
                    size_hint_y: None
                    height: self.texture_size[1] + dp(20)
        Widget:
            size_hint_y: 0.05
        CustomButton:
            text: 'Start Practice (10 Questions)'
            bg_color: 0, 0.9, 0.46, 1
            size_hint_x: 0.8
            pos_hint: {'center_x': 0.5}
            on_press: root.manager.transition = SlideTransition(direction='left'); root.manager.current = 'qa_1'
        Widget:
            size_hint_y: 0.1

<QAScreen@Screen>:
    qa_data: {}
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: 0.102, 0.102, 0.18, 1
            Rectangle:
                pos: self.pos
                size: self.size
        BoxLayout:
            size_hint_y: None
            height: dp(70)
            padding: dp(16)
            CustomButton:
                text: '← Back'
                size_hint_x: None
                width: dp(100)
                bg_color: 0.5, 0.5, 0.5, 1
                on_press: root.manager.transition = SlideTransition(direction='right'); root.manager.current = 'category'
            Label:
                text: f"Question {root.qa_data.get('num', 1)} of 10"
                font_size: sp(18)
                bold: True
                color: 0, 0.83, 1, 1
                halign: 'center'
                valign: 'middle'
                text_size: self.size
            Widget:
                size_hint_x: None
                width: dp(100)
        ScrollView:
            do_scroll_x: False
            BoxLayout:
                orientation: 'vertical'
                padding: dp(16)
                spacing: dp(16)
                size_hint_y: None
                height: self.minimum_height
                QACard:
                    Label:
                        text: 'QUESTION'
                        font_size: sp(12)
                        bold: True
                        color: 0, 0.83, 1, 1
                        size_hint_y: None
                        height: dp(25)
                        halign: 'left'
                        text_size: self.width, None
                    Label:
                        text: root.qa_data.get('q_hi', '')
                        font_size: sp(26)
                        bold: True
                        color: 1, 1, 1, 1
                        halign: 'left'
                        valign: 'middle'
                        text_size: self.width, None
                        size_hint_y: None
                        height: self.texture_size[1] + dp(10)
                    Label:
                        text: root.qa_data.get('q_en', '')
                        font_size: sp(18)
                        color: 0.69, 0.69, 0.69, 1
                        halign: 'left'
                        valign: 'middle'
                        text_size: self.width, None
                        size_hint_y: None
                        height: self.texture_size[1] + dp(10)
                BoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: dp(80)
                    padding: dp(20)
                    canvas:
                        Color:
                            rgba: 1, 0.42, 0.21, 1
                        RoundedRectangle:
                            pos: self.x + dp(40), self.center_y - dp(5)
                            size: self.width - dp(80), dp(10)
                            radius: [dp(5), dp(5), dp(5), dp(5)]
                        Color:
                            rgba: 1, 0.42, 0.21, 1
                        Triangle:
                            points: self.center_x, self.center_y + dp(15), self.center_x - dp(15), self.center_y - dp(5), self.center_x + dp(15), self.center_y - dp(5)
                    Label:
                        text: 'so / that\\'s why  •  इसलिए'
                        font_size: sp(14)
                        bold: True
                        color: 1, 1, 1, 1
                        halign: 'center'
                        valign: 'middle'
                        text_size: self.width, None
                QACard:
                    Label:
                        text: 'ANSWER'
                        font_size: sp(12)
                        bold: True
                        color: 0, 0.9, 0.46, 1
                        size_hint_y: None
                        height: dp(25)
                        halign: 'left'
                        text_size: self.width, None
                    Label:
                        text: root.qa_data.get('a_hi', '')
                        font_size: sp(24)
                        bold: True
                        color: 1, 1, 1, 1
                        halign: 'left'
                        valign: 'middle'
                        text_size: self.width, None
                        size_hint_y: None
                        height: self.texture_size[1] + dp(10)
                    Label:
                        text: root.qa_data.get('a_en', '')
                        font_size: sp(18)
                        color: 0.69, 0.69, 0.69, 1
                        halign: 'left'
                        valign: 'middle'
                        text_size: self.width, None
                        size_hint_y: None
                        height: self.texture_size[1] + dp(10)
        BoxLayout:
            size_hint_y: None
            height: dp(80)
            padding: dp(16)
            spacing: dp(16)
            CustomButton:
                text: 'Previous'
                bg_color: 0.5, 0.5, 0.5, 1
                on_press: root.go_previous()
                disabled: root.qa_data.get('num', 1) == 1
            CustomButton:
                text: 'Next'
                bg_color: 0, 0.83, 1, 1
                on_press: root.go_next()

<SummaryScreen@Screen>:
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: 0.102, 0.102, 0.18, 1
            Rectangle:
                pos: self.pos
                size: self.size
        BoxLayout:
            size_hint_y: None
            height: dp(80)
            padding: dp(20)
            Label:
                text: 'Practice & Summary'
                font_size: sp(28)
                bold: True
                color: 0, 0.83, 1, 1
                halign: 'left'
                valign: 'middle'
                text_size: self.size
            CustomButton:
                text: 'Home'
                size_hint_x: None
                width: dp(100)
                bg_color: 0.5, 0.5, 0.5, 1
                on_press: root.manager.transition = SlideTransition(direction='right'); root.manager.current = 'title'
        ScrollView:
            do_scroll_x: False
            BoxLayout:
                orientation: 'vertical'
                padding: dp(16)
                spacing: dp(16)
                size_hint_y: None
                height: self.minimum_height
                QACard:
                    Label:
                        text: 'Key Takeaways'
                        font_size: sp(22)
                        bold: True
                        color: 0, 0.83, 1, 1
                        size_hint_y: None
                        height: dp(40)
                        halign: 'left'
                        text_size: self.width, None
                    Label:
                        text: '✓  "So" connects reason to result\\n✓  "That\\'s why" emphasizes the cause\\n✓  Hindi: इसलिए / इसीलिए\\n✓  Works with Present & Future tense\\n✓  10 Home & Family scenarios covered\\n\\nStructure: Reason + इसलिए + Result'
                        font_size: sp(16)
                        color: 1, 1, 1, 1
                        halign: 'left'
                        valign: 'top'
                        text_size: self.width, None
                        size_hint_y: None
                        height: self.texture_size[1] + dp(20)
                QACard:
                    Label:
                        text: 'Your Turn: Create 3 Sentences'
                        font_size: sp(20)
                        bold: True
                        color: 1, 0.42, 0.21, 1
                        size_hint_y: None
                        height: dp(40)
                        halign: 'left'
                        text_size: self.width, None
                    Label:
                        text: '1. Why do you drink water?\\n   → I\\'m thirsty, so I drink water.\\n\\n2. Why will you study tonight?\\n   → Exam tomorrow, that\\'s why I\\'ll study.\\n\\n3. Why does she use AC?\\n   → It\\'s hot, इसलिए AC चलाती है।'
                        font_size: sp(16)
                        color: 0.878, 0.878, 0.878, 1
                        halign: 'left'
                        valign: 'top'
                        text_size: self.width, None
                        size_hint_y: None
                        height: self.texture_size[1] + dp(20)
                CustomButton:
                    text: 'Restart Learning'
                    bg_color: 0, 0.9, 0.46, 1
                    size_hint_x: 0.6
                    pos_hint: {'center_x': 0.5}
                    on_press: root.manager.transition = SlideTransition(direction='right'); root.manager.current = 'category'
''')


class TitleScreen(Screen):
    pass


class CategoryScreen(Screen):
    pass


class QAScreen(Screen):
    def go_next(self):
        current_num = self.qa_data.get('num', 1)
        if current_num < 10:
            next_screen = self.manager.get_screen(f'qa_{current_num + 1}')
            self.manager.transition = SlideTransition(direction='left')
            self.manager.current = f'qa_{current_num + 1}'
        else:
            self.manager.transition = SlideTransition(direction='left')
            self.manager.current = 'summary'

    def go_previous(self):
        current_num = self.qa_data.get('num', 1)
        if current_num > 1:
            prev_screen = self.manager.get_screen(f'qa_{current_num - 1}')
            self.manager.transition = SlideTransition(direction='right')
            self.manager.current = f'qa_{current_num - 1}'


class SummaryScreen(Screen):
    pass


class Pattern8App(App):
    def build(self):
        self.title = 'Pattern 8: So / That\'s why'
        Window.clearcolor = COLORS['bg_dark']
        
        sm = ScreenManager(transition=SlideTransition(duration=0.3))
        
        # Add screens
        sm.add_widget(TitleScreen(name='title'))
        sm.add_widget(CategoryScreen(name='category'))
        
        # Add QA screens dynamically
        for i, qa in enumerate(QA_PAIRS, 1):
            screen = QAScreen(name=f'qa_{i}')
            screen.qa_data = qa
            sm.add_widget(screen)
        
        sm.add_widget(SummaryScreen(name='summary'))
        
        return sm


if __name__ == '__main__':
    Pattern8App().run()