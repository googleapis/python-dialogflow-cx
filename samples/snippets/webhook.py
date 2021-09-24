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

# [START dialogflow_cx_webhook]

def handleWebhook(request):

    req = request.get_json()

    tag = req["fulfillmentInfo"]["tag"]

    if tag == "Default Welcome Intent":
        # You can also use the google.cloud.dialogflowcx_v3.types.WebhookRequest protos instead of manually writing the json object
        res = {
            "fulfillment_response": {
                "messages": [{"text": {"text": ["Hi from a GCF Webhook"]}}]
            }
        }
    elif tag == "get-name":
        res = {
            "fulfillment_response": {
                "messages": [{"text": {"text": ["My name is Phlowhook"]}}]
            }
        }
    else:
        res = {
            "fulfillment_response": {
                "messages": [
                    {
                        "text": {
                            "text": [
                                f"There are no fulfillment responses defined for {tag} tag"
                            ]
                        }
                    }
                ]
            }
        }

    # Returns json
    return res


# [END dialogflow_cx_webhook]
