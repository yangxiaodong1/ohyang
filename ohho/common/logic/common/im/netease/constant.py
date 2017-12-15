# APP_KEY = "efec4cbb9a1c436545ec76261a06131c"    # 自己的
# APP_SECRET = "d6cf63c8f5dc"                     # 自己的

APP_KEY = "a0edeb3a9c6265a365f75b72790da56f"    # 云飞的
APP_SECRET = "5fc8908abe8d"                     # 云飞的

HEADER_NAME_APP_KEY = "AppKey"
HEADER_NAME_NONCE = "Nonce"
HEADER_NAME_CURRENT_TIME = "CurTime"
HEADER_NAME_CHECK_SUM = "CheckSum"
HEADER_NAME_CONTENT_TYPE = "Content-Type"

PARAMETER_NAME_ACCID = "accid"
PARAMETER_NAME_FRIEND_ACCID = "faccid"
PARAMETER_NAME_ADD_FRIEND_TYPE = "type"  # 1直接加好友，2请求加好友，3同意加好友，4拒绝加好友
PARAMETER_NAME_UPDATE_FRIEND_ALIAS = "alias"
PARAMETER_NAME_UPDATE_FRIEND_EXTRA = "ex"

APPLY_FRIEND = 2
AGREE_FRIEND = 3
REFUSE_FRIEND = 4

PARAMETER_NAME_ADD_FRIEND_MESSAGE = "msg"  # 加好友对应的请求消息，第三方组装，最长256字符
PARAMETER_NAME_NAME = "name"
PARAMETER_NAME_PROPERTIES = "props"
PARAMETER_NAME_ICON = "icon"
PARAMETER_NAME_TOKEN = "token"

PARAMETER_UPDATE_USER_SIGN = "sign"
PARAMETER_UPDATE_USER_EMAIL = "email"
PARAMETER_UPDATE_USER_BIRTH = "birth"
PARAMETER_UPDATE_USER_MOBILE = "mobile"
PARAMETER_UPDATE_USER_GENDER = "gender"
PARAMETER_UPDATE_USER_EX = "ex"

PARAMETER_BLOCK_NEED_KICK = "needkick"

PARAMETER_SEND_MESSAGE_FROM = "from"
PARAMETER_SEND_MESSAGE_OPERATION = "ope"
PARAMETER_SEND_MESSAGE_TO = "to"
PARAMETER_SEND_MESSAGE_TYPE = "type"
PARAMETER_SEND_MESSAGE_BODY = "body"
PARAMETER_SEND_MESSAGE_ANTI_SPAM = "antispam"
PARAMETER_SEND_MESSAGE_ANTI_SPAM_CUSTOM = "antispamCustom"
PARAMETER_SEND_MESSAGE_OPTION = "option"
PARAMETER_SEND_MESSAGE_PUSH_CONTENT = "pushcontent"
PARAMETER_SEND_MESSAGE_PAYLOAD = "payload"
PARAMETER_SEND_MESSAGE_EXTENSION = "ext"
PARAMETER_SEND_MESSAGE_FORCE_PUSH_LIST = "forcepushlist"
PARAMETER_SEND_MESSAGE_FORCE_PUSH_CONTENT = "forcepushcontent"
PARAMETER_SEND_MESSAGE_FORCE_PUSH_ALL = "forcepushall"

PARAMETER_SEND_ATTACH_MESSAGE_TYPE = "msgtype"  # 0 点对点自定义通知， 1 群消息自定义通知，其他返回414
PARAMETER_SEND_ATTACH_MESSAGE_ATTACH = "attach"  # 自定义通知内容，第三方组装的字符串，建议是JSON串，最大长度4096字符
PARAMETER_SEND_ATTACH_MESSAGE_SAVE = "save"  # 1表示只发在线，2表示会存离线，其他会报414错误。默认会存离线

PARAMETER_SEND_SYSTEM_MESSAGE_FROM = "from"
PARAMETER_SEND_SYSTEM_MESSAGE_MESSAGE_TYPE = "msgType"
PARAMETER_SEND_SYSTEM_MESSAGE_TO = "to"
PARAMETER_SEND_SYSTEM_MESSAGE_ATTACH = "attach"
PARAMETER_SEND_SYSTEM_MESSAGE_PUSH_CONTENT = "pushcontent"
PARAMETER_SEND_SYSTEM_MESSAGE_PAYLOAD = "payload"
PARAMETER_SEND_SYSTEM_MESSAGE_SOUND = "sound"
PARAMETER_SEND_SYSTEM_MESSAGE_SAVE = "save"
PARAMETER_SEND_SYSTEM_MESSAGE_OPTION = "option"

RESPONSE_NAME_CODE = "code"
RESPONSE_NAME_INFO = "info"
RESPONSE_NAME_INFO_ACCID = "accid"
RESPONSE_NAME_INFO_TOKEN = "token"
RESPONSE_NAME_INFO_NAME = "name"
RESPONSE_CODE_SUCCESS = 200

HTTP_VERSION = 1.1

URL_CREATE = "https://api.netease.im/nimserver/user/create.action"
METHOD_CREATE = "POST"
CONTENT_TYPE_CREATE = "application/x-www-form-urlencoded;charset=utf-8"

URL_UPDATE = "https://api.netease.im/nimserver/user/update.action"
METHOD_UPDATE = "POST"
CONTENT_TYPE_UPDATE = "application/x-www-form-urlencoded;charset=utf-8"

URL_REFRESH_TOKEN = "https://api.netease.im/nimserver/user/refreshToken.action"
METHOD_REFRESH_TOKEN = "POST"
CONTENT_TYPE_REFRESH_TOKEN = "application/x-www-form-urlencoded;charset=utf-8"

URL_BLOCK = "https://api.netease.im/nimserver/user/block.action"
METHOD_BLOCK = "POST"
CONTENT_TYPE_BLOCK = "application/x-www-form-urlencoded;charset=utf-8"

URL_UNBLOCK = "https://api.netease.im/nimserver/user/unblock.action"
METHOD_UNBLOCK = "POST"
CONTENT_TYPE_UNBLOCK = "application/x-www-form-urlencoded;charset=utf-8"

URL_SEND_MESSAGE = "https://api.netease.im/nimserver/msg/sendMsg.action"
METHOD_SEND_MESSAGE = "POST"
CONTENT_TYPE_SEND_MESSAGE = "application/x-www-form-urlencoded;charset=utf-8"

URL_SEND_SYSTEM_MESSAGE = "https://api.netease.im/nimserver/msg/sendAttachMsg.action"
METHOD_SEND_SYSTEM_MESSAGE = "POST"
CONTENT_TYPE_SEND_SYSTEM_MESSAGE = "application/x-www-form-urlencoded;charset=utf-8"

URL_UPDATE_USER_INFO = "https://api.netease.im/nimserver/user/updateUinfo.action"
METHOD_UPDATE_USER_INFO = "POST"
CONTENT_TYPE_UPDATE_USER_INFO = "application/x-www-form-urlencoded;charset=utf-8"

URL_USER_RELATION_ADD_FRIEND = "https://api.netease.im/nimserver/friend/add.action"
METHOD_USER_RELATION_ADD_FRIEND = "POST"
CONTENT_TYPE_USER_RELATION_ADD_FRIEND = "application/x-www-form-urlencoded;charset=utf-8"

URL_USER_RELATION_UPDATE_FRIEND = "https://api.netease.im/nimserver/friend/update.action"
METHOD_USER_RELATION_UPDATE_FRIEND = "POST"
CONTENT_TYPE_USER_RELATION_UPDATE_FRIEND = "application/x-www-form-urlencoded;charset=utf-8"

URL_USER_RELATION_REMOVE_FRIEND = "https://api.netease.im/nimserver/friend/delete.action"
METHOD_USER_RELATION_REMOVE_FRIEND = "POST"
CONTENT_TYPE_USER_RELATION_REMOVE_FRIEND = "application/x-www-form-urlencoded;charset=utf-8"

URL_USER_RELATION_GET_FRIEND = "https://api.netease.im/nimserver/friend/delete.action"
METHOD_USER_RELATION_GET_FRIEND = "POST"
CONTENT_TYPE_USER_RELATION_GET_FRIEND = "application/x-www-form-urlencoded;charset=utf-8"

URL_USER_RELATION_SET_BLACK = "https://api.netease.im/nimserver/friend/setSpecialRelation.action"
METHOD_USER_RELATION_SET_BLACK = "POST"
CONTENT_TYPE_USER_RELATION_SET_BLACK = "application/x-www-form-urlencoded;charset=utf-8"
