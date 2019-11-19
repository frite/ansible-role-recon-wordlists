Role Name
=========

[![Build Status](https://api.travis-ci.com/frite/ansible-role-recon-wordlists.svg?branch=master)](https://travis-ci.com/frite/ansible-role-recon-wordlist)
Ansible role that installs wordlists.

Requirements
------------

It requires:
* `frite.recon_package_manager`. Can be installed using `ansible-galaxy frite.recon_package_manager`.

Role Variables
--------------

The only variable you will need is 
`wordlists`.

```
wordlists:
- name: 'SecLists'
  url: 'https://github.com/danielmiessler/SecLists.git' 
- name: 'fuzzdb'
 url: 'https://github.com/fuzzdb-project/fuzzdb/'
 ```
 
 If you don't set up any variables, SecLists and Fuzzdb are going to be installed in `/usr/share/local/wordlists/`

Dependencies
------------

It requires:
* `frite.recon_package_manager`. Can be installed using `ansible-galaxy frite.recon_package_manager`.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: ansible-role-recon-wordlists, wordlists: - name: 'blahblah', url: 'https://bluhbluh'}

License
-------

BSD

Author Information
------------------

e best way to reach out to me is through GH issues or ping me at [twitter](https://twitter.com/fr1t3).
