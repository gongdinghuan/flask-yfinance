from flask import Blueprint, jsonify, request
import yfinance as yf
import pandas as pd

from app.utils.error_handler import error_handler

bp = Blueprint('ticker', __name__, url_prefix='/api/ticker')

@bp.route('/<symbol>', methods=['GET'])
@error_handler
def get_ticker_info(symbol):
    """获取股票基本信息"""
    ticker = yf.Ticker(symbol)
    info = ticker.info
    
    # 过滤重要信息
    filtered_info = {
        "symbol": symbol,
        "name": info.get('longName', 'N/A'),
        "currentPrice": info.get('currentPrice', 'N/A'),
        "marketCap": info.get('marketCap', 'N/A'),
        "sector": info.get('sector', 'N/A'),
        "industry": info.get('industry', 'N/A'),
        "country": info.get('country', 'N/A'),
        "website": info.get('website', 'N/A'),
        "description": info.get('longBusinessSummary', 'N/A'),
        "previousClose": info.get('previousClose', 'N/A'),
        "open": info.get('open', 'N/A'),
        "dayLow": info.get('dayLow', 'N/A'),
        "dayHigh": info.get('dayHigh', 'N/A'),
        "yearLow": info.get('fiftyTwoWeekLow', 'N/A'),
        "yearHigh": info.get('fiftyTwoWeekHigh', 'N/A'),
        "dividendYield": info.get('dividendYield', 'N/A'),
        "peRatio": info.get('trailingPE', 'N/A'),
        "beta": info.get('beta', 'N/A')
    }
    
    return jsonify(filtered_info)

@bp.route('/<symbol>/history', methods=['GET'])
@error_handler
def get_ticker_history(symbol):
    """获取股票历史数据"""
    period = request.args.get('period', '1mo')
    interval = request.args.get('interval', '1d')
    
    ticker = yf.Ticker(symbol)
    hist = ticker.history(period=period, interval=interval)
    
    # 转换为字典格式
    data = []
    for date, row in hist.iterrows():
        data.append({
            "date": date.strftime('%Y-%m-%d'),
            "open": float(row['Open']),
            "high": float(row['High']),
            "low": float(row['Low']),
            "close": float(row['Close']),
            "volume": int(row['Volume'])
        })
    
    return jsonify({
        "symbol": symbol,
        "period": period,
        "interval": interval,
        "data": data
    })

@bp.route('/<symbol>/financials', methods=['GET'])
@error_handler
def get_ticker_financials(symbol):
    """获取股票财务数据"""
    ticker = yf.Ticker(symbol)
    
    # 获取财务报表
    income_stmt = ticker.income_stmt
    balance_sheet = ticker.balance_sheet
    cashflow = ticker.cashflow
    
    # 转换为字典格式
    financials = {
        "symbol": symbol,
        "income_statement": [],
        "balance_sheet": [],
        "cash_flow": []
    }
    
    # 处理利润表
    if not income_stmt.empty:
        for item, row in income_stmt.iterrows():
            item_data = {"item": item}
            for col in income_stmt.columns:
                item_data[str(col.date())] = float(row[col]) if not pd.isna(row[col]) else None
            financials["income_statement"].append(item_data)
    
    # 处理资产负债表
    if not balance_sheet.empty:
        for item, row in balance_sheet.iterrows():
            item_data = {"item": item}
            for col in balance_sheet.columns:
                item_data[str(col.date())] = float(row[col]) if not pd.isna(row[col]) else None
            financials["balance_sheet"].append(item_data)
    
    # 处理现金流量表
    if not cashflow.empty:
        for item, row in cashflow.iterrows():
            item_data = {"item": item}
            for col in cashflow.columns:
                item_data[str(col.date())] = float(row[col]) if not pd.isna(row[col]) else None
            financials["cash_flow"].append(item_data)
    
    return jsonify(financials)
