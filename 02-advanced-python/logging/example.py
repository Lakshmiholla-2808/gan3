import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(name)s: %(message)s")
log = logging.getLogger("orders")

log.info("order received id=%s", 42)
log.warning("stock low sku=%s", "A1")
try:
    1 / 0
except ZeroDivisionError:
    log.exception("payment failed")
