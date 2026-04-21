from behave import given, when, then

@when('users send a POST request to /{name}')
def step_impl(context, name):
    context.their_job = context.browser.get(context.base_url + "/" + name)
    assert context.their_job != None

@then("it returns {name}'s job: {job}")
def step_impl(context, name, job):
    assert context.their_job == job
