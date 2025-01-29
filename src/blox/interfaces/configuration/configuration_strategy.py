from abc import ABC, abstractmethod
from enum import StrEnum
from typing import Generic, TypeVar

I = TypeVar("I")  # noqa: E741
O = TypeVar("O")  # noqa: E741


class Configure(ABC, Generic[I, O]):
    """
    Abstract base class for a configurator that applies configuration to an object.

    This class defines the interface for a configuration class that is responsible
    for applying configurations from an input model (`I`) to a configuration model (`O`).
    It is intended to be an infterface, and the `configure` method must be implemented
    to provide the actual logic for the configuration process.

    Attributes:
        None (abstract base class)

    Methods:
        configure(self, input: I, configuration: O) -> O:
            Abstract method that applies the configuration logic to the input and configuration models.
            Subclasses must implement this method to define specific configuration behavior.

    Example:
        # Example of a subclass implementing the `configure` method:

        class MyConfigurator(Configure[InputModel, ConfigModel]):
            def configure(self, input: InputModel, configuration: ConfigModel) -> ConfigModel:
                # Implement specific configuration logic here
                return configuration
    """

    @abstractmethod
    def configure(self, input: I, configuration: O) -> O:
        """
        Abstract method to be implemented by subclasses for applying configuration logic.

        This method defines the process of applying the configuration to a given input model (`I`),
        modifying the provided configuration model (`O`).

        Args:
            input (I): The input model that provides the data to configure the configuration model.
            configuration (O): The configuration model to be updated based on the input model.

        Returns:
            O: The updated configuration model.

        Raises:
            NotImplementedError: This is an abstract method and must be implemented in a subclass.

        Example:
            # Example implementation in a subclass
            def configure(self, input: InputModel, configuration: ConfigModel) -> ConfigModel:
                # Apply configuration logic
                return configuration
        """
        pass


class StrictConfigurator:
    """
    A strict configurator that enforces configuration only on specified writable fields of a content model.

    This class ensures that only a predefined set of attributes can be set in the content model.
    It is used for creating objects that should only be configured with specific fields,
    as defined during the initialization of the `StrictConfigurator` instance.

    Attributes:
        writable_attributes (tuple): A tuple of field names (strings) that are allowed to be configured.
        configure (Configure): An instance of the `Configure` class, responsible for setting up the configuration.

    Methods:
        __init__(self, configure: Configure, *fields: StrEnum):
            Initializes the `StrictConfigurator` with a `Configure` instance and a list of writable fields.

        create_configured_object(self, input_model: I, content_model_class: O) -> O:
            Creates and returns an object of `content_model_class`, configuring it using the `input_model`.
            The configuration is applied strictly to the writable fields specified at initialization.

    Example:
        # Example usage of StrictConfigurator class

        # Initialize a configurator with the specific writable fields
        configurator = StrictConfigurator(configure_instance, 'field1', 'field2', 'field3')

        # Use the configurator to create and configure a new content model instance
        content_model_instance = configurator.create_configured_object(input_model, ContentModel)
    """

    def __init__(self, configure: Configure, *fields: StrEnum):
        """
        Initializes a StrictConfigurator instance with the provided `Configure` instance and the list
        of writable fields.

        Args:
            configure (Configure): An instance of the `Configure` class that provides the logic to configure the model.
            *fields (StrEnum): A variable number of fields that represent the attributes which can be written to
                                the content model.

        Example:
            configurator = StrictConfigurator(configure_instance, 'field1', 'field2', 'field3')
        """
        self.writable_attributes = fields
        self.__configure_instance = configure

    def configure(self, input_model: I, content_model_class: O) -> O:
        """
        Creates a configured object of type `content_model_class` by applying configuration from the
        `input_model`. This method ensures that only the specified writable attributes are configured,
        raising an `AttributeError` if an attempt is made to modify any non-writable field.

        Args:
            input_model (I): The model instance that contains the configuration data to apply.
            content_model_class (O): The class type of the content model to create and configure.

        Returns:
            content_model_class: An instance of the `content_model_class` with the configured attributes.

        Raises:
            AttributeError: If an attempt is made to modify a field that is not listed in the writable attributes.

        Example:
            configured_object = configurator.create_configured_object(input_model, ContentModel)
        """

        class mutable_content_model:
            """
            A mutable content model class used to apply configurations to the provided fields. This class
            ensures that only the specified writable attributes are modified.

            Attributes:
                writable_attributes (tuple): The list of fields that can be modified.
                init (bool): A flag used to differentiate between the initial and configured state.
            """

            init = True

            def __init__(self, writable_attributes):
                """
                Initializes the mutable content model with the list of writable attributes.

                Args:
                    writable_attributes (tuple): The list of attributes that are allowed to be modified.
                """
                self.writable_attributes = writable_attributes
                self.init = False

            def __setattr__(self, name, value):
                """
                Ensures that only writable attributes are set. If an attempt is made to set a non-writable
                attribute, an `AttributeError` is raised.

                Args:
                    name (str): The name of the attribute to set.
                    value (Any): The value to assign to the attribute.

                Raises:
                    AttributeError: If the attribute is not in the list of writable attributes.
                """
                if self.init or name in self.writable_attributes:
                    super(self.__class__, self).__setattr__(name, value)
                else:
                    raise AttributeError(f"Attribute '{name}' is not writable")

        # Create a temporary mutable content model instance
        temperary_mutable_content_instance = mutable_content_model(
            self.writable_attributes
        )

        # Configure the instance using the provided `Configure` implementation
        self.__configure_instance.configure(
            input_model, temperary_mutable_content_instance
        )

        # Transfer the writable attribute values to the content model class
        for field in dir(temperary_mutable_content_instance):
            if field in self.writable_attributes:
                value = getattr(temperary_mutable_content_instance, field)
                content_model_class.__setattr__(field, value)

        # Return the configured instance
        return content_model_class
