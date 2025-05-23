salt-ext-relenv
===============

A Salt extension for managing relocatable Python environments via [relenv](https://relenv.readthedocs.io/en/latest/usage.html).  
Provides both an execution module (`relenv.*`) and a state module (`relenv.*`) that wrap native `pip` and `virtualenv` functionality to create, update, and remove “relenv” environments.

Features
--------

- **Execution module** (`relenv.fetch`, `relenv.toolchain`, `relenv.create`)
  - Fetch relenv build tools and C toolchains
  - Create a fully relocatable Python virtual environment
  - Optional cross‐architecture and Python‐version parameters
- **State module** (`relenv.installed`, `relenv.removed`, `relenv.uptodate`, `relenv.managed`, `relenv.absent`)
  - Install or remove packages inside a relenv
  - Ensure a relenv is up to date
  - Wraps Salt’s `virtualenv` state to invoke `relenv.create` under the hood
  - Purge entire relenv directories

Requirements
------------

- SaltStack ≥ 3000
- Python 3.10+
- The [`relenv`](https://pypi.org/project/relenv/) Python package available on master and minions

Installation
------------

1. **Clone** this repository onto your Salt master (or distribute to minions):

   .. code-block:: bash

    salt \* pip.install salt-ext-relenv

2. **Sync** your custom modules and states:

   .. code-block:: bash

      salt '*' saltutil.sync_modules
      salt '*' saltutil.sync_states

3. **Verify** the relenv modules are available:

   .. code-block:: bash

      salt '*' sys.list_modules | grep relenv
      salt '*' sys.list_states  | grep relenv

Execution Module Usage
----------------------

**Fetch build tools** (downloads relenv wheel and helpers):

.. code-block:: bash

   salt '*' relenv.fetch arch=amd64 python=3.10.17

**Fetch C toolchain** (for building C extensions):

.. code-block:: bash

   salt '*' relenv.toolchain arch=amd64 clean=True crosstool_only=True

**Create a relenv** (must run fetch & toolchain first; ownership optional):

.. code-block:: bash

   salt '*' relenv.create /opt/my_relenv arch=amd64 python=3.10.17 user=deploy

State Module Usage
------------------

**Manage a relenv directory** (wraps virtualenv.managed to use relenv.create):

.. code-block:: yaml

   create_myenv:
     relenv.managed:
       - name: /opt/my_relenv
       - arch: amd64
       - python: 3.10.17
       - user: deploy

**Install a package** into an existing relenv:

.. code-block:: yaml

   install_requests:
     relenv.installed:
       - name: requests
       - relenv: /opt/my_relenv
       - require:
         - relenv: create_myenv

**Remove a package** from a relenv:

.. code-block:: yaml

   remove_requests:
     relenv.removed:
       - name: requests
       - relenv: /opt/my_relenv

**Ensure relenv is up to date** (upgrade pip & dependencies):

.. code-block:: yaml

   update_relenv:
     relenv.uptodate:
       - name: /opt/my_relenv

**Remove a relenv entirely**:

.. code-block:: yaml

   delete_myenv:
     relenv.absent:
       - name: /opt/my_relenv

Development
-----------

1. **Install** dev dependencies:

   .. code-block:: bash

      pip install -r requirements/tests.txt

2. **Test**:

   .. code-block:: bash

      pytest

3. **Lint**:

   .. code-block:: bash

      flake8
      mypy

Contributing
------------

1. Fork the repository and create a feature branch.  
2. Write tests under `tests/` for new behavior.  
3. Submit a Pull Request against `main`, referencing any related issues.

License
-------

Apache License 2.0 – see the bundled `LICENSE` file for details.  
