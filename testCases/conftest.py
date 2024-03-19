from selenium import webdriver
import pytest
import pytest_html
import pytest_metadata


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge")
    else:
        driver = webdriver.Firefox()
        print("Launching firefox by default")
    return driver


def pytest_addoption(parser):  # This will get the value  from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()  # This will return the browser value to setup method
def browser(request):
    return request.config.getoption("--browser")


#########pytest html report ##########

# It is hook for adding Environment info to HTML Report
def pytest_configure(config):
    metadata=config.pluginmanager.getplugin("metadata")
    if metadata:
        from pytest_metadata.plugin import metadata_key
        config.stash[metadata_key]['Project Name'] = 'nop Commerce'
        config.stash[metadata_key]['Module Name'] = 'Customer'
        config.stash[metadata_key]['Tester'] = 'Sumathi'


# It is hook for deleting/modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
