import yfinance as yf
import time
import logging
from app.utils.cache_utils import cache_manager

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FinanceService:
    """金融数据服务，封装 yfinance 调用并处理缓存和速率限制"""
    
    def __init__(self):
        self.max_retries = 3
        self.retry_delay = 2  # 秒
        self.cache_enabled = True
    
    def _with_retry(self, func, *args, **kwargs):
        """带重试机制的函数调用"""
        for attempt in range(self.max_retries):
            try:
                return func(*args, **kwargs)
            except yf.exceptions.YFRateLimitError as e:
                logger.warning(f"Rate limit hit (attempt {attempt+1}/{self.max_retries}): {e}")
                if attempt == self.max_retries - 1:
                    logger.error("Max retries reached, rate limit still active")
                    raise
                # 指数退避策略
                delay = self.retry_delay * (2 ** attempt)
                logger.info(f"Retrying in {delay} seconds...")
                time.sleep(delay)
            except Exception as e:
                logger.error(f"Unexpected error: {e}")
                raise
    
    def get_ticker_info(self, symbol):
        """获取股票基本信息"""
        def _fetch_info():
            ticker = yf.Ticker(symbol)
            return ticker.info
        
        return self._with_retry(_fetch_info)
    
    def get_ticker_history(self, symbol, period="1mo", interval="1d"):
        """获取股票历史数据"""
        def _fetch_history():
            ticker = yf.Ticker(symbol)
            return ticker.history(period=period, interval=interval)
        
        return self._with_retry(_fetch_history)
    
    def get_ticker_financials(self, symbol):
        """获取股票财务数据"""
        def _fetch_financials():
            ticker = yf.Ticker(symbol)
            return {
                "income_stmt": ticker.income_stmt,
                "balance_sheet": ticker.balance_sheet,
                "cashflow": ticker.cashflow
            }
        
        return self._with_retry(_fetch_financials)
    
    def get_market_info(self, market):
        """获取市场信息"""
        def _fetch_market():
            market_obj = yf.Market(market)
            return {
                "status": market_obj.status,
                "summary": market_obj.summary
            }
        
        return self._with_retry(_fetch_market)
    
    def search_ticker(self, query):
        """搜索股票"""
        def _fetch_search():
            search = yf.Search(query)
            return search.quotes
        
        return self._with_retry(_fetch_search)

# 创建全局服务实例
finance_service = FinanceService()
