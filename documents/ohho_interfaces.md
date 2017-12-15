# 登录
- Login
    - URL
        - /rest/api/ohho/login/
    - Method
        - POST
    - Parameters
        - 必填
            - username, string, 用户名
            - password, string, 密码
            - cellphone_key, string, 手机唯一标识符
        - 选填
            - cellphone_operation, string, 手机系统
            - cellphone_operation_version, string, 手机系统版本
            - cellphone_build_id, string, 设备版本号
            - cellphone_build_model, string, 设备名称
            - cellphone_manufacturer, string, 厂商
            - cellphone_brand, string, 品牌（如华为， 小米）
            - cellphone_platform_type, string, 平台类型（如android, IOS)
            - cellphone_platform_version, string, 平台版本（如7.0)
    - Return(json字典)
        - code, int, 状态码
            - 1 成功
            - 89 不安全登录
            - 1003 密码不正确
            - -1 失败
            
        - detail, string, 详细信息
        - data, 字典, 用户信息（只有成功时才有此字段）
      
# 登出
- Logout
    - URL
        - /rest/api/ohho/logout/
    - Method
        - POST
    - Parameters
        - 必填
            - user_id, int, 用户ID
            - token, string, 登录成功时的token
    - Return(json字典)
        - code, int, 状态码
            - 1 成功
            - 1002 未登录
            - -1 失败
        - detail, string, 详细信息

# 发送验证码
- SendVerificationCode
    - URL
       - /rest/api/ohho/send/verification/code/
    - Method
        - POST
    - Parameters
        - 必填
            - cellphone_number, string, 手机号
    - Return(json字典)
        - code, int, 状态码
            - 1 成功
            - -1 失败
        - detail, string, 详细信息

# 检查验证码
- CheckVerificationCode
    - URL
        - /rest/api/ohho/check/verification/code/
    - Method
        - GET
    - Parameters
        - 必填 
            - cellphone_number, string, 手机号
            - code, string, 验证码
    - Return(json字典)
        - code, int, 状态码
            - 1 成功
            - -1 失败
        - detail, string, 详细信息

# 重置密码
- ResetPassword
    - URL
        - /rest/api/ohho/reset/password/
    - Method
        - POST
    - Parameters
        - 必填
            - cellphone_number, string, 当前用户手机号
            - password, string, 密码
            - code, string, 验证码
    - Return(json字典)
        - code, int, 状态码
            - 1 成功
            - -1 失败
        - detail, string, 详细信息
        
# 重新绑定手机
- RebindCellphone
    - URL
        - /rest/api/ohho/rebind/cellphone/
    - Method
        - POST
    - Parameters
        - 必填
            - cellphone_key, string, 手机唯一标识符
            - cellphone_number, string, 手机号码
            - code, string, 验证码
    - Return(json 字典)
        - code, int, 状态码
            - 1 成功
            - -1 失败

# 更新用户与手机关系[废弃]
- UpdateUserAndCellphoneRelation
    - URL
        - /rest/api/ohho/update/user/and/cellphone/relation/
    - Method
        - POST
    - Parameters
        - cellphone_number, string, 当前用户手机号
        - user_id, int, 当前用户的ID
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
        - 必填
            - username, string, 用户名
            - password, string, 密码
            - code, string, 验证码
            - identity_id, string, 设备序列号（唯一标识符）
            - mac_address, string, 设备mac地址
            - cellphone_key, string, 手机唯一标识符
        - 选填
            - cellphone_operation, string, 手机系统
            - cellphone_operation_version, string, 手机系统版本
            - cellphone_build_id, string, 设备版本号
            - cellphone_build_model, string, 设备名称
            - cellphone_manufacturer, string, 厂商
            - cellphone_brand, string, 品牌（如华为， 小米）
            - cellphone_platform_type, string, 平台类型（如android, IOS)
            - cellphone_platform_version, string, 平台版本（如7.0)
    - Return(json字典)
        - code, int, 状态码
            - 1 成功
            - 1000 登录失败
            - 1001 设备被其它人占用
            - -1 失败
        - detail, string, 详细信息
        - data, 字典， 只有注册成功时才会有的字段
   
# 通过手机解绑设备
- UnbindDevice
    - URL
        - /rest/api/ohho/cellphone/unbind/device/
    - Method
        - POST
    - Parameters
        - 必填
            - cellphone_number, string, 手机号
            - identity_id, string, 设备唯一标识符
            - code, string, 验证码
    - Return(json字典)
        - code, int, 状态码
            - 1 成功
            - -1 失败
        - detail, string, 详细信息
   
# 解绑设备 [暂时不用]
- UnbindDevice
    - URL
        - /rest/api/ohho/unbind/device/
    - Method
        - POST
    - Parameters
        - 必填
            - user_id, int, 用户ID
            - token, string, 登录时的token
            - cellphone_number, string, 手机号
            - device_identity, string, 设备唯一标识符
    - Return(json字典)
        - code, int, 状态码
            - 1 成功
            - -1 失败
        - detail, string, 详细信息

# 检查设备有效性
- IsDeviceValid
    - URL
        - /rest/api/ohho/is/device/valid/
    - Method
        - GET
    - Parameters
        - 必填
            - user_id, int, 用户ID
            - token, string, 登录成功时的token
            - identity_id, string, 设备序列号（唯一标识符）
    - Return(json字典)
        - code, int, 状态码
            - 1 成功
            - -1 失败
        - detail, string, 详细信息

# 设置配对开关
- SetMatchSwitch
    - URL
        - /rest/api/ohho/set/match/switch/
    - Method
        - POST
    - Parameters
        - 必填
            - user_id, int, 当前用户的ID
            - is_match, bool, 开启配对开关（1，开启；0， 关闭)
            - token, string, 登录时的token
    - Return(json字典)
        - code, int, 状态码
            - 1 成功
            - -1 失败
        - detail, string, 详细信息

# 配对
- Match
    - URL
        - /rest/api/ohho/match/
    - Method
        - GET
    - Parameters
        - 必填
            - device_ids, string, 设备身份ID字符串，以逗号隔开
            - user_id, int, 当前用户的ID
            - token, string, 登录时的token
            - name, int, 配对条件名称
    - Return(json字典)
        - code, int, 状态码
            - 1 成功
            - -1 失败
        - detail, string, 详细信息
        - data, 字典列表， 匹配用户的信息列表

# 见过的人
- Meet
    - URL
        - /rest/api/ohho/meet/
    - Method
        - GET
    - Parameters
        - 必填
            - user_id, int, 当前用户的ID
            - token, string, 登录时的token
        - 选填
            - last_id, int, 上次最后一个显示的用户的ID（默认为0，从头开始）
            - limit, int, 获取用户的数量（默认是10， 如果为0则到最后）
    - Return(json字典)
        - code, int, 状态码
            - 1 成功
            - -1 失败
        - detail, string, 详细信息
        - data, list, 见过面的人的数据列表（这个字段始终存在）

# 申请见面
- ApplyMeet
    - URL
        - /rest/api/ohho/apply/meet/
    - Method
        - POST
    - Parameters
        - 必填
            - user_id, int, 当前用户的ID
            - token, string, 登录时的token
            - friend_user_id, int, 好友的ID
            - match_condition_id, int, 配对条件ID
    - Return(json字典)
        - code, int, 状态码
            - 1 成功
            - -1 失败
        - detail, string, 详细信息
        
# 同意见面
- AgreeMeet
    - URL
        - /rest/api/ohho/agree/meet/
    - Method
        - POST
    - Parameters
        - 必填
            - user_id, int, 当前用户的ID
            - token, string, 登录时的token
            - friend_user_id, int, 好友的ID
    - Return(json字典)
        - code, int, 状态码
            - 1 成功
            - -1 失败
        - detail, string, 详细信息
# 取消见面
- CancelMeet
    - URL
        - /rest/api/ohho/cancel/meet/
    - Method
        - POST
    - Parameters
        - 必填
            - user_id, int, 当前用户的ID
            - token, string, 登录时的token
            - friend_user_id, int, 好友的ID
    - Return(json字典)
        - code, int, 状态码
            - 1 成功
            - -1 失败
        - detail, string, 详细信息
# 拒绝见面
- RefuseMeet
    - URL
        - /rest/api/ohho/refuse/meet/
    - Method
        - POST
    - Parameters
        - 必填
            - user_id, int, 当前用户的ID
            - token, string, 登录时的token
            - friend_user_id, int, 好友的ID
    - Return(json字典)
        - code, int, 状态码
            - 1 成功
            - -1 失败
        - detail, string, 详细信息

# 申请好友
- ApplyFriend
    - URL
        - /rest/api/ohho/apply/friend/
    - Method
        - POST
    - Parameters
        - 必填
            - user_id, int, 当前用户的ID
            - token, string, 登录时的token
            - friend_user_id, int, 好友的ID
    - Return(json字典)
        - code, int, 状态码
            - 1 成功
            - -1 失败
        - detail, string, 详细信息

# 同意好友
- AgreeFriend
    - URL
        - /rest/api/ohho/agree/friend/
    - Method
        - POST
    - Parameters
        - 必填
            - user_id, int, 当前用户的ID
            - token, string, 登录时的token
            - friend_user_id, int, 好友的ID
    - Return(json字典)
        - code, int, 状态码
            - 1 成功
            - -1 失败
        - detail, string, 详细信息
# 拒绝好友
- RefuseFriend
    - URL
        - /rest/api/ohho/refuse/friend/
    - Method
        - POST
    - Parameters
        - 必填
            - user_id, int, 当前用户的ID
            - token, string, 登录时的token
            - friend_user_id, int, 好友的ID
    - Return(json字典)
        - code, int, 状态码
            - 1 成功
            - -1 失败
        - detail, string, 详细信息
        
# 好友列表
- ListFriends
    - URL
        - /rest/api/ohho/im/list/friends/
    - Method
        - GET
    - Parameters
        - 必填
            - user_id, int, 当前用户的ID
            - token, string, 登录时的token
    - Return(json字典)
        - code, int, 状态码
            - 1 成功
            - -1 失败
        - detail, string, 详细信息
        - data, 字典列表, 朋友信息列表
# 在线开关
- SetOnlineSwitch
    - URL
        - /rest/api/ohho/set/online/switch/
    - Method
        - POST
    - Parameters
        - 必填
            - is_online, bool, 开启在线开关（1，开启；0， 关闭)
            - user_id, int, 当前用户的ID
            - token, string, 登录时的token
    - Return(json字典)
        - code, int, 状态码
            - 1 成功
            - -1 失败
        - detail, string, 详细信息

# 黑名单列表
- ListBlacks
    - URL
        - /rest/api/ohho/im/list/blacks/
    - Method
        - GET
    - Parameters
        - 必填
              - user_id, int, 当前用户的ID
              - token, string, 登录时的token
    - Return(json字典)
        - code, int, 状态码
            - 1 成功
            - -1 失败
        - detail, string, 详细信息
        - data, 字典列表, 朋友信息列表
        
        
# 添加黑名单
- ListBlacks
    - URL
        - /rest/api/ohho/im/add/black/
    - Method
        - POST
    - Parameters
        - 必填
            - user_id, int, 当前用户的ID
            - token, string, 登录时的token
            - friend_user_id, int, 好友的用户ID
    - Return(json字典)
        - code, int, 状态码
            - 1 成功
            - -1 失败
        - detail, string, 详细信息

# 移出黑名单
- ListBlacks
    - URL
        - /rest/api/ohho/im/remove/black/
    - Method
        - POST
    - Parameters
        - 必填
            - user_id, int, 当前用户的ID
            - token, string, 登录时的token
            - friend_user_id, int, 好友的用户ID
    - Return(json字典)
        - code, int, 状态码
            - 1 成功
            - -1 失败
        - detail, string, 详细信息

# 举报
- Report
    - URL
        - /rest/api/ohho/add/report/
    -Method
        - POST
    - Parameters
        - 必填
            - user_id, int, 当前用户的ID
            - token, string, 登录时的token
            - reported_user_id, int, 被举报的用户ID
            - report_type, int, 举报类型
            - content, string, 举报内容
    - Return(json字典)
        - code, int, 状态码
            - 1 成功
            - -1 失败
        - detail, string, 详细信息

# 反馈
- Feedback
    - URL
        - /rest/api/ohho/add/feedback/
    - Method
        - POST
    - Parameters
        - 必填
            - user_id, int, 当前用户的ID
            - token, string, 登录时的token
            - feedback_type, int, 反馈类型
            - content, string, 反馈内容
    - Return(json字典)
        - code, int, 状态码
            - 1 成功
            - -1 失败
        - detail, string, 详细信息


# 上传本人坐标信息
- UploadMapPosition
    - URL
        - /rest/api/ohho/upload/map/position/
    - Method
        - POST
    - Parameters
        - 必填
            - user_id, int, 当前用户的ID
            - token, string, 登录时的token
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
        - code, int, 状态码
            - 1 成功
            - -1 失败
        - detail, string, 详细信息

# 获取朋友坐标信息
- FindMapPosition
    - URL
        - /rest/api/ohho/find/map/position/
    - Method
        - GET
    - Parameters
        - 必填
            - user_id, int, 当前用户的ID
            - token, string, 登录时的token
            - friend_user_id, int, 好友的用户ID
    - Return(json字典)
        - code, int, 状态码
            - 1 成功
            - -1 失败
        - detail, string, 详细信息
        - data, 字典列表， 经纬度坐标和半径

# 朋友坐标定位[暂时废弃（未实现）]
  - MapDistance
    - URL
      - /rest/api/ohho/map/distance/
    - Method
      - GET
    - Parameters
      - user_id, int, 当前用户ID
      - friend_id, int, 朋友ID
      - latitude, float, 当前用户纬度
      - longitude, float, 当前用户经度
    - Return(json字典)
      - distance, float, 距离
      - floor, string, 楼层

# 上传硬件定位
- BluetoothPosition
    - URL
        - /rest/api/ohho/bluetooth/position/
    - Method
        - POST
    - Parameters
        - 必填
            - user_id, int, 当前用户的ID
            - token, string, 登录时的token
            - identity_id, string, 设备序列号
            - rssi, int,
            - distance, float, 距离
    - Return(json字典)
        - code, int, 状态码
            - 1 成功
            - -1 失败
        - detail, string, 详细信息
        
# 获取硬件坐标信息
- FindDevicePosition
    - URL
        - /rest/api/ohho/find/device/position/
    - Method
        - GET
    - Parameters
        - 必填
            - user_id, int, 当前用户的ID
            - token, string, 登录时的token
            - identity_id, string, 设备序列号（唯一标识符）
    - Return(json字典)
        - code, int, 状态码
            - 1 成功
            - -1 失败
        - detail, string, 详细信息
        - data, 字典列表， 经纬度坐标和半径
# 获取硬件配置信息
- GetDeviceSetting
    - URL
        - /rest/api/ohho/get/device/setting/
    - Method
        - GET
    - Parameters
        - 必填
            - user_id, int, 当前用户的ID
            - token, string, 登录时的token
            - identity_id, string, 设备序列号（唯一标识符）
    - Return(json字典)
        - code, int, 状态码
            - 1 成功
            - -1 失败
        - detail, string, 详细信息
        - data, 字典列表， 设备配置信息
        
# 添加硬件配置信息
- AddDeviceSetting
    - URL
        - /rest/api/ohho/add/device/setting/
    - Method
        - POST
    - Parameters
        - 必填
            - user_id, int, 当前用户的ID
            - token, string, 登录时的token
            - identity_id, string, 设备序列号（唯一标识符）
            - password, string, 设备密码
            - name, string, 设备名称
            - power, int, 发射功率
            - periods, int, 发射周期，毫秒
    - Return(json字典)
        - code, int, 状态码
            - 1 成功
            - -1 失败
        - detail, string, 详细信息
# 更新硬件配置信息
- UpdateDeviceSetting
    - URL
        - /rest/api/ohho/update/device/setting/
    - Method
        - POST
    - Parameters
        - 必填
            - user_id, int, 当前用户的ID
            - token, string, 登录时的token
            - identity_id, string, 设备序列号（唯一标识符）
        - 选填
            - password, string, 设备密码
            - name, string, 设备名称
            - power, int, 发射功率
            - periods, int, 发射周期，毫秒
    - Return(json字典)
        - code, int, 状态码
            - 1 成功
            - -1 失败
        - detail, string, 详细信息
        
# 获取硬件最新版本信息
- GetDeviceVersion
    - URL
        - /rest/api/ohho/get/device/version/
    - Method
        - GET
    - Parameters
        - 必填
            - user_id, int, 当前用户的ID
            - token, string, 登录时的token
    - Return(json字典)
        - code, int, 状态码
            - 1 成功
            - -1 失败
        - detail, string, 详细信息
        - data, 字典列表， 设备最新版本信息