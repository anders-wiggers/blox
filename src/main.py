import ast
import copy
from typing import List
from blox.impl.posit.configure.configure_memory_usage import Configure_Memory_Usage
from blox.impl.posit.configure.configure_runtime_image import Configure_Runtime_Image
from blox.interfaces.configuration.configuration_strategy import StrictConfigurator, Configure
from blox.models.posit.posit_content_settings import Config, PositContentSettings
from blox.models.types import Deployment_Type, Language
import inspect



configurations: List[Configure] = [Configure_Memory_Usage(), Configure_Runtime_Image()] 


from blox.models.posit.config_release_model import ConfigReleaseModel

def get_var_name(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var]


contextConfig = PositContentSettings()
contextConfig.name = "Test"




conf: StrictConfigurator = StrictConfigurator(
        Configure_Memory_Usage(), 
        Config.MEMORY_LIMIT,
        Config.MEMORY_REQUEST
    )

input_model = ConfigReleaseModel(memory_limit=100, memory_request=200)

dd = conf.configure(input_model, contextConfig)


print(dd.memory_limit)





# Get input from config_release.yml

# Pre-process

# Configure Release


# Deploy Release


# Post-process
    # Test Release
    # Cleanup etc




contextConfig = PositContentSettings()

for configuration in configurations:
    configuration.configure("hi", contextConfig)

print(contextConfig)


client = clientFactory.createClient(Language.PYTHON, Deployment_Type.API)
client.configure()
client.deploy(contextConfig)