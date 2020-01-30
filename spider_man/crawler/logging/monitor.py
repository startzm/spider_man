import os
import logging

log_template = '%(service)s|%(customerId)s|%(step)s|%(state)s|%(other)s|%(text)s' \
               '|%(logTime)s|%(cost)s|%(reserved)s'

class Monitor():
    def __init__(self):
        self.logger = logging.getLogger('monitor_logger')

    def info(self, info):
        if not info.get('customerId'):
            info['customerId'] = 'nil'
        if info['step'] == 'request_url':
            info['reserved'] = info.get('scheduleTime')
        else:
            info['reserved'] = 'nil'
        self.logger.info(log_template % info)


monitor_logger = Monitor()