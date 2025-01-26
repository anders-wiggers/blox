
from blox.interfaces.configuration.configuration_strategy import ConcreteConfigurationContext, ConfigurationContextStrategy, Configure
from blox.models.posit.content_setting import PositContentSettings

class Configure_Memory_Usage(Configure):
    def configure(self, content: ConfigurationContextStrategy) -> PositContentSettings:
        context_str = str(content.get_context())
        settings = PositContentSettings(context_str)
        return settings