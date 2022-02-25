# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
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
# Snippet for UpdateSecuritySettings
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-dialogflowcx


# [START dialogflow_v3beta1_generated_SecuritySettingsService_UpdateSecuritySettings_async]
from google.cloud import dialogflowcx_v3beta1


async def sample_update_security_settings():
    # Create a client
    client = dialogflowcx_v3beta1.SecuritySettingsServiceAsyncClient()

    # Initialize request argument(s)
    security_settings = dialogflowcx_v3beta1.SecuritySettings()
    security_settings.retention_window_days = 2271
    security_settings.display_name = "display_name_value"

    request = dialogflowcx_v3beta1.UpdateSecuritySettingsRequest(
        security_settings=security_settings,
    )

    # Make the request
    response = await client.update_security_settings(request=request)

    # Handle the response
    print(response)

# [END dialogflow_v3beta1_generated_SecuritySettingsService_UpdateSecuritySettings_async]
