import requests
import json
from config import Config  # 确保从您的 config 导入

def test_deepseek_api():
    url = Config.DEEPSEEK_API_URL
    headers = {
        "Authorization": f"Bearer {Config.DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": Config.DEEPSEEK_MODEL,
        "messages": [
            {"role": "system", "content": "你是一个有帮助的助手。"},
            {"role": "user", "content": "你好！"}
        ],
        "temperature": 0.7,
        "max_tokens": 50
    }
    
    try:
        print("测试 DeepSeek API 连接...")
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        response.raise_for_status()
        
        print("API 连接成功！")
        print(f"状态码: {response.status_code}")
        print("响应内容:")
        print(json.dumps(response.json(), indent=2))
        
        return True
    except Exception as e:
        print(f"API 连接失败: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"错误响应: {e.response.text}")
        return False

if __name__ == "__main__":
    test_deepseek_api()