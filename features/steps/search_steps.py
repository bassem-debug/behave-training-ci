import time

from behave import then,given,when
from numpy.testing import assert_equal
from selenium import webdriver
from selenium.webdriver import ActionChains


@given(u'the user navigates to the PyPi Home page')
def step_impl(context):

    context.browser.get("https://qavbox.github.io/demo/dragndrop/")
    assert "DragnDrop" in context.browser.title

@when(u'he search for "behave"')
def step_impl(context):

    time.sleep(2)
    context.hp.drag_and_dop()
    time.sleep(2)
@then(u'he see a search result "behave 1.2.5"')
def step_impl(context):

    time.sleep(2)
    print(context.hp.return_target_message())
    assert_equal("Dropped!",context.hp.return_target_message())
