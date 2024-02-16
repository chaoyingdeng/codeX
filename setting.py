from pathlib import Path

# driver_path
BASE_PATH = Path(__file__).parent
CHROME_DRIVE_PATH = str(BASE_PATH / 'drivers' / 'chromedriver')
EDGE_DRIVE_PATH = str(BASE_PATH / 'drivers' / 'msedgedriver.exe')
FIREFOX_DRIVE_PATH = str(BASE_PATH / 'drivers' / 'geckodriver.exe')

# 项目
PHARMAOS_URL = 'https://test.pharmaos.com/'
USERNAME = '13193452734'
PASSWORD = 'Test123456'

# 邮件配置
SERVER = 'smtp.qq.com'
AUTH_CODE = 'rsabmlgwgcoebhfa'
SENDER = '406125295@qq.com'
RECEIVERS = '406125295@qq.com, dengchaoying18@gmail.com'