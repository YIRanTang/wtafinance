## 赢家通财经大数据(wtaFinance)SDK 方法说明

## 历史行情/复权数据
**接口：getWtaHistData**

**描述：获取股票基础K线数据**

### 输入参数
|  名称 | 类型  | 说明  |  是否必传 |  默认值 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|  code | String  | 股票代码  | 是  |  - |
|  type | String  | 股票类型(0深证,1上证) | 是  |  - |
|  date | Dict  | 时间区间 | 否  |  最近100天（示例：`{"start":"2020-08-10","end":"2020-08-20"}`） |
|is_dapan|Boolean|是否查找指数|否|-|
|fqt|String|复权值（0：不复权，1：前复权，2：后复权）|否|0|

### 输出参数
|  名称 | 类型  | 说明  |
| :------------ | :------------ | :------------ |
|code|String|股票代码|
|name|String|股票名称|
|data|String|日期,开盘价,收盘价,最高价,最低价,成交量,成交额,振幅,涨跌幅,换手率|
|is_dapan|Boolean|是否为指数数据|
|type|String|股票类型(0深证,1上证)|
|fqt|String|复权值(0前复权,1不复权,2后复权)|
|high|String|最高价|
|vol2|String|成交额|
|open|String|开盘价|
|low|String|最低价|
|tr|String|换手率|
|Amplitude|String|振幅|
|Change|String|涨跌幅|
|close|String|收盘价|
|date|String|时间|
|vol1|String|成交量|


### 接口示例
```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取平安银行历史的K线数据
data = wta.getWtaHistData(code="000001",is_dapan=False)
```
或者：

```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取平安银行复权后历史的K线数据
data = wta.getWtaHistData(code="000001",is_dapan=False,fqt="2")
```

------------

## 实时行情
**接口：getWtaRealQuotes**

**描述：获取股票每日的分时数据**

### 输入参数
|  名称 | 类型  | 说明  |  是否必传 |  默认值 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|  code | String  | 股票代码  | 是  |  - |
|  type | String  | 股票类型(0深证,1上证) | 是  |  - |
|is_dapan|Boolean|是否查找指数|否|-|
|  date | Dict  | 时间区间 | 否  |  最近100天（示例：`{"start":"2020-08-10","end":"2020-08-20"}`） |

### 输出参数
|  名称 | 类型  | 说明  |
| :------------ | :------------ | :------------ |
|code|String|股票代码|
|name|String|股票名称|
|trends|String|分时数据（日期,开盘价,收盘价,最高价,最低价,成交量,成交额,均价）|
|date|String|日期|
|preClose|Float|昨日收盘价|
|is_dapan|Boolean|是否为指数数据|
|type|String|股票类型(0深证,1上证)|

### 接口示例
```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取平安银行昨天的分钟走势数据
data = wta.getWtaRealQuotes(code="000001",is_dapan=False)
```
或者：

```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取平安银行2020-08-07日的分钟走势数据
data = wta.getWtaRealQuotes(code="000001",is_dapan=False,date="2020-08-07")
```

------------

## 历史分笔
**接口：getWtaTodayTick**

**描述：获取股票每日的分笔交易数据**

### 输入参数
|  名称 | 类型  | 说明  |  是否必传 |  默认值 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|  code | String  | 股票代码  | 是  |  - |
|  date | Dict  | 时间区间 | 否  |  最近100天（示例：`{"start":"2020-08-10","end":"2020-08-20"}`） |

### 输出参数
|  名称 | 类型  | 说明  |
| :------------ | :------------ | :------------ |
|code|String|股票代码|
|name|String|股票名称|
|data|String|分笔数据（序号/分时/成交价格/价格变动/成交量/成交价格/买卖性质(买盘，买盘，中性盘)）|
|date|String|日期|
|type|String|股票类型(0深证,1上证)|

### 接口示例
```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取平安银行昨天的分笔交易数据
data = wta.getWtaTodayTick(code="000001")
```
或者：

```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取平安银行2020-08-10的分笔交易数据
data = wta.getWtaTodayTick(code="000001",date="2020-08-10")
```

------------

## 股票代码分类
**接口：getWtaCodeClass**

**描述：获取股票代码列表**

### 输入参数
|  名称 | 类型  | 说明  |  是否必传 |  默认值 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|String|股票代码|否|-|
|name|String|股票名称|否|-|
|bk_name|String|板块名称(沪深A股，上证A股，深证A股，中小板，创业板，科创板，沪股通，深股通，B股)|否|-|

### 输出参数
|  名称 | 类型  | 说明  |
| :------------ | :------------ | :------------ |
|code|String|股票代码|
|name|String|股票名称|
|type|String|股票类型(0深证,1上证)|
|bk_name|String|板块名称|

### 接口示例
```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取沪深A股的股票列表
data = wta.getWtaCodeClass(bk_name="沪深A股")
```

------------

## 股票概念分类
**接口：getWtaCodeClass**

**描述：获取股票概念列表**

### 输入参数
|  名称 | 类型  | 说明  |  是否必传 |  默认值 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|String|股票代码|否|-|
|name|String|股票名称|否|-|
|bk_name|String|概念名称|否|-|

### 输出参数
|  名称 | 类型  | 说明  |
| :------------ | :------------ | :------------ |
|code|String|股票代码|
|name|String|股票名称|
|bk_name|String|概念名称|
|bk_code|String|概念名称|



### 接口示例
```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取证金持股概念的股票列表
data = wta.getWtaConceptClass(bk_name="证金持股")
```

------------

## 股票行业分类
**接口：getWtaIndustryClass**

**描述：获取股票行业列表**

### 输入参数
|  名称 | 类型  | 说明  |  是否必传 |  默认值 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|String|股票代码|否|-|
|name|String|股票名称|否|-|
|bk_name|String|行业名称|否|-|

### 输出参数
|  名称 | 类型  | 说明  |
| :------------ | :------------ | :------------ |
|code|String|股票代码|
|name|String|股票名称|
|bk_name|String|行业名称|
|bk_code|String|行业名称|

### 接口示例
```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取房地产行业的股票列表
data = wta.getWtaConceptClass(bk_name="房地产")
```

------------

## 股票地域分类
**接口：getWtaAreaClass**

**描述：获取股票地域列表**

### 输入参数
|  名称 | 类型  | 说明  |  是否必传 |  默认值 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|String|股票代码|否|-|
|name|String|股票名称|否|-|
|bk_name|String|行业名称|否|-|

### 输出参数
|  名称 | 类型  | 说明  |
| :------------ | :------------ | :------------ |
|code|String|股票代码|
|name|String|股票名称|
|bk_name|String|地域名称|
|bk_code|String|地域名称|


### 接口示例
```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取山东板块的股票列表
data = wta.getWtaConceptClass(bk_name="山东板块")
```

------------

## 终止上市股票列表
**接口：getWtaTerminaStocks**

**描述：获取终止获暂停上市的股票列表**

### 输入参数
|  名称 | 类型  | 说明  |  是否必传 |  默认值 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|String|股票代码|否|-|
|name|String|股票名称|否|-|
|bk_name|String|终止上市/暂停上市|否|-|

### 输出参数
|  名称 | 类型  | 说明  |
| :------------ | :------------ | :------------ |
|code|String|股票代码|
|name|String|股票名称|
|bk_name|String|概念名称|
|listing_date|String|上市日期|
|change_date|String|终止上市/暂停上市日期|


### 接口示例
```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取终止上市的股票列表
data = wta.getWtaTerminaStocks(bk_name="终止上市")
```

------------

## 个股上榜统计
**接口：getWtaCapTops**

**描述：获取个股龙虎板上板统计**

### 输入参数
|  名称 | 类型  | 说明  |  是否必传 |  默认值 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|String|股票代码|否|-|
|name|String|股票名称|否|-|
|date|String|日期|否|昨日|

### 输出参数
|  名称 | 类型  | 说明  |
| :------------ | :------------ | :------------ |
|code|String|股票代码|
|name|String|股票名称|
|scount|String|卖出席位数|
|bcount|String|买入席位数|
|date|String|日期|
|count|String|上榜次数|
|bamount|String|龙虎板买入额|
|samount|String|龙虎板卖出额|
|net|String|净额|
|zmoney|String|龙虎板总成交额|


### 接口示例
```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取2020-08-07日的龙虎板上板统计列表
data = wta.getWtaCapTops(date="2020-08-07")
```

------------

## 机构席位追踪
**接口：getWtaInstTops**

**描述：获取机构席位追踪数据**

### 输入参数
|  名称 | 类型  | 说明  |  是否必传 |  默认值 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|String|股票代码|否|-|
|name|String|股票名称|否|-|
|date|String|日期|否|昨日|

### 输出参数
|  名称 | 类型  | 说明  |
| :------------ | :------------ | :------------ |
|code|String|股票代码|
|name|String|股票名称|
|scount|String|卖出席位数|
|bcount|String|买入席位数|
|date|String|日期|
|bamount|String|机构购买额|
|samount|String|机构卖出额|
|net|String|净额|
|tmoney|String|龙虎板成交金额|


### 接口示例
```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取2020-08-07日的机构席位追踪数据列表
data = wta.getWtaInstTops(date="2020-08-07")
```

------------

## 营业部上榜统计
**接口：getWtaBrokerTops**

**描述：获取营业部上榜统计数据**

### 输入参数
|  名称 | 类型  | 说明  |  是否必传 |  默认值 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|broker|String|营业部名称|否|-|
|date|String|日期|否|-|

### 输出参数
|  名称 | 类型  | 说明  |
| :------------ | :------------ | :------------ |
|date|String|日期|
|sumActMoney|String|龙虎板成交金额|
|scount|String|卖出席位数|
|samount|String|累积卖出额|
|bcount|String|买入席位数|
|bamount|String|累积购买额|
|count|String|上榜次数|
|broker|String|营业部名称|


### 接口示例
```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取2020-08-07日的营业部上榜统计数据列表
data = wta.getWtaBrokerTops(date="2020-08-07")
```

------------

## 每日龙虎榜列表
**接口：getWtaTopList**

**描述：获取每日龙虎榜列表数据**

### 输入参数
|  名称 | 类型  | 说明  |  是否必传 |  默认值 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|String|股票代码|否|-|
|name|String|股票名称|否|-|
|date|String|日期|否|-|

### 输出参数
|  名称 | 类型  | 说明  |
| :------------ | :------------ | :------------ |
|name|String|股票名称|
|code|String|股票代码|
|date|String|日期|
|Turnover|String|市场总成交额|
|reason|String|上板原因|
|sratio|String|卖出占总成交比例|
|sell|String|卖出额|
|bratio|String|买入占总成交比例|
|buy|String|买入额|
|amount|String|龙虎板成交额|


### 接口示例
```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取2020-08-07日的龙虎榜列表列表
data = wta.getWtaTopList(date="2020-08-07")
```

------------

## 机构成交明细表
**接口：getWtaInstDetail**

**描述：获取机构成交明细数据**

### 输入参数
|  名称 | 类型  | 说明  |  是否必传 |  默认值 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|String|股票代码|否|-|
|name|String|股票名称|否|-|
|securities_company|String|证券公司名|否|-|

### 输出参数
|  名称 | 类型  | 说明  |
| :------------ | :------------ | :------------ |
|name|String|股票名称|
|code|String|股票代码|
|securities_company|String|证券公司名|
|salesName|String|营业部名称|
|samount|String|机构卖出额|
|bamount|String|机构买入额|
|pBuy|String|买卖净额|
|bcount|String|买入席位数|
|tDate|String|交易日期|


### 接口示例
```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取长江证券的机构成交明细数据
data = wta.getWtaInstDetail(securities_company="长江证券")
```

------------

## CPI信息
**接口：getWtaCPI**

**描述：获取CPI信息数据**

### 输入参数
|  名称 | 类型  | 说明  |  是否必传 |  默认值 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|-|-|-|-|-|

### 输出参数
|  名称 | 类型  | 说明  |
| :------------ | :------------ | :------------ |
|month|String|月份|
|datavalue|String|增加值/增长率|
|year|String|年份|
|affiliation|String|datavalue字段说明|



### 接口示例
```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取CPI信息数据
data = wta.getWtaCPI()
```

------------

## GDP信息
**接口：getWtaGDP**

**描述：获取GDP信息数据**

### 输入参数
|  名称 | 类型  | 说明  |  是否必传 |  默认值 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|-|-|-|-|-|

### 输出参数
|  名称 | 类型  | 说明  |
| :------------ | :------------ | :------------ |
|month|String|月份|
|datavalue|String|增加值/增长率|
|year|String|年份|
|affiliation|String|datavalue字段说明|



### 接口示例
```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取GDP信息数据
data = wta.getWtaGDP()
```

------------

## 存款准备金率
**接口：getWtaDepositReserve**

**描述：获取存款准备金率数据**

### 输入参数
|  名称 | 类型  | 说明  |  是否必传 |  默认值 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|-|-|-|-|-|

### 输出参数
|  名称 | 类型  | 说明  |
| :------------ | :------------ | :------------ |
|pubDate|String||
|mediumInstitutionsRatioPre|String||
|effectiveDate|String||
|mediumInstitutionsRatioAfter|String||
|bigInstitutionsRatioAfter|String||
|bigInstitutionsRatioPre|String||


### 接口示例
```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取存款准备金率数据
data = wta.getWtaDepositRate()
```

------------

## 存款利率
**接口：getWtaDepositRate**

**描述：获取存款利率数据**

### 输入参数
|  名称 | 类型  | 说明  |  是否必传 |  默认值 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|-|-|-|-|-|

### 输出参数
|  名称 | 类型  | 说明  |
| :------------ | :------------ | :------------ |
|pubDate|String||
|fixedDepositRate2Year|String||
|demandDepositRate|String||
|fixedDepositRate6Month|String||
|fixedDepositRate3Year|String||
|installmentFixedDepositRate5Year|String||
|fixedDepositRate5Year|String||
|installmentFixedDepositRate3Year|String||
|fixedDepositRate3Month|String||
|installmentFixedDepositRate1Year|String||
|fixedDepositRate1Year|String||


### 接口示例
```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取存款利率数据
data = wta.getWtaDepositRate()
```

------------

## 贷款利率
**接口：getWtaLoanRate**

**描述：获取贷款利率数据**

### 输入参数
|  名称 | 类型  | 说明  |  是否必传 |  默认值 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|-|-|-|-|-|

### 输出参数
|  名称 | 类型  | 说明  |
| :------------ | :------------ | :------------ |
|mortgateRateBelow5Year|String||
|pubDate|String||
|loanRate6MonthTo1Year|String||
|loanRateAbove5Year|String||
|loanRate1YearTo3Year|String||
|mortgateRateAbove5Year|String||
|loanRate6Month|String||
|loanRate3YearTo5Year|String||


### 接口示例
```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取贷款利率数据
data = wta.getWtaLoanRate()
```

------------

## 业绩报告
**接口：getWtaPerfReport**

**描述：获取业绩报告数据**

### 输入参数
|  名称 | 类型  | 说明  |  是否必传 |  默认值 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|SECCODE|String|股票代码|是|-|
|SECNAME|String|股票名称|否|-|
|F001D|String|报告时间|否|-|

### 输出参数
|  名称 | 类型  | 说明  |
| :------------ | :------------ | :------------ |
|SECNAME|String|股票名称|
|SECCODE|String|股票代码|
|F011N|Float|营业利润率|
|F010N|Float|毛利率|
|F009N|Float|归属母公司所有者净利润|
|F008N|Float|营业利润|
|F007N|Float|营业成本|
|F006N|Float|营业收入|
|F005N|Float|每股经营现金流量|
|F004N|Float|净资产收益率|
|F003N|Float|每股净资产|
|F002N|Float|每股收益|
|F001D|String|报告期|


### 接口示例
```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取平安银行的业绩报告数据
data = wta.getWtaPerfReport(SECCODE="000001")
```

------------

## 业绩预告
**接口：getWtaForecastData**

**描述：获取业绩预告数据**

### 输入参数
|  名称 | 类型  | 说明  |  是否必传 |  默认值 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|SECCODE|String|股票代码|是|-|
|SECNAME|String|股票名称|否|-|
|F001D|String|报告时间|否|-|

### 输出参数
|  名称 | 类型  | 说明  |
| :------------ | :------------ | :------------ |
|SECNAME|String|股票名称|
|SECCODE|String|股票代码|
|DECLAREDATE|String|公告日期|
|F003V|String|业绩类型|
|F009N|String|净利润增长幅下限|
|F010N|String|净利润增长幅上限|
|F001D|String|报告年度|
|F004V|String|业绩预告内容|
|F005V|String|业绩变化原因|
|F002V|String|申万二级行业|



### 接口示例
```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取平安银行的业绩预告数据
data = wta.getWtaForecastData(SECCODE="000001")
```

------------

## 货币供应量
**接口：getWtaMoneySupply**

**描述：获取货币供应量年底余额数据**

### 输入参数
|  名称 | 类型  | 说明  |  是否必传 |  默认值 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|-|-|-|-|-|

### 输出参数
|  名称 | 类型  | 说明  |
| :------------ | :------------ | :------------ |
|m1YOY|String||
|m0ChainRelative|String||
|m2ChainRelative|String||
|m1Month|String||
|statMonth|String||
|statYear|String||
|m2YOY|String||
|m1ChainRelative|String||
|m2Month|String||
|m0YOY|String||
|m0Month|String||


### 接口示例
```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取货币供应量数据
data = wta.getWtaMoneySupply()
```

------------

## 货币供应量年底余额
**接口：getWtaMoneySupplyBal**

**描述：获取货币供应量年底余额数据**

### 输入参数
|  名称 | 类型  | 说明  |  是否必传 |  默认值 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|-|-|-|-|-|

### 输出参数
|  名称 | 类型  | 说明  |
| :------------ | :------------ | :------------ |
|m0YearYOY|String||
|m1YearYOY|String||
|m0Year|String||
|m2Year|String||
|statYear|String||
|m1Year|String||
|m2YearYOY|String||


### 接口示例
```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取货币供应量年底余额数据
data = wta.getWtaMoneySupplyBal()
```

------------

## 偿债能力
**接口：getWtaDebtpayData**
**
描述：获取偿债能力数据**

### 输入参数
|  名称 | 类型  | 说明  |  是否必传 |  默认值 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|SECCODE|String|股票代码|是|-|
|SECNAME|String|股票名称|否|-|
|ENDDATE|String|报告时间|否|-|

### 输出参数
|  名称 | 类型  | 说明  |
| :------------ | :------------ | :------------ |
|SECNAME|String|股票名称|
|SECCODE|String|股票代码|
|F051N|Float|有形资产净值债务率|
|F050N|Float|现金到期债务比率|
|F049N|Float|保守速动比率|
|F048N|Float|流动负债比率|
|F047N|Float|非流动负债比率|
|F062N|Float|经营净现金比率（全部债务）|
|F061N|Float|经营净现金比率（短期债务）|
|F046N|Float|运营资金|
|F045N|Float|利息保障倍数|
|F044N|Float|现金比率|
|F039N|Float|产权比率|
|F041N|Float|资产负债比率|
|F043N|Float|速动比率|
|F042N|Float|流动比率|
|ENDDATE|String|报告期|


### 接口示例
```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取平安银行的偿债能力数据
data = wta.getWtaDebtpayData(SECCODE="000001")
```

------------

## 基金持股
**接口：getWtaFundHoldings**

**描述：获取基金持股数据**

### 输入参数
|  名称 | 类型  | 说明  |  是否必传 |  默认值 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|SECCODE|String|股票代码|是|-|
|SECNAME|String|股票名称|否|-|
|ENDDATE|String|报告时间|否|-|

### 输出参数
|  名称 | 类型  | 说明  |
| :------------ | :------------ | :------------ |
|SECNAME|String|股票名称|
|SECCODE|String|股票代码|
|F003N|Float|持股总市值|
|F002N|Int|持股总数|
|F001N|Int|基金覆盖家数|
|ID|Int|序号|
|ENDDATE|String|报告日期|


### 接口示例
```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取平安银行的基金持股数据
data = wta.getWtaFundHoldings(SECCODE="000001")
```

------------

## 成长能力
**接口：getWtaGrowthData**

**描述：获取成长能力数据**

### 输入参数
|  名称 | 类型  | 说明  |  是否必传 |  默认值 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|SECCODE|String|股票代码|是|-|
|SECNAME|String|股票名称|否|-|
|ENDDATE|String|报告时间|否|-|

### 输出参数
|  名称 | 类型  | 说明  |
| :------------ | :------------ | :------------ |
|SECNAME|String|股票名称|
|SECCODE|String|股票代码|
|F026N|Float|固定资产增长率|
|F057N|Float|投资收益增长率|
|F054N|Float|净资产增长率|
|F053N|Float|净利润增长率|
|F058N|Float|营业利润增长率|
|F056N|Float|总资产增长率|
|F052N|Float|营业收入增长率|
|ENDDATE|String|报告日期|



### 接口示例
```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取平安银行的成长能力数据
data = wta.getWtaGrowthData(SECCODE="000001")
```

------------

## 盈利能力
**接口：getWtaProfitData**

**描述：获取盈利能力数据**

### 输入参数
|  名称 | 类型  | 说明  |  是否必传 |  默认值 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|SECCODE|String|股票代码|否|-|
|SECNAME|String|股票名称|否|-|
|ENDDATE|String|报告时间|否|-|

### 输出参数
|  名称 | 类型  | 说明  |
| :------------ | :------------ | :------------ |
|SECNAME|String|股票名称|
|SECCODE|String|股票代码|
|F088N|Float|年化费用期间毛利率|
|F085N|Float|基本获利能力|
|F082N|Float|净利含金量|
|F079N|Float|期间费用率|
|F078N|Float|毛利率%|
|F021N|Float|三费比重%|
|F020N|Float|成本费用利润率|
|F019N|Float|财务费用率|
|F018N|Float|管理费用率|
|F016N|Float|总资产报酬率|
|F015N|Float|投资收益率|
|F013N|Float|营业成本率|
|F012N|Float|营业税金率|
|F011N|Float|营业利润率|
|F017N|Float|净利润率|
|F068N|Float|净资产收益率-加权（扣除非经常性损益）|
|F067N|Float|净资产收益率-加权|
|F066N|Float|净资产收益率（扣除非经常性损益）|
|F081N|Float|净资产收益率|
|ENDDATE|String|报告日期|



### 接口示例
```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取平安银行的盈利能力数据
data = wta.getWtaProfitData(SECCODE="000001")
```

------------

## 融资融券
**接口：getWtaMarginTrading**

**描述：获取融资融券数据**

### 输入参数
|  名称 | 类型  | 说明  |  是否必传 |  默认值 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|SECCODE|String|股票代码|否|-|
|SECNAME|String|股票名称|否|-|
|TRADEDATE|String|交易日期|否|-|

### 输出参数
|  名称 | 类型  | 说明  |
| :------------ | :------------ | :------------ |
|SECNAME|String|股票名称|
|SECCODE|String|股票代码|
|F009N|Int|融资融券余额|
|F008N|Float|融券余量金额|
|F006N|Int|本日融券卖出量|
|F004N|Int|本日融券余量|
|F002N|Float|本日融资买入额|
|F001N|Float|本日融资余额|
|TRADEDATE|String|上市日期|



### 接口示例
```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取平安银行的融资融券数据
data = wta.getWtaMarginTrading(SECCODE="000001")
```

------------

## 新股数据
**接口：getWtaNewStocks**

**描述：获取新股数据数据**

### 输入参数
|  名称 | 类型  | 说明  |  是否必传 |  默认值 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|SECCODE|String|股票代码|否|-|
|SECNAME|String|股票名称|否|-|

### 输出参数
|  名称 | 类型  | 说明  |
| :------------ | :------------ | :------------ |
|SECNAME|String|股票名称|
|SECCODE|String|股票代码|
|F037D|String|中签缴款日|
|F109D|String|中签公告日|
|F108D|String|摇号结果公告日|
|F006N|Float|上网发行中签率|
|F013N|Float|发行市盈率|
|F003N|Int|总发行数量|
|F008N|Float|发行价|
|F002D|String|申购日期|
|F006D|String|上市日期|


### 接口示例
```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取所有的新股数据
data = wta.getWtaNewStocks()
```

------------

## 运营能力
**接口：getWtaOperaData**

**描述：获取运营能力数据**

### 输入参数
|  名称 | 类型  | 说明  |  是否必传 |  默认值 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|SECCODE|String|股票代码|否|-|
|SECNAME|String|股票名称|否|-|
|ENDDATE|String|报告日期|否|-|

### 输出参数
|  名称 | 类型  | 说明  |
| :------------ | :------------ | :------------ |
|SECNAME|String|股票名称|
|SECCODE|String|股票代码|
|F080N|Int|现金转换周期|
|F027N|Int|应收账款周转天数|
|F022N|Float|应收账款周转率|
|F024N|Float|运营资金周转率|
|F026N|Float|固定资产周转率|
|F030N|Int|流动资产周转天数|
|F029N|Float|流动资产周转率|
|F028N|Int|存货周转天数|
|F023N|Float|存货周转率|
|F031N|Int|总资产周转天数|
|F025N|Float|总资产周转率|
|ENDDATE|String|报告日期|


### 接口示例
```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取平安银行的运营能力数据
data = wta.getWtaOperaData(SECCODE="000001")
```

------------

## 限售股解禁
**接口：getWtaReleStock**

**描述：获取限售股解禁数据**

### 输入参数
|  名称 | 类型  | 说明  |  是否必传 |  默认值 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|SECCODE|String|股票代码|否|-|
|SECNAME|String|股票名称|否|-|
|F003D|String|公告日期|否|-|

### 输出参数
|  名称 | 类型  | 说明  |
| :------------ | :------------ | :------------ |
|SECNAME|String|股票名称|
|SECCODE|String|股票代码|
|F008N|Int|实际可流通数量|
|F005N|Float|实际解除限售比例|
|F004N|Int|实际解除限售数量|
|F003D|String|实际解除限售日期|
|DECLAREDATE|String|公告日期|


### 接口示例
```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取平安银行的限售股解禁数据
data = wta.getWtaReleStock(SECCODE="000001")
```

------------

## 非金融利润表
**接口：getWtaIncomeStatement**

**描述：获取非金融利润表数据**

### 输入参数
|  名称 | 类型  | 说明  |  是否必传 |  默认值 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|SECCODE|String|股票代码|否|-|
|SECNAME|String|股票名称|否|-|
|ENDDATE|String|报告日期|否|-|

### 输出参数
|  名称 | 类型  | 说明  |
| :------------ | :------------ | :------------ |
|SECNAME|String|股票名称|
|SECCODE|String|股票代码|
|DECLAREDATE|String|公告日期|
|F065N|Float|资产减值损失（2019格式）|
|F064N|Float|信用减值损失（2019格式）|
|F063N|Float|其中：利息收入|
|F062N|Float|其中：利息费用|
|MEMO|String|备注|
|F041N|Float|其中：归属于少数股东|
|F040N|Float|其中：归属于母公司|
|F039N|Float|八、综合收益总额|
|F038N|Float|七、其他综合收益|
|F032N|Float|（二）稀释每股收益|
|F031N|Float|（一）基本每股收益|
|F029N|Float|少数股东损益|
|F028N|Float|归属于母公司所有者的净利润|
|F061N|Float|终止经营净利润|
|F060N|Float|持续经营净利润|
|F027N|Float|五、净利润|
|F026N|Float|加：影响净利润的其他科目|
|F025N|Float|减：所得税|
|F024N|Float|四、利润总额|
|F023N|Float|加：影响利润总额的其他科目|
|F022N|Float|其中：非流动资产处置损失|
|F021N|Float|减：营业外支出|
|F050N|Float|其中：非流动资产处置利得|
|F020N|Float|营业外收入|
|F019N|Float|加：补贴收入|
|F018N|Float|三、营业利|
|F017N|Float|影响营业利润的其他科目|
|F059N|Float|资产处置收益|
|F058N|Float|净敞口套期收益|
|F057N|Float|信用减值损失|
|F051N|Float|基它收入|
|F037N|Float|汇兑收益|
|F016N|Float|其中：对联营企业和合营企业的投资收益|
|F015N|Float|投资收益|
|F014N|Float|加：公允价值变动净收益|
|F013N|Float|资产减值损失|
|F056N|Float|研发费用|
|F012N|Float|财务费用|
|F011N|Float|堪探费用|
|F010N|Float|管理费用|
|F009N|Float|销售费用|
|F008N|Float|营业税金及附加|
|F049N|Float|分保费用|
|F048N|Float|保单红利支出|
|F047N|Float|提取保险合同准备金净额|
|F046N|Float|赔付支出净额|
|F045N|Float|退保金|
|F044N|Float|手续费及佣金支出|
|F043N|Float|利息支出|
|F007N|Float|其中：营业成本|
|F036N|Float|二、营业总成本|
|F042N|Float|手续费及佣金收入|
|F034N|Float|已赚保费|
|F033N|Float|利息收入|
|F006N|Float|其中：营业收入|
|F035N|Float|一、营业总收入|
|F005V|String|报表来源|
|F004V|String|报表来源编码|
|F003V|String|合并类型|
|F002V|String|合并类型编码|
|F001D|String|报告年度|
|ENDDATE|String|截止日期|
|STARTDATE|String|开始日期|
|ORGNAME|String|机构名称|


### 接口示例
```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取平安银行的非金融利润表数据
data = wta.getWtaIncomeStatement(SECCODE="000001")
```

------------

## 金融利润表
**接口：getWtaFIncomeStatement**

**描述：获取金融利润表数据**

### 输入参数
|  名称 | 类型  | 说明  |  是否必传 |  默认值 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|SECCODE|String|股票代码|否|-|
|SECNAME|String|股票名称|否|-|
|ENDDATE|String|报告日期|否|-|

### 输出参数
|  名称 | 类型  | 说明  |
| :------------ | :------------ | :------------ |
|SECCODE|String|股票代码|
|SECNAME|String|股票简称|
|STARTDATE|String|开始日期|
|DECLAREDATE|String|公告日期|
|ENDDATE|String|截止日期|
|F001D|String|报告年度|
|F002V|String|合并类型编码|
|F003V|String|合并类型|
|F004V|String|报表来源编码|
|F005V|String|报表来源|
|F006N|Float|一、营业收入|
|F007N|Float|利息净收入|
|F008N|Float|其中:利息收入|
|F009N|Float|其中:利息支出|
|F010N|Float|手续费及佣金净收入|
|F011N|Float|其中:手续费及佣金收入|
|F012N|Float|其中:手续费及佣金支出|
|F013N|Float|其中：代理买卖证券业务净收入|
|F014N|Float|其中:证券承销业务净收入　|
|F015N|Float|其中:委托客户管理资产业务净收入|
|F016N|Float|已赚保费|
|F017N|Float|保险业务收入|
|F018N|Float|其中：分保费收入|
|F019N|Float|减：分出保费|
|F020N|Float|提取未到期责任准备金|
|F021N|Float|投资收益|
|F022N|Float|其中：对联营企业和合营企业的投资收益|
|F023N|Float|公允价值变动收益|
|F024N|Float|汇兑收益|
|F025N|Float|其他业务收入|
|F026N|Float|二、营业支出|
|F027N|Float|退保金|
|F028N|Float|赔付支出|
|F029N|Float|减：摊回赔付支出|
|F030N|Float|提取保险责任准备金|
|F031N|Float|减：摊回保险责任准备金|
|F032N|Float|保单红利支出|
|F033N|Float|分保费用|
|F034N|Float|营业税金及附加|
|F035N|Float|手续费及佣金支出|
|F036N|Float|业务及管理费|
|F037N|Float|减：摊回分保费用|
|F038N|Float|资产减值损失|
|F039N|Float|其他业务成本|
|F040N|Float|三、营业利润|
|F041N|Float|加：补贴收入|
|F042N|Float|营业外收入|
|F043N|Float|减：营业外支出|
|F044N|Float|加：影响利润总额的其他科目|
|F045N|Float|四、利润总额|
|F046N|Float|减：所得税|
|F047N|Float|加：影响净利润的其他科目|
|F048N|Float|五、净利润|
|F049N|Float|（一）归属于母公司所有者的净利润|
|F050N|Float|（二）少数股东损益|
|F052N|Float|（一）基本每股收益|
|F053N|Float|（二）稀释每股收益|
|F054N|Float|八、综合收益总额|
|F055N|Float|其中：归属于母公司|
|F056N|Float|其中：归属于少数股东|
|F057N|Float|七、其他综合收益|
|F062N|Float|其它收益|
|F063N|Float|资产处置收益|
|F064N|Float|持续经营净利润|
|F065N|Float|终止经营净利润|
|ORGNAME|String|机构名称|


### 接口示例
```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取平安银行的金融利润表数据
data = wta.getWtaFIncomeStatement(SECCODE="000001")
```

------------

## 非金融现金表
**接口：getWtaCashStatement**

**描述：获取非金融现金表数据**

### 输入参数
|  名称 | 类型  | 说明  |  是否必传 |  默认值 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|SECCODE|String|股票代码|否|-|
|SECNAME|String|股票名称|否|-|
|ENDDATE|String|报告日期|否|-|

### 输出参数
|  名称 | 类型  | 说明  |
| :------------ | :------------ | :------------ |
|SECCODE|String|股票代码|
|SECNAME|String|股票名称|
|F070N|Float|加：其他原因对现金的影响|
|F071N|Float|现金及现金等价物净增加额|
|F069N|Float|减：现金等价物的期初余额|
|F068N|Float|加：现金等价物的期末余额|
|F067N|Float|减：现金的期初余额|
|F066N|Float|现金的期末余额|
|F064N|Float|融资租入固定资产|
|F063N|Float|一年内到期的可转换公司债券|
|F062N|Float|债务转为资本|
|F060N|Float|经营活动产生的现金流量净额2|
|F059N|Float|其他|
|F058N|Float|经营性应付项目的增加|
|F057N|Float|经营性应收项目的减少|
|F056N|Float|存货的减少|
|F055N|Float|递延所得税负债增加|
|F054N|Float|递延所得税资产减少|
|F053N|Float|投资损失|
|F052N|Float|财务费用|
|F051N|Float|公允价值变动损失|
|F050N|Float|固定资产报废损失|
|F049N|Float|处置固定资产、无形资产和其他长期资产的损失|
|F048N|Float|长期待摊费用摊销|
|F047N|Float|无形资产摊销|
|F091N|Float|投资性房地产的折旧及摊销|
|F046N|Float|固定资产折旧、油气资产折耗、生产性生物资产折旧|
|F045N|Float|加：资产减值准备|
|F044N|Float|净利润|
|F041N|Float|期末现金及现金等价物余额|
|F040N|Float|期初现金及现金等价物余额|
|F039N|Float|五、现金及现金等价物净增加额|
|F038N|Float|四(2)、其他原因对现金的影响|
|F037N|Float|四、汇率变动对现金的影响|
|F036N|Float|筹资活动产生的现金流量净额|
|F035N|Float|筹资活动现金流出小计|
|F034N|Float|支付其他与筹资活动有关的现金|
|F090N|Float|其中：子公司支付给少数股东的股利、利润|
|F033N|Float|分配股利、利润或偿付利息支付的现金|
|F032N|Float|偿还债务支付的现金|
|F031N|Float|筹资活动现金流入小计|
|F030N|Float|收到其他与筹资活动有关的现金|
|F076N|Float|发行债券收到的现金|
|F029N|Float|取得借款收到的现金|
|F089N|Float|其中：子公司吸收少数股东投资收到的现金|
|F028N|Float|吸收投资收到的现金|
|F027N|Float|投资活动产生的现金流量净额|
|F026N|Float|投资活动现金流出小计|
|F025N|Float|支付其他与投资活动有关的现金|
|F024N|Float|取得子公司及其他营业单位支付的现金净额|
|F075N|Float|质押贷款净增加额|
|F023N|Float|投资支付的现金|
|F022N|Float|购建固定资产、无形资产和其他长期资产支付的现金|
|F021N|Float|投资活动现金流入小计|
|F020N|Float|收到其他与投资活动有关的现金|
|F019N|Float|处置子公司及其他营业单位收到的现金净额|
|F018N|Float|处置固定资产、无形资产和其他长期资产收回的现金净额|
|F017N|Float|取得投资收益收到的现金|
|F016N|Float|收回投资收到的现金|
|F015N|Float|经营活动产生的现金流量净额|
|F014N|Float|经营活动现金流出小计|
|F013N|Float|支付其他与经营活动有关的现金|
|F012N|Float|支付的各项税费|
|F011N|Float|支付给职工以及为职工支付的现金|
|F088N|Float|支付保单红利的现金|
|F087N|Float|支付利息、手续费及佣金的现金|
|F086N|Float|支付原保险合同赔付款项的现金|
|F085N|Float|存放中央银行和同业款项净增加额|
|F084N|Float|客户贷款及垫款净增加额|
|F010N|Float|购买商品、接受劳务支付的现金|
|F009N|Float|经营活动现金流入小计|
|F008N|Float|收到其他与经营活动有关的现金|
|F007N|Float|收到的税费返还|
|F083N|Float|回购业务资金净增加额|
|F082N|Float|拆入资金净增加额|
|F081N|Float|收取利息、手续费及佣金的现金|
|F080N|Float|处置以公允价值计量且其变动计入当期损益的金融资产净增加额|
|F079N|Float|保户储金及投资款净增加额|
|F078N|Float|收到再保险业务现金净额|
|F077N|Float|收到原保险合同保费取得的现金|
|F074N|Float|向其他金融机构拆入资金净增加额|
|F073N|Float|向中央银行借款净增加额|
|F072N|Float|客户存款和同业存放款项净增加额|
|F006N|Float|销售商品、提供劳务收到的现金|
|F005V|String|报表来源|
|F004V|String|报表来源编码|
|F003V|String|合并类型|
|F002V|String|合并类型编码|
|F001D|String|报告年度|
|ENDDATE|String|截止日期|


### 接口示例
```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取平安银行的非金融现金表数据
data = wta.getWtaCashStatement(SECCODE="000001")
```

------------

## 金融现金表
**接口：getwtaFCashState**

**描述：获取金融现金表数据**

### 输入参数
|  名称 | 类型  | 说明  |  是否必传 |  默认值 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|SECCODE|String|股票代码|否|-|
|SECNAME|String|股票名称|否|-|
|ENDDATE|String|报告日期|否|-|

### 输出参数
|  名称 | 类型  | 说明  |
| :------------ | :------------ | :------------ |
|SECCODE|String|股票代码|
|SECNAME|String|股票名称|
|F028N|Float|吸收投资收到的现金|
|F071N|Float|现金及现金等价物净增加额2|
|F070N|Float|加：其他原因对现金的影响2|
|F069N|Float|减：现金等价物的期初余额|
|F068N|Float|加：现金等价物的期末余额|
|F067N|Float|减：现金的期初余额|
|F066N|Float|现金的期末余额|
|F064N|Float|融资租入固定资产|
|F063N|Float|一年内到期的可转换公司债券|
|F062N|Float|债务转为资本|
|F060N|Float|经营活动产生的现金流量净额2|
|F059N|Float|其他|
|F058N|Float|经营性应付项目的增加|
|F057N|Float|经营性应收项目的减少|
|F056N|Float|存货的减少|
|F055N|Float|递延所得税负债增加|
|F054N|Float|递延所得税资产减少|
|F053N|Float|投资损失|
|F052N|Float|财务费用|
|F051N|Float|公允价值变动损失|
|F050N|Float|固定资产报废损失|
|F049N|Float|处置固定资产、无形资产和其他长期资产的损失|
|F048N|Float|长期待摊费用摊销|
|F047N|Float|无形资产摊销|
|F091N|Float|投资性房地产的折旧及摊销|
|F046N|Float|固定资产折旧、油气资产折耗、生产性生物资产折旧|
|F045N|Float|加：资产减值准备|
|F044N|Float|净利润|
|F041N|Float|期末现金及现金等价物余额|
|F040N|Float|期初现金及现金等价物余额|
|F039N|Float|五、现金及现金等价物净增加额|
|F038N|Float|四(2)、其他原因对现金的影响|
|F037N|Float|四、汇率变动对现金的影响|
|F036N|Float|筹资活动产生的现金流量净额|
|F035N|Float|筹资活动现金流出小计|
|F034N|Float|支付其他与筹资活动有关的现金|
|F090N|Float|其中：子公司支付给少数股东的股利、利润|
|F033N|Float|分配股利、利润或偿付利息支付的现金|
|F032N|Float|偿还债务支付的现金|
|F031N|Float|筹资活动现金流入小计|
|F030N|Float|收到其他与筹资活动有关的现金|
|F076N|Float|发行债券收到的现金|
|F029N|Float|取得借款收到的现金|
|F089N|Float|其中：子公司吸收少数股东投资收到的现金|
|F027N|Float|投资活动产生的现金流量净额|
|F026N|Float|投资活动现金流出小计|
|F025N|Float|支付其他与投资活动有关的现金|
|F024N|Float|取得子公司及其他营业单位支付的现金净额|
|F075N|Float|质押贷款净增加额|
|F023N|Float|投资支付的现金|
|F022N|Float|购建固定资产、无形资产和其他长期资产支付的现金|
|F021N|Float|投资活动现金流入小计|
|F020N|Float|收到其他与投资活动有关的现金|
|F019N|Float|处置子公司及其他营业单位收到的现金净额|
|F018N|Float|处置固定资产、无形资产和其他长期资产收回的现金净额|
|F017N|Float|取得投资收益收到的现金|
|F016N|Float|收回投资收到的现金|
|F015N|Float|经营活动产生的现金流量净额|
|F014N|Float|经营活动现金流出小计|
|F013N|Float|支付其他与经营活动有关的现金|
|F012N|Float|支付的各项税费|
|F011N|Float|支付给职工以及为职工支付的现金|
|F088N|Float|支付保单红利的现金|
|F087N|Float|支付利息、手续费及佣金的现金|
|F086N|Float|支付原保险合同赔付款项的现金|
|F085N|Float|存放中央银行和同业款项净增加额|
|F084N|Float|客户贷款及垫款净增加额|
|F010N|Float|购买商品、接受劳务支付的现金|
|F009N|Float|经营活动现金流入小计|
|F008N|Float|收到其他与经营活动有关的现金|
|F007N|Float|收到的税费返还|
|F083N|Float|回购业务资金净增加额|
|F082N|Float|拆入资金净增加额|
|F081N|Float|收取利息、手续费及佣金的现金|
|F080N|Float|处置以公允价值计量且其变动计入当期损益的金融资产净增加额|
|F079N|Float|保户储金及投资款净增加额|
|F078N|Float|收到再保险业务现金净额|
|F077N|Float|收到原保险合同保费取得的现金|
|F074N|Float|向其他金融机构拆入资金净增加额|
|F073N|Float|向中央银行借款净增加额|
|F072N|Float|客户存款和同业存放款项净增加额|
|F006N|Float|销售商品、提供劳务收到的现金|
|F005V|String|报表来源|
|F004V|String|报表来源编码|
|F003V|String|合并类型|
|F002V|String|合并类型编码|
|F001D|String|报告年度|
|ENDDATE|String|截止日期|
|STARTDATE|String|开始日期|
|DECLAREDATE|String|公告日期|
|ORGNAME|String|机构名称|


### 接口示例
```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取平安银行的金融现金表数据
data = wta.getwtaFCashState(SECCODE="000001")
```


------------

## 非金融资产负债表
**接口：getWtaBalanceSheet**

**描述：获取非金融资产负债表数据**

### 输入参数
|  名称 | 类型  | 说明  |  是否必传 |  默认值 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|SECCODE|String|股票代码|否|-|
|SECNAME|String|股票名称|否|-|
|ENDDATE|String|报告日期|否|-|

### 输出参数
|  名称 | 类型  | 说明  |
| :------------ | :------------ | :------------ |
|SECCODE|String|股票代码|
|SECNAME|String|股票名称|
|F032N|Float|开发支出|
|F122N|Float|租赁负债|
|F121N|Float|使用权资产|
|F120N|Float|应收款项融资|
|MEMO|String|备注|
|F071N|Float|负债和所有者（或股东权益）合计|
|F070N|Float|所有者权益（或股东权益）合计|
|F069N|Float|非正常经营项目收益调整|
|F067N|Float|少数股东权益|
|F073N|Float|归属于母公司所有者权益|
|F068N|Float|外币报表折算价差|
|F065N|Float|未分配利润|
|F076N|Float|一般风险准备|
|F064N|Float|盈余公积|
|F072N|Float|专项储备|
|F074N|Float|其他综合收益|
|F066N|Float|减：库存股|
|F063N|Float|资本公积|
|F105N|Float|永续债-所有者权益|
|F104N|Float|其中：优先股-所有者权益|
|F103N|Float|其他权益工具|
|F062N|Float|实收资本（或股本）|
|F061N|Float|负债合计|
|F060N|Float|非流动负债合计|
|F059N|Float|其他非流动负债|
|F058N|Float|递延所得税负债|
|F075N|Float|递延收益-非流动负债|
|F057N|Float|预计负债|
|F056N|Float|专项应付款|
|F102N|Float|长期应付职工薪酬|
|F055N|Float|长期应付款|
|F101N|Float|永续债-非流动负债|
|F100N|Float|其中：优先股-非流动负债|
|F054N|Float|应付债券|
|F053N|Float|长期借款|
|F052N|Float|流动负债合计|
|F051N|Float|其他流动负债|
|F115N|Float|合同负债|
|F114N|Float|应付票据及应付账款|
|F113N|Float|交易性金融负债|
|F099N|Float|递延收益-流动负债|
|F098N|Float|预计负债-流动负债|
|F050N|Float|一年内到期的非流动负债|
|F097N|Float|划分为持有待售的负债|
|F096N|Float|代理承销证券款|
|F095N|Float|代理买卖证券款|
|F094N|Float|保险合同准备金|
|F093N|Float|应付分保账款|
|F049N|Float|应付关联公司款|
|F048N|Float|其他应付款|
|F047N|Float|其中：应付股利|
|F046N|Float|其中：应付利息|
|F045N|Float|应交税费|
|F044N|Float|应付职工薪酬|
|F092N|Float|应付手续费及佣金|
|F091N|Float|卖出回购金融资产款|
|F043N|Float|预收款项|
|F042N|Float|应付账款|
|F041N|Float|应付票据|
|F090N|Float|衍生金融负债|
|F040N|Float|以公允价值计量且其变动计入当期损益的金融负债（20190322弃用）|
|F089N|Float|拆入资金|
|F088N|Float|吸收存款及同业存放|
|F087N|Float|向中央银行借款|
|F039N|Float|短期借款|
|F038N|Float|资产总计|
|F037N|Float|非流动资产合计|
|F036N|Float|其他非流动资产|
|F112N|Float|其他非流动金融资产|
|F111N|Float|其他权益工具投资|
|F110N|Float|其他债权投资|
|F116N|Float|债权投资|
|F035N|Float|递延所得税资产|
|F034N|Float|长期待摊费用|
|F033N|Float|商誉|
|F031N|Float|无形资产|
|F030N|Float|油气资产|
|F029N|Float|生产性生物资产|
|F028N|Float|固定资产清理|
|F027N|Float|工程物资|
|F026N|Float|在建工程|
|F025N|Float|固定资产|
|F024N|Float|投资性房地产|
|F023N|Float|长期股权投资|
|F022N|Float|长期应收款|
|F021N|Float|持有至到期投资|
|F020N|Float|可供出售金融资产|
|F086N|Float|发放贷款及垫款-非流动资产|
|F019N|Float|流动资产合计|
|F018N|Float|其他流动资产|
|F119N|Float|合同资产|
|F118N|Float|应收票据及应收账款|
|F117N|Float|交易性金融资产|
|F017N|Float|一年内到期的非流动资产|
|F079N|Float|发放贷款及垫款-流动资产|
|F085N|Float|划分为持有待售的资产|
|F016N|Float|其中：消耗性生物资产|
|F015N|Float|存货|
|F084N|Float|买入返售金融资产|
|F012N|Float|应收关联公司款|
|DECLAREDATE|String|公告日期|
|ORGNAME|String|机构名称|


### 接口示例
```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取平安银行的非金融资产负债表数据
data = wta.getWtaBalanceSheet(SECCODE="000001")
```


------------

## 金融资产负债表
**接口：getWtaFBalanceSheet**

**描述：获取金融资产负债表数据**

### 输入参数
|  名称 | 类型  | 说明  |  是否必传 |  默认值 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|SECCODE|String|股票代码|否|-|
|SECNAME|String|股票名称|否|-|
|ENDDATE|String|报告日期|否|-|

### 输出参数
|  名称 | 类型  | 说明  |
| :------------ | :------------ | :------------ |
|SECCODE|String|股票代码|
|SECNAME|String|股票名称|
|F047N|Float|资产总计|
|F116N|Float|租赁负债|
|F115N|Float|使用权资产|
|F114N|Float|持有待售负债|
|F113N|Float|合同负债|
|F112N|Float|其他权益工具投资|
|F111N|Float|其他债权投资|
|F110N|Float|债权投资|
|F109N|Float|持有待售资产|
|F108N|Float|合同资产|
|F093N|Float|负债和所有者权益（或股东权益）总计|
|F092N|Float|所有者权益（或股东权益）合计|
|F089N|Float|少数股东权益|
|F094N|Float|归属于母公司所有者权益|
|F090N|Float|外币报表折算差额|
|F088N|Float|未分配利润|
|F087N|Float|一般风险准备|
|F086N|Float|盈余公积|
|F100N|Float|其他综合收益|
|F085N|Float|减：库存股|
|F084N|Float|资本公积|
|F099N|Float|永续债-权益|
|F098N|Float|其中：优先股-权益|
|F097N|Float|其他权益工具|
|F083N|Float|实收资本（或股本）|
|F082N|Float|负债合计|
|F081N|Float|其他负债|
|F080N|Float|递延所得税负债|
|F079N|Float|独立帐户负债|
|F095N|Float|其中：优先股-负债|
|F078N|Float|应付债券|
|F077N|Float|长期借款|
|F076N|Float|长期健康险责任准备金|
|F075N|Float|寿险责任准备金|
|F074N|Float|未决赔款准备金|
|F073N|Float|未到期责任准备金|
|F072N|Float|保户储金及投资款|
|F071N|Float|应付保单红利|
|F070N|Float|应付赔付款|
|F069N|Float|预计负债|
|F103N|Float|应付款项|
|F102N|Float|应付短期融资款|
|F068N|Float|代理业务负债|
|F067N|Float|应付利息|
|F065N|Float|应交税费|
|F066N|Float|应付职工薪酬|
|F064N|Float|应付分保帐款|
|F063N|Float|应付手续费及佣金|
|F062N|Float|预收保费|
|F061N|Float|预收款项|
|F060N|Float|应付票据|
|F059N|Float|应付帐款|
|F058N|Float|代理承销证券款|
|F057N|Float|代理买卖证券款|
|F056N|Float|吸收存款|
|F055N|Float|卖出回购金融资产款|
|F054N|Float|衍生金融负债|
|F053N|Float|交易性金融负债|
|F052N|Float|拆入资金|
|F051N|Float|其中：质押借款|
|F050N|Float|短期借款|
|F049N|Float|同业及其他金融机构存放款项|
|F048N|Float|向中央银行借款|
|F046N|Float|其他资产|
|F045N|Float|递延所得税资产|
|F044N|Float|独立帐户资产|
|F043N|Float|固定资产清理|
|F042N|Float|长期待摊费用|
|F101N|Float|商誉|
|F041N|Float|其中：交易席位费|
|F040N|Float|无形资产|
|F039N|Float|在建工程|
|F038N|Float|固定资产|
|F037N|Float|存货|
|F036N|Float|投资性房地产|
|F035N|Float|存出资本保证金|
|F091N|Float|贷款及应收款类金融资产|
|F034N|Float|长期股权投资|
|F033N|Float|持有至到期投资|
|F032N|Float|可供出售金融资产|
|F031N|Float|预付款项|
|F030N|Float|应收款项类投资|
|F029N|Float|代理业务资产|
|F028N|Float|存出保证金|
|F027N|Float|发放贷款及垫款|
|F026N|Float|定期存款|
|F025N|Float|保户质押贷款|
|F024N|Float|应收分保长期健康险责任准备金|
|F023N|Float|应收分保寿险责任准备金|
|F022N|Float|应收分保未决赔款准备金|
|F021N|Float|应收分保未到期责任准备金|
|F020N|Float|应收分保帐款|
|F019N|Float|应收代位追偿款|
|F018N|Float|应收保费|
|F017N|Float|应收利息|
|F096N|Float|应收款项|
|F016N|Float|买入返售金融资产|
|F015N|Float|衍生金融资产|
|F014N|Float|交易性金融资产|
|F013N|Float|拆出资金|
|DECLAREDATE|String|公告日期|
|ORGNAME|String|机构名称|


### 接口示例
```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取平安银行的金融资产负债表数据
data = wta.getWtaFBalanceSheet(SECCODE="000001")
```
------------
## 指数列表
**接口：getWtaStockIndex**

**描述：获取指数相关信息**

### 输入参数
|  名称 | 类型  | 说明  |  是否必传 |  默认值 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|  code | String  | 指数代码  | 否 |  - |
|  name | String  | 指数名称 | 否  |  - |
|  type | String  | 指数类型(0深证,1上证) | 否  |  - |

### 输出参数
|  名称 | 类型  | 说明  |
| :------------ | :------------ | :------------ |
|code|String|股票代码|
|name|String|股票名称|
|type|String|股票类型(0深证,1上证)|


### 接口示例
```python
wta = wta_data.wta_api("secret_key","secret_id")
# 获取平安银行历史的K线数据
data = wta.getWtaStockIndex()
```
------------
## 分配预案
**接口：getWtaProfitPlan**

**描述：获取指数相关信息**

### 输入参数
|  名称 | 类型  | 说明  |  是否必传 |  默认值 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|  SECCODE | String  | 股票代码 | 是 |  - |
|  SECNAME | String  | 股票名称 | 否  |  - |
|  F001D | String  | 分红年度 | 否  |  - |

### 输出参数
|  名称 | 类型  | 说明  |
| :------------ | :------------ | :------------ |
|SECCODE|String|股票代码|
|SECNAME|String|股票名称|
|F001D|String|分红年度|
|F010N|String|送股比例|
|F011N|String|转增比例|
|F012N|String|派息比例(人民币)|
|F018D|String|股权登记日|
|F020D|String|除权日|
|F006D|String|实施方案公告日期|
|F007V|String|实施方案分红说明|

### 接口示例
```python
wta = wta_data.wta_api("secret_key","secret_id")

data = wta.getWtaProfitPlan(SECCODE="000001")
```
