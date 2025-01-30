from blox.impl.posit.configure.configure_memory_usage import Configure_Memory_Usage
from blox.models.posit.config_release_model import ConfigReleaseModel
from blox.models.posit.posit_content_settings import PositContentSettings

configure_memory_strategy = Configure_Memory_Usage()


def test_configure_memory_usage():
	"""
	Test the configure method of Configure_Memory_Usage with valid memory limits and requests.
	"""
	contextConfig = PositContentSettings()
	input_model = ConfigReleaseModel(memory_limit=100, memory_request=200)

	configure_memory_strategy.configure(input_model, contextConfig)

	assert contextConfig.memory_limit == 100
	assert contextConfig.memory_request == 200
