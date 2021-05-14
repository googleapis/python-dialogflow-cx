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
import proto  # type: ignore

from google.protobuf import duration_pb2  # type: ignore
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.dialogflow.cx.v3",
    manifest={
        "Experiment",
        "VersionVariants",
        "VariantsHistory",
        "ListExperimentsRequest",
        "ListExperimentsResponse",
        "GetExperimentRequest",
        "CreateExperimentRequest",
        "UpdateExperimentRequest",
        "DeleteExperimentRequest",
        "StartExperimentRequest",
        "StopExperimentRequest",
    },
)


class Experiment(proto.Message):
    r"""Represents an experiment in an environment.
    Attributes:
        name (str):
            The name of the experiment.
            Format: projects/<Project
            ID>/locations/<Location ID>/agents/<Agent
            ID>/environments/<Environment
            ID>/experiments/<Experiment ID>..
        display_name (str):
            Required. The human-readable name of the
            experiment (unique in an environment). Limit of
            64 characters.
        description (str):
            The human-readable description of the
            experiment.
        state (google.cloud.dialogflowcx_v3.types.Experiment.State):
            The current state of the experiment.
            Transition triggered by
            Expriments.StartExperiment: PENDING->RUNNING.
            Transition triggered by
            Expriments.CancelExperiment: PENDING->CANCELLED
            or RUNNING->CANCELLED.
        definition (google.cloud.dialogflowcx_v3.types.Experiment.Definition):
            The definition of the experiment.
        result (google.cloud.dialogflowcx_v3.types.Experiment.Result):
            Inference result of the experiment.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Creation time of this experiment.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Start time of this experiment.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            End time of this experiment.
        last_update_time (google.protobuf.timestamp_pb2.Timestamp):
            Last update time of this experiment.
        experiment_length (google.protobuf.duration_pb2.Duration):
            Maximum number of days to run the
            experiment/rollout. If auto-rollout is not
            enabled, default value and maximum will be 30
            days. If auto-rollout is enabled, default value
            and maximum will be 6 days.
        variants_history (Sequence[google.cloud.dialogflowcx_v3.types.VariantsHistory]):
            The history of updates to the experiment
            variants.
    """

    class State(proto.Enum):
        r"""The state of the experiment."""
        STATE_UNSPECIFIED = 0
        DRAFT = 1
        RUNNING = 2
        DONE = 3

    class Definition(proto.Message):
        r"""Definition of the experiment.
        Attributes:
            condition (str):
                The condition defines which subset of sessions are selected
                for this experiment. If not specified, all sessions are
                eligible. E.g. "query_input.language_code=en" See the
                `conditions
                reference <https://cloud.google.com/dialogflow/cx/docs/reference/condition>`__.
            version_variants (google.cloud.dialogflowcx_v3.types.VersionVariants):
                The flow versions as the variants of this
                experiment.
        """

        condition = proto.Field(proto.STRING, number=1,)
        version_variants = proto.Field(
            proto.MESSAGE, number=2, oneof="variants", message="VersionVariants",
        )

    class Result(proto.Message):
        r"""The inference result which includes an objective metric to
        optimize and the confidence interval.

        Attributes:
            version_metrics (Sequence[google.cloud.dialogflowcx_v3.types.Experiment.Result.VersionMetrics]):
                Version variants and metrics.
            last_update_time (google.protobuf.timestamp_pb2.Timestamp):
                The last time the experiment's stats data was
                updated. Will have default value if stats have
                never been computed for this experiment.
        """

        class MetricType(proto.Enum):
            r"""Types of ratio-based metric for Dialogflow experiment."""
            METRIC_UNSPECIFIED = 0
            CONTAINED_SESSION_NO_CALLBACK_RATE = 1
            LIVE_AGENT_HANDOFF_RATE = 2
            CALLBACK_SESSION_RATE = 3
            ABANDONED_SESSION_RATE = 4
            SESSION_END_RATE = 5

        class CountType(proto.Enum):
            r"""Types of count-based metric for Dialogflow experiment."""
            COUNT_TYPE_UNSPECIFIED = 0
            TOTAL_NO_MATCH_COUNT = 1
            TOTAL_TURN_COUNT = 2
            AVERAGE_TURN_COUNT = 3

        class ConfidenceInterval(proto.Message):
            r"""A confidence interval is a range of possible values for the
            experiment objective you are trying to measure.

            Attributes:
                confidence_level (float):
                    The confidence level used to construct the
                    interval, i.e. there is X% chance that the true
                    value is within this interval.
                ratio (float):
                    The percent change between an experiment
                    metric's value and the value for its control.
                lower_bound (float):
                    Lower bound of the interval.
                upper_bound (float):
                    Upper bound of the interval.
            """

            confidence_level = proto.Field(proto.DOUBLE, number=1,)
            ratio = proto.Field(proto.DOUBLE, number=2,)
            lower_bound = proto.Field(proto.DOUBLE, number=3,)
            upper_bound = proto.Field(proto.DOUBLE, number=4,)

        class Metric(proto.Message):
            r"""Metric and corresponding confidence intervals.
            Attributes:
                type_ (google.cloud.dialogflowcx_v3.types.Experiment.Result.MetricType):
                    Ratio-based metric type. Only one of type or count_type is
                    specified in each Metric.
                count_type (google.cloud.dialogflowcx_v3.types.Experiment.Result.CountType):
                    Count-based metric type. Only one of type or count_type is
                    specified in each Metric.
                ratio (float):
                    Ratio value of a metric.
                count (float):
                    Count value of a metric.
                confidence_interval (google.cloud.dialogflowcx_v3.types.Experiment.Result.ConfidenceInterval):
                    The probability that the treatment is better
                    than all other treatments in the experiment
            """

            type_ = proto.Field(
                proto.ENUM, number=1, enum="Experiment.Result.MetricType",
            )
            count_type = proto.Field(
                proto.ENUM, number=5, enum="Experiment.Result.CountType",
            )
            ratio = proto.Field(proto.DOUBLE, number=2, oneof="value",)
            count = proto.Field(proto.DOUBLE, number=4, oneof="value",)
            confidence_interval = proto.Field(
                proto.MESSAGE, number=3, message="Experiment.Result.ConfidenceInterval",
            )

        class VersionMetrics(proto.Message):
            r"""Version variant and associated metrics.
            Attributes:
                version (str):
                    The name of the flow
                    [Version][google.cloud.dialogflow.cx.v3.Version]. Format:
                    ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/flows/<Flow ID>/versions/<Version ID>``.
                metrics (Sequence[google.cloud.dialogflowcx_v3.types.Experiment.Result.Metric]):
                    The metrics and corresponding confidence
                    intervals in the inference result.
                session_count (int):
                    Number of sessions that were allocated to
                    this version.
            """

            version = proto.Field(proto.STRING, number=1,)
            metrics = proto.RepeatedField(
                proto.MESSAGE, number=2, message="Experiment.Result.Metric",
            )
            session_count = proto.Field(proto.INT32, number=3,)

        version_metrics = proto.RepeatedField(
            proto.MESSAGE, number=1, message="Experiment.Result.VersionMetrics",
        )
        last_update_time = proto.Field(
            proto.MESSAGE, number=2, message=timestamp_pb2.Timestamp,
        )

    name = proto.Field(proto.STRING, number=1,)
    display_name = proto.Field(proto.STRING, number=2,)
    description = proto.Field(proto.STRING, number=3,)
    state = proto.Field(proto.ENUM, number=4, enum=State,)
    definition = proto.Field(proto.MESSAGE, number=5, message=Definition,)
    result = proto.Field(proto.MESSAGE, number=6, message=Result,)
    create_time = proto.Field(proto.MESSAGE, number=7, message=timestamp_pb2.Timestamp,)
    start_time = proto.Field(proto.MESSAGE, number=8, message=timestamp_pb2.Timestamp,)
    end_time = proto.Field(proto.MESSAGE, number=9, message=timestamp_pb2.Timestamp,)
    last_update_time = proto.Field(
        proto.MESSAGE, number=10, message=timestamp_pb2.Timestamp,
    )
    experiment_length = proto.Field(
        proto.MESSAGE, number=11, message=duration_pb2.Duration,
    )
    variants_history = proto.RepeatedField(
        proto.MESSAGE, number=12, message="VariantsHistory",
    )


class VersionVariants(proto.Message):
    r"""A list of flow version variants.
    Attributes:
        variants (Sequence[google.cloud.dialogflowcx_v3.types.VersionVariants.Variant]):
            A list of flow version variants.
    """

    class Variant(proto.Message):
        r"""A single flow version with specified traffic allocation.
        Attributes:
            version (str):
                The name of the flow version. Format:
                ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/flows/<Flow ID>/versions/<Version ID>``.
            traffic_allocation (float):
                Percentage of the traffic which should be
                routed to this version of flow. Traffic
                allocation for a single flow must sum up to 1.0.
            is_control_group (bool):
                Whether the variant is for the control group.
        """

        version = proto.Field(proto.STRING, number=1,)
        traffic_allocation = proto.Field(proto.FLOAT, number=2,)
        is_control_group = proto.Field(proto.BOOL, number=3,)

    variants = proto.RepeatedField(proto.MESSAGE, number=1, message=Variant,)


class VariantsHistory(proto.Message):
    r"""The history of variants update.
    Attributes:
        version_variants (google.cloud.dialogflowcx_v3.types.VersionVariants):
            The flow versions as the variants.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Update time of the variants.
    """

    version_variants = proto.Field(
        proto.MESSAGE, number=1, oneof="variants", message="VersionVariants",
    )
    update_time = proto.Field(proto.MESSAGE, number=2, message=timestamp_pb2.Timestamp,)


class ListExperimentsRequest(proto.Message):
    r"""The request message for
    [Experiments.ListExperiments][google.cloud.dialogflow.cx.v3.Experiments.ListExperiments].

    Attributes:
        parent (str):
            Required. The
            [Environment][google.cloud.dialogflow.cx.v3.Environment] to
            list all environments for. Format:
            ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/environments/<Environment ID>``.
        page_size (int):
            The maximum number of items to return in a
            single page. By default 20 and at most 100.
        page_token (str):
            The next_page_token value returned from a previous list
            request.
    """

    parent = proto.Field(proto.STRING, number=1,)
    page_size = proto.Field(proto.INT32, number=2,)
    page_token = proto.Field(proto.STRING, number=3,)


class ListExperimentsResponse(proto.Message):
    r"""The response message for
    [Experiments.ListExperiments][google.cloud.dialogflow.cx.v3.Experiments.ListExperiments].

    Attributes:
        experiments (Sequence[google.cloud.dialogflowcx_v3.types.Experiment]):
            The list of experiments. There will be a maximum number of
            items returned based on the page_size field in the request.
            The list may in some cases be empty or contain fewer entries
            than page_size even if this isn't the last page.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    experiments = proto.RepeatedField(proto.MESSAGE, number=1, message="Experiment",)
    next_page_token = proto.Field(proto.STRING, number=2,)


class GetExperimentRequest(proto.Message):
    r"""The request message for
    [Experiments.GetExperiment][google.cloud.dialogflow.cx.v3.Experiments.GetExperiment].

    Attributes:
        name (str):
            Required. The name of the
            [Environment][google.cloud.dialogflow.cx.v3.Environment].
            Format:
            ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/environments/<Environment ID>/experiments/<Experiment ID>``.
    """

    name = proto.Field(proto.STRING, number=1,)


class CreateExperimentRequest(proto.Message):
    r"""The request message for
    [Experiments.CreateExperiment][google.cloud.dialogflow.cx.v3.Experiments.CreateExperiment].

    Attributes:
        parent (str):
            Required. The [Agent][google.cloud.dialogflow.cx.v3.Agent]
            to create an
            [Environment][google.cloud.dialogflow.cx.v3.Environment]
            for. Format:
            ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/environments/<Environment ID>``.
        experiment (google.cloud.dialogflowcx_v3.types.Experiment):
            Required. The experiment to create.
    """

    parent = proto.Field(proto.STRING, number=1,)
    experiment = proto.Field(proto.MESSAGE, number=2, message="Experiment",)


class UpdateExperimentRequest(proto.Message):
    r"""The request message for
    [Experiments.UpdateExperiment][google.cloud.dialogflow.cx.v3.Experiments.UpdateExperiment].

    Attributes:
        experiment (google.cloud.dialogflowcx_v3.types.Experiment):
            Required. The experiment to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The mask to control which fields
            get updated.
    """

    experiment = proto.Field(proto.MESSAGE, number=1, message="Experiment",)
    update_mask = proto.Field(
        proto.MESSAGE, number=2, message=field_mask_pb2.FieldMask,
    )


class DeleteExperimentRequest(proto.Message):
    r"""The request message for
    [Experiments.DeleteExperiment][google.cloud.dialogflow.cx.v3.Experiments.DeleteExperiment].

    Attributes:
        name (str):
            Required. The name of the
            [Environment][google.cloud.dialogflow.cx.v3.Environment] to
            delete. Format:
            ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/environments/<Environment ID>/experiments/<Experiment ID>``.
    """

    name = proto.Field(proto.STRING, number=1,)


class StartExperimentRequest(proto.Message):
    r"""The request message for
    [Experiments.StartExperiment][google.cloud.dialogflow.cx.v3.Experiments.StartExperiment].

    Attributes:
        name (str):
            Required. Resource name of the experiment to start. Format:
            ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/environments/<Environment ID>/experiments/<Experiment ID>``.
    """

    name = proto.Field(proto.STRING, number=1,)


class StopExperimentRequest(proto.Message):
    r"""The request message for
    [Experiments.StopExperiment][google.cloud.dialogflow.cx.v3.Experiments.StopExperiment].

    Attributes:
        name (str):
            Required. Resource name of the experiment to stop. Format:
            ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/environments/<Environment ID>/experiments/<Experiment ID>``.
    """

    name = proto.Field(proto.STRING, number=1,)


__all__ = tuple(sorted(__protobuf__.manifest))
