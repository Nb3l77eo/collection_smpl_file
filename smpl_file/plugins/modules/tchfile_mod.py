#!/usr/bin/python

# Copyright: (c) 2018, https://github.com/Nb3l77eo
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
from fileinput import filename
from tabnanny import check
__metaclass__ = type

DOCUMENTATION = r'''
---
module: tchfile_mod

short_description: This is my test module to create file

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "0.0.1"

description: Simply file creator.

options:
    filename:
        description: full path file to crate.
        required: true
        type: str
    content:
        description:
            - Content you want add to file.
        required: false
        type: str
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
# extends_documentation_fragment:
#     - my_namespace.my_collection.my_doc_fragment_name

author:
    - https://github.com/Nb3l77eo
'''

EXAMPLES = r'''
# Pass in a message
- name: Create file with no content at /tmp/test.txt
  tchfile:
    filename: "/tmp/test.txt"

# pass in a message and have changed true
- name: Create gile with test content at /tmp/content.txt
  tchfile:
    filename: "/tmp/content.txt"
    content: "some\ncontent"

# fail the module
# - name: Test failure of the module
#   my_namespace.my_collection.my_test:
#     name: fail me
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
# original_message:
#     description: The original name param that was passed in.
#     type: str
#     returned: always
#     sample: 'hello world'
# message:
#     description: The output message that the test module generates.
#     type: str
#     returned: always
#     sample: 'goodbye'
'''

from ansible.module_utils.basic import AnsibleModule
import os.path


def run_module():
    module_args = dict(
        filename=dict(type='str', required=True),
        content=dict(type='str', required=False)
    )


    result = dict(
        changed=False,
        original_message='',
        message=''
    )


    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if os.path.exists(module.params['filename']):
        result = dict(
            changed=False,
            original_message=module.params['filename'],
            message='File already exists'
        )

    else:
        file=open(module.params['filename'],"w+")
        if bool(module.params['content']) is True:
            file.write(module.params['content'])
        file.close()
        result = dict(
            changed=True,
            original_message=module.params['filename'],
            message='Created'
        )
        # result['original_message'] = module.params['filename']
        # result['message'] = 'Created'


    if module.check_mode:
        module.exit_json(**result)





    # if module.params['new']:
    #     result['changed'] = True


    # if module.params['name'] == 'fail me':
    #     module.fail_json(msg='You requested this to fail', **result)


    module.exit_json(**result)



def main():
    run_module()



if __name__ == '__main__':
    main()