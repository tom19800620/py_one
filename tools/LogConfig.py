import logging


class Log:

    Print = None

    @staticmethod
    def gets():
        if Log.Print is None:
            print('initiating Log data')
            logging.basicConfig(level=logging.DEBUG,
                                format='%(asctime)s | %(name)s | %(funcName)s | (%(lineno)d) | %(levelname)s | %(message)s'
                                # , filename="C:\\temp\\Log\\file.log"
                                )
            # c_handler = logging.StreamHandler()
            # c_handler.setLevel(logging.DEBUG)
            #
            # # Create formatters and add it to handlers
            # c_format = logging.Formatter(
            #     '%(asctime)s | %(name)s | %(funcName)s | (%(lineno)d) | %(levelname)s | %(message)s')
            # c_handler.setFormatter(c_format)
            #
            # # Add handlers to the logger
            # logging.getLogger('').addHandler(c_handler)
            Log.Print = logging
            # return log.Print
        # return self.log