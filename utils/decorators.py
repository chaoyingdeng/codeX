from basic.exceptions import CodeXException


class Decorator:

    @classmethod
    def obs_exceptions(cls, fn):
        """ 业务执行过程中出现已知异常进行压制"""

        def wrapper(*args, **kwargs):
            try:
                res = fn(*args, **kwargs)
            except CodeXException:
                return
            return res

        return wrapper
