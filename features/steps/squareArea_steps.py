from behave import given, when, then
from hamcrest import assert_that, equal_to

class Calculator:
    def setSideLength(self, n):
        self.n = n
    def area(self):
        return self.n * self.n

calc = Calculator()

@given("I have a square with side length 3")
def step_impl(context):
    context.square_n = 3

@when("I input its side length")
def step_impl(context):
    calc.setSideLength(context.square_n)
    context.result = calc.area()

@then("the area should be n squared (n * n) which is {expected:d}")
def step_impl(context, expected):
    assert_that(context.result, equal_to(expected))

