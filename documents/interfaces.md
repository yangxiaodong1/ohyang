## 目前服务器为
- http://218.241.177.134:1345/

# 记录当前手机的经纬度
- URL
	+ /rest/api/positions/
- 方法
	+ POST
- 参数
	+ environment, string, 所处环境（如地下，室内等）
	+ name, string, 手机名称
	+ timestamp, long, 时间戳
	+ longitude, float, 经度
	+ latituce, float, 纬度
	+ input_distance, float, 实际距离（另一手机为默认值，默认只有两台手机）
	+ accuracy, float, 精度
- 返回值
	+ id, int, 当前数据在数据库中的唯一ID
	+ environment, string, 所处环境（如地下，室内等）
	+ latitude, float, 添加的纬度值
	+ longitude, float, 添加的经度值
	+ name, string, 添加的手机名称
	+ timestamp, long, 添加的时间戳
	+ input_distance, float, 实际距离（另一手机为默认值，默认只有两台手机）
	+ accuracy, float, 精度
	+ url, string, 访问本条信息的URL(get)
	


# 记录当前OHHO硬件的数据
- URL
	+ /rest/api/devices/
- 方法
	+ POST
- 参数
	+ environment, string, 所处环境（如地下，室内等）
	+ name, string, 设备标识
	+ phone_name, string, 手机名称
	+ timestamp, long, 时间戳
	+ rssi, int, 接收的信号强度指示
	+ tx_power, int, 发射功率
	+ compute_distance, float, 计算出的距离
	+ input_distance, float, 输入的距离
- 返回值
	+ id, int, 当前数据在数据库中的唯一ID
	+ environment, string, 所处环境（如地下，室内等）
	+ name, string, 添加的设备标识
	+ phone_name, string, 添加的手机名称
	+ timestamp, long, 添加的时间戳
	+ rssi, int, 添加的接收的信号强度指示
	+ tx_power, int, 添加的发射功率
	+ compute_distance, float, 添加的计算出的距离
	+ input_distance, float, 添加的输入的距离
	+ url, string, 访问本条信息的URL(get)

# 获取当前手机之间的距离
- URL
  + /rest/api/phone/distance/
- 方法
  + GET
- 参数
  + name1, string, 一台手机名称
  + name2, string, 另一台手机名称
- 返回值
  + phone_one_id, int, 一台手机位置信息的ID
  + phone_another_id, int, 另一台手机位置信息的ID
  + timestamp, long, 时间戳
  + distance, float, 两台手机间的距离

# 获取指定两手机的最新坐标（两手机的时间戳相近）
- URL
	+ /rest/api/postions/
- 方法
	+ GET
- 参数
	+ name1, string, 一台手机名称
	+ name2, string, 另一台手机名称
- 返回值
	+ latitude1, float, 第一台手机的纬度
	+ longitude1, float, 第一台手机的经度
	+ latitude2, float, 另一台手机的纬度
	+ longitude2, float, 另一台手机的经度
