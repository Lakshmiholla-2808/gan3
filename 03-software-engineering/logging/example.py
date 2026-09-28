import logging, logging.config

class RequestId(logging.Filter):
    def filter(self, record):
        record.request_id = "req-123"
        return True

logging.config.dictConfig({
    "version": 1,
    "formatters": {"std": {"format": "%(asctime)s [%(levelname)s] %(request_id)s %(message)s"}},
    "filters": {"rid": {"()": RequestId}},
    "handlers": {"console": {"class": "logging.StreamHandler", "formatter": "std", "filters": ["rid"]}},
    "root": {"level": "INFO", "handlers": ["console"]},
})

logging.getLogger("api").info("ticket created")
