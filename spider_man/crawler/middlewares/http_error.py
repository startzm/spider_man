

class HttpErrorCatchMiddleware(object):

    def process_exception(self, request, exception, spider):
        spider.logger.error(f'Tcp Error: {request.url}, {exception}')