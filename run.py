import time
from wtafinance.wtastock import wta_data

if __name__ == '__main__':
    # pro = ts.pro_api()
    #
    # df = pro.daily('000001.SZ')
    # print(df)
    wta = wta_data.wta_api("token")
    print(time.time())
    data = wta.getWtaHistData(code="300570",is_dapan=False)
    print(time.time())

    print(data)




