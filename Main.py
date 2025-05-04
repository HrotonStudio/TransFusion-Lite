"""
上一次编辑：2025-05-05
作者：HanWen_lu
"""

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtGui
from PySide6.QtCore import Qt
from Libs.Window import Ui_MainWindow
from Libs import translater
from Libs import Load_Qss
import threading
import json


class Main(QMainWindow):
    def __init__(self):
        # 初始化窗口
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 设置默认翻译方式
        self.fromLang = 'auto'
        self.toLang = 'zh'
        self.choose_circuit = 'xiaoniu'
        # 设置默认函数信号槽
        self.ui.pushButton_translate.clicked.connect(self.start)
        self.ui.pushButton.clicked.connect(self.copy)
        self.ui.combobox_tramslate_method.setCurrentIndex(0)
    def check_method(self):  # 翻译方法选择（好痛苦一个个翻官方文档
        if self.ui.combobox_tramslate_method.currentText() == '自动检测译中':
            self.fromLang = 'auto'
            self.toLang = 'zh'
        elif self.ui.combobox_tramslate_method.currentText() == '中译英':
            self.fromLang = 'zh'
            self.toLang = 'en'
        elif self.ui.combobox_tramslate_method.currentText() == '中译俄':
            self.fromLang = 'zh'
            self.toLang = 'ru'
        elif self.ui.combobox_tramslate_method.currentText() == '中译日':
            self.fromLang = 'zh'
            if  self.choose_circuit == 'xiaoniu' or self.choose_circuit == 'caiyun':
                self.toLang = 'ja'      
            elif self.choose_circuit == 'baidu':
                self.toLang = 'jp'
            else:
                self.toLang = 'ja'   
        elif self.ui.combobox_tramslate_method.currentText() == '中译法':
            self.fromLang = 'zh'
            if self.choose_circuit == 'xiaoniu':
                self.toLang = 'fr' 
            elif self.choose_circuit == 'baidu':
                self.toLang = 'fra'
            else:
                self.toLang = 'fr' 
        
    def start(self):
        # 设置翻译方法变量
        if self.ui.radioButton_baidu.isChecked():
            self.choose_circuit = 'baidu'
        elif self.ui.radioButton_xiaoniu.isChecked():
            self.choose_circuit = 'xiaoniu'
        elif self.ui.radioButton_caiyun.isChecked():
            self.choose_circuit = 'caiyun'
        elif self.ui.radioButton_deepseek.isChecked():
            self.choose_circuit = 'deepseek'
        else:
            self.choose_circuit = 'xiaoniu'  # if forget to choose, default is xiaoniu
        self.ui.combobox_tramslate_method.currentTextChanged.connect(self.check_method)

        # 读取输入信息    
        input_text = self.ui.textBrowser_input.toPlainText()


        # 向翻译模块传入翻译参数，返回一个翻译结果一个状态码
        if input_text != '':
            translation_result,status = translater.translate(input_text, Circuit=self.choose_circuit, fromLang=self.fromLang, toLang=self.toLang)

            # 这里只是将网站响应的状态码给了出来，而不是翻译引擎返回的状态码（以后再搞
            if status == 200:
                self.ui.label_5.setStyleSheet('color:green')
            else:
                self.ui.label_5.setStyleSheet('color:red')

            self.ui.label_5.setText(f'状态码: {str(status)}')

            self.ui.textBrowser_output.setText(translation_result)
        else:
            self.ui.textBrowser_output.setText('输入为空')

    # 生草复制功能
    def copy(self):
        self.ui.textBrowser_output.selectAll()
        self.ui.textBrowser_output.copy()
    # 读取并加载QSS
    def load_style_sheet():
        with open('./config.json', 'r', encoding='utf-8') as f:
            style_json = f.read()
        style = json.loads(style_json)['window_style']
        style_file = f'./assets/{style}.qss'
        style_sheet = Load_Qss.QSSLoader.read_qss_file(style_file)
        window.setStyleSheet(style_sheet)
    

if __name__ == "__main__":
    
    app = QApplication([])
    window = Main()
    window.setWindowIcon(QtGui.QIcon('./assets/icon.ico'))
    window.setWindowTitle('TransFusion-Lite')

    thread_qss = threading.Thread(target=Main.load_style_sheet(),daemon=True).start()

    window.show()

    # hotkey_thread = threading.Thread(target=Main.listen_hotkry(self=Main),daemon=True)
    # hotkey_thread.start()  这里以后再来填坑

    app.exec()



