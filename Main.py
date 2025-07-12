# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QSplashScreen
from PySide6 import QtGui
from PySide6.QtCore import Qt, QTimer, QThread, Signal
import Libs.Window as Window, Libs.translater as translater, Libs.about as about, Libs.Load_Qss as Load_Qss, Libs.settings as settings, Libs.load_window as load_window
import threading
import json
import webbrowser
from Libs import about_rc
import time

class LoadingWindow(QMainWindow):
    def __init__(self):
        super(LoadingWindow, self).__init__()
        self.ui = load_window.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon('./assets/icon.ico'))
        
        # 修复图标显示问题
        self.ui.label_4.setStyleSheet("background-image: url(./assets/icon.png); background-repeat: no-repeat; background-position: center;")
        
        # 居中显示
        screen_geometry = QApplication.primaryScreen().geometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Window.Ui_MainWindow()
        self.ui.setupUi(self)

        self.fromLang = 'auto'
        self.toLang = 'zh'
        self.choose_circuit = 'xiaoniu'

        self.ui.pushButton_translate.clicked.connect(self.start)
        self.ui.pushButton.clicked.connect(self.copy)
        
        self.ui.combobox_tramslate_method.setCurrentIndex(0)
        # 连接combobox信号并立即调用check_method初始化语言设置
        self.ui.combobox_tramslate_method.currentTextChanged.connect(self.check_method)
        self.check_method()  # 初始化语言设置
        
        menuabout = self.ui.menuabout.addAction("关于软件")
        menuabout.triggered.connect(self.about_show)
        menu_settings = self.ui.menuoptions.addAction("设置")
        menu_settings.triggered.connect(self.settings_show)
        
        # 安装事件过滤器以处理键盘事件
        self.ui.textBrowser_input.installEventFilter(self)

    def eventFilter(self, obj, event):
        from PySide6.QtCore import QEvent
        if obj == self.ui.textBrowser_input and event.type() == QEvent.KeyPress:
            from PySide6.QtCore import Qt
            # 检查是否是Enter键
            if (event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter):
                # 如果按下了Ctrl键，则执行翻译
                if event.modifiers() == Qt.ControlModifier:
                    self.start()
                    return True
        return super().eventFilter(obj, event)

    def settings_show(self):
        self.w = window_settings()
        self.w.show()

    def about_show(self):
        self.w = window_about()
        self.w.show()

        
    def check_method(self):
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
        
        # 移除重复的信号连接，因为已经在__init__中连接
        
        input_text = self.ui.textBrowser_input.toPlainText()

        if input_text != '':
            translation_result, status = translater.translate(input_text, Circuit=self.choose_circuit, fromLang=self.fromLang, toLang=self.toLang)

            if status == 200:
                self.ui.label_5.setStyleSheet('color:green')
            else:
                self.ui.label_5.setStyleSheet('color:red')

            self.ui.label_5.setText(f'状态码: {str(status)}')

            self.ui.textBrowser_output.setText(translation_result)
        else:
            self.ui.textBrowser_output.setText('输入为空')

    def copy(self):
        self.ui.textBrowser_output.selectAll()
        self.ui.textBrowser_output.copy()

class window_about(QMainWindow):
    def __init__(self):
        super(window_about, self).__init__()
        self.ui = about.Ui_MainWindow()
        self.ui.setupUi(self)
        # 禁用所有按钮但保留关闭按钮
        self.setWindowFlags(Qt.Window | Qt.WindowCloseButtonHint)
        self.setFixedSize(self.size())

class window_settings(QMainWindow):
    def __init__(self):
        super(window_settings,self).__init__()
        self.ui = settings.Ui_MainWindow()
        self.ui.setupUi(self)
        # 禁用所有按钮但保留关闭按钮
        self.setWindowFlags(Qt.Window | Qt.WindowCloseButtonHint)
        self.setFixedSize(self.size())
        # 读取配置文件
        self.readsettings()
        self.ui.pushButton_save.clicked.connect(self.savesettings)
        
    def readsettings(self):
        try:
            with open('./config.json', 'r', encoding='utf-8') as f:
                config = json.load(f)
                
            # 设置文本框内容
            self.ui.textBrowser_baiduappid.setPlainText(config.get('baidu_appid', ''))
            self.ui.textBrowser_baidusecretkey.setPlainText(config.get('baidu_secretKey', ''))
            self.ui.textBrowser_xiaoniuapikey.setPlainText(config.get('xiaoniu_apikey', ''))
            self.ui.textBrowser_caiyunapikey.setPlainText(config.get('caiyun_apikey', ''))
            self.ui.textBrowser_deepseekapikey.setPlainText(config.get('deepseek_apikey', ''))
            
            # 设置deepseek_model_r1单选按钮状态
            deepseek_r1 = config.get('deepseek_model_r1', 'False').lower() == 'true'
            self.ui.radioButton_enable_dsr1.setChecked(deepseek_r1)
            
            # 设置主题下拉框
            current_theme = config.get('window_style', 'Ubuntu')
            index = self.ui.comboBox_theme.findText(current_theme)
            if index >= 0:
                self.ui.comboBox_theme.setCurrentIndex(index)
            # 连接主题切换信号
            self.ui.comboBox_theme.currentTextChanged.connect(self.apply_theme)
            
        except FileNotFoundError:
            print("配置文件不存在")
        except json.JSONDecodeError:
            print("配置文件格式错误")

    def apply_theme(self, theme_name):
        """应用选择的主题"""
        try:
            style_file = f'./assets/{theme_name}.qss'
            style_sheet = Load_Qss.QSSLoader.read_qss_file(style_file)
            # 应用到当前窗口
            self.setStyleSheet(style_sheet)
            # 应用到主窗口
            if hasattr(self, 'parent') and self.parent():
                self.parent().setStyleSheet(style_sheet)
        except Exception as e:
            print(f'应用主题出错: {str(e)}')

    def savesettings(self):
        try:
            # 读取当前配置
            with open('./config.json', 'r', encoding='utf-8') as f:
                config = json.load(f)
                
            # 更新配置
            config['baidu_appid'] = self.ui.textBrowser_baiduappid.toPlainText()
            config['baidu_secretKey'] = self.ui.textBrowser_baidusecretkey.toPlainText()
            config['xiaoniu_apikey'] = self.ui.textBrowser_xiaoniuapikey.toPlainText()
            config['caiyun_apikey'] = self.ui.textBrowser_caiyunapikey.toPlainText()
            config['deepseek_apikey'] = self.ui.textBrowser_deepseekapikey.toPlainText()
            config['deepseek_model_r1'] = str(self.ui.radioButton_enable_dsr1.isChecked())
            config['window_style'] = self.ui.comboBox_theme.currentText()
            
            # 保存配置
            with open('./config.json', 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=4, ensure_ascii=False)
                
            # 应用新主题
            style_file = f'./assets/{config["window_style"]}.qss'
            style_sheet = Load_Qss.QSSLoader.read_qss_file(style_file)
            self.setStyleSheet(style_sheet)
            
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.information(
                self, 
                '保存成功', 
                '设置已成功保存',
                QMessageBox.StandardButton.Ok
            )
            self.close()  # 保存成功后关闭窗口
            
        except Exception as e:
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.warning(
                self,
                '保存失败',
                f'保存设置出错: {str(e)}',
                QMessageBox.StandardButton.Ok
            )

# 移除未使用的函数，因为我们使用AppManager类来管理窗口显示

class LoadingThread(QThread):
    finished = Signal()
    error = Signal(str)
    progress = Signal(int)
    
    def run(self):
        try:
            # 模拟加载过程
            for i in range(1, 101):
                time.sleep(0.02)  # 模拟加载延迟
                self.progress.emit(i)
            
            # 加载完成
            self.finished.emit()
        except Exception as e:
            self.error.emit(str(e))

class AppManager:
    def __init__(self):
        self.loading_window = None
        self.main_window = None
        self.loading_thread = None
    
    def start(self):
        # 显示加载窗口
        self.loading_window = LoadingWindow()
        self.loading_window.show()
        
        # 创建并启动加载线程
        self.loading_thread = LoadingThread()
        self.loading_thread.finished.connect(self.init_main_window)
        self.loading_thread.progress.connect(self.update_progress)
        self.loading_thread.error.connect(lambda msg: print(f"加载错误: {msg}"))
        self.loading_thread.start()
    
    def update_progress(self, value):
        # 更新加载文本和进度条以显示进度
        if hasattr(self.loading_window.ui, 'label_3'):
            self.loading_window.ui.label_3.setText(f"加载中... {value}%")
            
        # 更新进度条
        if hasattr(self.loading_window.ui, 'progressBar'):
            self.loading_window.ui.progressBar.setValue(value)
            
        # 确保UI立即更新显示
        QApplication.processEvents()
    
    def init_main_window(self):
        # 在主线程中创建主窗口
        self.main_window = Main()
        
        # 加载样式表
        try:
            with open('./config.json', 'r', encoding='utf-8') as f:
                style_json = f.read()
            style = json.loads(style_json)['window_style']
            style_file = f'./assets/{style}.qss'
            style_sheet = Load_Qss.QSSLoader.read_qss_file(style_file)
            self.main_window.setStyleSheet(style_sheet)
        except Exception as e:
            print(f"加载样式表出错: {str(e)}")
        
        # 设置窗口图标和标题
        self.main_window.setWindowIcon(QtGui.QIcon('./assets/icon.ico'))
        self.main_window.setWindowTitle('TransFusion-Lite')
        
        # 显示主窗口，关闭加载窗口
        self.main_window.show()
        self.loading_window.close()

if __name__ == "__main__":
    app = QApplication([])
    
    manager = AppManager()
    manager.start()
    
    app.exec()