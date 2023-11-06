import sys
import unittest.mock as mock
from oslotest import mock_fixture

mock_fixture.patch_mock_module()

sys.modules["ctypes"] = mock.MagicMock()
sys.modules["ctypes.wintypes"] = mock.MagicMock()

sys.modules["ctypes.windll"] = mock.MagicMock()
sys.modules["ctypes.windll.advapi32"] = mock.MagicMock()
sys.modules["ctypes.windll.crypt32"] = mock.MagicMock()
sys.modules["ctypes.windll.kernel32"] = mock.MagicMock()
