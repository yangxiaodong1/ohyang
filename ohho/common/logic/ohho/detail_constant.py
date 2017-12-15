english = True
chinese = True

if english:

    CODE_SUCCESS = 1

    CODE_FAILED = -1
    CODE_EXIST = 2
    CODE_NOT_EXIST = -2
    CODE_PARAMETERS_ARE_INVALID = 400
    CODE_INVALID_CODE = 600
    CODE_EXCEPTION = 500

    CODE_UNSAFE = 89
    CODE_LOGIN_FAILED = 1000
    CODE_DEVICE_USED_BY_OTHER = 1001
    CODE_NOT_LOGIN = 1002
    CODE_PASSWORD_IS_INCORRECT = 1003
    CODE_HAS_VALID_MEET_APPLY = 1100
    CODE_HAS_MET = 1101
    CODE_UPDATE_BEYOND_THREE_MONTH = 1201  # 修改时间超过3个月状态码

    CODE_NO_PERMISSION = 1403  # 没有权限
    NO_PERMISSION = "您没有权限访问该页面，请联系管理员打开权限！"

    UPDATE_BEYOND_THREE_MONTH = "update beyond three month"
    SUCCESS = "OK!"
    DEFAULT = "The data is default!"
    FAILED = "Failed!"
    EXCEPTION_DETAIL = "exception!"
    PARAMETERS_ARE_INVALID = "parameters are invalid!"
    INVALID_CODE = "invalid code!"
    PASSWORD_IS_INCORRECT = "password is incorrect!"
    EXIST = "exist!"
    NOT_EXIST = "not exist!"
    RESTORE_SUCCESS = "restore successfully!"
    RESTORE_FAILED = "restore failed!"
    UPDATE_SUCCESS = "update successfully!"
    DELETE_SUCCESS = "delete successfully!"
    DELETE_FAILED = "delete failed!"
    ADD_SUCCESS = "add successfully!"
    ADD_FAILED = "add failed!"
    LOGIN_UNSAFE = "cellphone is unsafe!"
    HAS_VALID_MEET_APPLY = "has valid meet apply!"
    HAS_MET = "has met!"
    NOT_LOGIN = "not login!"

    USER_NOT_EXIST = "user not exist!"
    USER_EXIST = "user exist!"
    TOKEN_EXIST = "token exist!"
    TOKEN_NOT_EXIST = "token not exist!"
    IM_USER_EXIST = "im user exist！"
    IM_USER_NOT_EXIST = "im user not exist！"
    RELATION_EXIST = "relation exist!"
    USED_BY_OTHER = "used by other!"
    RELATION_NOT_EXIST = "relation not exist!"
    RELATION_UPDATE = "relation is updated!"
    RELATION_NOT_UPDATE = "relation is not updated!"
    RELATION_RESTORE = "relation is restored!"
    RELATION_NOT_RESTORE = "relation is not restored!"
    INVALID_DEVICE = "invalid device!"

    ADD_CELLPHONE_SUCCESS = "add cellphone information successfully!"
    ADD_CELLPHONE_FAILED = "add cellphone information failed!"
    CELLPHONE_EXIST = "cellphone information has been there!"
    CELLPHONE_KEY_EMPTY = "cellphone key is empty!"
    CELLPHONE_IS_SAFE = "cellphone is safe!"
    CELLPHONE_IS_UNSAFE = "cellphone is unsafe!"

    ADD_USER_SUCCESS = "add user successfully!"
    ADD_USER_FAILED = "add user failed!"

    USER_LOGIN = "user has login"
    USER_NOT_LOGIN = "user does not login"
    RESTORE_USER_SUCCESS = "restore user successfully!"
    RESTORE_USER_FAILED = "restore user failed!"
    CHANGE_USER_PASSWORD_SUCCESS = "change user password successfully!"
    CHANGE_USER_PASSWORD_FAILED = "change user password failed!"
    UPDATE_USER_SUCCESS = "update user successfully!"
    UPDATE_USER_FAILED = "update user failed!"

    ADD_USER_TOKEN_SUCCESS = "add user token successfully!"
    ADD_USER_TOKEN_FAILED = "add user token failed!"
    DELETE_USER_TOKEN_SUCCESS = "delete user token successfully!"
    DELETE_USER_TOKEN_FAILED = "delete user token failed!"
    USER_TOKEN_EXIST = "the user token has been there!"
    USER_TOKEN_NOT_EXIST = "the user token does not exist!"

    ADD_USER_AND_MATCH_CONDITION_SUCCESS = "add user and match condition successfully!"
    ADD_USER_AND_MATCH_CONDITION_FAILED = "add user and match condition failed!"
    USER_AND_MATCH_CONDITION_EXIST = "user and match condition has been there!"

    NO_RIGHT_TO_LOGOUT = "you have no right to logout!"

    ADD_IM_USER_SUCCESS = "add im user successfully!"
    ADD_IM_USER_FAILED = "add im user failed!"
    RESTORE_IM_USER_SUCCESS = "restore im user successfully!"
    RESTORE_IM_USER_FAILED = "restore im user failed!"
    IM_USER_EXIST = "im user has been there!"
    IM_USER_NOT_EXIST = "im user does not exist!"

    ADD_USER_AND_CELLPHONE_RELATION_SUCCESS = "add user and cellphone relation successfully!"
    ADD_USER_AND_CELLPHONE_RELATION_FAILED = "add user and cellphone relation failed!"
    RESTORE_USER_AND_CELLPHONE_RELATION_SUCCESS = "restore user and cellphone relation successfully!"
    RESTORE_USER_AND_CELLPHONE_RELATION_FAILED = "restore user and cellphone relation failed!"
    USER_AND_CELLPHONE_RELATION_EXIST = "user and cellphone relation has been there!"
    USER_AND_CELLPHONE_NOT_EXIST = "user and cellphone relation does not exist!"

    ADD_USER_AND_DEVICE_RELATION_SUCCESS = "add user and device relation successfully!"
    ADD_USER_AND_DEVICE_RELATION_FAILED = "add user and device relation failed!"
    RESTORE_USER_AND_DEVICE_RELATION_SUCCESS = "restore user and device relation successfully!"
    RESTORE_USER_AND_DEVICE_RELATION_FAILED = "restore user and device relation failed!"
    USER_AND_CELLPHONE_RELATION_EXIST = "user and cellphone relation has been there!"

    ADD_MATCH_REFUSE_SUCCESS = "add match refuse successfully!"
    ADD_MATCH_REFUSE_FAILED = "add match refuse failed!"
    MATCH_REFUSE_NOT_EXIST = "match refuse does not exist!"
    MATCH_REFUSE_EXIST = "match refuse has been there!"
    VALID_MATCH_REFUSE_NOT_EXIST = "valid match refuse does not exist!"
    VALID_MATCH_REFUSE_EXIST = "valid match refuse has been there!"

    ADD_MATCH_AGREE_SUCCESS = "add match agree successfully!"
    ADD_MATCH_AGREE_FAILED = "add match agree failed!"
    MATCH_AGREE_NOT_EXIST = "match agree does not exist!"
    MATCH_AGREE_EXIST = "match agree has been there!"
    VALID_MATCH_AGREE_NOT_EXIST = "valid match agree does not exist!"
    VALID_MATCH_AGREE_EXIST = "valid match agree has been there!"

    ADD_MATCH_APPLY_SUCCESS = "add match apply successfully!"
    ADD_MATCH_APPLY_FAILED = "add match apply failed!"
    MATCH_APPLY_NOT_EXIST = "match apply does not exist!"
    MATCH_APPLY_EXIST = "match apply has been there!"
    VALID_MATCH_APPLY_NOT_EXIST = "valid match apply does not exist!"
    VALID_MATCH_APPLY_EXIST = "valid match apply has been there!"

    ADD_MATCH_CONDITION_SUCCESS = "add match condition successfully!"
    ADD_MATCH_CONDITION_FAILED = "add match condition failed!"
    MATCH_CONDITION_NOT_EXIST = "match condition does not exist!"
    MATCH_CONDITION_EXIST = "match condition has been there!"

    FRIEND_RELATION_EXIST = "friend relation has been there!"
    FRIEND_RELATION_NOT_EXIST = "friend relation does not exist!"

    DEVICE_EXIST = "device has been there!"
    DEVICE_NOT_EXIST = "device does not exist!"

    DEVICE_SETTING_EXIST = "device setting has been there!"
    DEVICE_SETTING_NOT_EXIST = "device setting does not exist!"

    ADD_FRIEND_REFUSE_SUCCESS = "add friend refuse successfully!"
    ADD_FRIEND_REFUSE_FAILED = "add friend refuse failed!"
    FRIEND_REFUSE_NOT_EXIST = "friend refuse does not exist!"
    FRIEND_REFUSE_EXIST = "friend refuse has been there!"
    VALID_FRIEND_REFUSE_NOT_EXIST = "valid friend refuse does not exist!"
    VALID_FRIEND_REFUSE_EXIST = "valid friend refuse has been there!"

    ADD_FRIEND_AGREE_SUCCESS = "add friend agree successfully!"
    ADD_FRIEND_AGREE_FAILED = "add friend agree failed!"
    FRIEND_AGREE_NOT_EXIST = "friend agree does not exist!"
    FRIEND_AGREE_EXIST = "friend agree has been there!"
    VALID_FRIEND_AGREE_NOT_EXIST = "valid friend agree does not exist!"
    VALID_FRIEND_AGREE_EXIST = "valid friend agree has been there!"

    ADD_FRIEND_APPLY_SUCCESS = "add friend apply successfully!"
    ADD_FRIEND_APPLY_FAILED = "add friend apply failed!"
    FRIEND_APPLY_NOT_EXIST = "friend apply does not exist!"
    FRIEND_APPLY_EXIST = "friend apply has been there!"
    VALID_FRIEND_APPLY_NOT_EXIST = "valid friend apply does not exist!"
    VALID_FRIEND_APPLY_EXIST = "valid friend apply has been there!"

elif chinese:
    ADD_USER_SUCCESS = "添加用户成功！"
    ADD_USER_FAILED = "添加用户失败！"
    ADD_IM_USER_SUCCESS = "添加IM用户成功！"
    ADD_IM_USER_FAILED = "添加IM用户失败！"
    ADD_USER_AND_CELLPHONE_RELATION_SUCCESS = "添加用户与手机关系成功！"
    ADD_USER_AND_CELLPHONE_RELATION_FAILED = "添加用户与手机关系失败！"
    USER_AND_CELLPHONE_RELATION_EXIST = "用户与手机关系已经存在！"

    CHECK_VERIFICATION_CODE_SUCCESS = "检查验证码成功！"
    CHECK_VERIFICATION_CODE_FAILED = "验证码与服务端不一致！"
