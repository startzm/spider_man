from spider_man.crawler.extractors import JsonExtractor
from spider_man.crawler.fields import ContainerField, JsonField
from spider_man.spiders.jumei.good.items.good_static_detail_item import GoodStaticDetailItem

__all__ = ['GoodStaticDetailPageExtractor', 'GoodDetailCommentPageExtractor', 'GoodDetailCommentExtractor']


class GoodStaticDetailPageExtractor():
    @classmethod
    def get_item(cls, response):
        return cls._extract(response)

    @classmethod
    def _extract(cls, response):
        item = GoodStaticDetailExtractor.get_item(response)
        good_item = GoodStaticDetailItem()
        good_item['type'] = item.type
        good_item['item_id'] = item.item_id
        good_item['qrshare_product_name'] = item.qrshare_product_name
        good_item['short_name'] = item.short_name
        good_item['name'] = item.name
        good_item['product_id'] = item.product_id
        good_item['brand_id'] = item.brand_id
        good_item['category_id'] = item.category_id
        good_item['function_ids'] = item.function_ids
        good_item['image_url_set'] = item.image_url_set
        good_item['tag'] = item.tag
        good_item['show_category'] = item.show_category
        good_item['has_short_video'] = item.has_short_video
        good_item['guarantee'] = item.guarantee
        good_item['rating'] = item.rating
        good_item['product_attr_aca'] = item.product_attr_aca
        good_item['shopname'] = item.shopname
        good_item['brand_name'] = item.brand_name
        good_item['description_url_set'] = item.description_url_set
        good_item['description_url'] = item.description_url
        good_item['properties'] = item.properties
        good_item['price_ext_title'] = item.price_ext_title
        good_item['nav'] = item.nav
        good_item['ext_desc'] = item.ext_desc
        good_item['guonei_baoyou'] = item.guonei_baoyou
        good_item['refund_policy'] = item.refund_policy
        good_item['merchant_id'] = item.merchant_id
        good_item['store_id'] = item.store_id
        good_item['bonded_area_id'] = item.bonded_area_id
        good_item['size'] = item.size
        good_item['is_auth_brand'] = item.is_auth_brand
        good_item['category_ids'] = item.category_ids
        good_item['sale_forms'] = item.sale_forms
        good_item['warehouse_name'] = item.warehouse_name
        good_item['shipping_system_id'] = item.shipping_system_id
        good_item['baoyou_desc'] = item.baoyou_desc
        good_item['baoyou_text'] = item.baoyou_text
        good_item['shipping_time'] = item.shipping_time
        good_item['wuliu_text'] = item.wuliu_text
        good_item['price_detail'] = item.price_detail
        good_item['foreign_language_name'] = item.foreign_language_name
        good_item['area_name'] = item.area_name
        good_item['area_icon'] = item.area_icon
        good_item['area_icon_v2'] = item.area_icon_v2
        good_item['guo_min_v3_3'] = item.guo_min_v3_3
        good_item['ext_info'] = item.ext_info
        good_item['recommend_title'] = item.recommend_title
        good_item['special_tags'] = item.special_tags
        good_item['scan_control'] = item.scan_control
        good_item['video_info'] = item.video_info
        good_item['share_info'] = item.share_info
        good_item['tag_ids'] = item.tag_ids
        good_item['sale_short_name'] = item.sale_short_name
        good_item['tax_info'] = item.tax_info
        good_item['verify_code'] = item.verify_code
        good_item['is_pop'] = item.is_pop
        good_item['is_simple'] = item.is_simple
        good_item['description_info'] = item.description_info
        good_item['consumer_notice_data'] = item.consumer_notice_data
        good_item['hide_download_banner'] = item.hide_download_banner
        good_item['gohome'] = item.gohome
        good_item['register_send_promocard'] = item.register_send_promocard
        good_item['is_hide_partner_info'] = item.is_hide_partner_info
        if good_item['item_id']:
            return good_item


class GoodDetailCommentPageExtractor():
    @classmethod
    def get_item(cls, response):
        return cls._extract(response)

    @classmethod
    def _extract(cls, response):
        good_item = response.meta.get('item')
        item = GoodDetailCommentExtractor.get_item(response)
        good_item['filterList'] = item.filterList
        good_item['page_count'] = item.page_count
        good_item['row_count'] = item.row_count
        good_item['rows_per_page'] = item.rows_per_page
        good_item['page_number'] = item.page_number
        good_item['is_show_checkall'] = item.is_show_checkall
        good_item['rate_high'] = item.rate_high
        good_item['tag'] = item.tag
        if good_item['item_id']:
            return good_item


class GoodStaticDetailExtractor(JsonExtractor):
    type = JsonField(json_selector='$.data.type')
    item_id = JsonField(json_selector='$.data.item_id')
    qrshare_product_name = JsonField(json_selector='$.data.qrshare_product_name')
    short_name = JsonField(json_selector='$.data.short_name')
    name = JsonField(json_selector='$.data.name')
    product_id = JsonField(json_selector='$.data.product_id')
    brand_id = JsonField(json_selector='$.data.brand_id')
    category_id = JsonField(json_selector='$.data.category_id')
    function_ids = JsonField(json_selector='$.data.function_ids')
    image_url_set = JsonField(json_selector='$.data.image_url_set')
    tag = JsonField(json_selector='$.data.tag')
    show_category = JsonField(json_selector='$.data.show_category')
    has_short_video = JsonField(json_selector='$.data.has_short_video')
    guarantee = JsonField(json_selector='$.data.guarantee')
    rating = JsonField(json_selector='$.data.rating')
    product_attr_aca = JsonField(json_selector='$.data.product_attr_aca')
    shopname = JsonField(json_selector='$.data.shopname')
    brand_name = JsonField(json_selector='$.data.brand_name')
    description_url_set = JsonField(json_selector='$.data.description_url_set')
    description_url = JsonField(json_selector='$.data.description_url')
    properties = JsonField(json_selector='$.data.properties')
    price_ext_title = JsonField(json_selector='$.data.price_ext_title')
    nav = JsonField(json_selector='$.data.nav')
    ext_desc = JsonField(json_selector='$.data.ext_desc')
    guonei_baoyou = JsonField(json_selector='$.data.guonei_baoyou')
    refund_policy = JsonField(json_selector='$.data.refund_policy')
    merchant_id = JsonField(json_selector='$.data.merchant_id')
    store_id = JsonField(json_selector='$.data.store_id')
    bonded_area_id = JsonField(json_selector='$.data.bonded_area_id')
    size = JsonField(json_selector='$.data.size')
    is_auth_brand = JsonField(json_selector='$.data.is_auth_brand')
    category_ids = JsonField(json_selector='$.data.category_ids')
    sale_forms = JsonField(json_selector='$.data.sale_forms')
    warehouse_name = JsonField(json_selector='$.data.warehouse_name')
    shipping_system_id = JsonField(json_selector='$.data.shipping_system_id')
    baoyou_desc = JsonField(json_selector='$.data.baoyou_desc')
    baoyou_text = JsonField(json_selector='$.data.baoyou_text')
    shipping_time = JsonField(json_selector='$.data.shipping_time')
    wuliu_text = JsonField(json_selector='$.data.wuliu_text')
    price_detail = JsonField(json_selector='$.data.price_detail')
    foreign_language_name = JsonField(json_selector='$.data.foreign_language_name')
    area_name = JsonField(json_selector='$.data.area_name')
    area_icon = JsonField(json_selector='$.data.area_icon')
    area_icon_v2 = JsonField(json_selector='$.data.area_icon_v2')
    guo_min_v3_3 = JsonField(json_selector='$.data.guo_min_v3_3')
    ext_info = JsonField(json_selector='$.data.ext_info')
    recommend_title = JsonField(json_selector='$.data.recommend_title')
    special_tags = JsonField(json_selector='$.data.special_tags')
    scan_control = JsonField(json_selector='$.data.scan_control')
    video_info = JsonField(json_selector='$.data.video_info')
    share_info = JsonField(json_selector='$.data.share_info')
    tag_ids = JsonField(json_selector='$.data.tag_ids')
    sale_short_name = JsonField(json_selector='$.data.sale_short_name')
    tax_info = JsonField(json_selector='$.data.tax_info')
    verify_code = JsonField(json_selector='$.data.verify_code')
    is_pop = JsonField(json_selector='$.data.is_pop')
    is_simple = JsonField(json_selector='$.data.is_simple')
    description_info = JsonField(json_selector='$.data.description_info')
    consumer_notice_data = JsonField(json_selector='$.data.consumer_notice_data')
    hide_download_banner = JsonField(json_selector='$.data.hide_download_banner')
    gohome = JsonField(json_selector='$.data.gohome')
    register_send_promocard = JsonField(json_selector='$.data.register_send_promocard')
    is_hide_partner_info = JsonField(json_selector='$.data.is_hide_partner_info')


class GoodDetailCommentExtractor(JsonExtractor):
    filterList = JsonField(json_selector='$.data.filterList')
    page_count = JsonField(json_selector='$.data.page_count')
    row_count = JsonField(json_selector='$.data.row_count')
    rows_per_page = JsonField(json_selector='$.data.rows_per_page')
    page_number = JsonField(json_selector='$.data.page_number')
    is_show_checkall = JsonField(json_selector='$.data.is_show_checkall')
    rate_high = JsonField(json_selector='$.data.rate_high')
    tag = JsonField(json_selector='$.data.tag')