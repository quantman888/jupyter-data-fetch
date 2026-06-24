from http.cookies import SimpleCookie

from jupyter_kernel_client import KernelClient

from jupyter_date_fetch.codec import PickleB85Codec, PickleImageCodec

Cookie = 'user-12345678901=2|1:0|10:1782299974|16:user-12345678901|48:OGYwNDMwYTItNzRhYS00MzFkLTllNTQtMzg1ZjFiYzkyYTlm|4176159ad874b6d10a669843372e3145ee402b26f7757e69427d54ae1d2cb4c8; uid=wKgyrWie/38DxnbRN5/yAg==; _xsrf=2|949f5998|2cf1cdfee6cddd473b2261e1876ac40b|1780041427; token=5744247f87648dae96726fa83d3b8c64c748c60f; PHPSESSID=3t1slsrfid9m5fef6id6aikfr1'

headers = {'Cookie': Cookie, 'X-XSRFToken': SimpleCookie(Cookie)['_xsrf'].value}

with KernelClient(server_url="https://www.joinquant.com/user/12345678901", token=None, headers=headers) as kernel:
    code = """
df = get_fundamentals(query(
        valuation, income
    ).filter(
        # 这里不能使用 in 操作, 要使用in_()函数
        valuation.code.in_(['000001.XSHE', '600000.XSHG'])
    ), date='2015-10-15')
"""
    reply = kernel.execute(PickleB85Codec.generate_code(code, var_name='df'))
    # print(reply)
    obj = PickleB85Codec.extract_decode(reply)
    print(obj)

    reply = kernel.execute(PickleImageCodec.generate_code(var_name='df'))
    # print(reply)
    obj = PickleImageCodec.extract_decode(reply)
    print(obj)
