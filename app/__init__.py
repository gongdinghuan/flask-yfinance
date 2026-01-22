from flask import Flask
from flask_cors import CORS

from app.routes import ticker_routes, market_routes, main_routes
from app.utils.json_encoder import NumpyEncoder

def create_app():
    """创建和配置 Flask 应用"""
    app = Flask(__name__)
    
    # 配置
    app.config['SECRET_KEY'] = 'your-secret-key-here'
    app.json_encoder = NumpyEncoder
    
    # 启用 CORS
    CORS(app)
    
    # 注册蓝图
    app.register_blueprint(ticker_routes.bp)
    app.register_blueprint(market_routes.bp)
    app.register_blueprint(main_routes.bp)
    
    return app
