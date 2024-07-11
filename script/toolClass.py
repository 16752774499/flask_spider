# # 自定义JSON编码器以处理datetime类型的对象
import json
from datetime import datetime

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        """
        将JSONEncoder类的default方法重写，用于处理datetime类型的数据。

        Args:
            obj (Any): 需要进行序列化的对象。

        Returns:
            Union[str, Any]: 序列化后的结果。如果obj是datetime类型，则返回其isoformat()方法返回的字符串；
            否则调用父类的default方法返回结果。

        """
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)
