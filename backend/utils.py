import requests
import random
import json
import time
from .config import Config
from .mock_db import db

class DeepSeekResponseGenerator:
    def __init__(self, use_ai=True):
        self.use_ai = use_ai
    
    def generate_response(self, user_id, user_message, chat_history=None):
        # 首先尝试匹配知识库
        category = db.find_knowledge_category(user_message)
        if category:
            return db.get_knowledge_response(category)
        
        # 如果启用AI且配置了API key，使用DeepSeek API
        if self.use_ai and Config.DEEPSEEK_API_KEY:
            try:
                return self._generate_deepseek_response(user_message, chat_history)
            except Exception as e:
                print(f"DeepSeek API调用失败: {e}")
        
        # 回退到默认回复
        return self._generate_default_response(user_message)
    
    def _generate_deepseek_response(self, user_message, chat_history=None):
        """使用DeepSeek API生成智能回复"""
        # 准备API请求头
        headers = {
            "Authorization": f"Bearer {Config.DEEPSEEK_API_KEY}",
            "Content-Type": "application/json"
        }
        
        # 构建对话历史
        messages = []
        
        # 系统提示词 - 定义客服角色和行为准则
        system_prompt = """
你是一个淘宝客服助手，名字叫小蜜。你的任务是友好、专业地帮助用户解决淘宝购物相关的问题。
你的回答需要符合以下要求：
1. 使用中文回复，语气亲切友好
2. 回答简洁明了，不超过3句话
3. 专注于解决淘宝购物相关的问题
4. 对于不清楚的问题，引导用户提供更多信息
5. 不要回答与淘宝购物无关的问题
6. 当用户需要人工客服时，引导转接流程

用户可能的问题类型包括：订单查询、物流跟踪、退货退款、支付问题、优惠券使用等。
"""
        messages.append({"role": "system", "content": system_prompt})
        
        # 添加上下文历史
        if chat_history:
            for msg in chat_history:
                role = "user" if msg["sender"] == "user" else "assistant"
                messages.append({"role": role, "content": msg["content"]})
        
        # 添加当前用户消息
        messages.append({"role": "user", "content": user_message})
        
        # 构建请求体
        payload = {
            "model": Config.DEEPSEEK_MODEL,
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 256,
            "top_p": 0.9
        }
        
        # 调用DeepSeek API
        response = requests.post(
            Config.DEEPSEEK_API_URL,
            headers=headers,
            data=json.dumps(payload)
        
        # 检查响应状态
        if response.status_code != 200:
            error_msg = f"DeepSeek API错误: {response.status_code} - {response.text}"
            raise Exception(error_msg)
        
        # 解析响应
        response_data = response.json()
        bot_response = response_data["choices"][0]["message"]["content"].strip()
        
        return bot_response
    
    def _generate_default_response(self, user_message):
        """生成默认回复"""
        responses = [
            '我理解您的需求，让我帮您查询一下相关信息。',
            '关于您的问题，建议您查看订单详情页面获取更多信息。',
            '为了更好地帮助您，能否提供更多关于问题的细节？',
            '我这边查到您的订单状态正常，预计明天可以送达。',
            '您可以进入"我的淘宝"->"订单中心"查看详细信息。'
        ]
        return random.choice(responses)

# 创建响应生成器实例
response_generator = DeepSeekResponseGenerator(use_ai=True)