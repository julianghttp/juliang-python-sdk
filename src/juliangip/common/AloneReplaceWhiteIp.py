class AloneReplaceWhiteIp(object):
    def __init__(self, key, trade_no):
        self.key = key
        self.trade_no = trade_no

    # 业务秘钥
    key = ""
    # 业务编号
    trade_no = ""
    # ip列表
    old_ip = ""
    # 已存在,需要被替换的白名单IP
    new_ip = ""
    # 是否重置已存在的白名单IP
    reset = ""