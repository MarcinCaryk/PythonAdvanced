import logging

wlasne_dane = "Testowanie Loggera"


def main() -> None:
    logging.basicConfig(
        format="[%(asctime)s] [%(wlasne_dane)s] [%(name)s] %(levelname)s: %(message)s", level=logging.DEBUG)

    old_factory = logging.getLogRecordFactory()

    def record_factory(*args: object, **kwargs: object) -> logging.LogRecord:
        global wlasne_dane
        record = old_factory(*args, **kwargs)

        record.wlasne_dane = wlasne_dane

        return record

    logging.setLogRecordFactory(record_factory)

    logger = logging.getLogger(__name__)
    logger.info("Wszystko ok dla testowania logRecord - Testowanie Loggera")
    global wlasne_dane
    wlasne_dane = "Some Text"
    logger.info("Wszystko ok dla testowania logRecord - Some Text")


if __name__ == "__main__":
    main()