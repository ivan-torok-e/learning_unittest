import os
import sys
sys.path.append(os.getcwd())
import unittest
from unittest import TestCase, mock
import source.envs as envs


class test_envs(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.env_patcher = mock.patch.dict(os.environ, {
            "ZENDESK_API_KEY": "ZENDESK_API_KEY_VALUE"
            ,"JIRA_API_KEY": "JIRA_API_KEY_VALUE"
            ,"ZENDESK_API_USER": "ZENDESK_API_USER_VALUE"
            ,"JIRA_API_USER": "JIRA_API_USER_VALUE"
            ,"ZENDESK_URL": "ZENDESK_URL_VALUE"
            ,"JIRA_URL": "JIRA_URL_VALUE"
            ,"THIRD_EMAILS": "THIRD_EMAILS_VALUE"
            ,"THIRD_IDS_IN_JIRA": "THIRD_IDS_IN_JIRA_VALUE"
            ,"SEARCH_IN_JIRA": "SEARCH_IN_JIRA_VALUE"
            ,"APP_ENV": "APP_ENV_VALUE"
            })
        cls.env_patcher.start()

        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

        cls.env_patcher.stop()

    def setUp(self):
        super().setUp()
        self.assertEqual(os.environ["ZENDESK_API_KEY"], "ZENDESK_API_KEY_VALUE")
        self.assertEqual(os.environ["JIRA_API_KEY"], "JIRA_API_KEY_VALUE")
        self.assertEqual(os.environ["ZENDESK_API_USER"], "ZENDESK_API_USER_VALUE")
        self.assertEqual(os.environ["JIRA_API_USER"], "JIRA_API_USER_VALUE")
        self.assertEqual(os.environ["ZENDESK_URL"], "ZENDESK_URL_VALUE")
        self.assertEqual(os.environ["JIRA_URL"], "JIRA_URL_VALUE")
        self.assertEqual(os.environ["THIRD_EMAILS"], "THIRD_EMAILS_VALUE")
        self.assertEqual(os.environ["THIRD_IDS_IN_JIRA"], "THIRD_IDS_IN_JIRA_VALUE")
        self.assertEqual(os.environ["SEARCH_IN_JIRA"], "SEARCH_IN_JIRA_VALUE")
        self.assertEqual(os.environ["APP_ENV"], "APP_ENV_VALUE")
        

    def test_envs_get_api_zendesk(self):
        self.assertEqual(envs.get_api('zendesk'), 'ZENDESK_API_KEY_VALUE')

    def test_envs_get_api_jira(self):
        self.assertEqual(envs.get_api('jira'), 'JIRA_API_KEY_VALUE')

    def test_envs_get_api_else(self):
        self.assertEqual(envs.get_api(''), 0)




    # def test_envs_get_api_jira(self):
    #     self.assertEqual(envs.get_api('jira','zendesk'), 'JIRA_API_KEY_VALUE')

    # def test_envs_get_api_(self):
    #     self.assertEqual(envs.get_api(''), 0)



    def test_envs_get_api_user_zendesk(self):
        self.assertEqual(envs.get_api_user('zendesk'), 'ZENDESK_API_USER_VALUE')

    def test_envs_get_api_user_jira(self):
        self.assertEqual(envs.get_api_user('jira'), 'JIRA_API_USER_VALUE')

    def test_envs_get_api_user_else(self):
        self.assertEqual(envs.get_api_user(''), 0)



    def test_envs_get_url_zendesk(self):
        self.assertEqual(envs.get_url('zendesk'), 'https://ZENDESK_URL_VALUE')

    def test_envs_get_url_jira(self):
        self.assertEqual(envs.get_url('jira'), 'https://JIRA_URL_VALUE')

    def test_envs_get_url_else(self):
        self.assertEqual(envs.get_url(''), 0)



    def test_envs_get_email_addresses_of_3rd_level_support_zendesk(self):
        self.assertEqual(envs.get_email_addresses_of_3rd_level_support(), 'THIRD_EMAILS_VALUE')

    # def test_envs_get_email_addresses_of_3rd_level_support_jira(self):
    #     self.assertEqual(envs.get_email_addresses_of_3rd_level_support('jira'), 'JIRA_API_KEY_VALUE')

    # def test_envs_get_email_addresses_of_3rd_level_support_else(self):
    #     self.assertEqual(envs.get_email_addresses_of_3rd_level_support(''), 0)



    def test_envs_get_jira_id_of_3rd_level_support_zendesk(self):
        self.assertEqual(envs.get_jira_id_of_3rd_level_support(), 'THIRD_IDS_IN_JIRA_VALUE')

    # def test_envs_get_jira_id_of_3rd_level_support_jira(self):
    #     self.assertEqual(envs.get_jira_id_of_3rd_level_support('jira'), 'JIRA_API_KEY_VALUE')

    # def test_envs_get_jira_id_of_3rd_level_support_else(self):
    #     self.assertEqual(envs.get_jira_id_of_3rd_level_support(''), 0)



    def test_envs_get_jira_search_terms_zendesk(self):
        self.assertEqual(envs.get_jira_search_terms(), 'SEARCH:IN:JIRA:VALUE')

    # def test_envs_get_jira_search_terms_jira(self):
    #     self.assertEqual(envs.get_jira_search_terms('jira'), 'JIRA_API_KEY_VALUE')

    # def test_envs_get_jira_search_terms_else(self):
    #     self.assertEqual(envs.get_jira_search_terms(''), 0)



    def test_envs_get_environment_zendesk(self):
        self.assertEqual(envs.get_environment(), 'APP_ENV_VALUE')

    # def test_envs_get_environment_jira(self):
    #     self.assertEqual(envs.get_environment('jira'), 'JIRA_API_KEY_VALUE')

    # def test_envs_get_environment_else(self):
    #     self.assertEqual(envs.get_environment(''), 0)

if __name__ == '__main__':
    unittest.main()