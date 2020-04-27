import typing
from typing import Any, Optional, Text, Dict, List, Type

from rasa.nlu.components import Component
from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.training_data import Message, TrainingData

if typing.TYPE_CHECKING:
    from rasa.nlu.model import Metadata

from fasttext import load_model


class CustomLangDetect(Component):
    """Component to detect language of user input and pass down the language code
        in th pipeline in order to trigger a switch agent action"""

    name = "language_detect"
    provides = ["entities"]
    requires = ["text"]


    # Which components are required by this component.
    # Listed components should appear before the component itself in the pipeline.
    @classmethod
    def required_components(cls) -> List[Type[Component]]:
        """Specify which components need to be present in the pipeline."""

        return []

    # Defines the default configuration parameters of a component
    # these values can be overwritten in the pipeline configuration
    # of the model. The component should choose sensible defaults
    # and should be able to create reasonable results with the defaults.
    defaults = {}

    # Defines what language(s) this component can handle.
    # This attribute is designed for instance method: `can_handle_language`.
    # Default value is None which means it can handle all languages.
    # This is an important feature for backwards compatibility of components.
    language_list = None

    def __init__(self, component_config: Optional[Dict[Text, Any]] = None) -> None:
        super().__init__(component_config)
        self._model = load_model('./language_detection/lid.176.ftz') # to be put in component_config

    def train(
        self,
        training_data: TrainingData,
        config: Optional[RasaNLUModelConfig] = None,
        **kwargs: Any,
    ) -> None:
        """Train this component.

        This is the components chance to train itself provided
        with the training data. The component can rely on
        any context attribute to be present, that gets created
        by a call to :meth:`components.Component.pipeline_init`
        of ANY component and
        on any context attributes created by a call to
        :meth:`components.Component.train`
        of components previous to this one."""
        pass
    
    def convert_to_rasa(self, value, confidence = 1):
        """Convert model output into the Rasa NLU compatible output format."""

        entity = {"value": value,
                "confidence": confidence,
                "entity": "language_code",
                "extractor": "language_detector"}

        return entity

    def process(self, message: Message, **kwargs: Any) -> None:
        """Process an incoming message.

        This is the components chance to process an incoming
        message. The component can rely on
        any context attribute to be present, that gets created
        by a call to :meth:`components.Component.pipeline_init`
        of ANY component and
        on any context attributes created by a call to
        :meth:`components.Component.process`
        of components previous to this one."""

        if not self._model:
            language_codes = None
        
        else:
            text = message.get("text")
            prediction = self._model.predict(text)
            language_code = prediction[0][0][9:]
            confidence = float(prediction[1])
            entity = self.convert_to_rasa(value=language_code, confidence=confidence)
            message.set("entities", [entity], add_to_output=True)
        
    def persist(self, file_name: Text, model_dir: Text) -> Optional[Dict[Text, Any]]:
        """Persist this component to disk for future loading."""
        
        # might be usefull for snappier response -> to set after first approach is set

        pass

    @classmethod
    def load(
        cls,
        meta: Dict[Text, Any],
        model_dir: Optional[Text] = None,
        model_metadata: Optional["Metadata"] = None,
        cached_component: Optional["Component"] = None,
        **kwargs: Any,
    ) -> "Component":
        """Load this component from file."""

        if cached_component:
            return cached_component
        else:
            return cls(meta)