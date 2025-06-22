import sys
import logging
import traceback


def error_message_details(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = (
        "Error occurred in Python script name [{0}] line number [{1}] with error message [{2}]"
        .format(file_name, exc_tb.tb_lineno, str(error))
    )
    return error_message  # <-- THIS WAS MISSING

class CustomException(Exception):
    def __init__(self, error, error_detail: sys):
        self.error_message = error_message_details(error, error_detail)
        super().__init__(self.error_message)

    def __str__(self):
        return self.error_message

