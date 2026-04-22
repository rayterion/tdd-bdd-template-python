from behave import given, when, then

@when('users send a GET request to /{name}')
def step_impl(context, name):
    context.browser.get(context.base_url + "/" + name)
    context.their_job = context.browser.find_element("tag name", "body").text
    assert context.their_job != None

@then("it returns {name}'s job: {job}")
def step_impl(context, name, job):
    print("one %s two %s" %(job, context.their_job))
    assert context.their_job == job
