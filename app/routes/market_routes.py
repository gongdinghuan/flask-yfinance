from flask import Blueprint, jsonify

from app.services.finance_service import finance_service

bp = Blueprint('market', __name__, url_prefix='/api/market')

@bp.route('/<market>', methods=['GET'])
def get_market_info(market):
    """获取市场信息"""
    try:
        market_data = finance_service.get_market_info(market)
        
        return jsonify({
            "market": market,
            "status": market_data['status'],
            "summary": market_data['summary']
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/search/<query>', methods=['GET'])
def search_ticker(query):
    """搜索股票"""
    try:
        quotes = finance_service.search_ticker(query)
        
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
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/markets', methods=['GET'])
def get_available_markets():
    """获取可用市场列表"""
    markets = [
        "US", "GB", "ASIA", "EUROPE",
        "RATES", "COMMODITIES", "CURRENCIES", "CRYPTOCURRENCIES"
    ]
    return jsonify({"markets": markets})
