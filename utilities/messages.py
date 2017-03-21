__author__ = 'anna'

#finding elements
#info
template_default = ' Locator_type: {}, locator: {}'
template_send_keys = ' Locator_type: {}, locator: {}, keys: {}'
def element_found_message(locator_type, locator):
    return 'Element found.'+ template_default.format(locator_type, locator)
def element_not_found_message(locator_type, locator):
    return 'Element not found.' +template_default.format(locator_type, locator)
def element_clicked_message(locator_type, locator):
    return 'Clicked on element.'+ template_default.format(locator_type, locator)
def element_not_clicked_message(locator_type, locator):
    return 'Cannot click on element.' + template_default.format(locator_type, locator)
def element_send_keys_message(locator_type, locator, keys):
    return 'Send keys to the element.' + template_send_keys.format(locator_type, locator, keys)
def element_cannot_send_keys_message(locator_type, locator, keys):
    return 'Cannot send keys to the element.' + template_send_keys.format(locator_type, locator, keys)
def element_appeared_message(locator_type, locator):
    return 'Element appeared on the page.' + template_default.format(locator_type, locator)
def element_not_appeared_message(locator_type, locator):
    return 'Element not appeared on the page.' + template_default.format(locator_type, locator)

def waiting_message(locator_type, locator, timeout):
    return 'Waiting explicitly for maximum {} seconds for element to be clickable.'.format(timeout)

# errors
def locator_error_message(locator_type):
    return 'Locator type {} not correct/ not supported.'.format(locator_type)




#verification
#info
def verification_successful_message(test_name):
    return '### {}: VERIFICATION SUCCESSFUL.'.format(test_name)
def test_successful_message(test_funk_name):
    return '### {}: TEST SUCCESSFUL.'.format(test_funk_name)

#errors
def verification_failed_message(test_name):
    return '### {}: VERIFICATION FAILED.'.format(test_name)
def exception_occurred_message(test_name):
    return '### {}: EXCEPTION OCCURRED.'.format(test_name)
def test_failed_message(test_funk_name):
    return '### {}: TEST FAILED.'.format(test_funk_name)
def test_cannot_collect_message(test_funk_name):
    return '### {}: TEST CANNOT COLLECT.'.format(test_funk_name)

#screenshots
def screenshot_saved_message(test_name, destination_file):
    return '{}: Screenshot saved to directory: {}'.format(test_name, destination_file)


def screenshot_exception_occurred_message(test_name, destination_file):
    return '### {}: EXCEPTION OCCURRED when taking screenshot. {}'.format(test_name, destination_file)







