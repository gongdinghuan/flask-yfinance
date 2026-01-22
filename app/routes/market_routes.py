from flask import Blueprint, jsonify
import yfinance as yf

from app.utils.error_handler import error_handler

bp = Blueprint('market', __name__, url_prefix='/api/market')

@bp.route('/<market>', methods=['GET'])
@error_handler
def get_market_info(market):
    """获取市场信息"""
    market_obj = yf.Market(market)
    status = market_obj.status
    summary = market_obj.summary
    
    return jsonify({
        "market": market,
        "status": status,
        "summary": summary
    })

@bp.route('/search/<query>', methods=['GET'])
@error_handler
def search_ticker(query):
    """搜索股票"""
    search = yf.Search(query)
    quotes = search.quotes
    
    results = []
    for quote in quotes:
        results.append({
            "symbol": quote.get('symbol', 'N/A'),
            "name": quote.get('shortname', 'N/A'),
            "type": quote.get('quoteType', 'N/A'),
            "exchange": quote.get('exchange', 'N/A'),
            "price": quote.get('regularMarketPrice', 'N/A')
        })
    
    return jsonify({
        "query": query,
        "results": results
    })

@bp.route('/markets', methods=['GET'])
@error_handler
def get_available_markets():
    """获取可用市场列表"""
    markets = [
        "US", "GB", "ASIA", "EUROPE",
        "RATES", "COMMODITIES", "CURRENCIES", "CRYPTOCURRENCIES"
    ]
    return jsonify({"markets": markets})
