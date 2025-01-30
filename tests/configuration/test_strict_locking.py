import pytest
from blox.interfaces.configuration.configuration_strategy import (
	Configure,
	StrictConfigurator,
)
from blox.models.posit.posit_content_settings import Config


class TestInputModel:
	memory_limit: int
	memory_request: int

	def __init__(self, memory_limit: int, memory_request: int):
		self.memory_limit = memory_limit
		self.memory_request = memory_request


class TestContextConfig:
	memory_limit: int
	memory_request: int

	def __init__(self, memory_limit: int = 0, memory_request: int = 0):
		self.memory_limit = memory_limit
		self.memory_request = memory_request


class TestConfiguration(Configure[TestInputModel, TestContextConfig]):
	def configure(self, input: TestInputModel, content: TestContextConfig) -> TestContextConfig:
		content.memory_limit = input.memory_limit
		content.memory_request = input.memory_request
		return content


input_model = TestInputModel(memory_limit=100, memory_request=200)
test_config = TestContextConfig()  # Assuming contextConfig is a dictionary for this example


def test_strict_locking_mechanism_should_allow_with_config():
	stict_configurator = StrictConfigurator(TestConfiguration(), Config.MEMORY_LIMIT, Config.MEMORY_REQUEST)

	resulting_config = stict_configurator.configure(input_model, test_config)

	assert resulting_config.memory_limit == 100
	assert resulting_config.memory_request == 200


def test_strict_locking_mechanism_should_fail_when_chaning_non_allowed_config():
	strict_configurator = StrictConfigurator(TestConfiguration(), Config.MEMORY_LIMIT)

	with pytest.raises(AttributeError):
		strict_configurator.configure(input_model, test_config)
