import scrapy

__all__ = ['GoodDynamicDetailItem']


class GoodDynamicDetailItem(scrapy.Item):
    # 动态详情
    _id = scrapy.Field()
    item_id = scrapy.Field()
    type = scrapy.Field()
    status = scrapy.Field()
    is_sellable = scrapy.Field()
    selling_forms = scrapy.Field()
    discount = scrapy.Field()
    market_price = scrapy.Field()
    size = scrapy.Field()
    default_sku = scrapy.Field()
    tag_ids = scrapy.Field()
    show_category = scrapy.Field()
    warehouse_code = scrapy.Field()
    sale_type = scrapy.Field()
    sale_type_id = scrapy.Field()
    merchant_id = scrapy.Field()
    product_id = scrapy.Field()
    brand_id = scrapy.Field()
    category_v3_3 = scrapy.Field()
    category_v3_4 = scrapy.Field()
    category = scrapy.Field()
    shipping_system_id = scrapy.Field()
    product_attr_aca = scrapy.Field()
    refund_policy = scrapy.Field()
    exchange_policy = scrapy.Field()
    value_of_goods = scrapy.Field()
    tax = scrapy.Field()
    anchor_uid = scrapy.Field()
    is_support_refund_window = scrapy.Field()
    countries = scrapy.Field()
    author_id = scrapy.Field()
    video_id = scrapy.Field()
    is_hide_juhe_sku = scrapy.Field()
    size_attr = scrapy.Field()
    fare = scrapy.Field()
    baoyou = scrapy.Field()
    area_code = scrapy.Field()
    area_name = scrapy.Field()
    shipping_system_type = scrapy.Field()
    shipping_time = scrapy.Field()
    baoyou_desc = scrapy.Field()
    baoyou_text = scrapy.Field()
    wuliu_text = scrapy.Field()
    guonei_baoyou = scrapy.Field()
    bonded_area_id = scrapy.Field()
    jumei_price = scrapy.Field()
    start_time = scrapy.Field()
    end_time = scrapy.Field()
    second_kill_time = scrapy.Field()
    buyer_number = scrapy.Field()
    wish_number = scrapy.Field()
    status_num = scrapy.Field()
    sale_short_name = scrapy.Field()
    sku_min_price = scrapy.Field()
    sku_max_price = scrapy.Field()
    product_detail_price_text = scrapy.Field()
    buyer_number_text = scrapy.Field()
    cart_action = scrapy.Field()
    cart_action_title = scrapy.Field()
    is_dm = scrapy.Field()
    show_sku = scrapy.Field()
    stocks_alarm = scrapy.Field()
    status_tag = scrapy.Field()
    right_top_icon = scrapy.Field()
    tag = scrapy.Field()
    is_show_value_of_goods = scrapy.Field()
    is_check_delivery_address = scrapy.Field()
    is_show_delivery_address = scrapy.Field()
    limit_buy_detail_sku_num = scrapy.Field()
    is_show_score = scrapy.Field()
    is_show_koubei = scrapy.Field()
    is_show_comment = scrapy.Field()
    is_show_new_comment_pop = scrapy.Field()
    is_show_new_comment_jumei = scrapy.Field()
    img = scrapy.Field()
    promotion_set = scrapy.Field()
    detail_page_show_promocard = scrapy.Field()
    fen_qi = scrapy.Field()
    icon_tag = scrapy.Field()
    freight = scrapy.Field()
    show_single_skuview = scrapy.Field()
    extra_data = scrapy.Field()
    shop_info = scrapy.Field()
    activity_list = scrapy.Field()
    price_des = scrapy.Field()
    product_desc = scrapy.Field()
    relate_deal = scrapy.Field()
    trust_info = scrapy.Field()
    is_phone_cost = scrapy.Field()
    detail_comment_num = scrapy.Field()
    bottom_button = scrapy.Field()
    is_first_click_window = scrapy.Field()
    countdown_time = scrapy.Field()
    recommend_soldout_title = scrapy.Field()
    recommend_soldout_status = scrapy.Field()
    sellparams = scrapy.Field()
    jumei_counter_title = scrapy.Field()
    marquee = scrapy.Field()
    quiz_module_detail = scrapy.Field()
    comment_list = scrapy.Field()
    graphic_details_other = scrapy.Field()
    url_schema = scrapy.Field()
    yanzhidai = scrapy.Field()
    show_kou_bei_cate = scrapy.Field()
    show_cart_big_img_ab = scrapy.Field()
    show_cart_big_img_onoff = scrapy.Field()
    show_comment_tab_dot = scrapy.Field()
    customer_service = scrapy.Field()
    sku_no_stock_click = scrapy.Field()
    is_service_info = scrapy.Field()
    is_show_counter = scrapy.Field()
    new_video_info = scrapy.Field()
    is_has_new_short_video = scrapy.Field()
    is_jump_app = scrapy.Field()
    coutuan_enter_info = scrapy.Field()
    has_video_img = scrapy.Field()
    video_info_test = scrapy.Field()
    is_limited = scrapy.Field()
    hide_touch_header = scrapy.Field()
    cart_host_h5 = scrapy.Field()
    address_list_version = scrapy.Field()
    is_login = scrapy.Field()
    address_list = scrapy.Field()
    default_address = scrapy.Field()
    special_deal_id = scrapy.Field()
    seckill_car_domain = scrapy.Field()
    seckill_car_event_status = scrapy.Field()
    is_dj_item = scrapy.Field()
    comment_verify_code = scrapy.Field()