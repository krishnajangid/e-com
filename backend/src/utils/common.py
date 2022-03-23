import logging


def get_logger(level: int = logging.INFO) -> logging:
    """
    Create and return logger object.

    :param level: Log level to be set
    :return: logging
    """
    logging.basicConfig(
        level=level,
        format="[%(asctime)s] %(levelname)s {%(pathname)s:%(lineno)d} %(message)s"
    )

    return logging.getLogger("e-com")
