config = {
    "interfaces": {
        "google.cloud.dialogflow.cx.v3beta1.Versions": {
            "retry_codes": {
                "retry_policy_1_codes": ["UNAVAILABLE"],
                "no_retry_codes": [],
                "retry_policy_2_codes": ["UNAVAILABLE"],
                "no_retry_1_codes": [],
            },
            "retry_params": {
                "retry_policy_1_params": {
                    "initial_retry_delay_millis": 100,
                    "retry_delay_multiplier": 1.3,
                    "max_retry_delay_millis": 60000,
                    "initial_rpc_timeout_millis": 60000,
                    "rpc_timeout_multiplier": 1.0,
                    "max_rpc_timeout_millis": 60000,
                    "total_timeout_millis": 60000,
                },
                "retry_policy_2_params": {
                    "initial_retry_delay_millis": 100,
                    "retry_delay_multiplier": 1.3,
                    "max_retry_delay_millis": 60000,
                    "initial_rpc_timeout_millis": 220000,
                    "rpc_timeout_multiplier": 1.0,
                    "max_rpc_timeout_millis": 220000,
                    "total_timeout_millis": 220000,
                },
                "no_retry_params": {
                    "initial_retry_delay_millis": 0,
                    "retry_delay_multiplier": 0.0,
                    "max_retry_delay_millis": 0,
                    "initial_rpc_timeout_millis": 0,
                    "rpc_timeout_multiplier": 1.0,
                    "max_rpc_timeout_millis": 0,
                    "total_timeout_millis": 0,
                },
                "no_retry_1_params": {
                    "initial_retry_delay_millis": 0,
                    "retry_delay_multiplier": 0.0,
                    "max_retry_delay_millis": 0,
                    "initial_rpc_timeout_millis": 220000,
                    "rpc_timeout_multiplier": 1.0,
                    "max_rpc_timeout_millis": 220000,
                    "total_timeout_millis": 220000,
                },
            },
            "methods": {
                "ListVersions": {
                    "timeout_millis": 60000,
                    "retry_codes_name": "retry_policy_1_codes",
                    "retry_params_name": "retry_policy_1_params",
                },
                "GetVersion": {
                    "timeout_millis": 60000,
                    "retry_codes_name": "retry_policy_1_codes",
                    "retry_params_name": "retry_policy_1_params",
                },
                "CreateVersion": {
                    "timeout_millis": 60000,
                    "retry_codes_name": "retry_policy_1_codes",
                    "retry_params_name": "retry_policy_1_params",
                },
                "UpdateVersion": {
                    "timeout_millis": 60000,
                    "retry_codes_name": "retry_policy_1_codes",
                    "retry_params_name": "retry_policy_1_params",
                },
                "DeleteVersion": {
                    "timeout_millis": 60000,
                    "retry_codes_name": "retry_policy_1_codes",
                    "retry_params_name": "retry_policy_1_params",
                },
                "LoadVersion": {
                    "timeout_millis": 60000,
                    "retry_codes_name": "retry_policy_1_codes",
                    "retry_params_name": "retry_policy_1_params",
                },
            },
        }
    }
}
