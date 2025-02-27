<img src="./assets/icon.png"/>
<h1 align = "center" > TransFusion Lite</h1>
<p align = "center">一款通过调用翻译器 API 的多语言翻译器</p>
> 此项目已暂时停更

## 为什么选择 TransFusion Lite

### 对接专业翻译 API

TransFusion Lite 通过调用各专业翻译器 API 进行翻译。

### 多种翻译方式

因为 TransFusion Lite 通过调用翻译器的 API Key 进行翻译，用户可通过提供不同翻译器的 API 来使用多种不同翻译方式。

以下是目前 TransFusion Lite 支持调用的翻译器 API：

- 百度翻译
- 小牛翻译
- 彩云翻译
- DeepSeek 翻译

### 支持 DeepSeek 翻译

只要用户提供 DeepSeek API Key，TransFusion Lite支持使用 DeepSeek v3 和 DeepSeek R1。

### 可自定义风格

只需要修改配置文件（config.json）中的Style栏，可以根据assets目录下的qss文件的文件名更改配置
将配置文件中的`'deepseek_model_r1' = 'False'`改为`'deepseek_model_r1' = 'True'`并配置API密钥即可使用DeepSeek-R1模型进行翻译，用R1模型翻译文学类作品效果会更好


### 注意事项

使用翻译需要在配置文件的对应的地方填写apikey
使用DeepSeek翻译时，出现短暂的未响应是正常的，是因为正在输出

### 下载并安装

1. 从右上角的“CODE”下载整个项目，可以使用git
2. 下载python（教程自行网络查阅）
	- 建议使用 Python 3.12
	- 最低版本 Python 3.7
	- **必须安装PIP**
3. 安装完Python之后打开, 下载后的文件夹，打开cmd,输入如下指令
	`pip install -r requirements.txt`
4. 最终打开主程序Main.py，如果你按照教程做，应该是没有问题的,如果还有问题，请提交Issue或者联系我们：support@hroton.cn


HrotonStudio
2025-2-27

