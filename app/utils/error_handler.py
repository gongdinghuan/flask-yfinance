from functools import wraps
from flask import jsonify
import yfinance as yf

def error_handler(func):
    """错误处理装饰器"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except yf.exceptions.YFRateLimitError:
            return jsonify({"error": "Too Many Requests. Please try again later."}), 429
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return wrapper
