tchfile_role
=========

Роль для создания текстовых файлов.

Requirements
------------

None

Role Variables
--------------

filename: "" - Полный путь создаваемого файла.
content: "" - Содержимое файла, если требуется.

Dependencies
------------

None

Example Playbook
----------------
```yaml
    - hosts: servers
      roles:
         - tchfile_role
```

License
-------

BSD

Author Information
------------------

https://github.com/Nb3l77eo
