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

from webhook_prebuilt_telecom import cxPrebuiltAgentsTelecom


@pytest.fixture(name="app", scope="module")
def fixture_app():
    """Flask fixture to pass a flask.Request to the test function"""
    return flask.Flask(__name__)


def test_validate_phoneline(app):
    """Parameterized test for validate form parameter webhook snippet."""

    request = {"fulfillmentInfo": {"tag": "validatePhoneLine"},
               "pageInfo": {"formInfo": {"parameterInfo": [{"displayName": "phone_number", "value": 5105105100}]}}}

    with app.test_request_context(json=request):
        res = cxPrebuiltAgentsTelecom(flask.request)
        print(res)
        assert (
            res["sessionInfo"]["parameters"]["phone_line_verified"] == 'true'
        )


def test_validate_cruiseplan(app):
    """Parameterized test for validate form parameter webhook snippet."""

    request = {"fulfillmentInfo": {"tag": "cruisePlanCoverage"},
               "pageInfo": {"formInfo": {"parameterInfo": [{"displayName": "destination", "value": 'mexico'}]}}}

    with app.test_request_context(json=request):
        res = cxPrebuiltAgentsTelecom(flask.request)
        print(res)
        assert (
            res["sessionInfo"]["parameters"]["port_is_covered"] == 'true'
        )
