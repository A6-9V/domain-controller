import sys
import unittest
from unittest.mock import MagicMock, patch

# Mock requests before importing manage_cloudflare
# This is necessary because requests is not installed in the environment
mock_requests = MagicMock()
mock_requests.exceptions.RequestException = type('RequestException', (Exception,), {})
sys.modules['requests'] = mock_requests

import manage_cloudflare

class TestManageCloudflare(unittest.TestCase):
    def setUp(self):
        self.zone_id = "test_zone_id"
        self.api_token = "test_token"
        # Reset mocks before each test
        mock_requests.reset_mock()
        mock_requests.patch.side_effect = None
        mock_requests.get.side_effect = None
        mock_requests.post.side_effect = None

    def test_get_headers(self):
        headers = manage_cloudflare.get_headers(self.api_token)
        self.assertEqual(headers["Authorization"], f"Bearer {self.api_token}")
        self.assertEqual(headers["Content-Type"], "application/json")

    def test_get_security_level_success(self):
        mock_response = MagicMock()
        mock_response.json.return_value = {"success": True, "result": {"value": "medium"}}
        mock_requests.get.return_value = mock_response

        result = manage_cloudflare.get_security_level(self.zone_id, self.api_token)

        self.assertEqual(result, "medium")
        mock_requests.get.assert_called_once()

    def test_get_security_level_api_error(self):
        mock_response = MagicMock()
        mock_response.json.return_value = {"success": False, "errors": [{"message": "error"}]}
        mock_requests.get.return_value = mock_response

        result = manage_cloudflare.get_security_level(self.zone_id, self.api_token)

        self.assertIsNone(result)

    def test_get_security_level_exception(self):
        mock_requests.get.side_effect = mock_requests.exceptions.RequestException("Network error")

        result = manage_cloudflare.get_security_level(self.zone_id, self.api_token)

        self.assertIsNone(result)

    def test_set_security_level_success(self):
        mock_response = MagicMock()
        mock_response.json.return_value = {"success": True, "result": {"value": "high"}}
        mock_requests.patch.return_value = mock_response

        result = manage_cloudflare.set_security_level(self.zone_id, self.api_token, "high")

        self.assertTrue(result)
        # Verify the call to requests.patch
        expected_url = f"{manage_cloudflare.BASE_URL}/zones/{self.zone_id}/settings/security_level"
        expected_headers = manage_cloudflare.get_headers(self.api_token)
        expected_payload = {"value": "high"}

        mock_requests.patch.assert_called_once_with(
            expected_url,
            headers=expected_headers,
            json=expected_payload
        )
        mock_response.raise_for_status.assert_called_once()

    def test_set_security_level_invalid_level(self):
        result = manage_cloudflare.set_security_level(self.zone_id, self.api_token, "invalid_level")
        self.assertFalse(result)
        mock_requests.patch.assert_not_called()

    def test_set_security_level_api_error(self):
        mock_response = MagicMock()
        mock_response.json.return_value = {"success": False, "errors": [{"message": "error"}]}
        mock_requests.patch.return_value = mock_response

        result = manage_cloudflare.set_security_level(self.zone_id, self.api_token, "high")

        self.assertFalse(result)
        mock_response.raise_for_status.assert_called_once()

    def test_set_security_level_exception(self):
        # This addresses the missing error test: set_security_level (RequestException)
        mock_requests.patch.side_effect = mock_requests.exceptions.RequestException("Network error")

        result = manage_cloudflare.set_security_level(self.zone_id, self.api_token, "high")

        self.assertFalse(result)

    def test_list_dns_records_success(self):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "success": True,
            "result": [
                {"type": "A", "name": "example.com", "content": "1.2.3.4", "id": "123"}
            ]
        }
        mock_requests.get.return_value = mock_response

        result = manage_cloudflare.list_dns_records(self.zone_id, self.api_token)

        self.assertTrue(result)
        mock_requests.get.assert_called_once()

    def test_list_dns_records_api_error(self):
        mock_response = MagicMock()
        mock_response.json.return_value = {"success": False, "errors": [{"message": "error"}]}
        mock_requests.get.return_value = mock_response

        result = manage_cloudflare.list_dns_records(self.zone_id, self.api_token)

        self.assertFalse(result)

    def test_list_dns_records_exception(self):
        mock_requests.get.side_effect = mock_requests.exceptions.RequestException("Network error")

        result = manage_cloudflare.list_dns_records(self.zone_id, self.api_token)

        self.assertFalse(result)

    @patch('os.environ.get')
    def test_load_config(self, mock_env_get):
        def side_effect(key, default=None):
            env = {
                "CLOUDFLARE_ZONE_ID_LENGKUNDEE": "zone_leng",
                "CLOUDFLARE_ZONE_ID_GENXFX": "zone_genx",
                "CLOUDFLARE_ACCOUNT_ID": "acc_id",
                "CLOUDFLARE_API_TOKEN": "api_tok"
            }
            return env.get(key, default)

        mock_env_get.side_effect = side_effect

        config = manage_cloudflare.load_config()

        self.assertEqual(config["zones"]["lengkundee01.org"], "zone_leng")
        self.assertEqual(config["zones"]["genxfx.org"], "zone_genx")
        self.assertEqual(config["account_id"], "acc_id")
        self.assertEqual(config["api_token"], "api_tok")

if __name__ == '__main__':
    unittest.main()
