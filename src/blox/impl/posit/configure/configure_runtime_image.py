
from blox.interfaces.configuration.configuration_strategy import Configure
from blox.models.posit.config_release_model import ConfigReleaseModel
from blox.models.posit.posit_content_settings import PositContentSettings

class Configure_Runtime_Image(Configure[ConfigReleaseModel,PositContentSettings]):
    def configure(self, input: ConfigReleaseModel ,configuration: PositContentSettings) -> PositContentSettings:
        configuration.default_image_name = input.run_time_image
        return configuration