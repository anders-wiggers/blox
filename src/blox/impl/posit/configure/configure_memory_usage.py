from blox.interfaces.configuration.configuration_strategy import Configure
from blox.models.posit.config_release_model import ConfigReleaseModel
from blox.models.posit.posit_content_settings import PositContentSettings


class Configure_Memory_Usage(Configure[ConfigReleaseModel, PositContentSettings]):
    def configure(
        self, input: ConfigReleaseModel, content: PositContentSettings
    ) -> PositContentSettings:
        content.memory_limit = input.memory_limit
        content.memory_request = input.memory_request
        return content
