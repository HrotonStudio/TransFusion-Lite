
<h1 align = "center" > TransFusion-Lite</h1>
<p align = "center">一款通过调用多个翻译引擎API的多语言翻译器</p>


## 为什么选择 TransFusion-Lite

### :fire:对接专业翻译 API

TransFusion Lite 通过调用各专业翻译器 API 进行翻译。

### :star:多种翻译方式

因为 TransFusion-Lite 通过调用翻译器的 API Key 进行翻译，用户可通过提供不同翻译器的 API 来使用多种不同翻译方式。

以下是目前 TransFusion-Lite 支持调用的翻译器 API：

- 百度翻译
- 小牛翻译
- 彩云翻译
- DeepSeek 翻译

### :white_check_mark:支持 DeepSeek 翻译

只要用户提供 DeepSeek API Key，TransFusion-Lite支持使用 DeepSeek v3 和 DeepSeek R1。

### :star:可自定义风格

可在设置更改软件主题风格，如果想自定义风格，可将asstes里的qss文件替换


### :warning:注意事项

使用翻译需要在设置的对应的地方填写apikey
使用DeepSeek翻译时，出现短暂的未响应是正常的，是因为正在输出

### :confused:下载并安装

##方法1 直接下载安装包
1. 在release界面下载最新版安装包，
2. 按照安装包提供的引导进行安装，安装后可以在电脑上看见图标

##方法2 下载源码自构建运行
1. 从右上角的“CODE”下载整个项目，可以使用git
2. 下载python（教程自行网络查阅）
	- 建议使用 Python 3.13  
	- **必须安装PIP**
3. 安装完Python之后打开, 下载后的文件夹，打开cmd,输入如下指令
	`pip install -r requirements.txt`
4. 最终打开主程序Main.py，如果你按照教程做，应该是没有问题的,如果还有问题，请提交Issue或者联系我们：support@hroton.cn


HrotonStudio
2025-07-12

