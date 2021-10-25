from enum import Enum, unique


@unique
class URL(Enum):
    # 主站地址
    DOMAIN = "https://v1.api.juliangip.com"
    # 获取账户余额
    USERS_GETBALANCE = DOMAIN + "/v1/users/getbalance"
    # 动态代理 - - 提取动态代理
    DYNAMIC_GETIPS = DOMAIN + "/v1/dynamic/getips"
    # 动态代理 - - 校验IP可用性
    DYNAMIC_CHECK = DOMAIN + "/v1/dynamic/check"
    # 动态代理 - - 设置代理IP白名单
    DYNAMIC_SETWHITEIP = DOMAIN + "/v1/dynamic/setwhiteip"
    # 动态代理 - - 获取IP白名单
    DYNAMIC_GETWHITEIP = DOMAIN + "/v1/dynamic/getwhiteip"
    # 动态代理 - - 获取代理剩余可用时长
    DYNAMIC_REMAIN = DOMAIN + "/v1/dynamic/remain"
    # 动态代理 - - 获取剩余可用时长
    DYNAMIC_BALANCE = DOMAIN + "/v1/dynamic/balance"
    # 独享代理 - - 获取代理详情
    ALONE_GETIPS = DOMAIN + "/v1/alone/getips"
    # 独享代理 - - 设置代理IP白名单
    ALONE_SETWHITEIP = DOMAIN + "/v1/alone/setwhiteip"
    # 独享代理 - - 获取代理IP白名单
    ALONE_GETWHITEIP = DOMAIN + "/v1/alone/getwhiteip"
