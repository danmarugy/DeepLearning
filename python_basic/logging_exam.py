import logging

# logging의  default log level이 warning으로 되어있기 때문에 실행시 info는 출력되지 않는다.
logging.info('my INFO log')
logging.warning('my WARNING log') # WARNING:root:my WARNING log

# default log level 변경
logging.basicConfig(level = logging.DEBUG)

print(logging.getLevelName('DEBUG'))

logging.debug('my DEBUG log')
logging.info('my INFO log')
logging.warning('my WARNING log')
logging.error('my ERROR log')
logging.critical('my CRITICAL log')
