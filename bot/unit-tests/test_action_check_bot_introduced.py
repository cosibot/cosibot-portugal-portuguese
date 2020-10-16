import pytest

from rasa.core.domain import Domain
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from bot.actions.action_check_Bot_Introduced import ActionCheckBotIntroduced


@pytest.fixture
def check_bot_introduced():
    return ActionCheckBotIntroduced()


@pytest.fixture
def default_domain():
    return Domain(
        intents={},
        entities=[],
        slots=[],
        templates={},
        action_names=["utter_pt_welcome", ],
        form_names=[],
    )


@pytest.fixture
def default_dispatcher():
    return CollectingDispatcher()


def test_name(check_bot_introduced):
    name = check_bot_introduced.name()

    assert name == "action_check_Bot_Introduced"


def test_run_slot_false(check_bot_introduced, default_dispatcher, default_domain):

    false_slot_tracker = Tracker(
        sender_id="c9er45css2923",
        slots={"bot_introduced": False},
        latest_message={},
        events=[],
        paused=False,
        followup_action=None,
        active_form=None,
        latest_action_name=None,
    )

    result = check_bot_introduced.run(default_dispatcher, false_slot_tracker, default_domain)

    bot_introduced = result[0]['value']
    followup_action = result[1]['name']
    assert bot_introduced is True
    assert followup_action == "utter_pt_welcome"


def test_run_slot_true(check_bot_introduced, default_dispatcher, default_domain):

    true_slot_tracker = Tracker(
        sender_id="c9er45css2923",
        slots={"bot_introduced": True},
        latest_message={},
        events=[],
        paused=False,
        followup_action=None,
        active_form=None,
        latest_action_name=None,
    )

    result = check_bot_introduced.run(default_dispatcher, true_slot_tracker, default_domain)

    followup_action = result[0]['name']
    assert followup_action == "utter_pt_greeting_hello"
