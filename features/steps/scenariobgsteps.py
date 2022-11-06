
from behave import *
from selenium import webdriver
import time


@given('user should able to launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://in.bookmyshow.com/")
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)


@then('user should select the location')
def bengaluru(context):
    context.driver.find_element("xpath", '//input[@type="text"]').send_keys("bengaluru")


@when('user should click on the location')
def c_loc(context):
    context.driver.find_element("xpath", '//strong[text()="Bengaluru"]').click()


@then('user should able to click on events page')
def c_event(context):
    context.driver.find_element("xpath", '//a[text()="Events"]').click()
    context.driver.refresh()


@then('user should click on browse by venue')
def c_venue(context):
    context.driver.find_element("xpath", '(//div[text()="Browse by Venues"])[1]').click()


@then('user should click on art beat:bengaluru')
def art(context):
    context.driver.find_element("xpath", '//div[text()="Art Beat: Bengaluru"]').click()


@then('user should click on texture painting on canvas')
def canvas(context):
    context.driver.find_element("xpath", '//img[@alt="Texture painting on canvas"]').click()


@then('user should click on book')
def c_book(context):
    context.driver.find_element("id", "synopsis-book-button").click()


@then('user should click on add')
def c_add(context):
    context.driver.find_element("xpath", '//div[text()="Add"]').click()


@then('user should click on proceed')
def c_proceed(context):
    context.driver.find_element("id", "booking-proceed-button").click()


@when('user enter "{name}" into name textfield')
def enter_name(context, name):
    context.driver.find_element("xpath", '//input[@name="name"]').send_keys(name)


@then('user enter mobile_no "{number}" into mobile number textfield')
def mob_no(context, number):
    if isinstance(number, float):
        number = str(int(number))
    context.driver.find_element("xpath", '//input[@type="number"]').send_keys(number)


@then('user enter the email "{email}" into email textfield')
def e_mail(context, email):
    context.driver.find_element("xpath", '//input[@type="email"]').send_keys(email)
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")


@when('user should able to click on checkbox')
def c_check(context):
    time.sleep(5)
    context.driver.find_element("xpath", '//input[@type="checkbox"]').click()
    time.sleep(5)


@then('user should able to click on submit button')
def click_submit(context):
    context.driver.find_element("id", "registration-submit-button").click()


@then('user should able to click on proceed to pay')
def pay(context):
    context.driver.find_element("xpath", '//button[text()="Login to Proceed"]').click()


