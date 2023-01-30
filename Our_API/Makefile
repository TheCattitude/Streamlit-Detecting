#################### PACKAGE ACTIONS ###################

#reinstall_package:
#	@pip uninstall -y package_name || :
#	@pip install -e .

run_api:
	uvicorn speeches.api.fast:app --reload

##################### TESTS #####################
default:
	@echo 'tests are only executed locally'

test_api: test_api_root test_api_predict

test_api_root:
	TEST_ENV=development pytest tests/api -k 'test_root' --asyncio-mode=strict -W "ignore"

test_api_predict:
	TEST_ENV=development pytest tests/api -k 'test_predict' --asyncio-mode=strict -W "ignore"