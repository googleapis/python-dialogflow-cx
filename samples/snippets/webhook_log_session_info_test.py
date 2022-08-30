# Copyright 2022, Google LLC
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Test validate form parameter webhook snippet."""

import flask
import pytest

from webhook_log_session_info import log_session_info_for_troubleshooting


@pytest.fixture(name="app", scope="module")
def fixture_app():
    """Flask fixture to pass a flask.Request to the test function"""
    return flask.Flask(__name__)


def test_log_session_info_for_troubleshooting(app):
    """Parameterized test for validate form parameter webhook snippet."""

    # session components
    project = "test_project"
    location = "us-central1"
    agent_id = "000000f0-f000-00b0-0000-af00d0e00000"
    session_id = "d0bdaa0c-0d00-0000-b0eb-b00b0db000b0"
    environment = "0d0000f0-0aac-0d0c-0a00-b00b0000a000"

    # build session uris
    session_prefix = f"projects/{project}/locations/{location}/agents/{agent_id}"
    session = f"{session_prefix}/sessions/{session_id}"
    env_session = f"{session_prefix}/environments/{environment}/sessions/{session_id}"

    # session without environment path
    request = {"sessionInfo": {"session": session}}
    with app.test_request_context(json=request):
        res = log_session_info_for_troubleshooting(flask.request)
        assert session_id in str(res)

    # session with environment path
    request = {"sessionInfo": {"session": env_session}}
    with app.test_request_context(json=request):
        res = log_session_info_for_troubleshooting(flask.request)
        assert session_id in str(res)
