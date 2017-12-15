# 手机(cellphone) CELLPHONE
    - id int(11) NOT NULL AUTO_INCREMENT, PRIMARY
    - created_at datetime DEFAULT NULL
    - changed_at datetime DEFAULT NULL
    - timestamp bigint(20) DEFAULT NULL
    - key varchar(128) UNIQUE
    - operation varchar(64) DEFAULT NULL
    - operation_version varchar(64) DEFAULT NULL
    - manufacturer varchar(64) DEFAULT NULL
    - brand varchar(64) DEFAULT NULL
    - build_id varchar(64) DEFAULT NULL
    - build_model varchar(64) DEFAULT NULL
    - platform_version varchar(64) DEFAULT NULL
    - platform_type varchar(8) DEFAULT NULL
    
# 硬件设备(device) OHHO_DEVICE
    - id int(11) NOT NULL AUTO_INCREMENT, PRIMARY
    - created_at datetime DEFAULT NULL
    - changed_at datetime DEFAULT NULL
    - timestamp bigint(20) DEFAULT NULL
    - application_id varchar(128) DEFAULT NULL
    - identity_id varchar(32) DEFAULT NULL UNIQUE
    - mac_address varchar(32) DEFAULT NULL
    - tx_power varchar(32) DEFAULT NULL

# 硬件设备配置 OHHO_DEVICE_SETTING
    - id int(11) NOT NULL AUTO_INCREMENT, PRIMARY
    - created_at datetime DEFAULT NULL
    - changed_at datetime DEFAULT NULL
    - timestamp bigint(20) DEFAULT NULL
    - device int(11) DEFAULT NULL UNIQUE KEY
    - password varchar(128) DEFAULT NULL
    - name varchar(64) DEFAULT NULL
    - power int(11) DEFAULT NULL
    - periods int(11) DEFAULT NULL
    
# 硬件设备版本 OHHO_DEVICE_VERSION
    - id int(11) NOT NULL AUTO_INCREMENT, PRIMARY
    - created_at datetime DEFAULT NULL
    - changed_at datetime DEFAULT NULL
    - timestamp bigint(20) DEFAULT NULL
    - version int(11) DEFAULT NULL UNIQUE
    - url varchar(1024) DEFAULT NULL

# IM用户 OHHO_IM_USER 
    - id int(11) NOT NULL AUTO_INCREMENT, PRIMARY
    - created_at datetime DEFAULT NULL
    - changed_at datetime DEFAULT NULL
    - timestamp bigint(20) DEFAULT NULL
    - account_id int(11) DEFAULT NULL UNIQUE(外键)
    - token varchar(128) DEFAULT NULL
    - name varchar(64) DEFAULT NULL
    - props varchar(1024) DEFAULT NULL
    - icon varchar(1024) DEFAULT NULL
    - type int(11) DEFAULT NULL
    - state tinyint(1) DEFAULT NULL
    
# IM用户关系 OHHO_IM_USER_RELATION
    - id int(11) NOT NULL AUTO_INCREMENT, PRIMARY
    - created_at datetime DEFAULT NULL
    - changed_at datetime DEFAULT NULL
    - timestamp bigint(20) DEFAULT NULL
    - account_id int(11) DEFAULT NULL 外键
    - friend_account_id int(11) DEFAULT NULL 外键
    - mark varchar(64) DEFAULT NULL
    - type int(11) DEFAULT NULL
    - state tinyint(1) DEFAULT NULL

# 地图信息 OHHO_MAP_INFORMATION
    - id int(11) NOT NULL AUTO_INCREMENT, PRIMARY
    - created_at datetime DEFAULT NULL
    - changed_at datetime DEFAULT NULL
    - timestamp bigint(20) DEFAULT NULL
    - user_id int(11) DEFAULT NULL 外键
    - type int(11) DEFAULT NULL
    - longitude decimal(10, 6) DEFAULT NULL
    - latitude decimal(10, 6) DEFAULT NULL
    - accuracy float DEFAULT NULL
    - supplier varchar(32) DEFAULT NULL
    - alititude float DEFAULT NULL
    - floor varchar(16) DEFAULT NULL
    - building_id int(11) DEFAULT NULL
    - speed varchar(16) DEFAULT NULL
    - angle float DEFAULT NULL
    - satellite_number int(11) DEFAULT NULL
    - country varchar(32) DEFAULT NULL
    - province varchar(32) DEFAULT NULL
    - city varchar(32) DEFAULT NULL
    - city_code varchar(32) DEFAULT NULL
    - area varchar(32) DEFAULT NULL
    - area_code varchar(32) DEFAULT NULL
    - address varchar(128) DEFAULT NULL
    - interest_point varchar(64) DEFAULT NULL


# 记录好友同意  OHHO_FRIEND_AGREE
    - id int(11) NOT NULL AUTO_INCREMENT, PRIMARY
    - created_at datetime DEFAULT NULL
    - changed_at datetime DEFAULT NULL
    - timestamp bigint(20) DEFAULT NULL
    - apply_id int(11) DEFAULT NULL 外键
    
# 记录好友申请 OHHO_FRIEND_APPLY
    - id int(11) NOT NULL AUTO_INCREMENT, PRIMARY
    - created_at datetime DEFAULT NULL
    - changed_at datetime DEFAULT NULL
    - timestamp bigint(20) DEFAULT NULL
    - one_user_id int(11) DEFAULT NULL 外键
    - another_user_id int(11) DEFAULT NULL 外键
    - message varchar(256) DEFAULT NULL
    
# 记录好友拒绝 OHHO_FRIEND_REFUSE
    - id int(11) NOT NULL AUTO_INCREMENT, PRIMARY
    - created_at datetime DEFAULT NULL
    - changed_at datetime DEFAULT NULL
    - timestamp bigint(20) DEFAULT NULL
    - apply_id int(11) DEFAULT NULL 外键
    - user_id int(11) DEFAULT NULL 外键
    
# 记录配对不喜欢用户 OHHO_RECORD_EXCLUDE
    - id int(11) NOT NULL AUTO_INCREMENT, PRIMARY
    - created_at datetime DEFAULT NULL
    - changed_at datetime DEFAULT NULL
    - timestamp bigint(20) DEFAULT NULL
    - user_id   int(11) DEFAULT NULL
    - exclude_user_id   int(11) DEFAULT NULL

    
# 记录配对同意 OHHO_RECORD_MATCH_AGREE
    - id int(11) NOT NULL AUTO_INCREMENT, PRIMARY
    - created_at datetime DEFAULT NULL
    - changed_at datetime DEFAULT NULL
    - timestamp bigint(20) DEFAULT NULL
    - apply_id int(11) DEFAULT NULL 外键
    
# 记录配对申请 OHHO_RECORD_MATCH_APPLY
    - id int(11) NOT NULL AUTO_INCREMENT, PRIMARY
    - created_at datetime DEFAULT NULL
    - changed_at datetime DEFAULT NULL
    - timestamp bigint(20) DEFAULT NULL
    - one_user_id int(11) DEFAULT NULL 外键
    - another_user_id int(11) DEFAULT NULL 外键
    - message varchar(256)  DEFAULT NULL
    - one_user_match_condition_id int(11) DEFAULT NULL  外键
    - another_user_match_condition_id int(11) DEFAULT NULL  外键
    
# 记录配对拒绝 OHHO_RECORD_MATCH_REFUSE
    - id int(11) NOT NULL AUTO_INCREMENT, PRIMARY
    - created_at datetime DEFAULT NULL
    - changed_at datetime DEFAULT NULL
    - timestamp bigint(20) DEFAULT NULL
    - apply_id  int(11) DEFAULT NULL    外键
    - user_id   int(11) DEFAULT NULL    外键
    - distance  float   DEFAULT NULL    (未用到）
    - information   varchar(256)    DEFAULT NULL（未用到）
    
# 记录配对条件 OHHO_RECORD_MATCH_CONDITION
    - id int(11) NOT NULL AUTO_INCREMENT, PRIMARY
    - created_at datetime DEFAULT NULL
    - changed_at datetime DEFAULT NULL
    - timestamp bigint(20) DEFAULT NULL
    - sex int(11) DEFAULT NULL
    - big_age int DEFAULT NULL
    - small_age int DEFAULT NULL
    - interest varchar(1024) DEFAULT NULL
    
# 记录配对双向同意
    - id int(11) NOT NULL AUTO_INCREMENT, PRIMARY
    - created_at datetime DEFAULT NULL
    - changed_at datetime DEFAULT NULL
    - timestamp bigint(20) DEFAULT NULL
    - apply_id int(11)  DEFAULT NULL    外键
    - another_user_id   int(11) DEFAULT NULL    外键
    - user_id   int(11) DEFAULT NULL    外键
    
# 记录配对见面（单方） OHHO_RECORD_MATCH_MEET
    - id int(11) NOT NULL AUTO_INCREMENT, PRIMARY
    - created_at datetime DEFAULT NULL
    - changed_at datetime DEFAULT NULL
    - timestamp bigint(20) DEFAULT NULL
    - apply_id int(11) DEFAULT NULL 外键
    - address varchar(128) DEFAULT NULL
    - user_id int(11) DEFAULT NULL 外键
    
# 记录配对见面结束（单方） OHHO_RECORD_MATCH_MEET_END
    - id int(11) NOT NULL AUTO_INCREMENT, PRIMARY
    - created_at datetime DEFAULT NULL
    - changed_at datetime DEFAULT NULL
    - timestamp bigint(20) DEFAULT NULL
    - apply_id int(11) DEFAULT NULL 外键
    - address varchar(128) DEFAULT NULL
    - user_id int(11) DEFAULT NULL 外键
    
# 记录配对见面中（单方） OHHO_RECORD_MATCH_MEETING
    - id int(11) NOT NULL AUTO_INCREMENT, PRIMARY
    - created_at datetime DEFAULT NULL
    - changed_at datetime DEFAULT NULL
    - timestamp bigint(20) DEFAULT NULL
    - apply_id int(11) DEFAULT NULL 外键
    - address varchar(128) DEFAULT NULL
    - user_id int(11) DEFAULT NULL 外键
    - state int(11) DEFAULT NULL 
    
# 记录配对已经见面（双方） OHHO_RECORD_MATCH_MET
    - id int(11) NOT NULL AUTO_INCREMENT, PRIMARY
    - created_at datetime DEFAULT NULL
    - changed_at datetime DEFAULT NULL
    - timestamp bigint(20) DEFAULT NULL
    - apply_id int(11) DEFAULT NULL 外键
    - user_id int(11) DEFAULT NULL 外键
    - another_user_id   int(11) DEFAULT NULL 外键
    - user_address varchar(64)  DEFAULT NULL
    - another_user_address  varchar(64) DEFAULT NULL
    - type  int(11) DEFAULT NULL
    
# 记录用户与配对条件的关系 OHHO_RECORD_USER_AND_MATCH_CONDITION
    - id int(11) NOT NULL AUTO_INCREMENT, PRIMARY
    - created_at datetime DEFAULT NULL
    - changed_at datetime DEFAULT NULL
    - timestamp bigint(20) DEFAULT NULL
    - name varchar(64) DEFAULT NULL(未用到）
    - user_id int(11) DEFAULT NULL 外键
    - match_condition_id int(11) DEFAULT NULL 外键

# 举报 OHHO_REPORT
    - id int(11) NOT NULL AUTO_INCREMENT, PRIMARY
    - created_at datetime DEFAULT NULL
    - changed_at datetime DEFAULT NULL
    - timestamp bigint(20) DEFAULT NULL
    - user_id int(11) DEFAULT NULL 外键
    - reported_user_id int(11) DEFAULT NULL 外键
    - report_type int(11) DEFAULT NULL
    - content varchar(1024) DEFAULT NULL
    
# 用户 OHHO_USER
    - id int(11) NOT NULL AUTO_INCREMENT, PRIMARY
    - created_at datetime DEFAULT NULL
    - changed_at datetime DEFAULT NULL
    - timestamp bigint(20) DEFAULT NULL
    - username varchar(32) DEFAULT NULL UNIQUE
    - password varchar(128) DEFAULT NULL
    - last_login datetime DEFAULT NULL
    - state tinyint(1) DEFAULT NULL
    
# 用户精确信息 OHHO_USER_ACCURACY_EXTENSION
    - id int(11) NOT NULL AUTO_INCREMENT, PRIMARY
    - created_at datetime DEFAULT NULL
    - changed_at datetime DEFAULT NULL
    - timestamp bigint(20) DEFAULT NULL
    - user_id int(11) DEFAULT NULL 外键
    - sex int(11) DEFAULT NULL
    - identity_card varchar(18) DEFAULT NULL
    - real_name varchar(32) DEFAULT NULL
    - email varchar(128) DEFAULT NULL
    - icon varchar(128) DEFAULT NULL
    - source_icon varchar(128) DEFAULT NULL
    - nickname varchar(64) DEFAULT NULL
    - birthday date DEFAULT NULL
    - height float DEFAULT NULL
    - weight float DEFAULT NULL
    - marriage int(11) DEFAULT NULL（目前是string)
    - hometown int(11) DEFAULT NULL 外键（目前是string)
    - current int(11) DEFAULT NULL 外键(目前是string)
    - blood int(11) 外键(目前是string)
    - resume varchar(1024)  DEFAULT NULL
    - school int(11) 外键 (目前是string)
    - company int(11) 外键(目前是string)
    - education int(11) 外键(目前是string)
    - interest varchar(1024) 
    - exclude varchar(1024)

# 用户与手机的关系 OHHO_USER_AND_CELLPHONE_RELATION
    - id int(11) NOT NULL AUTO_INCREMENT, PRIMARY
    - created_at datetime DEFAULT NULL
    - changed_at datetime DEFAULT NULL
    - timestamp bigint(20) DEFAULT NULL
    - cellphone_id int(11) DEFAULT NULL 外键
    - user_id int(11) DEFAULT NULL 外键
    - state tinyint(1) DEFAULT NULL
    
# 用户与设备的关系 OHHO_USER_AND_DEVICE_RELATION
    - id int(11) NOT NULL AUTO_INCREMENT, PRIMARY
    - created_at datetime DEFAULT NULL
    - changed_at datetime DEFAULT NULL
    - timestamp bigint(20) DEFAULT NULL
    - user_id int(11) DEFAULT NULL 外键
    - device_id int(11) DEFAULT NULL 外键
    - version int(11) DEFAULT NULL
    - state tinyint(1) DEFAULT NULL
    
# 用户配置 OHHO_USER_CONFIGURATION
    - id int(11) NOT NULL AUTO_INCREMENT, PRIMARY
    - created_at datetime DEFAULT NULL
    - changed_at datetime DEFAULT NULL
    - timestamp bigint(20) DEFAULT NULL
    - user_id int(11) DEFAULT NULL 外键
    - is_match tinyint(1) DEFAULT NULL
    - is_online tinyint(1) DEFAULT NULL
    
# 用户登录TOKEN
    - id int(11) NOT NULL AUTO_INCREMENT, PRIMARY
    - created_at datetime DEFAULT NULL
    - changed_at datetime DEFAULT NULL
    - timestamp bigint(20) DEFAULT NULL
    - user_id int(11) DEFAULT NULL
    - token varchar(128) DEFAULT NULL
    
# 取消见面反馈
    - id int(11) NOT NULL AUTO_INCREMENT, PRIMARY
    - created_at datetime DEFAULT NULL
    - changed_at datetime DEFAULT NULL
    - timestamp bigint(20) DEFAULT NULL
    - apply_id int(11) DEFAULT NULL 外键
    - user_id int(11) DEFAULT NULL  外键
    - another_user_id int(11) DEFAULT NULL  外键
    - reason    varchar(128)    DEFAULT NULL
    - message   varchar(128)    DEFAULT NULL
    
# 完成见面反馈
    - id int(11) NOT NULL AUTO_INCREMENT, PRIMARY
    - created_at datetime DEFAULT NULL
    - changed_at datetime DEFAULT NULL
    - timestamp bigint(20) DEFAULT NULL
    - apply_id int(11) DEFAULT NULL 外键
    - user_id int(11) DEFAULT NULL  外键
    - another_user_id   int(11) DEFAULT NULL 外键
    - score float   DEFAULT NULL
    - impression    varchar(128)    DEFAULT NULL
    - message       varchar(128)    DEFAULT NULL
    
# 兴趣表
    - id int(11) NOT NULL AUTO_INCREMENT, PRIMARY
    - created_at datetime DEFAULT NULL
    - changed_at datetime DEFAULT NULL
    - timestamp bigint(20) DEFAULT NULL
    - name  varchar(64)  DEFAULT NULL
    - parent_id int(11) DEFAULT NULL    外键
    - state     int(11) DEFAULT NULL
    
# 用户，设备IMEI ohho_user_and_device_imei
    - id int(11) NOT NULL AUTO_INCREMENT, PRIMARY
    - created_at datetime DEFAULT NULL
    - changed_at datetime DEFAULT NULL
    - timestamp bigint(20) DEFAULT NULL    
    - device_id int(11) DEFAULT NULL 外键
    - user_id int(11) DEFAULT NULL 外键
    - imei varchar(128) DEFAULT NULL
    

# 数据库表分类
- 基础数据（相对固定）
	- 区域数据 - 省市区
	- 兴趣
        - 体型
        - 公司
        - 喝酒
        - 教育
        - 行业
        - 职业
        - 学校
        - 抽烟
        - 暗语（废弃）
        - 工作领域
	    - 标签
	

- 硬件信息（相对固定）
	- 手机
	- 蓝牙设备
		- 设备信息
		- 设备感知数据
		- 设备配置
		- 设备版本

- 用户信息（相对固定，但增长快）
	- 用户
	- 用户扩展
	- 用户配置
	- 用户展示配置（废弃）
	- 用户登录token

- IM（）
	- 用户
	- 用户关系
	- 用户请求关系（废弃）
	
- 关系
	- 用户与手机的关系
	- 用户与蓝牙设备的关系
	- 用户与蓝牙设备的IMEI
	
- 配对
	- 配对已经拒绝（exclude)
	- 配对请求
	- 配对同意
	- 配对（见面）拒绝
	- 配对条件
	- 配对双向同意（保留）
	- 配对用户与配对条件的关系
	
- 见面
	- 见面中
	- 见面（单向）
	- 双向见面
	- 见面结束
	
- 好友
	- 好友申请
	- 好友同意
	- 好友拒绝
	
- 反馈（少）
	- 取消见面反馈
	- 完成见面反馈
	- 反馈
	
- 举报（少）
	- 举报
	
- 地图信息
	- 地图信息
    





