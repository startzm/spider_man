import signal
import os

from scrapy.http import HtmlResponse
from scrapy.downloadermiddlewares.retry import RetryMiddleware


from selenium.common.exceptions import TimeoutException

from spider_man.crawler.utils.selenium import SeleniumDriver

__all__ = ['SeleniumMiddlerware']


class SeleniumMiddlerware(RetryMiddleware):
    driver = None

    def _set_driver(self, request, spider):
        is_ajax = request.meta.get('is_ajax')

        # 如果非ajax
        if not is_ajax:
            return

        if not self.driver:
            self.driver = SeleniumDriver().get_driver()
            spider.logger.info(f'Create Driver Success')

    def _close_driver(self, request, spider):
        try:
            self.driver.close()
            self.driver.quit()
            self.driver.service.process.send_signal(signal.SIGTERM)
        except Exception as e:
            spider.logger.error(f'Quit Driver Error：{e}')

        try:
            os.system('ps -ef | grep chrome | awk \'{print $2}\' | xargs kill -9')
        except Exception as e:
            spider.logger.error(f'Quit Driver Error：{e}')
        finally:
            self.driver = None
            del self.driver


    def _get_response(self, request, spider):
        spider.logger.info('Use Proxy Selenium: ' + request.url)
        try:
            self.driver.get(request.url)
        except TimeoutException:
            self.driver.execute_script('window.stop()')
        finally:
            try:
                body = self.driver.page_source
                return HtmlResponse(self.driver.current_url, body=body, encoding='utf-8', request=request)
            finally:
                self._close_driver(request, spider)

    def process_request(self, request, spider):
        if request.meta.get('is_ajax'):
            self._set_driver(request, spider)
            response = self._get_response(request, spider)
            return response

    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):
        return self._retry(request, 'Error Proxy', spider)
