from typing import List
from blox.impl.posit.configure.configure_memory_usage import Configure_Memory_Usage
from blox.impl.posit.configure.configure_runtime_image import Configure_Runtime_Image
from blox.interfaces.configuration.configuration_strategy import Configure
from blox.models.posit.content_setting import PositContentSettings
from blox.models.types import Deployment_Type, Language

configurations: List[Configure] = [Configure_Memory_Usage(), Configure_Runtime_Image()]


contextConfig = PositContentSettings()

for configuration in configurations:
    configuration.configure(contextConfig)

client = clientFactory.createClient(Language.PYTHON, Deployment_Type.API)
client.configure()
client.deploy(contextConfig)