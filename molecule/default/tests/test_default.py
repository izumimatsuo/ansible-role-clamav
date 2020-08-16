import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_clamav_is_installed(host):
    package = host.package('clamav')
    assert package.is_installed
    assert package.version.startswith("0.102")


def test_clamd_running_and_enabled(host):
    service = host.service('clamd@scan')
    assert service.is_running
    assert service.is_enabled
