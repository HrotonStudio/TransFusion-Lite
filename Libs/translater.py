import requests,json,hashlib,random,urllib,http.client,subprocess,sys

def translate(query,Circuit,fromLang='en',toLang='zh'):

    # Load config.json for apikey
    with open('config.json', 'r', encoding='utf-8') as file:
        json_str = file.read()
    config_data = json.loads(json_str)
    config_data_baidu_appid = config_data['baidu_appid']
    config_data_baidu_secretKey = config_data['baidu_secretKey']
    config_data_xiaoniu_apikey = config_data['xiaoniu_apikey']
    config_data_caiyun_apikey = config_data['caiyun_apikey']
    config_data_deepseek_apikey = config_data['deepseek_apikey']
    config_data_deepseek_model_r1 = config_data['deepseek_model_r1']

    if Circuit == 'xiaoniu':
        url = 'http://api.niutrans.com/NiuTransServer/translation'
        data = {
            "from":fromLang,
            "to":toLang,
            "apikey":config_data_xiaoniu_apikey,
            "src_text":query
        }
        res = requests.post(url, data=data)
        json_data = json.loads(res.text)
        status_code = res.status_code
        return str(json_data['tgt_text']),status_code
    if Circuit == 'baidu':

        httpClient = None
        myurl = '/api/trans/vip/translate'

        salt = random.randint(32768, 65536)

        sign = config_data_baidu_appid + query + str(salt) + config_data_baidu_secretKey
        sign = hashlib.md5(sign.encode()).hexdigest()
        myurl = myurl + '?appid=' + config_data_baidu_appid + '&q=' + urllib.parse.quote(query) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign

        try:
            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl)

            response = httpClient.getresponse()
            result_all = response.read().decode("utf-8")
            result = json.loads(result_all)
            status_code = response.getcode()
            return result['trans_result'][0]['dst'],status_code

        except Exception as e:
            return e
        finally:
            if httpClient:
                httpClient.close()
    if Circuit == 'caiyun':
        url = "http://api.interpreter.caiyunai.com/v1/translator"

        # 比较逆天的彩云小译的翻译方式转换
        if fromLang == 'auto':
            if toLang == 'zh':
                direction = "auto2zh"
            elif toLang == 'en':
                direction = "auto2en"
            elif toLang == 'ja' or fromLang == 'jp':
                direction = "auto2ja"
            else:
                return "彩云小译暂不支持此翻译方式！"
        elif fromLang == 'zh':
            if toLang == 'en':
                direction = "zh2en"
            elif toLang == 'ja' or fromLang == 'jp':
                direction = "zh2ja"
            else:
                return "彩云小译暂不支持此翻译方式！"
        elif fromLang == 'en':
            if toLang == 'zh':
                direction = "en2zh"
        elif fromLang == 'ja' or fromLang == 'jp':
            if toLang == 'zh':
                direction = "ja2zh"
            else:
                return "彩云小译暂不支持此翻译方式！"
        else:
            return "彩云小译暂不支持此翻译方式！"
        payload = {
        "source": query,
        "trans_type": direction,
        "request_id": "demo",
        "detect": True,
                    }

        headers = {
        "content-type": "application/json",
        "x-authorization": "token " + config_data_caiyun_apikey
                    }

        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
        status_code = response.status_code
        return json.loads(response.text)["target"],status_code
    elif Circuit == 'deepseek':
        headers = {
            "Authorization": f"Bearer {config_data_deepseek_apikey}",
            "Content-Type": "application/json"
                }
        if config_data_deepseek_model_r1 == 'False':
            model = "deepseek-chat"
        elif config_data_deepseek_model_r1:
            model = "deepseek-reasoner"
        else:
            model = "deepseek-chat"
        data = {
            
        "model": model,  # 使用 DeepSeek 模型
        "messages": [
            {"role": "system", "content": f"You are a helpful translate assistant,you just need to translate the sentence or waords to {toLang},if the FromLanguage is same as ToLanguage,please repeat the sentence the user input,if the user said the language that you don't support,please input the sentence again and say 'DeepSeek不支持！"},
            {"role": "user", "content": query}
                    ],
            "stream": False  # 是否启用流式输出
                }
        url = "https://api.deepseek.com/chat/completions" 
        
        response = requests.post(url, headers=headers, json=data)
        status_code = response.status_code
        return str(response.json()['choices'][0]['message']['content']),status_code

        
        
    elif Circuit == None:
        return "请选择翻译器"


