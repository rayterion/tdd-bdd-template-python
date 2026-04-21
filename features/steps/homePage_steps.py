from behave import given, when, then

@given("The website's running")
def step_impl(context):
    context.browser.get(context.base_url)
    assert context.browser.current_url == context.base_url + "/"

@when(u'The user reches the default route: /')
def step_impl(context):
    context.browser.get(context.base_url + "/")

@then(u'the website returns the home page')
def step_impl(context):
    assert context.browser.current_url == context.base_url + "/"

@then(u'the home page contains the text: {Text}')
def step_impl(context, Text):
    page_text = context.browser.page_source
    assert Text in page_text