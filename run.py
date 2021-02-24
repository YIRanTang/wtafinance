from wtafinance.stock import wta_data

if __name__ == '__main__':
    # pro = ts.pro_api()
    #
    # df = pro.daily('000001.SZ')
    # print(df)
    # wta = wta_data.wta_api("TPcvTnvcDNBMq4j0d8TVdA==\n","s8PkWSSy4WK1IJJOwZ5tvRc/vpUYVB25jq5qzlqXxXNHdLsODOkQPZpyN+oLHmjk\n")
    # # # 获取沪深A股的股票列表,type="0",date = {"start":"2020-08-10","end":"2020-12-20"}
    # res_data = wta.getWtaBalanceSheet(SECCODE="300100")
    # print(data)





    #  读取文件数据
    wta_data.set_path(r"D:\tby_svn\wta_finance\trunk\2 项目实施阶段\2.4 系统开发\2.4.1 系统实现\WtaFinancePlatform\WtaFinancePlatform_WPF\bin\x86\Debug\Data")

    mainclass = wta_data.get_mainClass()
    # date_time = {
    #     "startTime": "2015-01-01 00:00:00",
    #     "endTime": "2021-01-01 00:00:00"
    # }
    mainclass.change_field_code("close","close123",className="日数据")

    res_data = mainclass.get_hist_data("600000","2015-01-01",fqt="1",ktype="D")
    # res_data = mainclass.get_stockIndex_data("600000","000001","2015-01-01",fqt="0",ktype="5")
    # res_data = mainclass.get_index("000001","2015-01-01",fqt="2",ktype="D")
    # res_data = mainclass.income("600000","2015-01-01")
    # res_data = mainclass.cashflow("600000","2015-01-01","2018-01-01")
    # res_data = mainclass.balancesheet("600000","2015-01-01")
    print(res_data)

    # from wtafinance.stock import wta_data
    # res = wta_data.get_table_field_code(isParent=True)  # 获取所有表的编码
    # res = wta_data.get_table_field_code(parentTableName="利润表(非金融)")  # 获取某个表所有字段的编码
    res = wta_data.wta_file_config_code() #  # 获取所有表与字段的编码
    print(res)




