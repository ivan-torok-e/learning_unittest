import os

def get_api(whichOne):
    if whichOne == 'zendesk':
        return os.getenv('ZENDESK_API_KEY')
    elif whichOne == 'jira':
        return os.getenv('JIRA_API_KEY')
    else:
        return 0


def get_api_user(whichOne):
    if whichOne == 'zendesk':
        return os.getenv('ZENDESK_API_USER')
    elif whichOne == 'jira':
        return os.getenv('JIRA_API_USER')
    else:
        return 0

def get_url(whichOne):
    if whichOne == 'zendesk':
        return 'https://' + os.getenv('ZENDESK_URL')
    elif whichOne == 'jira':
        return 'https://' + os.getenv('JIRA_URL')
    else:
        return 0


def get_email_addresses_of_3rd_level_support():
    return os.getenv('THIRD_EMAILS')

def get_jira_id_of_3rd_level_support():
    return os.getenv('THIRD_IDS_IN_JIRA')


def get_jira_search_terms():
    return os.getenv('SEARCH_IN_JIRA').replace('_',':')

def get_environment():
    return os.getenv('APP_ENV')

# this is a comment