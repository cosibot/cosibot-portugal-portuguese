import pytest
import time

from rasa.core.domain import Domain
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from bot.actions.action_get_time import GetTimeValue


@pytest.fixture
def get_time_value():
    return GetTimeValue()


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


def test_name(get_time_value):
    name = get_time_value.name()

    assert name == "action_get_time"


def test_run(get_time_value, default_dispatcher, default_domain):

    en_tracker = Tracker(
        sender_id="c9er45css2923",
        slots={"bot_location": "en"},
        latest_message={},
        events=[],
        paused=False,
        followup_action=None,
        active_form=None,
        latest_action_name=None,
    )

    result = get_time_value.run(default_dispatcher, en_tracker, default_domain)

    bot_time = result[0]['value']
    followup_action = result[1]['name']
    assert bot_time == time.strftime("%H:%M:%S", time.localtime())
    assert followup_action == "utter_pt_features_time"
