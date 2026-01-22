import json
import numpy as np
import pandas as pd

class NumpyEncoder(json.JSONEncoder):
    """自定义 JSON 编码器处理 numpy 类型"""
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, pd.Timestamp):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        return super(NumpyEncoder, self).default(obj)
