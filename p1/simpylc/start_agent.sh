#!/usr/bin/env bash

export LIBGL_ALLOW_SOFTWARE=1
(cd simulations/car/control_client; python ./driving_agent_jan.py)