==========
Mars Rover
==========


Solution for `EventMobi engineering code test`_.


Quick start
-----------

.. code-block:: bash

    $ git clone https://github.com/pv8/marsrover
    $ cd marsrover
    $ pip install .
    $ rover

Then type the instructions:

.. code-block:: bash

    Plateau:5 5
    Rover1 Landing:1 2 N
    Rover1 Instructions:LMLMLMLMM
    Rover2 Landing:3 3 E
    Rover2 Instructions:MMRMMRMRRM

*Note*: It's recommended to install inside a virtualenv_.

The instructions can be in a file (i.e. ``input.txt``) and its content redirect to ``stdin``:

.. code-block:: bash

    $ rover < input.txt

.. code-block:: bash

    $ cat input.txt | rover

With Docker_, build the image:

.. code-block:: bash

    $ docker build -t rover .

And run with helper script ``run.sh``:

.. code-block:: bash

    $ ./run.sh rover < input.txt



Development environment
-----------------------

Running tests
~~~~~~~~~~~~~

* With Docker_:

Build the image:

.. code-block:: bash

    $ docker build -t rover .

Then run with the helper script ``run.sh``

.. code-block:: bash

    $ ./run.sh tests

* Without Docker:

Install the development requirements:

.. code-block:: bash

    (marsrover)$ pip install -r requirements_dev.txt

Then run with pytest_:

.. code-block:: bash

    (marsrover)$ pytest --cov-report term-missing --cov=.

Debugging
~~~~~~~~~

Include the ipdb_ breakpoint (``import ipdb; ipdb.set_trace()``) and run:

* With Docker:

.. code-block:: bash

    $ ./run.sh tests

* Without Docker:

.. code-block:: bash

    $ (marsrover)$ pytest -s

Linting
~~~~~~~

* With Docker:

.. code-block:: bash

    $ ./run.sh pep8

* Without Docker:

.. code-block:: bash

    $ (marsrover)$ flake8 --statistics .


.. _`Python 3`: https://www.python.org/downloads/release/python-364/
.. _Docker: https://docs.docker.com/install/
.. _`EventMobi engineering code test`: https://github.com/abdulg/Mars-Rover
.. _virtualenv: https://virtualenv.pypa.io/en/stable/
.. _pytest: https://docs.pytest.org/en/latest/
.. _ipdb: https://github.com/gotcha/ipdb


License
-------

MIT
