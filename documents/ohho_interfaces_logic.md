# 登录
  - Login
    - URL
      - /rest/api/ohho/login/
    - Method
      - POST
    - Parameters
      - username, string, 用户名
      - password, string, 密码
      - cellphone_identity, string, 手机设备ID
    - Return(json字典)
      - success, bool, 登录是否成功
      - type, int, 登录成功或失败的类型
      - detail, string, 详细信息
      - token, string, 登录成功凭证
    - Logic
        - 密码验证
        - 手机验证
     
  - Logout
    - URL
      - /rest/api/ohho/logout/
    - Method
      - POST
    - Parameters
      - user_id, int, 用户ID
    - Return(json字典)
      - success, bool, 登出是否成功
      - type, int, 登出成功或失败的类型
      - detail, string, 详细信息

  - SendVerificationCode
    - URL
      - /rest/api/ohho/send/verification/code/
    - Method
      - POST
    - Parameters
      - cellphone_number, string, 手机号
    - Return(json字典)
      - success, bool, 获取验证码是否成功
      - type, int, 详细信息类型
      - detail, string, 详细信息

  - CheckVerificationCode
    - URL
      - /rest/api/ohho/check/verification/code/
    - Method
      - GET
    - Parameters
      - cellphone_number, string, 手机号
      - code, string, 验证码
    - Return(json字典)
      - success, bool, 验证码是否正确
      - type, int, 详细信息类型
      - detail, string, 详细信息

  - ResetPassword
    - URL
      - /rest/api/ohho/reset/password/
    - Method
      - POST
    - Parameters
      - cellphone_number, string, 当前用户手机号
      - password, string, 密码
      - code, string, 验证码
    - Return(json字典)
      - success, bool, 修改密码是否成功
      - type, int, 详细信息类型
      - detail, string, 详细信息

  - UpdateUserAndCellphoneRelation（重新绑定手机）
    - URL
      - /rest/api/ohho/update/user/and/cellphone/relation/
    - Method
      - POST
    - Parameters
      - cellphone_key, string, 当前手机唯一标识
      - user_id, int, 当前用户的ID
      - code, string, 验证码
    - Return(json字典)
      - success, bool, 更新用户和手机信息是否成功
      - type, int, 详细信息类型
      - detail, string, 详细信息    

# 注册
  - Register
    - URL
      - /rest/api/ohho/register/
    - Method
      - POST
    - Parameters
      - username, string, 用户名
      - password, string, 密码
      - code, string, 验证码
      - device_id, int, 硬件设备ID
      
      - cellphone_id, string, 手机唯一标识
      - 
    - Return(json字典)
      - success, bool, 注册是否成功
      - type, int, 详细信息类型
      - detail, string, 详细信息
    - Logic
        - 验证码检查
        - 注册用户
        - 绑定硬件设备
        - 录入手机信息
        - 绑定手机设备
   
  - UnbindDevice（解绑设备）
    - URL
      - /rest/api/ohho/unbind/device/
    - Method
      - POST
    - Parameters
      - cellphone_number, string, 手机号
      - device_identity, string, 设备唯一标识符
    - Return(json字典)
      - success, bool, 解绑是否成功
      - type, int, 详细信息类型
      - detail, string, 详细信息
      
  - BindDevice（绑定设备）
    - URL
      - /rest/api/ohho/bind/device/
    - Method
      - POST
    - Parameters
      - cellphone_number, string, 手机号
      - device_identity, string, 设备唯一标识符
      - code, string, 验证码
    - Return(json字典)
      - success, bool, 绑定是否成功
      - type, int, 详细信息类型
      - detail, string, 详细信息

  - IsDeviceValid（设备是否有效）
    - URL
      - /rest/api/ohho/is/device/valid/
    - Method
      - GET
    - Parameters
      - device_id, string, 设备身份ID
    - Return(json字典)
      - success, bool, 设备是否有效
      - type, int, 详细信息类型
      - detail, string, 详细信息
    - Logic
        - 设备是否我们的
        - 设备是否已经绑定

# 配对
  - SetMatchSwitch
    - URL
      - /rest/api/ohho/set/match/switch/
    - Method
      - POST
    - Parameters
      - is_match, bool, 开启配对开关（1，开启；0， 关闭)
      - user_id, int, 当前用户的ID
    - Return(json字典)
      - success, bool, 设置配对开关是否成功
      - type, int, 详细信息类型
      - detail, string, 详细信息

  - Match
    - URL
      - /rest/api/ohho/match/
    - Method
      - POST
    - Parameters
      - device_ids, string, 设备身份ID字符串，以逗号隔开
      - user_id, int, 当前用户的ID
      - match_condition_id, int, 配对条件ID
      - match_condition_json, string, 配对条件
    - Return(json字典)
      - success, bool, 配对条件是否修改成功
      - data, list, 配对成功的数据列表
    - Logic
        - 保存配对接口
        - 通过device_ids获取相应的用户列表
        - 从用户列表中根据配对条件筛选
        
  - Conditions
    - URL
        - /rest/api/ohho/conditions/
    - Method
        - GET
    - Parameters
        - user_id, int, 当前用户的ID
    - Return(json字典）
        - 配对条件信息列表
        

  - Meet
    - URL
      - /rest/api/ohho/meet/
    - Method
      - GET
    - Parameters
      - user_id, int, 当前用户的ID
    - Return(json字典)
      - data, list, 见过面的人的数据列表

  - ApplyMeet
    - URL
      - /rest/api/ohho/apply/meet/
    - Method
      - POST
    - Parameters
      - user_id, int, 当前用户的ID
      - friend_id, int, 好友的ID
      - attribute, int, 同意or拒绝
    - Retun(json字典)
      - success, bool, 是否同意见面执行是否成功
      - type, int, 详细信息类型
      - detail, string, 详细信息

  - ApplyFriend
    - URL
      - /rest/api/ohho/apply/friend/
    - Method
      - POST
    - Parameters
      - user_id, int, 当前用户的ID
      - friend_id, int, 好友的ID
      - attribute, int, 同意or拒绝
      - type, int, 1-好友， 2-黑名单
    - Retun(json字典)
      - success, bool, 是否添加好友执行是否成功
      - type, int, 详细信息类型
      - detail, string, 详细信息

# IM

  - SetOnlineSwitch
    - URL
      - /rest/api/ohho/set/online/switch/
    - Method
      - POST
    - Parameters
      - is_online, bool, 开启在线开关（1，开启；0， 关闭)
      - user_id, int, 当前用户的ID
    - Return(json字典)
      - success, bool, 开启在线开关是否成功
      - type, int, 详细信息类型
      - detail, string, 详细信息

  - Friends
    - URL
      - /rest/api/ohho/im/friends/
    - Method
      - GET
    - Parameters
      - user_id, int, 当前用户的ID
    - Return(json字典)
      - data, list, 好友列表

  - Blacks
    - URL
      - /rest/api/ohho/im/blacks/
    - Method
      - GET
    - Parameters
      - user_id, int, 当前用户的ID
    - Return(json字典)
      - data, list, 黑名单列表

# 举报
  - Report
    - URL
      - /rest/api/ohho/report/
    -Method
      - POST
    - Paramters
      - user_id, int, 当前用户的ID
      - reported_user_id, int, 被举报的用户ID
      - type, int, 举报类型
      - content, string, 举报内容
    - Return(json字典)
      - success, bool, 举报是否成功
      - type, int, 详细信息类型
      - detail, string, 详细信息

# 反馈
  - Feedback
    - URL
      - /rest/api/ohho/feedback/
    - Method
      - POST
    - Paramters
      - user_id, int, 当前用户的ID
      - type, int, 反馈类型
      - content, string, 反馈内容
    - Return(json字典)
      - success, bool, 反馈是否成功
      - type, int, 详细信息类型
      - detail, string, 详细信息


# 地图定位
  - MapPosition
    - URL
      - /rest/api/ohho/map/position/
    - Method
      - POST
    - Paramters
      - user_id, int, 当前用户的ID
      - type, int, 定位类型
      - latitude, float, 纬度
      - longitude, float, 经度
      - accuracy, float, 精度
      - supplier, string， 提供者
      - altitude, float, 海拔
      - floor, string, 楼层
      - building_id, int, 建筑ID
      - speed, string, 速度
      - angle, float, 角度
      - satellite_number, 卫星数目
      - country, string, 国家
      - province, string, 省
      - city, string, 市
      - city_code, string, 城市编码
      - area, string, 区
      - area_code, string, 区域码
      - address, string, 地址
      - interest_point, string, 兴趣点
    - Return(json字典)
      - success, bool, 地图定位是否成功（是否将信息保存到数据库中）
      - type, int, 详细信息编号
      - detail, string, 详细信息

      
  - MapUserPosition
    - URL
      - /rest/api/ohho/map/user/position/
    - Method
      - POST
    - Parameters
      - user_id, int, 用户的ID
      - friend_id, int, 朋友ID
    - Return(json字典)
      - latitude, float, 纬度
      - longitude, string, 经度


# 蓝牙定位
  - BluetoothPosition
    - URL
      - /rest/api/ohho/bluetooth/position/
    - Method
      - POST
    - Paramters
      - device_identity, string, 设备标识
      - user_id, int, 本人用户ID
      - rssi, int,
      - distance, float, 距离
    - Return(json字典)
      - success, bool, 保存是否成功
      - type, int, 详细信息类型
      - detail, string, 详细信息
      
 
  - BluetoothFind
    - URL
      - /rest/api/ohho/bluetooth/find/
    - Method
      - GET
    - Paramters
      - device_identity, string, 设备标识
    - Return(json字典)
      - latitude, float, 纬度
      - longitude, float, 经度
      - distance, float, 距离

   


# 硬件信息
  - DeviceInformation
    - URL
        - /rest/api/ohho/device/information/
    - Method
        - GET
    - Parameters
        - device_identity, string, 设备唯一标识ID
    - Return(json字典)
        - name, string, 名称
        - password, string, 密码
        - power, int, 发射功率
        

# 个人信息
  - UserInformation
    - URL
        - /rest/api/ohho/user/information/
    - Method
        - POST
    - Parameters
        - device_identity, string, 设备唯一标识ID
    - Return(json字典)
        - name, string, 名称
        - password, string, 密码
        - power, int, 发射功率
  - UserImage
    - URL
        - /rest/api/ohho/user/image/
    - Method
        - POST
    - Parameters
        - icon, string, 设备唯一标识ID
    - Return(json字典)
        - name, string, 名称
        - password, string, 密码
        - power, int, 发射功率