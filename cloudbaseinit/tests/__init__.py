import sys
import unittest.mock as mock


sys.modules["ctypes"] = mock.MagicMock()
sys.modules["ctypes.wintypes"] = mock.MagicMock()

sys.modules["ctypes.windll"] = mock.MagicMock()
sys.modules["ctypes.windll.advapi32"] = mock.MagicMock()
sys.modules["ctypes.windll.crypt32"] = mock.MagicMock()
sys.modules["ctypes.windll.kernel32"] = mock.MagicMock()
