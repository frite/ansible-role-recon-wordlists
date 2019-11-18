import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_git_exists(host):
    """ Assert git is installed. """
    f = host.exists('git')

    assert f.exists


def test_wordlist_path_exists(host):
    """ Assert wordlist path exists """
    custom_dir = host.file('/usr/local/share/wordlists/')

    assert custom_dir.exists
    assert custom_dir.is_directory
    assert custom_dir.user == 'root'
    assert custom_dir.group == 'root'
    assert oct(custom_dir.mode) == '0o755'


def test_SecLists_path_exists(host):
    """ Assert wordlist path exists """
    custom_dir = host.file('/usr/local/share/wordlists/SecLists')

    assert custom_dir.exists
    assert custom_dir.is_directory


def test_fuzzdb_path_exists(host):
    """ Assert wordlist path exists """
    custom_dir = host.file('/usr/local/share/wordlists/fuzzdb')

    assert custom_dir.exists
    assert custom_dir.is_directory
