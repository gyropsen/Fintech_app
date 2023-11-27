from src.masks import get_mask_bank_card, get_mask_bank_account
from src.utils import get_transactions_list, get_amount_transaction
from src.logger import setup_logging

logger = setup_logging()

if __name__ == "__main__":
    logger.info(f"Start {__name__}")
    get_mask_bank_card("1234567891234567")
    get_mask_bank_account("")
    get_transactions_list("")
    get_amount_transaction(get_transactions_list(""))
