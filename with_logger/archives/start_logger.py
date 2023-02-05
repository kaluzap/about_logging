import logging

def start_log_system(log_file_path = None):
    
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    # stream_formatter = logging.Formatter("")
    stream_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_handler.setFormatter(stream_formatter)
    
    file_handler = logging.FileHandler(log_file_path, "w")
    file_handler.setLevel(logging.DEBUG)
    # file_formatter = logging.Formatter("")
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)
    
    logging.basicConfig(handlers= [file_handler, stream_handler], level=logging.DEBUG)


    # NOTE:
    # https://stackoverflow.com/questions/50714316/how-to-use-logging-getlogger-name-in-multiple-modules
