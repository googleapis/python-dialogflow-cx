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
import proto  # type: ignore

from google.cloud.dialogflowcx_v3beta1.types import flow as gcdc_flow
from google.cloud.dialogflowcx_v3beta1.types import intent as gcdc_intent
from google.cloud.dialogflowcx_v3beta1.types import page as gcdc_page
from google.cloud.dialogflowcx_v3beta1.types import response_message
from google.cloud.dialogflowcx_v3beta1.types import session
from google.cloud.dialogflowcx_v3beta1.types import transition_route_group
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import struct_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
from google.rpc import status_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.dialogflow.cx.v3beta1",
    manifest={
        "TestResult",
        "TestCase",
        "TestCaseResult",
        "TestConfig",
        "ConversationTurn",
        "TestRunDifference",
        "TransitionCoverage",
        "TransitionRouteGroupCoverage",
        "IntentCoverage",
        "CalculateCoverageRequest",
        "CalculateCoverageResponse",
        "ListTestCasesRequest",
        "ListTestCasesResponse",
        "BatchDeleteTestCasesRequest",
        "CreateTestCaseRequest",
        "UpdateTestCaseRequest",
        "GetTestCaseRequest",
        "RunTestCaseRequest",
        "RunTestCaseResponse",
        "RunTestCaseMetadata",
        "BatchRunTestCasesRequest",
        "BatchRunTestCasesResponse",
        "BatchRunTestCasesMetadata",
        "TestError",
        "ImportTestCasesRequest",
        "ImportTestCasesResponse",
        "ImportTestCasesMetadata",
        "TestCaseError",
        "ExportTestCasesRequest",
        "ExportTestCasesResponse",
        "ExportTestCasesMetadata",
        "ListTestCaseResultsRequest",
        "ListTestCaseResultsResponse",
        "GetTestCaseResultRequest",
    },
)


class TestResult(proto.Enum):
    r"""The test result for a test case and an agent environment."""
    TEST_RESULT_UNSPECIFIED = 0
    PASSED = 1
    FAILED = 2


class TestCase(proto.Message):
    r"""Represents a test case.

    Attributes:
        name (str):
            The unique identifier of the test case.
            [TestCases.CreateTestCase][google.cloud.dialogflow.cx.v3beta1.TestCases.CreateTestCase]
            will populate the name automatically. Otherwise use format:
            ``projects/<Project ID>/locations/<LocationID>/agents/ <AgentID>/testCases/<TestCase ID>``.
        tags (Sequence[str]):
            Tags are short descriptions that users may
            apply to test cases for organizational and
            filtering purposes. Each tag should start with
            "#" and has a limit of 30 characters.
        display_name (str):
            Required. The human-readable name of the test
            case, unique within the agent. Limit of 200
            characters.
        notes (str):
            Additional freeform notes about the test
            case. Limit of 400 characters.
        test_config (google.cloud.dialogflowcx_v3beta1.types.TestConfig):
            Config for the test case.
        test_case_conversation_turns (Sequence[google.cloud.dialogflowcx_v3beta1.types.ConversationTurn]):
            The conversation turns uttered when the test
            case was created, in chronological order. These
            include the canonical set of agent utterances
            that should occur when the agent is working
            properly.
        creation_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the test was created.
        last_test_result (google.cloud.dialogflowcx_v3beta1.types.TestCaseResult):
            The latest test result.
    """

    name = proto.Field(proto.STRING, number=1,)
    tags = proto.RepeatedField(proto.STRING, number=2,)
    display_name = proto.Field(proto.STRING, number=3,)
    notes = proto.Field(proto.STRING, number=4,)
    test_config = proto.Field(proto.MESSAGE, number=13, message="TestConfig",)
    test_case_conversation_turns = proto.RepeatedField(
        proto.MESSAGE, number=5, message="ConversationTurn",
    )
    creation_time = proto.Field(
        proto.MESSAGE, number=10, message=timestamp_pb2.Timestamp,
    )
    last_test_result = proto.Field(proto.MESSAGE, number=12, message="TestCaseResult",)


class TestCaseResult(proto.Message):
    r"""Represents a result from running a test case in an agent
    environment.

    Attributes:
        name (str):
            The resource name for the test case result. Format:
            ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/testCases/ <TestCase ID>/results/<TestCaseResult ID>``.
        environment (str):
            Environment where the test was run. If not
            set, it indicates the draft environment.
        conversation_turns (Sequence[google.cloud.dialogflowcx_v3beta1.types.ConversationTurn]):
            The conversation turns uttered during the
            test case replay in chronological order.
        test_result (google.cloud.dialogflowcx_v3beta1.types.TestResult):
            Whether the test case passed in the agent
            environment.
        test_time (google.protobuf.timestamp_pb2.Timestamp):
            The time that the test was run.
    """

    name = proto.Field(proto.STRING, number=1,)
    environment = proto.Field(proto.STRING, number=2,)
    conversation_turns = proto.RepeatedField(
        proto.MESSAGE, number=3, message="ConversationTurn",
    )
    test_result = proto.Field(proto.ENUM, number=4, enum="TestResult",)
    test_time = proto.Field(proto.MESSAGE, number=5, message=timestamp_pb2.Timestamp,)


class TestConfig(proto.Message):
    r"""Represents configurations for a test case.

    Attributes:
        tracking_parameters (Sequence[str]):
            Session parameters to be compared when
            calculating differences.
        flow (str):
            Flow name. If not set, default start flow is assumed.
            Format:
            ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/flows/<Flow ID>``.
    """

    tracking_parameters = proto.RepeatedField(proto.STRING, number=1,)
    flow = proto.Field(proto.STRING, number=2,)


class ConversationTurn(proto.Message):
    r"""One interaction between a human and virtual agent. The human
    provides some input and the virtual agent provides a response.

    Attributes:
        user_input (google.cloud.dialogflowcx_v3beta1.types.ConversationTurn.UserInput):
            The user input.
        virtual_agent_output (google.cloud.dialogflowcx_v3beta1.types.ConversationTurn.VirtualAgentOutput):
            The virtual agent output.
    """

    class UserInput(proto.Message):
        r"""The input from the human user.

        Attributes:
            input (google.cloud.dialogflowcx_v3beta1.types.QueryInput):
                Supports [text
                input][google.cloud.dialogflow.cx.v3beta1.QueryInput.text],
                [event
                input][google.cloud.dialogflow.cx.v3beta1.QueryInput.event],
                [dtmf
                input][google.cloud.dialogflow.cx.v3beta1.QueryInput.dtmf]
                in the test case.
            injected_parameters (google.protobuf.struct_pb2.Struct):
                Parameters that need to be injected into the
                conversation during intent detection.
            is_webhook_enabled (bool):
                If webhooks should be allowed to trigger in
                response to the user utterance. Often if
                parameters are injected, webhooks should not be
                enabled.
            enable_sentiment_analysis (bool):
                Whether sentiment analysis is enabled.
        """

        input = proto.Field(proto.MESSAGE, number=5, message=session.QueryInput,)
        injected_parameters = proto.Field(
            proto.MESSAGE, number=2, message=struct_pb2.Struct,
        )
        is_webhook_enabled = proto.Field(proto.BOOL, number=3,)
        enable_sentiment_analysis = proto.Field(proto.BOOL, number=7,)

    class VirtualAgentOutput(proto.Message):
        r"""The output from the virtual agent.

        Attributes:
            session_parameters (google.protobuf.struct_pb2.Struct):
                The session parameters available to the bot
                at this point.
            differences (Sequence[google.cloud.dialogflowcx_v3beta1.types.TestRunDifference]):
                Output only. If this is part of a [result conversation
                turn][TestCaseResult.conversation_turns], the list of
                differences between the original run and the replay for this
                output, if any.
            diagnostic_info (google.protobuf.struct_pb2.Struct):
                Required. Input only. The diagnostic
                [info][Session.DetectIntentResponse.QueryResult.diagnostic_info]
                output for the turn. Required to calculate the testing
                coverage.
            triggered_intent (google.cloud.dialogflowcx_v3beta1.types.Intent):
                The [Intent][google.cloud.dialogflow.cx.v3beta1.Intent] that
                triggered the response. Only name and displayName will be
                set.
            current_page (google.cloud.dialogflowcx_v3beta1.types.Page):
                The [Page][google.cloud.dialogflow.cx.v3beta1.Page] on which
                the utterance was spoken. Only name and displayName will be
                set.
            text_responses (Sequence[google.cloud.dialogflowcx_v3beta1.types.ResponseMessage.Text]):
                The
                [text][google.cloud.dialogflow.cx.v3beta1.ResponseMessage.Text]
                responses from the agent for the turn.
            status (google.rpc.status_pb2.Status):
                Response error from the agent in the test
                result. If set, other output is empty.
        """

        session_parameters = proto.Field(
            proto.MESSAGE, number=4, message=struct_pb2.Struct,
        )
        differences = proto.RepeatedField(
            proto.MESSAGE, number=5, message="TestRunDifference",
        )
        diagnostic_info = proto.Field(
            proto.MESSAGE, number=6, message=struct_pb2.Struct,
        )
        triggered_intent = proto.Field(
            proto.MESSAGE, number=7, message=gcdc_intent.Intent,
        )
        current_page = proto.Field(proto.MESSAGE, number=8, message=gcdc_page.Page,)
        text_responses = proto.RepeatedField(
            proto.MESSAGE, number=9, message=response_message.ResponseMessage.Text,
        )
        status = proto.Field(proto.MESSAGE, number=10, message=status_pb2.Status,)

    user_input = proto.Field(proto.MESSAGE, number=1, message=UserInput,)
    virtual_agent_output = proto.Field(
        proto.MESSAGE, number=2, message=VirtualAgentOutput,
    )


class TestRunDifference(proto.Message):
    r"""The description of differences between original and replayed
    agent output.

    Attributes:
        type_ (google.cloud.dialogflowcx_v3beta1.types.TestRunDifference.DiffType):
            The type of diff.
        description (str):
            A description of the diff, showing the actual
            output vs expected output.
    """

    class DiffType(proto.Enum):
        r"""What part of the message replay differs from the test case."""
        DIFF_TYPE_UNSPECIFIED = 0
        INTENT = 1
        PAGE = 2
        PARAMETERS = 3
        UTTERANCE = 4

    type_ = proto.Field(proto.ENUM, number=1, enum=DiffType,)
    description = proto.Field(proto.STRING, number=2,)


class TransitionCoverage(proto.Message):
    r"""Transition coverage represents the percentage of all possible
    page transitions (page-level transition routes and event
    handlers, excluding transition route groups) present within any
    of a parent's test cases.

    Attributes:
        transitions (Sequence[google.cloud.dialogflowcx_v3beta1.types.TransitionCoverage.Transition]):
            The list of Transitions present in the agent.
        coverage_score (float):
            The percent of transitions in the agent that
            are covered.
    """

    class TransitionNode(proto.Message):
        r"""The source or target of a transition.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            page (google.cloud.dialogflowcx_v3beta1.types.Page):
                Indicates a transition to a
                [Page][google.cloud.dialogflow.cx.v3beta1.Page]. Only some
                fields such as name and displayname will be set.

                This field is a member of `oneof`_ ``kind``.
            flow (google.cloud.dialogflowcx_v3beta1.types.Flow):
                Indicates a transition to a
                [Flow][google.cloud.dialogflow.cx.v3beta1.Flow]. Only some
                fields such as name and displayname will be set.

                This field is a member of `oneof`_ ``kind``.
        """

        page = proto.Field(
            proto.MESSAGE, number=1, oneof="kind", message=gcdc_page.Page,
        )
        flow = proto.Field(
            proto.MESSAGE, number=2, oneof="kind", message=gcdc_flow.Flow,
        )

    class Transition(proto.Message):
        r"""A transition in a page.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            source (google.cloud.dialogflowcx_v3beta1.types.TransitionCoverage.TransitionNode):
                The start node of a transition.
            index (int):
                The index of a transition in the transition
                list. Starting from 0.
            target (google.cloud.dialogflowcx_v3beta1.types.TransitionCoverage.TransitionNode):
                The end node of a transition.
            covered (bool):
                Whether or not the transition is covered by
                at least one of the agent's test cases.
            transition_route (google.cloud.dialogflowcx_v3beta1.types.TransitionRoute):
                Intent route or condition route.

                This field is a member of `oneof`_ ``detail``.
            event_handler (google.cloud.dialogflowcx_v3beta1.types.EventHandler):
                Event handler.

                This field is a member of `oneof`_ ``detail``.
        """

        source = proto.Field(
            proto.MESSAGE, number=1, message="TransitionCoverage.TransitionNode",
        )
        index = proto.Field(proto.INT32, number=4,)
        target = proto.Field(
            proto.MESSAGE, number=2, message="TransitionCoverage.TransitionNode",
        )
        covered = proto.Field(proto.BOOL, number=3,)
        transition_route = proto.Field(
            proto.MESSAGE, number=5, oneof="detail", message=gcdc_page.TransitionRoute,
        )
        event_handler = proto.Field(
            proto.MESSAGE, number=6, oneof="detail", message=gcdc_page.EventHandler,
        )

    transitions = proto.RepeatedField(proto.MESSAGE, number=1, message=Transition,)
    coverage_score = proto.Field(proto.FLOAT, number=2,)


class TransitionRouteGroupCoverage(proto.Message):
    r"""Transition route group coverage represents the percentage of
    all possible transition routes present within any of a parent's
    test cases. The results are grouped by the transition route
    group.

    Attributes:
        coverages (Sequence[google.cloud.dialogflowcx_v3beta1.types.TransitionRouteGroupCoverage.Coverage]):
            Transition route group coverages.
        coverage_score (float):
            The percent of transition routes in all the
            transition route groups that are covered.
    """

    class Coverage(proto.Message):
        r"""Coverage result message for one transition route group.

        Attributes:
            route_group (google.cloud.dialogflowcx_v3beta1.types.TransitionRouteGroup):
                Transition route group metadata. Only name
                and displayName will be set.
            transitions (Sequence[google.cloud.dialogflowcx_v3beta1.types.TransitionRouteGroupCoverage.Coverage.Transition]):
                The list of transition routes and coverage in
                the transition route group.
            coverage_score (float):
                The percent of transition routes in the
                transition route group that are covered.
        """

        class Transition(proto.Message):
            r"""A transition coverage in a transition route group.

            Attributes:
                transition_route (google.cloud.dialogflowcx_v3beta1.types.TransitionRoute):
                    Intent route or condition route.
                covered (bool):
                    Whether or not the transition route is
                    covered by at least one of the agent's test
                    cases.
            """

            transition_route = proto.Field(
                proto.MESSAGE, number=1, message=gcdc_page.TransitionRoute,
            )
            covered = proto.Field(proto.BOOL, number=2,)

        route_group = proto.Field(
            proto.MESSAGE,
            number=1,
            message=transition_route_group.TransitionRouteGroup,
        )
        transitions = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="TransitionRouteGroupCoverage.Coverage.Transition",
        )
        coverage_score = proto.Field(proto.FLOAT, number=3,)

    coverages = proto.RepeatedField(proto.MESSAGE, number=1, message=Coverage,)
    coverage_score = proto.Field(proto.FLOAT, number=2,)


class IntentCoverage(proto.Message):
    r"""Intent coverage represents the percentage of all possible
    intents in the agent that are triggered in any of a parent's
    test cases.

    Attributes:
        intents (Sequence[google.cloud.dialogflowcx_v3beta1.types.IntentCoverage.Intent]):
            The list of Intents present in the agent
        coverage_score (float):
            The percent of intents in the agent that are
            covered.
    """

    class Intent(proto.Message):
        r"""The agent's intent.

        Attributes:
            intent (str):
                The intent full resource name
            covered (bool):
                Whether or not the intent is covered by at
                least one of the agent's test cases.
        """

        intent = proto.Field(proto.STRING, number=1,)
        covered = proto.Field(proto.BOOL, number=2,)

    intents = proto.RepeatedField(proto.MESSAGE, number=1, message=Intent,)
    coverage_score = proto.Field(proto.FLOAT, number=2,)


class CalculateCoverageRequest(proto.Message):
    r"""The request message for
    [TestCases.CalculateCoverage][google.cloud.dialogflow.cx.v3beta1.TestCases.CalculateCoverage].

    Attributes:
        agent (str):
            Required. The agent to calculate coverage for. Format:
            ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>``.
        type_ (google.cloud.dialogflowcx_v3beta1.types.CalculateCoverageRequest.CoverageType):
            Required. The type of coverage requested.
    """

    class CoverageType(proto.Enum):
        r"""The type of coverage score requested."""
        COVERAGE_TYPE_UNSPECIFIED = 0
        INTENT = 1
        PAGE_TRANSITION = 2
        TRANSITION_ROUTE_GROUP = 3

    agent = proto.Field(proto.STRING, number=3,)
    type_ = proto.Field(proto.ENUM, number=2, enum=CoverageType,)


class CalculateCoverageResponse(proto.Message):
    r"""The response message for
    [TestCases.CalculateCoverage][google.cloud.dialogflow.cx.v3beta1.TestCases.CalculateCoverage].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        agent (str):
            The agent to calculate coverage for. Format:
            ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>``.
        intent_coverage (google.cloud.dialogflowcx_v3beta1.types.IntentCoverage):
            Intent coverage.

            This field is a member of `oneof`_ ``coverage_type``.
        transition_coverage (google.cloud.dialogflowcx_v3beta1.types.TransitionCoverage):
            Transition (excluding transition route
            groups) coverage.

            This field is a member of `oneof`_ ``coverage_type``.
        route_group_coverage (google.cloud.dialogflowcx_v3beta1.types.TransitionRouteGroupCoverage):
            Transition route group coverage.

            This field is a member of `oneof`_ ``coverage_type``.
    """

    agent = proto.Field(proto.STRING, number=5,)
    intent_coverage = proto.Field(
        proto.MESSAGE, number=2, oneof="coverage_type", message="IntentCoverage",
    )
    transition_coverage = proto.Field(
        proto.MESSAGE, number=4, oneof="coverage_type", message="TransitionCoverage",
    )
    route_group_coverage = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="coverage_type",
        message="TransitionRouteGroupCoverage",
    )


class ListTestCasesRequest(proto.Message):
    r"""The request message for
    [TestCases.ListTestCases][google.cloud.dialogflow.cx.v3beta1.TestCases.ListTestCases].

    Attributes:
        parent (str):
            Required. The agent to list all pages for. Format:
            ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>``.
        page_size (int):
            The maximum number of items to return in a
            single page. By default 20. Note that when
            TestCaseView = FULL, the maximum page size
            allowed is 20. When TestCaseView = BASIC, the
            maximum page size allowed is 500.
        page_token (str):
            The next_page_token value returned from a previous list
            request.
        view (google.cloud.dialogflowcx_v3beta1.types.ListTestCasesRequest.TestCaseView):
            Specifies whether response should include all
            fields or just the metadata.
    """

    class TestCaseView(proto.Enum):
        r"""Specifies how much test case information to include in the
        response.
        """
        TEST_CASE_VIEW_UNSPECIFIED = 0
        BASIC = 1
        FULL = 2

    parent = proto.Field(proto.STRING, number=1,)
    page_size = proto.Field(proto.INT32, number=2,)
    page_token = proto.Field(proto.STRING, number=3,)
    view = proto.Field(proto.ENUM, number=4, enum=TestCaseView,)


class ListTestCasesResponse(proto.Message):
    r"""The response message for
    [TestCases.ListTestCases][google.cloud.dialogflow.cx.v3beta1.TestCases.ListTestCases].

    Attributes:
        test_cases (Sequence[google.cloud.dialogflowcx_v3beta1.types.TestCase]):
            The list of test cases. There will be a maximum number of
            items returned based on the page_size field in the request.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    test_cases = proto.RepeatedField(proto.MESSAGE, number=1, message="TestCase",)
    next_page_token = proto.Field(proto.STRING, number=2,)


class BatchDeleteTestCasesRequest(proto.Message):
    r"""The request message for
    [TestCases.BatchDeleteTestCases][google.cloud.dialogflow.cx.v3beta1.TestCases.BatchDeleteTestCases].

    Attributes:
        parent (str):
            Required. The agent to delete test cases from. Format:
            ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>``.
        names (Sequence[str]):
            Required. Format of test case names:
            ``projects/<Project ID>/locations/ <Location ID>/agents/<AgentID>/testCases/<TestCase ID>``.
    """

    parent = proto.Field(proto.STRING, number=1,)
    names = proto.RepeatedField(proto.STRING, number=3,)


class CreateTestCaseRequest(proto.Message):
    r"""The request message for
    [TestCases.CreateTestCase][google.cloud.dialogflow.cx.v3beta1.TestCases.CreateTestCase].

    Attributes:
        parent (str):
            Required. The agent to create the test case for. Format:
            ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>``.
        test_case (google.cloud.dialogflowcx_v3beta1.types.TestCase):
            Required. The test case to create.
    """

    parent = proto.Field(proto.STRING, number=1,)
    test_case = proto.Field(proto.MESSAGE, number=2, message="TestCase",)


class UpdateTestCaseRequest(proto.Message):
    r"""The request message for
    [TestCases.UpdateTestCase][google.cloud.dialogflow.cx.v3beta1.TestCases.UpdateTestCase].

    Attributes:
        test_case (google.cloud.dialogflowcx_v3beta1.types.TestCase):
            Required. The test case to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The mask to specify which fields should be
            updated. The
            [``creationTime``][google.cloud.dialogflow.cx.v3beta1.TestCase.creation_time]
            and
            [``lastTestResult``][google.cloud.dialogflow.cx.v3beta1.TestCase.last_test_result]
            cannot be updated.
    """

    test_case = proto.Field(proto.MESSAGE, number=1, message="TestCase",)
    update_mask = proto.Field(
        proto.MESSAGE, number=2, message=field_mask_pb2.FieldMask,
    )


class GetTestCaseRequest(proto.Message):
    r"""The request message for
    [TestCases.GetTestCase][google.cloud.dialogflow.cx.v3beta1.TestCases.GetTestCase].

    Attributes:
        name (str):
            Required. The name of the testcase. Format:
            ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/testCases/<TestCase ID>``.
    """

    name = proto.Field(proto.STRING, number=1,)


class RunTestCaseRequest(proto.Message):
    r"""The request message for
    [TestCases.RunTestCase][google.cloud.dialogflow.cx.v3beta1.TestCases.RunTestCase].

    Attributes:
        name (str):
            Required. Format of test case name to run:
            ``projects/<Project ID>/locations/ <Location ID>/agents/<AgentID>/testCases/<TestCase ID>``.
        environment (str):
            Optional. Environment name. If not set, draft environment is
            assumed. Format:
            ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/environments/<Environment ID>``.
    """

    name = proto.Field(proto.STRING, number=1,)
    environment = proto.Field(proto.STRING, number=2,)


class RunTestCaseResponse(proto.Message):
    r"""The response message for
    [TestCases.RunTestCase][google.cloud.dialogflow.cx.v3beta1.TestCases.RunTestCase].

    Attributes:
        result (google.cloud.dialogflowcx_v3beta1.types.TestCaseResult):
            The result.
    """

    result = proto.Field(proto.MESSAGE, number=2, message="TestCaseResult",)


class RunTestCaseMetadata(proto.Message):
    r"""Metadata returned for the
    [TestCases.RunTestCase][google.cloud.dialogflow.cx.v3beta1.TestCases.RunTestCase]
    long running operation. This message currently has no fields.

    """


class BatchRunTestCasesRequest(proto.Message):
    r"""The request message for
    [TestCases.BatchRunTestCases][google.cloud.dialogflow.cx.v3beta1.TestCases.BatchRunTestCases].

    Attributes:
        parent (str):
            Required. Agent name. Format:
            ``projects/<Project ID>/locations/<Location ID>/agents/ <AgentID>``.
        environment (str):
            Optional. If not set, draft environment is assumed. Format:
            ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/environments/<Environment ID>``.
        test_cases (Sequence[str]):
            Required. Format:
            ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/testCases/<TestCase ID>``.
    """

    parent = proto.Field(proto.STRING, number=1,)
    environment = proto.Field(proto.STRING, number=2,)
    test_cases = proto.RepeatedField(proto.STRING, number=3,)


class BatchRunTestCasesResponse(proto.Message):
    r"""The response message for
    [TestCases.BatchRunTestCases][google.cloud.dialogflow.cx.v3beta1.TestCases.BatchRunTestCases].

    Attributes:
        results (Sequence[google.cloud.dialogflowcx_v3beta1.types.TestCaseResult]):
            The test case results. The detailed [conversation
            turns][google.cloud.dialogflow.cx.v3beta1.TestCaseResult.conversation_turns]
            are empty in this response.
    """

    results = proto.RepeatedField(proto.MESSAGE, number=1, message="TestCaseResult",)


class BatchRunTestCasesMetadata(proto.Message):
    r"""Metadata returned for the
    [TestCases.BatchRunTestCases][google.cloud.dialogflow.cx.v3beta1.TestCases.BatchRunTestCases]
    long running operation.

    Attributes:
        errors (Sequence[google.cloud.dialogflowcx_v3beta1.types.TestError]):
            The test errors.
    """

    errors = proto.RepeatedField(proto.MESSAGE, number=1, message="TestError",)


class TestError(proto.Message):
    r"""Error info for running a test.

    Attributes:
        test_case (str):
            The test case resource name.
        status (google.rpc.status_pb2.Status):
            The status associated with the test.
        test_time (google.protobuf.timestamp_pb2.Timestamp):
            The timestamp when the test was completed.
    """

    test_case = proto.Field(proto.STRING, number=1,)
    status = proto.Field(proto.MESSAGE, number=2, message=status_pb2.Status,)
    test_time = proto.Field(proto.MESSAGE, number=3, message=timestamp_pb2.Timestamp,)


class ImportTestCasesRequest(proto.Message):
    r"""The request message for
    [TestCases.ImportTestCases][google.cloud.dialogflow.cx.v3beta1.TestCases.ImportTestCases].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. The agent to import test cases to. Format:
            ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>``.
        gcs_uri (str):
            The `Google Cloud
            Storage <https://cloud.google.com/storage/docs/>`__ URI to
            import test cases from. The format of this URI must be
            ``gs://<bucket-name>/<object-name>``.

            This field is a member of `oneof`_ ``source``.
        content (bytes):
            Uncompressed raw byte content for test cases.

            This field is a member of `oneof`_ ``source``.
    """

    parent = proto.Field(proto.STRING, number=1,)
    gcs_uri = proto.Field(proto.STRING, number=2, oneof="source",)
    content = proto.Field(proto.BYTES, number=3, oneof="source",)


class ImportTestCasesResponse(proto.Message):
    r"""The response message for
    [TestCases.ImportTestCases][google.cloud.dialogflow.cx.v3beta1.TestCases.ImportTestCases].

    Attributes:
        names (Sequence[str]):
            The unique identifiers of the new test cases. Format:
            ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/testCases/<TestCase ID>``.
    """

    names = proto.RepeatedField(proto.STRING, number=1,)


class ImportTestCasesMetadata(proto.Message):
    r"""Metadata returned for the
    [TestCases.ImportTestCases][google.cloud.dialogflow.cx.v3beta1.TestCases.ImportTestCases]
    long running operation.

    Attributes:
        errors (Sequence[google.cloud.dialogflowcx_v3beta1.types.TestCaseError]):
            Errors for failed test cases.
    """

    errors = proto.RepeatedField(proto.MESSAGE, number=1, message="TestCaseError",)


class TestCaseError(proto.Message):
    r"""Error info for importing a test.

    Attributes:
        test_case (google.cloud.dialogflowcx_v3beta1.types.TestCase):
            The test case.
        status (google.rpc.status_pb2.Status):
            The status associated with the test case.
    """

    test_case = proto.Field(proto.MESSAGE, number=1, message="TestCase",)
    status = proto.Field(proto.MESSAGE, number=2, message=status_pb2.Status,)


class ExportTestCasesRequest(proto.Message):
    r"""The request message for
    [TestCases.ExportTestCases][google.cloud.dialogflow.cx.v3beta1.TestCases.ExportTestCases].


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. The agent where to export test cases from. Format:
            ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>``.
        gcs_uri (str):
            The `Google Cloud
            Storage <https://cloud.google.com/storage/docs/>`__ URI to
            export the test cases to. The format of this URI must be
            ``gs://<bucket-name>/<object-name>``. If unspecified, the
            serialized test cases is returned inline.

            This field is a member of `oneof`_ ``destination``.
        data_format (google.cloud.dialogflowcx_v3beta1.types.ExportTestCasesRequest.DataFormat):
            The data format of the exported test cases. If not
            specified, ``BLOB`` is assumed.
        filter (str):
            The filter expression used to filter exported test cases,
            see `API Filtering <https://aip.dev/160>`__. The expression
            is case insensitive and supports the following syntax:

            name = [OR name = ] ...

            For example:

            -  "name = t1 OR name = t2" matches the test case with the
               exact resource name "t1" or "t2".
    """

    class DataFormat(proto.Enum):
        r"""Data format of the exported test cases."""
        DATA_FORMAT_UNSPECIFIED = 0
        BLOB = 1
        JSON = 2

    parent = proto.Field(proto.STRING, number=1,)
    gcs_uri = proto.Field(proto.STRING, number=2, oneof="destination",)
    data_format = proto.Field(proto.ENUM, number=3, enum=DataFormat,)
    filter = proto.Field(proto.STRING, number=4,)


class ExportTestCasesResponse(proto.Message):
    r"""The response message for
    [TestCases.ExportTestCases][google.cloud.dialogflow.cx.v3beta1.TestCases.ExportTestCases].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_uri (str):
            The URI to a file containing the exported test cases. This
            field is populated only if ``gcs_uri`` is specified in
            [ExportTestCasesRequest][google.cloud.dialogflow.cx.v3beta1.ExportTestCasesRequest].

            This field is a member of `oneof`_ ``destination``.
        content (bytes):
            Uncompressed raw byte content for test cases.

            This field is a member of `oneof`_ ``destination``.
    """

    gcs_uri = proto.Field(proto.STRING, number=1, oneof="destination",)
    content = proto.Field(proto.BYTES, number=2, oneof="destination",)


class ExportTestCasesMetadata(proto.Message):
    r"""Metadata returned for the
    [TestCases.ExportTestCases][google.cloud.dialogflow.cx.v3beta1.TestCases.ExportTestCases]
    long running operation. This message currently has no fields.

    """


class ListTestCaseResultsRequest(proto.Message):
    r"""The request message for
    [TestCases.ListTestCaseResults][google.cloud.dialogflow.cx.v3beta1.TestCases.ListTestCaseResults].

    Attributes:
        parent (str):
            Required. The test case to list results for. Format:
            ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/ testCases/<TestCase ID>``.
            Specify a ``-`` as a wildcard for TestCase ID to list
            results across multiple test cases.
        page_size (int):
            The maximum number of items to return in a
            single page. By default 100 and at most 1000.
        page_token (str):
            The next_page_token value returned from a previous list
            request.
        filter (str):
            The filter expression used to filter test case results. See
            `API Filtering <https://aip.dev/160>`__.

            The expression is case insensitive. Only 'AND' is supported
            for logical operators. The supported syntax is listed below
            in detail:

             [AND ] ... [AND latest]

            The supported fields and operators are: field operator
            ``environment`` ``=``, ``IN`` (Use value ``draft`` for draft
            environment) ``test_time`` ``>``, ``<``

            ``latest`` only returns the latest test result in all
            results for each test case.

            Examples:

            -  "environment=draft AND latest" matches the latest test
               result for each test case in the draft environment.
            -  "environment IN (e1,e2)" matches any test case results
               with an environment resource name of either "e1" or "e2".
            -  "test_time > 1602540713" matches any test case results
               with test time later than a unix timestamp in seconds
               1602540713.
    """

    parent = proto.Field(proto.STRING, number=1,)
    page_size = proto.Field(proto.INT32, number=2,)
    page_token = proto.Field(proto.STRING, number=3,)
    filter = proto.Field(proto.STRING, number=4,)


class ListTestCaseResultsResponse(proto.Message):
    r"""The response message for
    [TestCases.ListTestCaseResults][google.cloud.dialogflow.cx.v3beta1.TestCases.ListTestCaseResults].

    Attributes:
        test_case_results (Sequence[google.cloud.dialogflowcx_v3beta1.types.TestCaseResult]):
            The list of test case results.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    test_case_results = proto.RepeatedField(
        proto.MESSAGE, number=1, message="TestCaseResult",
    )
    next_page_token = proto.Field(proto.STRING, number=2,)


class GetTestCaseResultRequest(proto.Message):
    r"""The request message for
    [TestCases.GetTestCaseResult][google.cloud.dialogflow.cx.v3beta1.TestCases.GetTestCaseResult].

    Attributes:
        name (str):
            Required. The name of the testcase. Format:
            ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/testCases/<TestCase ID>/results/<TestCaseResult ID>``.
    """

    name = proto.Field(proto.STRING, number=1,)


__all__ = tuple(sorted(__protobuf__.manifest))
