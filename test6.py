import logging

logging.basicConfig(level=logging.DEBUG,#控制台打印的日志级别
                    filename='new.log',
                    filemode='a',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    #日志格式
                    )

logging.debug('debug级别，最低级别，一般开发人员用来打印一些调试信息')
logging.info('info级别，正常输出信息，一般用来打印一些正常的操作')
logging.warning('waring级别，一般用来打印警信息')
logging.error('error级别，一般用来打印一些错误信息')
logging.critical('critical 级别，一般用来打印一些致命的错误信息,等级最高')

