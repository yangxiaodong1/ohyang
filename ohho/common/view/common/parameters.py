from ohho.common.view.common.constant import *
from Tools.ohho_datetime import OHHODatetime
from Tools.ohho_operation import OHHOOperation
from Tools.ohho_log import OHHOLog

DEFAULT = None
DEFAULT_ZERO = 0
DEFAULT_STRING = ""
DEFAULT_FORMAT = "JSON"
DEFAULT_PAGE = 1
DEFAULT_COUNT_PER_PAGE = 10


class RequestMethod(object):
    def get_the_argument(self, obj, parameter, default):
        pass

    def get_format(self, obj):
        return self.get_the_argument(obj, FORMAT, DEFAULT_FORMAT)

    def get_page(self, obj):
        try:
            return int(self.get_the_argument(obj, PAGE, DEFAULT_PAGE))
        except:
            return DEFAULT_PAGE

    def get_data_count_per_page(self, obj):
        try:
            return int(self.get_the_argument(obj, DATA_COUNT_PER_PAGE, DEFAULT_COUNT_PER_PAGE))
        except:
            return DEFAULT_COUNT_PER_PAGE

    def get_page_count_per_page(self, obj):
        try:
            return int(self.get_the_argument(obj, PAGE_COUNT_PER_PAGE, DEFAULT_COUNT_PER_PAGE))
        except:
            return DEFAULT_COUNT_PER_PAGE

    def get_device_version(self, obj):
        return self.get_the_argument(obj, DEVICE_VERSION, DEFAULT)

    def get_device_application_id(self, obj):
        return self.get_the_argument(obj, DEVICE_APPLICATION_ID, DEFAULT)

    def get_device_identity_id(self, obj):
        return self.get_the_argument(obj, DEVICE_IDENTITY_ID, DEFAULT)

    def get_cellphone_country_code(self, obj):
        return self.get_the_argument(obj, CELLPHONE_COUNTRY_CODE, DEFAULT)

    def get_description(self, obj):
        return self.get_the_argument(obj, DESCRIPTION, DEFAULT)

    def get_cellphone_country_code_id(self, obj):
        return self.get_the_argument(obj, CELLPHONE_COUNTRY_CODE_ID, DEFAULT)

    def get_device_mac_address(self, obj):
        return self.get_the_argument(obj, DEVICE_MAC_ADDRESS, DEFAULT)

    def get_imei(self, obj):
        return self.get_the_argument(obj, DEVICE_IMEI, DEFAULT)

    def get_device_type(self, obj):
        return self.get_the_argument(obj, DEVICE_TYPE, DEFAULT)

    def get_device_tx_power(self, obj):
        return self.get_the_argument(obj, DEVICE_TX_POWER, DEFAULT)

    def get_device(self, obj):
        data = dict()
        identity_id = self.get_device_identity_id(obj)
        if identity_id is not None:
            data["identity_id"] = identity_id

        application_id = self.get_device_application_id(obj)
        if application_id is not None:
            data["application_id"] = application_id

        tx_power = self.get_device_tx_power(obj)
        if tx_power is not None:
            data["tx_power"] = tx_power

        mac_address = self.get_device_mac_address(obj)
        if mac_address is not None:
            data["mac_address"] = mac_address
        return data

    def get_header_content_type(self, obj):
        return self.get_the_argument(obj, HEADER_CONTENT_TYPE, "application/json")

    def get_username(self, obj):
        return self.get_the_argument(obj, USERNAME, DEFAULT)

    def get_password(self, obj):
        return self.get_the_argument(obj, PASSWORD, DEFAULT)

    def get_key(self, obj):
        return self.get_the_argument(obj, KEY, DEFAULT)

    def get_name(self, obj):
        return self.get_the_argument(obj, NAME, DEFAULT)

    def get_country_code(self, obj):
        return self.get_the_argument(obj, COUNTRY_CODE, DEFAULT)

    def get_first(self, obj):
        return self.get_the_argument(obj, FIRST, DEFAULT)

    def get_second(self, obj):
        return self.get_the_argument(obj, SECOND, DEFAULT)

    def get_distance(self, obj):
        return self.get_the_argument(obj, DISTANCE, DEFAULT)

    def get_has_sex(self, obj):
        return self.get_the_argument(obj, HAS_SEX, DEFAULT)

    def get_has_identity_card(self, obj):
        return self.get_the_argument(obj, HAS_IDENTITY_CARD, DEFAULT)

    def get_has_real_name(self, obj):
        return self.get_the_argument(obj, HAS_REAL_NAME, DEFAULT)

    def get_has_email(self, obj):
        return self.get_the_argument(obj, HAS_EMAIL, DEFAULT)

    def get_has_icon(self, obj):
        return self.get_the_argument(obj, HAS_ICON, DEFAULT)

    def get_has_source_icon(self, obj):
        return self.get_the_argument(obj, HAS_SOURCE_ICON, DEFAULT)

    def get_has_nickname(self, obj):
        return self.get_the_argument(obj, HAS_NICKNAME, DEFAULT)

    def get_has_birthday(self, obj):
        return self.get_the_argument(obj, HAS_BIRTHDAY, DEFAULT)

    def get_has_height(self, obj):
        return self.get_the_argument(obj, HAS_HEIGHT, DEFAULT)

    def get_has_weight(self, obj):
        return self.get_the_argument(obj, HAS_WEIGHT, DEFAULT)

    def get_has_marriage(self, obj):
        return self.get_the_argument(obj, HAS_MARRIAGE, DEFAULT)

    def get_has_resume(self, obj):
        return self.get_the_argument(obj, HAS_RESUME, DEFAULT)

    def get_has_blood(self, obj):
        return self.get_the_argument(obj, HAS_BLOOD, DEFAULT)

    def get_has_hometown(self, obj):
        return self.get_the_argument(obj, HAS_HOMETOWN, DEFAULT)

    def get_has_current(self, obj):
        return self.get_the_argument(obj, HAS_CURRENT, DEFAULT)

    def get_has_industry_id(self, obj):
        return self.get_the_argument(obj, HAS_INDUSTRY_ID, DEFAULT)

    def get_has_body_type_id(self, obj):
        return self.get_the_argument(obj, HAS_BODY_TYPE_ID, DEFAULT)

    def get_has_smoke_id(self, obj):
        return self.get_the_argument(obj, HAS_SMOKE_ID, DEFAULT)

    def get_has_drink_id(self, obj):
        return self.get_the_argument(obj, HAS_DRINK_ID, DEFAULT)

    def get_has_work_domain_id(self, obj):
        return self.get_the_argument(obj, HAS_WORK_DOMAIN_ID, DEFAULT)

    def get_has_profession_id(self, obj):
        return self.get_the_argument(obj, HAS_PROFESSION_ID, DEFAULT)

    def get_has_school(self, obj):
        return self.get_the_argument(obj, HAS_SCHOOL, DEFAULT)

    def get_has_company(self, obj):
        return self.get_the_argument(obj, HAS_COMPANY, DEFAULT)

    def get_has_education(self, obj):
        return self.get_the_argument(obj, HAS_EDUCATION, DEFAULT)

    def get_has_interest(self, obj):
        return self.get_the_argument(obj, HAS_INTEREST, DEFAULT)

    def get_conditions(self, obj):
        return self.get_the_argument(obj, CONDITIONS, DEFAULT)

    def get_url(self, obj):
        return self.get_the_argument(obj, URL, DEFAULT)

    def get_state(self, obj):
        return self.get_the_argument(obj, STATE, DEFAULT)

    def get_power(self, obj):
        return self.get_the_argument(obj, POWER, DEFAULT)

    def get_periods(self, obj):
        return self.get_the_argument(obj, PERIODS, DEFAULT)

    def get_password_again(self, obj):
        return self.get_the_argument(obj, PASSWORD_AGAIN, DEFAULT)

    def get_staff_id(self, obj):
        staff_id = self.get_the_argument(obj, STAFF_ID, DEFAULT_ZERO)
        return staff_id

    def get_user_id(self, obj):
        user_id = self.get_the_argument(obj, USER_ID, DEFAULT_ZERO)
        if user_id:
            return int(user_id)
        else:
            user_id = self.get_the_argument(obj, HEADER_USER_ID, DEFAULT_ZERO)
            if user_id:
                user_id = int(user_id)
            else:
                user_id = 0
        return user_id

    def get_sequence(self, obj):
        sequence = self.get_the_argument(obj, SEQUENCE, DEFAULT_ZERO)
        return sequence if sequence else 0

    def get_apply_id(self, obj):
        return self.get_the_argument(obj, APPLY_ID, DEFAULT)

    def get_movie_id(self, obj):
        return self.get_the_argument(obj, MOVIE_ID, DEFAULT)

    def get_music_id(self, obj):
        return self.get_the_argument(obj, MUSIC_ID, DEFAULT)

    def get_isbn(self, obj):
        return self.get_the_argument(obj, ISBN, DEFAULT)

    def get_sport_id(self, obj):
        return self.get_the_argument(obj, SPORT_ID, DEFAULT)

    def get_timestamp(self, obj):
        return self.get_the_argument(obj, TIMESTAMP, DEFAULT_ZERO)

    def get_score(self, obj):
        return self.get_the_argument(obj, SCORE, DEFAULT_ZERO)

    def get_impression(self, obj):
        return self.get_the_argument(obj, IMPRESSION, DEFAULT)

    def get_reason(self, obj):
        return self.get_the_argument(obj, REASON, DEFAULT)

    def get_category(self, obj):
        return self.get_the_argument(obj, CATEGORY, DEFAULT)

    def get_data(self, obj):
        return self.get_the_argument(obj, DATA, DEFAULT_STRING)

    def get_exclude_user_id(self, obj):
        user_id = self.get_the_argument(obj, EXCLUDE_USER_ID, DEFAULT)
        if user_id:
            return int(user_id)
        return user_id

    def get_last_id(self, obj):
        return self.get_the_argument(obj, LAST_ID, DEFAULT)

    def get_id(self, obj):
        return self.get_the_argument(obj, ID, DEFAULT)

    def get_group_id(self, obj):
        return self.get_the_argument(obj, BACKSTAGE_PERMISSION_GROUP_ID, DEFAULT_ZERO)

    def get_page_id(self, obj):
        return self.get_the_argument(obj, BACKSTAGE_PERMISSION_PAGE_ID, DEFAULT_ZERO)

    def get_page_permission_id(self, obj):
        return self.get_the_argument(obj, BACKSTAGE_PERMISSION_PAGE_PERMISSION_ID, DEFAULT_ZERO)

    def get_page_name(self, obj):
        return self.get_the_argument(obj, BACKSTAGE_PERMISSION_PAGE_NAME, DEFAULT_STRING)

    def get_insert(self, obj):
        result = self.get_the_argument(obj, BACKSTAGE_PERMISSION_INSERT, DEFAULT_ZERO)
        if result:
            result = int(result)
        else:
            result = 0
        return result

    def get_delete(self, obj):
        delete = self.get_the_argument(obj, BACKSTAGE_PERMISSION_DELETE, DEFAULT_ZERO)
        if delete:
            delete = int(delete)
        else:
            delete = 0
        return delete

    def get_update(self, obj):
        result = self.get_the_argument(obj, BACKSTAGE_PERMISSION_UPDATE, DEFAULT_ZERO)
        if result:
            result = int(result)
        else:
            result = 0
        return result

    def get_select(self, obj):
        result = self.get_the_argument(obj, BACKSTAGE_PERMISSION_SELECT, DEFAULT_ZERO)
        if result:
            result = int(result)
        else:
            result = 0
        return result

    def get_parent_id(self, obj):
        return self.get_the_argument(obj, PARENT_ID, DEFAULT)

    def get_limit(self, obj):
        return self.get_the_argument(obj, LIMIT, DEFAULT)

    def get_token(self, obj):
        return self.get_the_argument(obj, TOKEN, DEFAULT)

    def get_reported_user_id(self, obj):
        return self.get_the_argument(obj, REPORTED_USER_ID, DEFAULT)

    def get_friend_id(self, obj):
        return int(self.get_the_argument(obj, FRIEND_ID, DEFAULT_ZERO))

    def get_type(self, obj):
        return self.get_the_argument(obj, TYPE, DEFAULT)

    def get_content(self, obj):
        return self.get_the_argument(obj, CONTENT, DEFAULT)

    def get_is_apply(self, obj):
        return self.get_the_argument(obj, IS_APPLY, DEFAULT)

    def get_code(self, obj):
        return self.get_the_argument(obj, CODE, DEFAULT)

    def get_device_identities(self, obj):
        return self.get_the_argument(obj, DEVICE_IDENTITIES, DEFAULT)

    def get_device_id(self, obj):
        return self.get_the_argument(obj, DEVICE_ID, DEFAULT)

    def get_device_rssi(self, obj):
        return self.get_the_argument(obj, DEVICE_RSSI, DEFAULT)

    def get_device_distance(self, obj):
        return self.get_the_argument(obj, DEVICE_DISTANCE, DEFAULT)

    def get_attribute(self, obj):
        return self.get_the_argument(obj, ATTRIBUTE, DEFAULT)

    def get_cellphone_number(self, obj):
        return self.get_the_argument(obj, CELLPHONE_NUMBER, DEFAULT)

    def get_cellphone_key(self, obj):
        return self.get_the_argument(obj, CELLPHONE_KEY, DEFAULT)

    def get_cellphone_brand(self, obj):
        return self.get_the_argument(obj, CELLPHONE_BRAND, DEFAULT)

    def get_cellphone_build_id(self, obj):
        return self.get_the_argument(obj, CELLPHONE_BUILD_ID, DEFAULT)

    def get_cellphone_build_model(self, obj):
        return self.get_the_argument(obj, CELLPHONE_BUILD_MODEL, DEFAULT)

    def get_cellphone_operation(self, obj):
        return self.get_the_argument(obj, CELLPHONE_OPERATION, DEFAULT)

    def get_cellphone_operation_version(self, obj):
        return self.get_the_argument(obj, CELLPHONE_OPERATION_VERSION, DEFAULT)

    def get_cellphone_manufacturer(self, obj):
        return self.get_the_argument(obj, CELLPHONE_MANUFACTURER, DEFAULT)

    def get_cellphone_platform_type(self, obj):
        return self.get_the_argument(obj, CELLPHONE_PLATFORM_TYPE, DEFAULT)

    def get_cellphone_platform_version(self, obj):
        return self.get_the_argument(obj, CELLPHONE_PLATFORM_VERSION, DEFAULT)

    def get_cellphone(self, obj):
        data = dict()
        key = self.get_cellphone_key(obj)
        if key is not None:
            data["key"] = key

        operation = self.get_cellphone_operation(obj)
        if operation is not None:
            data["operation"] = operation

        operation_version = self.get_cellphone_operation_version(obj)
        if operation_version is not None:
            data["operation_version"] = operation_version

        build_id = self.get_cellphone_build_id(obj)
        if build_id is not None:
            data["build_id"] = build_id

        build_model = self.get_cellphone_build_model(obj)
        if build_model is not None:
            data["build_model"] = build_model

        manufacturer = self.get_cellphone_manufacturer(obj)
        if manufacturer is not None:
            data["manufacturer"] = manufacturer

        platform_type = self.get_cellphone_platform_type(obj)
        if platform_type is not None:
            data["platform_type"] = platform_type

        platform_version = self.get_cellphone_platform_version(obj)
        if platform_version is not None:
            data["platform_version"] = platform_version

        brand = self.get_cellphone_brand(obj)
        if brand is not None:
            data["brand"] = brand
        return data

    def get_is_match(self, obj):
        return self.get_the_argument(obj, IS_MATCH, DEFAULT)

    def get_is_online(self, obj):
        return self.get_the_argument(obj, IS_ONLINE, DEFAULT)

    def get_map_location_type(self, obj):
        return self.get_the_argument(obj, MAP_LOCATION_TYPE, DEFAULT_ZERO)

    def get_map_latitude(self, obj):
        return float(self.get_the_argument(obj, MAP_LATITUDE, DEFAULT_ZERO))

    def get_map_longitude(self, obj):
        return float(self.get_the_argument(obj, MAP_LONGITUDE, DEFAULT_ZERO))

    def get_map_accuracy(self, obj):
        return float(self.get_the_argument(obj, MAP_ACCURACY, DEFAULT_ZERO))

    def get_map_supplier(self, obj):
        return self.get_the_argument(obj, MAP_SUPPLIER, DEFAULT_STRING)

    def get_map_altitude(self, obj):
        return float(self.get_the_argument(obj, MAP_ALTITUDE, DEFAULT_ZERO))

    def get_map_floor(self, obj):
        return self.get_the_argument(obj, MAP_FLOOR, DEFAULT_STRING)

    def get_map_building_id(self, obj):
        return self.get_the_argument(obj, MAP_BUILDING_ID, DEFAULT_STRING)

    def get_map_speed(self, obj):
        return self.get_the_argument(obj, MAP_SPEED, DEFAULT_STRING)

    def get_map_angle(self, obj):
        return float(self.get_the_argument(obj, MAP_ANGLE, DEFAULT_ZERO))

    def get_map_satellite_number(self, obj):
        return int(self.get_the_argument(obj, MAP_SATELLITE_NUMBER, DEFAULT_ZERO))

    def get_map_country(self, obj):
        return self.get_the_argument(obj, MAP_COUNTRY, DEFAULT_STRING)

    def get_map_province(self, obj):
        return self.get_the_argument(obj, MAP_PROVINCE, DEFAULT_STRING)

    def get_map_city(self, obj):
        return self.get_the_argument(obj, MAP_CITY, DEFAULT_STRING)

    def get_map_city_code(self, obj):
        return self.get_the_argument(obj, MAP_CITY_CODE, DEFAULT_STRING)

    def get_map_area(self, obj):
        return self.get_the_argument(obj, MAP_AREA, DEFAULT_STRING)

    def get_sign(self, obj):
        return self.get_the_argument(obj, SIGN, DEFAULT)

    def get_map_area_code(self, obj):
        return self.get_the_argument(obj, MAP_AREA_CODE, DEFAULT_STRING)

    def get_map_address(self, obj):
        return self.get_the_argument(obj, MAP_ADDRESS, DEFAULT_STRING)

    def get_map_interest_point(self, obj):
        return self.get_the_argument(obj, MAP_INTEREST_POINT, DEFAULT)

    def get_all_map_information(self, obj):
        result = dict()

        result[MAP_INTEREST_POINT] = self.get_map_interest_point(obj)
        result[MAP_ADDRESS] = self.get_map_address(obj)
        result[MAP_AREA_CODE] = self.get_map_area_code(obj)
        result[MAP_AREA] = self.get_map_area(obj)
        result[MAP_CITY_CODE] = self.get_map_city_code(obj)
        result[MAP_CITY] = self.get_map_city(obj)
        result[MAP_PROVINCE] = self.get_map_province(obj)
        result[MAP_COUNTRY] = self.get_map_country(obj)
        result[MAP_SATELLITE_NUMBER] = self.get_map_satellite_number(obj)
        result[MAP_ANGLE] = self.get_map_angle(obj)
        result[MAP_SPEED] = self.get_map_speed(obj)
        result[MAP_BUILDING_ID] = self.get_map_building_id(obj)
        result[MAP_FLOOR] = self.get_map_floor(obj)
        result[MAP_ALTITUDE] = self.get_map_altitude(obj)
        result[MAP_SUPPLIER] = self.get_map_supplier(obj)
        result[MAP_ACCURACY] = self.get_map_accuracy(obj)
        result[MAP_LATITUDE] = self.get_map_latitude(obj)
        result[MAP_LONGITUDE] = self.get_map_longitude(obj)
        result[MAP_LOCATION_TYPE] = self.get_map_location_type(obj)

        return result

    def get_map_information(self, obj):
        result = dict()

        value = self.get_map_interest_point(obj)
        if value:
            result[MAP_INTEREST_POINT] = value

        value = self.get_map_address(obj)
        if value:
            result[MAP_ADDRESS] = value

        value = self.get_map_area_code(obj)
        if value:
            result[MAP_AREA_CODE] = value

        value = self.get_map_area(obj)
        if value:
            result[MAP_AREA] = value

        value = self.get_map_city_code(obj)
        if value:
            result[MAP_CITY_CODE] = value

        value = self.get_map_city(obj)
        if value:
            result[MAP_CITY] = value

        value = self.get_map_province(obj)
        if value:
            result[MAP_PROVINCE] = value

        value = self.get_map_country(obj)
        if value:
            result[MAP_COUNTRY] = value

        value = self.get_map_satellite_number(obj)
        if value:
            result[MAP_SATELLITE_NUMBER] = value

        value = self.get_map_angle(obj)
        if value:
            result[MAP_ANGLE] = value

        value = self.get_map_speed(obj)
        if value:
            result[MAP_SPEED] = value

        value = self.get_map_building_id(obj)
        if value:
            result[MAP_BUILDING_ID] = value

        value = self.get_map_floor(obj)
        if value:
            result[MAP_FLOOR] = value

        value = self.get_map_altitude(obj)
        if value:
            result[MAP_ALTITUDE] = value

        value = self.get_map_supplier(obj)
        if value:
            result[MAP_SUPPLIER] = value

        value = self.get_map_accuracy(obj)
        if value:
            result[MAP_ACCURACY] = value

        value = self.get_map_latitude(obj)
        if value:
            result[MAP_LATITUDE] = value

        value = self.get_map_longitude(obj)
        if value:
            result[MAP_LONGITUDE] = value

        value = self.get_map_location_type(obj)
        if value:
            result[MAP_LOCATION_TYPE] = value

        return result

    def get_submit(self, obj):
        return self.get_the_argument(obj, SUBMIT, DEFAULT)

    def get_delete(self, obj):
        return self.get_the_argument(obj, DELETE, DEFAULT)

    def get_delete_or_restore(self, obj):
        return self.get_the_argument(obj, DELETE_OR_RESTORE, DEFAULT)

    def get_user_extension_sex(self, obj):
        sex = self.get_the_argument(obj, USER_EXTENSION_SEX, DEFAULT)
        if sex:
            return sex
        return DEFAULT

    def get_user_extension_real_name(self, obj):
        return self.get_the_argument(obj, USER_EXTENSION_REAL_NAME, DEFAULT)

    def get_user_extension_identity_card(self, obj):
        return self.get_the_argument(obj, USER_EXTENSION_IDENTITY_CARD, DEFAULT)

    def get_user_extension_nickname(self, obj):
        return self.get_the_argument(obj, USER_EXTENSION_NICK_NAME, DEFAULT)

    def get_user_extension_email(self, obj):
        return self.get_the_argument(obj, USER_EXTENSION_EMAIL, DEFAULT)

    def get_user_extension_exclude(self, obj):
        return self.get_the_argument(obj, USER_EXTENSION_EXCLUDE, DEFAULT_STRING)

    def get_user_extension_birthday(self, obj):
        try:
            birthday = self.get_the_argument(obj, USER_EXTENSION_BIRTHDAY, DEFAULT)
            if not birthday:
                return DEFAULT
            else:
                return OHHODatetime.string2date(birthday)
        except Exception as ex:
            return DEFAULT

    def get_user_extension_certification(self, obj):
        return self.get_the_argument(obj, USER_EXTENSION_CERTIFICATION, DEFAULT_ZERO)

    def get_user_extension_body_type_id(self, obj):
        return self.get_the_argument(obj, USER_EXTENSION_BODY_TYPE_ID, DEFAULT)

    def get_user_extension_current_area(self, obj):
        return self.get_the_argument(obj, USER_EXTENSION_CURRENT_AREA, DEFAULT)

    def get_user_extension_drink_id(self, obj):
        return self.get_the_argument(obj, USER_EXTENSION_DRINK_ID, DEFAULT)

    def get_user_extension_height(self, obj):
        return self.get_the_argument(obj, USER_EXTENSION_HEIGHT, DEFAULT)

    def get_match_condition_big_height(self, obj):
        return self.get_the_argument(obj, MATCH_CONDITION_BIG_HEIGHT, DEFAULT)

    def get_match_condition_small_height(self, obj):
        return self.get_the_argument(obj, MATCH_CONDITION_SMALL_HEIGHT, DEFAULT)

    def get_match_condition_small_age(self, obj):
        return self.get_the_argument(obj, MATCH_CONDITION_SMALL_AGE, DEFAULT)

    def get_match_condition_big_age(self, obj):
        return self.get_the_argument(obj, MATCH_CONDITION_BIG_AGE, DEFAULT)

    def get_user_extension_weight(self, obj):
        return self.get_the_argument(obj, USER_EXTENSION_WEIGHT, DEFAULT)

    def get_match_condition_big_weight(self, obj):
        return self.get_the_argument(obj, MATCH_CONDITION_BIG_WEIGHT, DEFAULT)

    def get_match_condition_small_weight(self, obj):
        return self.get_the_argument(obj, MATCH_CONDITION_SMALL_WEIGHT, DEFAULT)

    def get_user_extension_hometown_area(self, obj):
        return self.get_the_argument(obj, USER_EXTENSION_HOMETOWN_AREA, DEFAULT)

    def get_user_extension_industry_id(self, obj):
        return self.get_the_argument(obj, USER_EXTENSION_INDUSTRY_ID, DEFAULT)

    def get_user_extension_marriage(self, obj):
        return self.get_the_argument(obj, USER_EXTENSION_MARRIAGE, DEFAULT)

    def get_user_extension_profession_id(self, obj):
        return self.get_the_argument(obj, USER_EXTENSION_PROFESSION_ID, DEFAULT)

    def get_user_extension_smoke_id(self, obj):
        return self.get_the_argument(obj, USER_EXTENSION_SMOKE_ID, DEFAULT)

    def get_user_extension_work_domain_id(self, obj):
        return self.get_the_argument(obj, USER_EXTENSION_WORK_DOMAIN_ID, DEFAULT)

    def get_user_extension(self, obj):
        result = dict()
        domain_id = self.get_user_extension_work_domain_id(obj)
        if domain_id:
            result[USER_EXTENSION_WORK_DOMAIN_ID] = domain_id

        smoke_id = self.get_user_extension_smoke_id(obj)
        if smoke_id:
            result[USER_EXTENSION_SMOKE_ID] = smoke_id
        drink_id = self.get_user_extension_drink_id(obj)
        if drink_id:
            result[USER_EXTENSION_DRINK_ID] = drink_id
        profession_id = self.get_user_extension_profession_id(obj)
        if profession_id:
            result[USER_EXTENSION_PROFESSION_ID] = profession_id

        marriage = self.get_user_extension_marriage(obj)
        if marriage or marriage == 0:
            result[USER_EXTENSION_MARRIAGE] = marriage
        industry_id = self.get_user_extension_industry_id(obj)
        if industry_id:
            result[USER_EXTENSION_INDUSTRY_ID] = industry_id
        hometown_area = self.get_user_extension_hometown_area(obj)
        if hometown_area:
            result[USER_EXTENSION_HOMETOWN_AREA] = hometown_area
        current_area = self.get_user_extension_current_area(obj)
        if current_area:
            result[USER_EXTENSION_CURRENT_AREA] = current_area
        body_type_id = self.get_user_extension_body_type_id(obj)
        if body_type_id:
            result[USER_EXTENSION_BODY_TYPE_ID] = body_type_id

        weight = self.get_user_extension_weight(obj)
        if weight:
            result[USER_EXTENSION_WEIGHT] = weight
        height = self.get_user_extension_height(obj)
        if height:
            result[USER_EXTENSION_HEIGHT] = height

        email = self.get_user_extension_email(obj)
        if email:
            result[USER_EXTENSION_EMAIL] = email
        nickname = OHHOOperation.to_bytes(self.get_user_extension_nickname(obj))
        if nickname:
            result[USER_EXTENSION_NICK_NAME] = nickname
        sex = self.get_user_extension_sex(obj)
        if sex or sex == 0:
            result[USER_EXTENSION_SEX] = sex

        birthday = self.get_user_extension_birthday(obj)
        if birthday:
            result[USER_EXTENSION_BIRTHDAY] = birthday

        certification = self.get_user_extension_certification(obj)
        if certification is not None:
            result[USER_EXTENSION_CERTIFICATION] = certification

        # real_name = OHHOOperation.to_bytes(self.get_user_extension_real_name(obj))
        # if real_name:
        #     result[USER_EXTENSION_REAL_NAME] = real_name
        #
        # identity_card = self.get_user_extension_identity_card(obj)
        # if identity_card:
        #     result[USER_EXTENSION_IDENTITY_CARD] = identity_card

        return result

    def get_match_condition_id(self, obj):
        return self.get_the_argument(obj, MATCH_CONDITION_ID, DEFAULT)

    def get_match_condition(self, obj):
        result = dict()
        work_domain_id = self.get_user_extension_work_domain_id(obj)
        if work_domain_id:
            result[USER_EXTENSION_WORK_DOMAIN_ID] = work_domain_id
        smoke_id = self.get_user_extension_smoke_id(obj)
        if smoke_id:
            result[USER_EXTENSION_SMOKE_ID] = smoke_id
        drink_id = self.get_user_extension_drink_id(obj)
        if drink_id:
            result[USER_EXTENSION_DRINK_ID] = drink_id
        profession_id = self.get_user_extension_profession_id(obj)
        if profession_id:
            result[USER_EXTENSION_PROFESSION_ID] = profession_id
        marriage = self.get_user_extension_marriage(obj)
        if marriage or marriage == 0:
            result[USER_EXTENSION_MARRIAGE] = marriage
        industry_id = self.get_user_extension_industry_id(obj)
        if industry_id:
            result[USER_EXTENSION_INDUSTRY_ID] = industry_id
        hometown_area = self.get_user_extension_hometown_area(obj)
        if hometown_area:
            result[USER_EXTENSION_HOMETOWN_AREA] = hometown_area
        current_area = self.get_user_extension_current_area(obj)
        if current_area:
            result[USER_EXTENSION_CURRENT_AREA] = current_area
        body_type_id = self.get_user_extension_body_type_id(obj)
        if body_type_id:
            result[USER_EXTENSION_BODY_TYPE_ID] = body_type_id
        big_weight = self.get_match_condition_big_weight(obj)
        if big_weight:
            result[MATCH_CONDITION_BIG_HEIGHT] = big_weight
        small_weight = self.get_match_condition_small_weight(obj)
        if small_weight:
            result[MATCH_CONDITION_SMALL_HEIGHT] = small_weight
        big_height = self.get_match_condition_big_height(obj)
        if big_height:
            result[MATCH_CONDITION_BIG_HEIGHT] = big_height
        small_height = self.get_match_condition_small_height(obj)
        if small_height:
            result[MATCH_CONDITION_SMALL_HEIGHT] = small_height
        email = self.get_user_extension_email(obj)
        if email:
            result[USER_EXTENSION_EMAIL] = email
        nickname = self.get_user_extension_nickname(obj)
        if nickname:
            result[USER_EXTENSION_NICK_NAME] = nickname
        sex = self.get_user_extension_sex(obj)
        if sex or sex == 0:
            result[USER_EXTENSION_SEX] = sex
        birthday = self.get_user_extension_birthday(obj)
        if birthday:
            result[USER_EXTENSION_BIRTHDAY] = birthday

        small_age = self.get_match_condition_small_age(obj)
        if small_age is not None:
            result[MATCH_CONDITION_SMALL_AGE] = small_age

        big_age = self.get_match_condition_big_age(obj)
        if big_age is not None:
            result[MATCH_CONDITION_BIG_AGE] = big_age

        return result

    def get_base_url(self, obj):
        return "http://" + obj.request.host + "/"

    def get_files_icon0(self, obj):
        return obj.request.files.get("icon0", DEFAULT)

    def get_files_icon1(self, obj):
        return obj.request.files.get("icon1", DEFAULT)

    def get_files_icon2(self, obj):
        return obj.request.files.get("icon2", DEFAULT)

    def get_files_icon3(self, obj):
        return obj.request.files.get("icon3", DEFAULT)


class Post(RequestMethod):
    def get_the_argument(self, obj, parameter, default):
        value = obj.get_body_argument(parameter, default)
        # OHHOLog.print_log(parameter)
        if not value:
            headers = Headers()
            value = headers.get_headers(obj, parameter, default)
        return value


class Get(RequestMethod):
    def get_the_argument(self, obj, parameter, default):
        return obj.get_argument(parameter, default)


class Headers(RequestMethod):
    def get_headers(self, obj, parameter, default):
        headers = obj.request.headers
        # OHHOLog.print_log(headers)
        if parameter in headers:
            return headers[parameter]
        else:
            return default
