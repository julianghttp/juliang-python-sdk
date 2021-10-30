import unittest
import Juliang
import common.DynamicGetIps as dgi
import common.DynamicCheck as check
import common.DynamicSetWhiteIp as dswi
import common.DynamicGetWhiteIp as dgwi
import common.DynamicRemain as dr
import common.DynamicBalance as db
import common.UsersGetBalance as ugb
import common.AloneGetIps as agi
import common.AloneSetWhiteIp as aswi
import common.AloneGetWhiteIp as agwi
import common.DynamicReplaceWhiteIp as drwi
import common.AloneReplaceWhiteIp as arwi

dynamic_trade_no = "11351242352345234523453465735679"
dynamic_key = "0794dsfdsgsdgw3tg45t324502bb21cbcd"

user_id = "1215104"
key = "514a5dfgsdgshwry45gergwerg2817a866328c"

alone_trade_no = "405856456453623452345135232429"
alone_key = "7cc5a5ba63sgeuhfr9u2hihr30u3hq9ef84a82f1"


class MyTestCase(unittest.TestCase):
    # 动态代理 --提取动态代理
    def test_dynamic_get_ips(self):
        m = dgi.DynamicGetIps(dynamic_key, dynamic_trade_no, "10")
        m.pt = "1"
        m.result_type = "json"
        value = Juliang.dynamic_get_ips(m)
        print(value)

    # 动态代理 -- 校验IP可用性
    def test_dynamic_check(self):
        m = check.DynamicCheck(dynamic_key, dynamic_trade_no)
        m.proxy = "1.1.1.1:8088"
        value = Juliang.dynamic_check(m)
        print(value)

    # 动态代理 -- 设置代理IP白名单
    def test_dynamic_set_white_ip(self):
        m = dswi.DynamicSetWhiteIp(dynamic_key, dynamic_trade_no)
        m.ips = "66.66.66.66"
        value = Juliang.dynamic_set_white_ip(m)
        print(value)

    # 动态代理 -- 获取IP白名单
    def test_dynamic_get_white_ip(self):
        m = dgwi.DynamicGetWhiteIp(dynamic_key, dynamic_trade_no)
        value = Juliang.dynamic_get_white_ip(m)
        print(value)

    # 动态代理 -- 修改IP白名单
    def test_dynamic_replace_white_ip(self):
        m = drwi.DynamicReplaceWhiteIp(dynamic_key, dynamic_trade_no)
        m.old_ip = "1.1.1.1"
        m.new_ip = "3.3.3.3"
        value = Juliang.dynamic_replace_white_ip(m)
        print(value)

    # 动态代理 -- 获取代理剩余可用时长
    def test_dynamic_remain(self):
        m = dr.DynamicRemain(dynamic_key, dynamic_trade_no)
        m.proxy = "12.12.12.12:8088"
        value = Juliang.dynamic_remain(m)
        print(value)

    # 动态代理 -- 获取剩余可提取IP数量
    def test_dynamic_balance(self):
        m = db.DynamicBalance(dynamic_key, dynamic_trade_no)
        value = Juliang.dynamic_balance(m)
        print(value)

    # 获取账户余额
    def test_users_get_balance(self):
        m = ugb.UsersGetBalance(key, user_id)
        value = Juliang.users_get_balance(m)
        print(value)

    # 独享代理 -- 获取代理详情[异常]
    def test_alone_get_ips(self):
        m = agi.AloneGetIps(alone_key, alone_trade_no)
        value = Juliang.alone_get_ips(m)
        print(value)

    # 独享代理 -- 替换IP白名单
    def test_alone_replace_white_ip(self):
        m = arwi.AloneReplaceWhiteIp(alone_key, alone_trade_no)
        m.old_ip = "1.1.1.1"
        m.new_ip = "2.2.2.2"
        value = Juliang.alone_replace_white_ip(m)
        print(value)

    # 独享代理 -- 设置代理IP白名单
    def test_alone_set_white_ip(self):
        m = aswi.AloneSetWhiteIp(alone_key, alone_trade_no)
        m.ips = "66.66.66.66"
        value = Juliang.alone_set_white_ip(m)
        print(value)

    # 独享代理 -- 获取代理IP白名单
    def test_alone_get_white_ip(self):
        m = agwi.AloneGetWhiteIp(alone_key, alone_trade_no)
        value = Juliang.alone_get_white_ip(m)
        print(value)


if __name__ == '__main__':
    unittest.main()
