# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Wrappers for protocol buffer enum types."""

import enum


class AudioEncoding(enum.IntEnum):
    """
    Audio encoding of the audio content sent in the conversational query
    request. Refer to the `Cloud Speech API
    documentation <https://cloud.google.com/speech-to-text/docs/basics>`__
    for more details.

    Attributes:
      AUDIO_ENCODING_UNSPECIFIED (int): Not specified.
      AUDIO_ENCODING_LINEAR_16 (int): Uncompressed 16-bit signed little-endian samples (Linear PCM).
      AUDIO_ENCODING_FLAC (int): ```FLAC`` <https://xiph.org/flac/documentation.html>`__ (Free
      Lossless Audio Codec) is the recommended encoding because it is lossless
      (therefore recognition is not compromised) and requires only about half
      the bandwidth of ``LINEAR16``. ``FLAC`` stream encoding supports 16-bit
      and 24-bit samples, however, not all fields in ``STREAMINFO`` are
      supported.
      AUDIO_ENCODING_MULAW (int): 8-bit samples that compand 14-bit audio samples using G.711 PCMU/mu-law.
      AUDIO_ENCODING_AMR (int): Adaptive Multi-Rate Narrowband codec. ``sample_rate_hertz`` must be
      8000.
      AUDIO_ENCODING_AMR_WB (int): Adaptive Multi-Rate Wideband codec. ``sample_rate_hertz`` must be
      16000.
      AUDIO_ENCODING_OGG_OPUS (int): Opus encoded audio frames in Ogg container
      (`OggOpus <https://wiki.xiph.org/OggOpus>`__). ``sample_rate_hertz``
      must be 16000.
      AUDIO_ENCODING_SPEEX_WITH_HEADER_BYTE (int): Although the use of lossy encodings is not recommended, if a very
      low bitrate encoding is required, ``OGG_OPUS`` is highly preferred over
      Speex encoding. The `Speex <https://speex.org/>`__ encoding supported by
      Dialogflow API has a header byte in each block, as in MIME type
      ``audio/x-speex-with-header-byte``. It is a variant of the RTP Speex
      encoding defined in `RFC 5574 <https://tools.ietf.org/html/rfc5574>`__.
      The stream is a sequence of blocks, one block per RTP packet. Each block
      starts with a byte containing the length of the block, in bytes,
      followed by one or more frames of Speex data, padded to an integral
      number of bytes (octets) as specified in RFC 5574. In other words, each
      RTP header is replaced with a single byte containing the block length.
      Only Speex wideband is supported. ``sample_rate_hertz`` must be 16000.
    """

    AUDIO_ENCODING_UNSPECIFIED = 0
    AUDIO_ENCODING_LINEAR_16 = 1
    AUDIO_ENCODING_FLAC = 2
    AUDIO_ENCODING_MULAW = 3
    AUDIO_ENCODING_AMR = 4
    AUDIO_ENCODING_AMR_WB = 5
    AUDIO_ENCODING_OGG_OPUS = 6
    AUDIO_ENCODING_SPEEX_WITH_HEADER_BYTE = 7


class IntentView(enum.IntEnum):
    """
    Represents the options for views of an intent.
    An intent can be a sizable object. Therefore, we provide a resource view that
    does not return training phrases in the response.

    Attributes:
      INTENT_VIEW_UNSPECIFIED (int): Not specified. Treated as INTENT_VIEW_FULL.
      INTENT_VIEW_PARTIAL (int): Training phrases field is not populated in the response.
      INTENT_VIEW_FULL (int): All fields are populated.
    """

    INTENT_VIEW_UNSPECIFIED = 0
    INTENT_VIEW_PARTIAL = 1
    INTENT_VIEW_FULL = 2


class NullValue(enum.IntEnum):
    """
    ``NullValue`` is a singleton enumeration to represent the null value
    for the ``Value`` type union.

    The JSON representation for ``NullValue`` is JSON ``null``.

    Attributes:
      NULL_VALUE (int): Null value.
    """

    NULL_VALUE = 0


class OutputAudioEncoding(enum.IntEnum):
    """
    Audio encoding of the output audio format in Text-To-Speech.

    Attributes:
      OUTPUT_AUDIO_ENCODING_UNSPECIFIED (int): Not specified.
      OUTPUT_AUDIO_ENCODING_LINEAR_16 (int): Uncompressed 16-bit signed little-endian samples (Linear PCM).
      Audio content returned as LINEAR16 also contains a WAV header.
      OUTPUT_AUDIO_ENCODING_MP3 (int): MP3 audio at 32kbps.
      OUTPUT_AUDIO_ENCODING_MP3_64_KBPS (int): MP3 audio at 64kbps.
      OUTPUT_AUDIO_ENCODING_OGG_OPUS (int): Opus encoded audio wrapped in an ogg container. The result will be a
      file which can be played natively on Android, and in browsers (at least
      Chrome and Firefox). The quality of the encoding is considerably higher
      than MP3 while using approximately the same bitrate.
      OUTPUT_AUDIO_ENCODING_MULAW (int): 8-bit samples that compand 14-bit audio samples using G.711 PCMU/mu-law.
    """

    OUTPUT_AUDIO_ENCODING_UNSPECIFIED = 0
    OUTPUT_AUDIO_ENCODING_LINEAR_16 = 1
    OUTPUT_AUDIO_ENCODING_MP3 = 2
    OUTPUT_AUDIO_ENCODING_MP3_64_KBPS = 4
    OUTPUT_AUDIO_ENCODING_OGG_OPUS = 3
    OUTPUT_AUDIO_ENCODING_MULAW = 5


class SpeechModelVariant(enum.IntEnum):
    """
    Variant of the specified ``Speech model`` to use.

    See the `Cloud Speech
    documentation <https://cloud.google.com/speech-to-text/docs/enhanced-models>`__
    for which models have different variants. For example, the "phone_call"
    model has both a standard and an enhanced variant. When you use an
    enhanced model, you will generally receive higher quality results than
    for a standard model.

    Attributes:
      SPEECH_MODEL_VARIANT_UNSPECIFIED (int): No model variant specified. In this case Dialogflow defaults to
      USE_BEST_AVAILABLE.
      USE_BEST_AVAILABLE (int): Use the best available variant of the ``Speech model`` that the
      caller is eligible for.

      Please see the `Dialogflow
      docs <https://cloud.google.com/dialogflow/docs/data-logging>`__ for how
      to make your project eligible for enhanced models.
      USE_STANDARD (int): Use standard model variant even if an enhanced model is available.
      See the `Cloud Speech
      documentation <https://cloud.google.com/speech-to-text/docs/enhanced-models>`__
      for details about enhanced models.
      USE_ENHANCED (int): Use an enhanced model variant:

      -  If an enhanced variant does not exist for the given ``model`` and
         request language, Dialogflow falls back to the standard variant.

         The `Cloud Speech
         documentation <https://cloud.google.com/speech-to-text/docs/enhanced-models>`__
         describes which models have enhanced variants.

      -  If the API caller isn't eligible for enhanced models, Dialogflow
         returns an error. Please see the `Dialogflow
         docs <https://cloud.google.com/dialogflow/docs/data-logging>`__ for
         how to make your project eligible.
    """

    SPEECH_MODEL_VARIANT_UNSPECIFIED = 0
    USE_BEST_AVAILABLE = 1
    USE_STANDARD = 2
    USE_ENHANCED = 3


class SsmlVoiceGender(enum.IntEnum):
    """
    Gender of the voice as described in `SSML voice
    element <https://www.w3.org/TR/speech-synthesis11/#edef_voice>`__.

    Attributes:
      SSML_VOICE_GENDER_UNSPECIFIED (int): An unspecified gender, which means that the client doesn't care which
      gender the selected voice will have.
      SSML_VOICE_GENDER_MALE (int): A male voice.
      SSML_VOICE_GENDER_FEMALE (int): A female voice.
      SSML_VOICE_GENDER_NEUTRAL (int): A gender-neutral voice.
    """

    SSML_VOICE_GENDER_UNSPECIFIED = 0
    SSML_VOICE_GENDER_MALE = 1
    SSML_VOICE_GENDER_FEMALE = 2
    SSML_VOICE_GENDER_NEUTRAL = 3


class EntityType(object):
    class AutoExpansionMode(enum.IntEnum):
        """
        Represents different entity type expansion modes. Automated expansion
        allows an agent to recognize values that have not been explicitly listed in
        the entity (for example, new kinds of shopping list items).

        Attributes:
          AUTO_EXPANSION_MODE_UNSPECIFIED (int): Auto expansion disabled for the entity.
          AUTO_EXPANSION_MODE_DEFAULT (int): Allows an agent to recognize values that have not been explicitly
          listed in the entity.
        """

        AUTO_EXPANSION_MODE_UNSPECIFIED = 0
        AUTO_EXPANSION_MODE_DEFAULT = 1

    class Kind(enum.IntEnum):
        """
        Represents kinds of entities.

        Attributes:
          KIND_UNSPECIFIED (int): Not specified. This value should be never used.
          KIND_MAP (int): Map entity types allow mapping of a group of synonyms to a canonical
          value.
          KIND_LIST (int): List entity types contain a set of entries that do not map to canonical
          values. However, list entity types can contain references to other entity
          types (with or without aliases).
          KIND_REGEXP (int): Regexp entity types allow to specify regular expressions in entries
          values.
        """

        KIND_UNSPECIFIED = 0
        KIND_MAP = 1
        KIND_LIST = 2
        KIND_REGEXP = 3


class Match(object):
    class MatchType(enum.IntEnum):
        """
        Type of a Match.

        Attributes:
          MATCH_TYPE_UNSPECIFIED (int): Not specified. Should never be used.
          INTENT (int): The query was matched to an intent.
          DIRECT_INTENT (int): The query directly triggered an intent.
          PARAMETER_FILLING (int): The query was used for parameter filling.
          NO_MATCH (int): No match was found for the query.
          NO_INPUT (int): Indicates an empty query.
        """

        MATCH_TYPE_UNSPECIFIED = 0
        INTENT = 1
        DIRECT_INTENT = 2
        PARAMETER_FILLING = 3
        NO_MATCH = 4
        NO_INPUT = 5


class NluSettings(object):
    class ModelTrainingMode(enum.IntEnum):
        """
        NLU model training mode.

        Attributes:
          MODEL_TRAINING_MODE_UNSPECIFIED (int): Not specified. ``MODEL_TRAINING_MODE_AUTOMATIC`` will be used.
          MODEL_TRAINING_MODE_AUTOMATIC (int): NLU model training is automatically triggered when a flow gets modified.
          User can also manually trigger model training in this mode.
          MODEL_TRAINING_MODE_MANUAL (int): User needs to manually trigger NLU model training. Best for large flows
          whose models take long time to train.
        """

        MODEL_TRAINING_MODE_UNSPECIFIED = 0
        MODEL_TRAINING_MODE_AUTOMATIC = 1
        MODEL_TRAINING_MODE_MANUAL = 2

    class ModelType(enum.IntEnum):
        """
        NLU model type.

        Attributes:
          MODEL_TYPE_UNSPECIFIED (int): Not specified. ``MODEL_TYPE_STANDARD`` will be used.
          MODEL_TYPE_STANDARD (int): Use standard NLU model.
          MODEL_TYPE_ADVANCED (int): Use advanced NLU model.
        """

        MODEL_TYPE_UNSPECIFIED = 0
        MODEL_TYPE_STANDARD = 1
        MODEL_TYPE_ADVANCED = 3


class PageInfo(object):
    class FormInfo(object):
        class ParameterInfo(object):
            class ParameterState(enum.IntEnum):
                """
                Represents the state of a parameter.

                Attributes:
                  PARAMETER_STATE_UNSPECIFIED (int): Not specified. This value should be never used.
                  EMPTY (int): Indicates that the parameter does not have a value.
                  INVALID (int): Indicates that the parameter value is invalid. This field can be used
                  by the webhook to invalidate the parameter and ask the server to
                  collect it from the user again.
                  FILLED (int): Indicates that the parameter has a value.
                """

                PARAMETER_STATE_UNSPECIFIED = 0
                EMPTY = 1
                INVALID = 2
                FILLED = 3


class SessionEntityType(object):
    class EntityOverrideMode(enum.IntEnum):
        """
        The types of modifications for the session entity type.

        Attributes:
          ENTITY_OVERRIDE_MODE_UNSPECIFIED (int): Not specified. This value should be never used.
          ENTITY_OVERRIDE_MODE_OVERRIDE (int): The collection of session entities overrides the collection of entities
          in the corresponding custom entity type.
          ENTITY_OVERRIDE_MODE_SUPPLEMENT (int): The collection of session entities extends the collection of
          entities in the corresponding custom entity type.

          Note: Even in this override mode calls to ``ListSessionEntityTypes``,
          ``GetSessionEntityType``, ``CreateSessionEntityType`` and
          ``UpdateSessionEntityType`` only return the additional entities added in
          this session entity type. If you want to get the supplemented list,
          please call ``EntityTypes.GetEntityType`` on the custom entity type and
          merge.
        """

        ENTITY_OVERRIDE_MODE_UNSPECIFIED = 0
        ENTITY_OVERRIDE_MODE_OVERRIDE = 1
        ENTITY_OVERRIDE_MODE_SUPPLEMENT = 2


class StreamingRecognitionResult(object):
    class MessageType(enum.IntEnum):
        """
        Type of the response message.

        Attributes:
          MESSAGE_TYPE_UNSPECIFIED (int): Not specified. Should never be used.
          TRANSCRIPT (int): Message contains a (possibly partial) transcript.
          END_OF_SINGLE_UTTERANCE (int): Event indicates that the server has detected the end of the user's
          speech utterance and expects no additional speech. Therefore, the server
          will not process additional audio (although it may subsequently return
          additional results). The client should stop sending additional audio
          data, half-close the gRPC connection, and wait for any additional
          results until the server closes the gRPC connection. This message is
          only sent if ``single_utterance`` was set to ``true``, and is not used
          otherwise.
        """

        MESSAGE_TYPE_UNSPECIFIED = 0
        TRANSCRIPT = 1
        END_OF_SINGLE_UTTERANCE = 2


class Version(object):
    class State(enum.IntEnum):
        """
        The state of the version.

        Attributes:
          STATE_UNSPECIFIED (int): Not specified. This value is not used.
          RUNNING (int): Version is not ready to serve (e.g. training is running).
          SUCCEEDED (int): Training has succeeded and this version is ready to serve.
          FAILED (int): Version training failed.
        """

        STATE_UNSPECIFIED = 0
        RUNNING = 1
        SUCCEEDED = 2
        FAILED = 3


class WebhookResponse(object):
    class FulfillmentResponse(object):
        class MergeBehavior(enum.IntEnum):
            """
            Defines merge behavior for ``messages``.

            Attributes:
              MERGE_BEHAVIOR_UNSPECIFIED (int): Not specified. ``APPEND`` will be used.
              APPEND (int): ``messages`` will be appended to the list of messages waiting to be
              sent to the user.
              REPLACE (int): ``messages`` will replace the list of messages waiting to be sent to
              the user.
            """

            MERGE_BEHAVIOR_UNSPECIFIED = 0
            APPEND = 1
            REPLACE = 2
