from test.helper import *
from test.fixtures import *


def test_add(daemon_setup):
    command_factory('pause')
    response = send_command({
        'mode': 'add',
        'command': 'ls',
        'path': '/tmp',
        'status': 'queued',
        'returncode': ''
    })
    assert response['status'] == 'success'
    status = get_status()
    assert status['data'][0]['command'] == 'ls'
    assert status['data'][0]['path'] == '/tmp'
