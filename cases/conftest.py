import pytest
from business.instance import Instance
from basic.asserts import CodeXAssert
from basic.chrome_browser import ChromeBrowser
from pathlib import Path
from utils.times import Times


@pytest.fixture(name='driver', scope='session')
def driver():
    browser = ChromeBrowser().browser
    yield browser
    browser.quit()


@pytest.fixture(name='instance', scope='session')
def instance(driver):
    instance = Instance(driver)
    yield instance


@pytest.fixture(name='times', scope='session')
def times():
    return Times()


@pytest.fixture(name='codex_assert')
def codex_assert(request, driver):
    file_name = request.node.fspath

    def inner_assert(*args):
        return CodeXAssert(*args, file_name=file_name, strategy=None, driver=driver).assert_with_element()

    return inner_assert


@pytest.fixture(scope='session', autouse=True)
def clear_screenshot(times):
    """ 应该把这个函数注册成钩子函数才对,后续优化 """
    screenshots = Path(__file__).parent.parent / 'data' / 'screenshot'
    for file in screenshots.iterdir():
        if times.today not in file.name:
            file.unlink()

# -------------------------------------------------------------------------#
# pytest hooks                                                             #
# -------------------------------------------------------------------------#
#
# def pytest_configure(config):
#     """ pytest_sessionstart钩子函数实在是无法触发, 希望你后续能找到原因 清除已有截图 """
#     screenshots = Path(__file__).parent.parent / 'data' / 'screenshot'
#     for file in screenshots.iterdir():
#         if times.today not in file.name:
#             file.unlink()
