from exmo_api_repository import ExmoApiRepository
from exmo_api_model import ExmoApiModel
from core import Core
import sys

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

CURRENCIES_PAIR = "BTC_RUB"
INITIAL_MONEY_AMOUNT = 100000

apiRepository = ExmoApiRepository()
apiModel = ExmoApiModel(apiRepository, CURRENCIES_PAIR, INITIAL_MONEY_AMOUNT)

core = Core(apiModel)
core.start()
