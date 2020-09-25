from wtafinance.stock import wta_data
if __name__ == '__main__':
    # pro = ts.pro_api()
    #
    # df = pro.daily('000001.SZ')
    # print(df)
    wta = wta_data.wta_api("TPcvTnvcDNBMq4j0d8TVdA==\n","GH3FUuZk9aniiKAKxpJxO9AVZtlFIC3gdc3jR4QvZtwTuWcSLAjrc6r/C3wCWzFX\n")

    # 获取沪深A股的股票列表
    data = wta.getWtaTodayTick(code="002026")
    print(data)




