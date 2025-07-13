from datetime import datetime

class User:
    def __init__(self, user_id, username, avatar, vip_level, points):
        self.id = user_id
        self.username = username
        self.avatar = avatar
        self.vip_level = vip_level
        self.points = points
        self.created_at = datetime.now()
        
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "avatar": self.avatar,
            "vip_level": self.vip_level,
            "points": self.points,
            "created_at": self.created_at.isoformat()
        }

class Order:
    def __init__(self, order_id, user_id, title, price, status, date, items=None):
        self.id = order_id
        self.user_id = user_id
        self.title = title
        self.price = price
        self.status = status
        self.date = date
        self.items = items or []
        
    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "title": self.title,
            "price": self.price,
            "status": self.status,
            "date": self.date,
            "items": self.items
        }

class ChatMessage:
    def __init__(self, message_id, user_id, content, sender, timestamp):
        self.id = message_id
        self.user_id = user_id
        self.content = content
        self.sender = sender  # 'user' or 'bot'
        self.timestamp = timestamp
        
    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "content": self.content,
            "sender": self.sender,
            "timestamp": self.timestamp.isoformat()
        }