import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from flask import Flask, jsonify, request
from flask_cors import CORS
from .services import CustomerService
from .config import Config
import time

app = Flask(__name__)
CORS(app)  # 允许跨域请求

# 默认用户ID (实际应用中应从认证信息获取)
DEFAULT_USER_ID = "TB123456789"

@app.route('/')
def index():
    return "淘宝智能客服系统后端服务"

@app.route('/api/user', methods=['GET'])
def get_user_info():
    """获取用户信息"""
    user_id = request.args.get('user_id', DEFAULT_USER_ID)
    user_info = CustomerService.get_user_info(user_id)
    if user_info:
        return jsonify({"success": True, "data": user_info})
    return jsonify({"success": False, "message": "用户不存在"}), 404

@app.route('/api/orders', methods=['GET'])
def get_user_orders():
    """获取用户订单列表"""
    user_id = request.args.get('user_id', DEFAULT_USER_ID)
    orders = CustomerService.get_user_orders(user_id)
    return jsonify({"success": True, "data": orders})

@app.route('/api/order/<order_id>', methods=['GET'])
def get_order_details(order_id):
    """获取订单详情"""
    order = CustomerService.get_order_details(order_id)
    if order:
        return jsonify({"success": True, "data": order})
    return jsonify({"success": False, "message": "订单不存在"}), 404

@app.route('/api/chat', methods=['POST'])
def handle_chat():
    """处理聊天消息"""
    data = request.json
    user_id = data.get('user_id', DEFAULT_USER_ID)
    message = data.get('message', '')
    
    if not message:
        return jsonify({"success": False, "message": "消息内容不能为空"}), 400
    
    # 模拟客服思考时间
    time.sleep(0.5)
    
    response = CustomerService.handle_user_message(user_id, message)
    return jsonify({"success": True, "response": response})

@app.route('/api/chat/history', methods=['GET'])
def get_chat_history():
    """获取聊天历史"""
    user_id = request.args.get('user_id', DEFAULT_USER_ID)
    history = CustomerService.get_chat_history(user_id)
    return jsonify({"success": True, "data": history})

@app.route('/api/chat/transfer', methods=['POST'])
def transfer_to_human():
    """转接人工客服"""
    data = request.json
    user_id = data.get('user_id', DEFAULT_USER_ID)
    
    # 模拟转接过程
    response = CustomerService.transfer_to_human(user_id)
    return jsonify({"success": True, "response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)