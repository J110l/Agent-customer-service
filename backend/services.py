import time
from .mock_db import db
from .response_generator import response_generator

class CustomerService:
    @staticmethod
    def get_user_info(user_id):
        """获取用户信息"""
        user = db.get_user(user_id)
        if user:
            return user.to_dict()
        return None
    
    @staticmethod
    def get_user_orders(user_id):
        """获取用户订单列表"""
        orders = db.get_user_orders(user_id)
        return [order.to_dict() for order in orders]
    
    @staticmethod
    def get_order_details(order_id):
        """获取订单详情"""
        order = db.get_order(order_id)
        if order:
            return order.to_dict()
        return None
    
    @staticmethod
    def handle_user_message(user_id, message):
        """处理用户消息并返回客服回复"""
        # 获取最近的聊天历史作为上下文
        chat_history = db.get_chat_history(user_id, limit=5)
        chat_history_dict = [msg.to_dict() for msg in chat_history]
        
        # 记录用户消息
        db.add_chat_message(user_id, message, 'user')
        
        # 生成回复
        bot_response = response_generator.generate_response(
            user_id, 
            message,
            chat_history=chat_history_dict
        )
        
        # 记录客服回复
        db.add_chat_message(user_id, bot_response, 'bot')
        
        return bot_response
    
    @staticmethod
    def get_chat_history(user_id):
        """获取聊天历史"""
        messages = db.get_chat_history(user_id)
        return [msg.to_dict() for msg in messages]
    
    @staticmethod
    def transfer_to_human(user_id):
        """转接人工客服"""
        # 记录用户请求
        db.add_chat_message(user_id, "请求转接人工客服", 'user')
        
        # 生成回复
        response = "正在为您转接人工客服，请稍候..."
        db.add_chat_message(user_id, response, 'bot')
        
        # 模拟人工客服连接
        time.sleep(1.5)
        response = "已连接人工客服，请问有什么可以帮您？"
        db.add_chat_message(user_id, response, 'bot')
        
        return response