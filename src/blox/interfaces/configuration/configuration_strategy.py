from abc import ABC, abstractmethod
from blox.models.posit.content_setting import PositContentSettings, Settings

class Configure(ABC):
    @abstractmethod
    def configure(self, content: ConfigurationContextStrategy) -> Settings:
        pass
    
class ConfigurationContextStrategy(ABC):
    @abstractmethod
    def get_context(self) -> Settings:
        pass

class ConcreteConfigurationContext(ConfigurationContextStrategy):
    def get_context(self) -> PositContentSettings:
        return PositContentSettings()