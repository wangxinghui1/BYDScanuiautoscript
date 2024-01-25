import logging
def get_logger(logger_name,log_file):
    # get a logger
    logger=logging.getLogger(logger_name)
    #set logger debug level
    logger.setLevel(logging.DEBUG)
    #set denug content
    formatter=logging.Formatter('%(asctime)s-%(filename)s-%(levelname)s:%(message)s')
    #Save settingts to file
    file_handler=logging.FileHandler(log_file)
    #set file debug
    file_handler.setLevel(logging.DEBUG)
    #add log content to file
    file_handler.setFormatter(formatter)
    #Output log content to file
    logger.addHandler(file_handler)
    return logger