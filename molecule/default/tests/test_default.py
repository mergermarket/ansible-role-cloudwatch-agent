import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

def test_cloudwatch_agent_installed(host):
    package = host.package('amazon-cloudwatch-agent')
    assert package.is_installed


def test_cloudwatch_config_exists(host):
    f = host.file('/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json')
    assert f.exists

