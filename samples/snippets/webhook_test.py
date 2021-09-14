# Copyright 2021, Google LLC
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

"""Test webhook"""

from webhook import handleWebhook


requestJson = {
    "detectIntentResponseId": "0a190188-37e9-400a-89e3-f3e878c86916",
    "intentInfo": {
        "lastMatchedIntent": "projects/galstarter-316823/locations/us-central1/agents/0078f973-e212-4c69-a707-a6e66e3270ce/intents/00000000-0000-0000-0000-000000000000",
        "displayName": "Default Welcome Intent",
        "confidence": 1.0
    },
    "pageInfo": {
        "currentPage": "projects/galstarter-316823/locations/us-central1/agents/0078f973-e212-4c69-a707-a6e66e3270ce/flows/00000000-0000-0000-0000-000000000000/pages/START_PAGE"
    },
    "sessionInfo": {
        "session": "projects/galstarter-316823/locations/us-central1/agents/0078f973-e212-4c69-a707-a6e66e3270ce/sessions/bd38c7-398-d25-963-7c23a0533"
    },
    "fulfillmentInfo": {
        "tag": "Default Welcome Intent"
    },
    "text": "hi",
    "languageCode": "en"
}


def test_handleWebhook():
    res = handleWebhook(requestJson)

    assert "Hi from a GCF Webhook" in res
