from handlers.ohho.ohho_api import handlers as api_handlers
from handlers.ohho.ohho_test_api import handlers as test_api_handlers
from handlers.ohho.ohho_backstage import handlers as backstage_handlers
from handlers.test.test import handlers as test_handlers

handlers = api_handlers + test_api_handlers + backstage_handlers + test_handlers
