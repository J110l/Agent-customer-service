import uuid
from datetime import datetime, timedelta
from .models import User, Order, ChatMessage
from .config import Config

class MockDB:
    def __init__(self):
        self.users = {}
        self.orders = {}
        self.chat_messages = {}
        self._init_mock_data()
        
    def _init_mock_data(self):
        # 初始化模拟用户
        for user_data in Config.MOCK_USERS:
            user = User(
                user_id=user_data["id"],
                username=user_data["username"],
                avatar=user_data.get("avatar", ""),
                vip_level=user_data.get("vip_level", 1),
                points=user_data.get("points", 0)
            )
            self.users[user.id] = user
        
        # 初始化模拟订单
        for order_data in Config.MOCK_ORDERS:
            order = Order(
                order_id=order_data["id"],
                user_id=order_data["user_id"],
                title=order_data["title"],
                price=order_data["price"],
                status=order_data["status"],
                date=order_data["date"],
                items=order_data.get("items", [])
            )
            self.orders[order.id] = order
    
    # 用户相关操作
    def get_user(self, user_id):
        return self.users.get(user_id)
    
    def get_all_users(self):
        return list(self.users.values())
    
    # 订单相关操作
    def get_order(self, order_id):
        return self.orders.get(order_id)
    
    def get_user_orders(self, user_id):
        return [order for order in self.orders.values() if order.user_id == user_id]
    
    # 聊天消息相关操作
    def add_chat_message(self, user_id, content, sender):
        message_id = str(uuid.uuid4())
        message = ChatMessage(
            message_id=message_id,
            user_id=user_id,
            content=content,
            sender=sender,
            timestamp=datetime.now()
        )
        self.chat_messages[message_id] = message
        return message
    
    def get_chat_history(self, user_id, limit=20):
        user_messages = [msg for msg in self.chat_messages.values() if msg.user_id == user_id]
        sorted_messages = sorted(user_messages, key=lambda x: x.timestamp, reverse=True)
        return sorted_messages[:limit]
    
    # 知识库操作
    def get_knowledge_response(self, category):
        responses = Config.KNOWLEDGE_BASE.get(category, [])
        if responses:
            return responses[0]  # 返回第一个预设回复
        return None
    
    def find_knowledge_category(self, message):
        message_lower = message.lower()
        
        # 关键词匹配
        keyword_map = {
            "订单查询": ["订单", "购买", "买了", "下单", "历史"],
            "物流查询": ["物流", "快递", "发货", "配送", "运输"],
            "退货退款": ["退货", "退款", "退钱", "取消", "退换"],
            "支付问题": ["支付", "付款", "付钱", "银行卡", "支付宝", "微信"],
            "优惠券": ["优惠", "优惠券", "折扣", "打折", "促销"]
        }
        
        for category, keywords in keyword_map.items():
            if any(keyword in message_lower for keyword in keywords):
                return category
        
        return None

# 创建全局数据库实例
db = MockDB()