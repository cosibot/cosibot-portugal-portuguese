import pytest

from rasa.core.domain import Domain
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from bot.actions.action_default_fallback import ActionDefaultFallback


@pytest.fixture
def action_default_fallback():
    return ActionDefaultFallback()


@pytest.fixture
def default_domain():
    return Domain(
        intents={},
        entities=[],
        slots=[],
        templates={'utter_fallback_request_hasdata': [{'custom': {'answers': ['something']}}]},
        action_names=["utter_welcome", ],
        form_names=[],
    ).as_dict()


@pytest.fixture
def default_dispatcher():
    return CollectingDispatcher()


def test_name(action_default_fallback):
    name = action_default_fallback.name()

    assert name == "action_default_fallback"


def test_run_first(action_default_fallback, default_dispatcher, default_domain):

    first_try = Tracker(
        sender_id="c9er45css2923",
        slots={"total_nr_tries": 0},
        latest_message={'text': 'lalal'},
        events=[],
        paused=False,
        followup_action=None,
        active_form=None,
        latest_action_name=None,
    )

    result = action_default_fallback.run(default_dispatcher, first_try, default_domain)

    total_nr_tries = result[0]['value']
    assert total_nr_tries == 1.0


def test_run_subsequent(action_default_fallback, default_dispatcher, default_domain):

    subsequent_tries = Tracker(
        sender_id="c9er45css2923",
        slots={"total_nr_tries": 1.0},
        latest_message={'text': 'covid'},
        events=[],
        paused=False,
        followup_action=None,
        active_form=None,
        latest_action_name=None,
    )

    result = action_default_fallback.run(default_dispatcher, subsequent_tries, default_domain)
    print(result)
    total_nr_tries = result[0]['value']
    assert total_nr_tries == 0.0
