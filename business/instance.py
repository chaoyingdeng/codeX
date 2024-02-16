from business.sfe.sfe_manage import SFeManage
from business.mdm.mdm_manage import MdmManage


class Instance:
    def __init__(self, driver):
        self.sfe = SFeManage(driver)
        self.mdm = MdmManage(driver)
