import requests_cache
from requests_ratelimiter import LimiterSession
from datetime import timedelta

class CacheManager:
    """缓存管理器，用于处理 API 请求的缓存和速率限制"""
    
    def __init__(self):
        # 配置缓存
        self.cache_session = requests_cache.CachedSession(
            'yfinance_cache',
            backend='sqlite',
            expire_after=timedelta(hours=1),  # 缓存1小时
            allowable_methods=['GET'],
            allowable_codes=[200, 201, 202, 203, 204, 205, 206]
        )
        
        # 配置速率限制会话
        self.rate_limit_session = LimiterSession(
            per_second=2,  # 每秒最多2个请求
            per_minute=60,  # 每分钟最多60个请求
            per_hour=1000,  # 每小时最多1000个请求
            session=self.cache_session
        )
    
    def get_session(self):
        """获取带有缓存和速率限制的会话"""
        return self.rate_limit_session
    
    def clear_cache(self):
        """清空缓存"""
        self.cache_session.cache.clear()
    
    def get_cache_size(self):
        """获取缓存大小"""
        return len(self.cache_session.cache.responses)

# 创建全局缓存管理器实例
cache_manager = CacheManager()
