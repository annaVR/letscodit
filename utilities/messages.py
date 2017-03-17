__author__ = 'anna'

#info
template_default = ' Locator_type: {}, locator: {}'
template_send_keys = ' Locator_type: {}, locator: {}, keys: {}'
def element_found_message(locator_type, locator):
    return 'Element found.'+ template_default.format(locator_type, locator)
def element_not_found_message(locator_type, locator):
    return 'Element not found.' +template_default.format(locator_type, locator)
def element_clicked(locator_type, locator):
    return 'Clicked on element.'+ template_default.format(locator_type, locator)
def element_not_clicked(locator_type, locator):
    return 'Cannot click on element.' + template_default.format(locator_type, locator)
def element_send_keys(locator_type, locator, keys):
    return 'Send keys to the element.' + template_send_keys.format(locator_type, locator, keys)
def element_not_send_keys(locator_type, locator, keys):
    return 'Cannot send keys to the element.' + template_send_keys.format(locator_type, locator, keys)
def element_appeared(locator_type, locator):
    return 'Element appeared on the page.' + template_default.format(locator_type, locator)
def element_not_appeared(locator_type, locator):
    return 'Element not appeared on the page.' + template_default.format(locator_type, locator)

def waiting_message(locator_type, locator, timeout):
    return 'Waiting explicitly for maximum {} seconds for element to be clickable.'.format(timeout)


# errors
def locator_error(locator_type):
    return 'Locator type {} not correct/ not supported'.format(locator_type)

