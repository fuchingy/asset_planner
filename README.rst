Asset Planner
======

The Asset Planner.


Build docker
----

::

    $ cd docker
    $ docker build -t "asset_planner:1.0.0" .


Run docker
----

::

    docker run --rm --privileged=true -it -p 8051:8050 -v asset_planner:/tmp/asset_planner asset_planner:1.0.0
    bash /tmp/launch_app.sh

Open http://localhost:8051 in a browser.
