# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for MatchIntent
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-dialogflowcx


# [START dialogflow_v3beta1_generated_Sessions_MatchIntent_sync]
from google.cloud import dialogflowcx_v3beta1


def sample_match_intent():
    # Create a client
    client = dialogflowcx_v3beta1.SessionsClient()

    # Initialize request argument(s)
    query_input = dialogflowcx_v3beta1.QueryInput()
    query_input.text.text = "text_value"
    query_input.language_code = "language_code_value"

    request = dialogflowcx_v3beta1.MatchIntentRequest(
        session="session_value",
        query_input=query_input,
    )

    # Make the request
    response = client.match_intent(request=request)

    # Handle the response
    print(response)

# [END dialogflow_v3beta1_generated_Sessions_MatchIntent_sync]