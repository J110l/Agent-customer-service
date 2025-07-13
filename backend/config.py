# 后端配置
class Config:
    # Flask 配置
    SECRET_KEY = 'taobao_customer_service_secret_key'
    
    # DeepSeek API 配置
    DEEPSEEK_API_KEY = 'sk-152249eea92f436589c2201348d38461'  # 替换为你的 DeepSeek API key
    DEEPSEEK_API_URL = 'https://api.deepseek.com/v1/chat/completions'
    DEEPSEEK_MODEL = 'deepseek-chat'  # 使用 DeepSeek 的聊天模型
    
    # 数据库配置
    DATABASE = {
        'name': 'taobao_cs.db',
        'engine': 'sqlite'
    }
    
    # 模拟用户数据
    MOCK_USERS = [
        {
            "id": "TB123456789",
            "username": "淘小宝",
            "avatar": "https://example.com/avatar1.jpg",
            "vip_level": 3,
            "points": 1250
        }
    ]
    
    # 模拟订单数据
    MOCK_ORDERS = [
        {
            "id": "TB20230712001",
            "user_id": "TB123456789",
            "title": "Apple iPhone 14 Pro",
            "price": 8999.00,
            "status": "已发货",
            "date": "2023-07-12",
            "items": [
                {"name": "iPhone 14 Pro 256G", "quantity": 1, "price": 8999.00}
            ]
        }
    ]
    
    # 知识库配置
    KNOWLEDGE_BASE = {
        "订单查询": [
            "您可以在'我的订单'页面查看所有订单",
            "需要帮助查询特定订单吗？请提供订单号",
            "订单状态包括：待付款、待发货、已发货、已完成、已取消"
        ],
        "物流查询": [
            "物流信息可在订单详情页面查看",
            "发货后24小时内会更新物流信息",
            "提供订单号我可以帮您查询最新物流状态"
        ],
        "退货退款": [
            "7天无理由退货，商品需保持完好",
            "退货流程：1.申请退货 2.商家同意 3.寄回商品 4.退款",
            "退款通常会在商家收货后1-3个工作日内退回"
        ],
        "支付问题": [
            "支持支付宝、微信、银行卡等多种支付方式",
            "支付失败可能是网络问题或银行卡限额，请稍后再试",
            "支付成功后订单状态会立即更新为'待发货'"
        ],
        "优惠券": [
            "优惠券可在结算时选择使用",
            "部分优惠券有使用门槛，请留意使用条件",
            "您可以在'我的优惠券'中查看可用优惠券"
        ]
    }