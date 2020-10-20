import pytest

from rasa.core.domain import Domain
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from bot.actions.action_change_preferred_language import ChangePreferredLanguage


@pytest.fixture
def change_preferred_language():
    return ChangePreferredLanguage()


@pytest.fixture
def default_domain():
    return Domain(
        intents={},
        entities=[],
        slots=[],
        templates={},
        action_names=["utter_welcome", ],
        form_names=[],
    )


@pytest.fixture
def default_dispatcher():
    return CollectingDispatcher()


def test_name(change_preferred_language):
    name = change_preferred_language.name()

    assert name == "action_change_preferred_language"


def test_run(change_preferred_language, default_dispatcher, default_domain):

    default_tracker = Tracker(
        sender_id="c9er45css2923",
        slots={},
        latest_message={'entities': [{'entity': 'preferred_lang', 'value': 'en'}],
                        'intent': {},
                        'text': None,
                        'message_id': None,
                        'metadata': {},
                        },
        events=[],
        paused=False,
        followup_action=None,
        active_form=None,
        latest_action_name=None,
    )

    result = change_preferred_language.run(default_dispatcher, default_tracker, default_domain)

    preferred_lang = result[0]['value']
    followup_action = result[1]['name']
    assert preferred_lang == "en"
    assert followup_action == "utter_pt_command_change_bot"
