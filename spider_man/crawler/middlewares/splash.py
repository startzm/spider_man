from spider_man.custom_settings import SPLASH_SETTINGS


__all__ = ['SplashMiddlerware']


class SplashMiddlerware(object):

    def _set_request(self, request, spider):
        if 'http://splash.1datatech.cn' in request.url:
            return

        spider.logger.info(f'Start Set Splash Request: {request.url}')

        # 当未设置splash配置时，设置
        if not request.meta.get('splash'):
            request.meta['splash'] = SPLASH_SETTINGS

        # 为其设置代理
        if request.meta.get('proxy'):
            request.meta['splash']['args']['proxy'] = request.meta.get('proxy')

    def process_request(self, request, spider):
        if request.meta.get('is_ajax'):
            self._set_request(request, spider)

