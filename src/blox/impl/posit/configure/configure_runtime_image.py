
from blox.interfaces.configuration.configuration_strategy import Configure
from blox.models.content_config_model import ContentSettings

class Configure_Runtime_Image(Configure):

    def configure(self, content: ContentSettings) -> ContentSettings:
        return content