import logging
import datetime

class _LoggingHandler(object):

    def __init__(self):
        #super().__init__()
        # Init Logger
        self.logger = logging.getLogger(__name__)
        # add new levels
        self.add_log_levels()
        # setup Logger
        self.__setup_logger()

    def add_log_levels(self):
        self.__add_logger_level_debug()
        self.__add_logger_level_info()
        self.__add_logger_level_warning()
        self.__add_logger_level_critical()
        self.__add_logger_level_error()
        self.__add_logger_level_note()
        self.__add_logger_level_trace()
        self.__add_logger_level_pass()
        self.__add_logger_level_fail()

    def __add_logger_level_debug(self):
        logging.addLevelName(logging.DEBUG, '%-8s' % logging.getLevelName(logging.DEBUG))

    def __add_logger_level_info(self):
        logging.addLevelName(logging.INFO, '%-8s' % logging.getLevelName(logging.INFO))

    def __add_logger_level_warning(self):
        logging.addLevelName(logging.WARNING, '%-8s' % logging.getLevelName(logging.WARNING))

    def __add_logger_level_error(self):
        logging.addLevelName(logging.ERROR, '%-8s' % logging.getLevelName(logging.ERROR))

    def __add_logger_level_critical(self):
        logging.addLevelName(logging.CRITICAL, '%-8s' % logging.getLevelName(logging.CRITICAL))

    def __add_logger_level_note(self):
        logging.NOTE = 11
        logging.addLevelName(logging.NOTE, '%-8s' % 'NOTE')
        self.logger.note = lambda msg, *args: self.logger._log(logging.NOTE, msg, args)

    def __add_logger_level_trace(self):
        logging.TRACE = 12
        logging.addLevelName(logging.TRACE, '%-8s' % 'TRACE')
        self.logger.trace = lambda msg, *args: self.logger._log(logging.TRACE, msg, args)

    def __add_logger_level_pass(self):
        logging.OK = 13
        logging.addLevelName(logging.OK, '%-8s' % 'OK')
        self.logger.ok = lambda msg, *args: self.logger._log(logging.OK, msg, args)

    def __add_logger_level_fail(self):
        logging.FAIL = 14
        logging.addLevelName(logging.FAIL, '%-8s' % 'FAIL')
        self.logger.fail = lambda msg, *args: self.logger._log(logging.FAIL, msg, args)

    def set_logger_formatter(self):
        # setup formatter
        self.formatter = logging.Formatter('%(levelname)s %(asctime)-8s - %(message)s',
                                      "%Y-%m-%d %H:%M:%S")

    def set_sys_stream_handler(self):
        # create console handler
        handler = logging.StreamHandler()
        # set handler level info
        handler.setLevel(logging.DEBUG)
        # add formatter to handler
        handler.setFormatter(self.formatter)
        # add handler to logger
        self.logger.addHandler(handler)

    def  set_file_handler(self, mfilename = 'robot'):
        dfilename = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        # create file handler
        filename = '{}.{}'.format(mfilename,'log')
        fhandler = logging.FileHandler(filename)
        # set handler level info
        fhandler.setLevel(logging.DEBUG)
        # add formatter to handler
        fhandler.setFormatter(self.formatter)
        # add handler to logger
        self.logger.addHandler(fhandler)

    def __setup_logger(self):
        self.set_logger_formatter()
        # setup Level
        self.logger.setLevel(logging.DEBUG)
        self.set_sys_stream_handler()
        self.set_file_handler()


log_handler = _LoggingHandler()

class RobotLogHandler():

    @staticmethod
    def debug(msg):
        log_handler.logger.debug(msg)

    @staticmethod
    def info(msg):
        log_handler.logger.info(msg)

    @staticmethod
    def warning(msg):
        log_handler.logger.warning(msg)

    @staticmethod
    def critical(msg):
        log_handler.logger.critical(msg)

    @staticmethod
    def error(msg):
        log_handler.logger.error(msg)

    @staticmethod
    def note(msg):
        log_handler.logger.note(msg)

    @staticmethod
    def trace(msg):
        log_handler.logger.trace(msg)

    @staticmethod
    def ok(msg):
        log_handler.logger.ok(msg)

    @staticmethod
    def fail(msg):
        log_handler.logger.fail(msg)

    @staticmethod
    def set_log_file_name(filename):
        log_handler.set_file_handler(filename)

if __name__ == '__main__':

    RobotLogHandler.debug('debug message')
    RobotLogHandler.info('info message')
    RobotLogHandler.warning('warn message')
    RobotLogHandler.error('error message')
    RobotLogHandler.critical('critical message')
    RobotLogHandler.note('note message')
    RobotLogHandler.trace('trace message')
    RobotLogHandler.ok('ok message')
    RobotLogHandler.fail('fail message')