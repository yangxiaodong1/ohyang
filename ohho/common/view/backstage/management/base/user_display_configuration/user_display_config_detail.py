from ohho.common.view.common.parameters import Get, Post
from ohho.common.view.backstage.management.base.constant import *
from ohho.common.logic.common.base.user_display_configuration import UserDisplayConfiguration
from ohho.common.view.backstage.base_handler import BaseHandler
from tornado.web import authenticated


class BackstageUserDisplayConfigDetailHandler(BaseHandler):
    def post(self):
        data = dict()
        instance = UserDisplayConfiguration()
        the_post = Post()
        distance = the_post.get_distance(self)
        has_sex = the_post.get_has_sex(self)
        has_identity_card = the_post.get_has_identity_card(self)
        has_real_name = the_post.get_has_real_name(self)
        has_email = the_post.get_has_email(self)
        has_icon = the_post.get_has_icon(self)
        has_source_icon = the_post.get_has_source_icon(self)
        has_nickname = the_post.get_has_nickname(self)
        has_birthday = the_post.get_has_birthday(self)
        has_height = the_post.get_has_height(self)
        has_weight = the_post.get_has_weight(self)
        has_marriage = the_post.get_has_marriage(self)
        has_resume = the_post.get_has_resume(self)
        has_blood = the_post.get_has_blood(self)
        has_hometown = the_post.get_has_hometown(self)
        has_current = the_post.get_has_current(self)
        has_industry_id = the_post.get_has_industry_id(self)
        has_body_type_id = the_post.get_has_body_type_id(self)
        has_smoke_id = the_post.get_has_smoke_id(self)
        has_drink_id = the_post.get_has_drink_id(self)
        has_work_domain_id = the_post.get_has_work_domain_id(self)
        has_profession_id = the_post.get_has_profession_id(self)
        has_school = the_post.get_has_school(self)
        has_company = the_post.get_has_company(self)
        has_education = the_post.get_has_education(self)
        has_interest = the_post.get_has_interest(self)
        data["distance"] = distance
        data["has_sex"] = has_sex
        data["has_identity_card"] = has_identity_card
        data["has_real_name"] = has_real_name
        data["has_email"] = has_email
        data["has_icon"] = has_icon
        data["has_source_icon"] = has_source_icon
        data["has_nickname"] = has_nickname
        data["has_birthday"] = has_birthday
        data["has_height"] = has_height
        data["has_weight"] = has_weight
        data["has_marriage"] = has_marriage
        data["has_resume"] = has_resume
        data["has_blood"] = has_blood
        data["has_hometown"] = has_hometown
        data["has_current"] = has_current
        data["has_industry_id"] = has_industry_id
        data["has_body_type_id"] = has_body_type_id
        data["has_smoke_id"] = has_smoke_id
        data["has_drink_id"] = has_drink_id
        data["has_work_domain_id"] = has_work_domain_id
        data["has_profession_id"] = has_profession_id
        data["has_school"] = has_school
        data["has_company"] = has_company
        data["has_education"] = has_education
        data["has_interest"] = has_interest
        user_display_config_id = the_post.get_id(self)
        user_display_config_obj = instance.get(user_display_config_id)
        submit = the_post.get_submit(self)
        delete_or_retore = the_post.get_delete_or_restore(self)
        success = False
        if submit:
            success = instance.update(user_display_config_obj, data)

        if delete_or_retore:
            if user_display_config_obj.id:
                success = instance.delete(user_display_config_obj)
        if success:
            return self.redirect(BASE_USER_DISPLAY_CONFIG_LIST_URL)
        return self.redirect(BASE_USER_DISPLAY_CONFIG_DETAIL_HTML + "?id=" + str(user_display_config_id))




    def get(self):
        instance = UserDisplayConfiguration()
        the_get = Get()
        userDisplayConfig_id = the_get.get_id(self)
        query_obj = ""
        if userDisplayConfig_id:
            query_obj = instance.get(userDisplayConfig_id)

        return self.render(BASE_USER_DISPLAY_CONFIG_DETAIL_HTML,
                           detail_url=BASE_USER_DISPLAY_CONFIG_DETAIL_URL,
                           list_url=BASE_USER_DISPLAY_CONFIG_LIST_URL,
                           query_obj = query_obj
                           )