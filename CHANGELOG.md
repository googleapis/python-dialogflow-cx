# Changelog

## [1.14.1](https://github.com/googleapis/python-dialogflow-cx/compare/v1.14.0...v1.14.1) (2023-01-06)


### Documentation

* **samples:** Update previous month logic to avoid zero-index bug in webhook_prebuilt_telecom sample ([#479](https://github.com/googleapis/python-dialogflow-cx/issues/479)) ([38c188a](https://github.com/googleapis/python-dialogflow-cx/commit/38c188ac7ec89471fdaff3981e8e66c820ff683c))

## [1.14.0](https://github.com/googleapis/python-dialogflow-cx/compare/v1.13.5...v1.14.0) (2022-12-15)


### Features

* Add files field to finding's list of attributes ([ff576ee](https://github.com/googleapis/python-dialogflow-cx/commit/ff576eefe4a202327fd3de6e98da1cca24ddad4e))
* Add support for `google.cloud.dialogflowcx.__version__` ([ff576ee](https://github.com/googleapis/python-dialogflow-cx/commit/ff576eefe4a202327fd3de6e98da1cca24ddad4e))
* Add typing to proto.Message based class attributes ([ff576ee](https://github.com/googleapis/python-dialogflow-cx/commit/ff576eefe4a202327fd3de6e98da1cca24ddad4e))


### Bug Fixes

* Add dict typing for client_options ([ff576ee](https://github.com/googleapis/python-dialogflow-cx/commit/ff576eefe4a202327fd3de6e98da1cca24ddad4e))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0 ([ff576ee](https://github.com/googleapis/python-dialogflow-cx/commit/ff576eefe4a202327fd3de6e98da1cca24ddad4e))
* Drop usage of pkg_resources ([ff576ee](https://github.com/googleapis/python-dialogflow-cx/commit/ff576eefe4a202327fd3de6e98da1cca24ddad4e))
* Fix timeout default values ([ff576ee](https://github.com/googleapis/python-dialogflow-cx/commit/ff576eefe4a202327fd3de6e98da1cca24ddad4e))


### Documentation

* Clarified Agent Assist max retention is 30 days ([ff576ee](https://github.com/googleapis/python-dialogflow-cx/commit/ff576eefe4a202327fd3de6e98da1cca24ddad4e))
* Clarify interactive logging TTL behavior ([ff576ee](https://github.com/googleapis/python-dialogflow-cx/commit/ff576eefe4a202327fd3de6e98da1cca24ddad4e))
* **samples:** Snippetgen handling of repeated enum field ([ff576ee](https://github.com/googleapis/python-dialogflow-cx/commit/ff576eefe4a202327fd3de6e98da1cca24ddad4e))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([ff576ee](https://github.com/googleapis/python-dialogflow-cx/commit/ff576eefe4a202327fd3de6e98da1cca24ddad4e))

## [1.13.5](https://github.com/googleapis/python-dialogflow-cx/compare/v1.13.4...v1.13.5) (2022-10-26)


### Documentation

* Clarified TTL as time-to-live ([#465](https://github.com/googleapis/python-dialogflow-cx/issues/465)) ([5e8fc34](https://github.com/googleapis/python-dialogflow-cx/commit/5e8fc34f7a40351c2a3092fb835bf8ac0f3e63d1))

## [1.13.4](https://github.com/googleapis/python-dialogflow-cx/compare/v1.13.3...v1.13.4) (2022-10-07)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#462](https://github.com/googleapis/python-dialogflow-cx/issues/462)) ([8cd6d6d](https://github.com/googleapis/python-dialogflow-cx/commit/8cd6d6df6c19b93e8116e968fb63292153a019b7))

## [1.13.3](https://github.com/googleapis/python-dialogflow-cx/compare/v1.13.2...v1.13.3) (2022-10-04)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#458](https://github.com/googleapis/python-dialogflow-cx/issues/458)) ([07e19d4](https://github.com/googleapis/python-dialogflow-cx/commit/07e19d476e3382ead73b44f4bc8b84e230aa6115))


### Documentation

* Clarified gcs_bucket field of the SecuritySettings message ([#460](https://github.com/googleapis/python-dialogflow-cx/issues/460)) ([f922211](https://github.com/googleapis/python-dialogflow-cx/commit/f922211c6dde44572303926f9456d040e041a224))
* **samples:** Adding snippet to extract SessionInfo ([d6ef048](https://github.com/googleapis/python-dialogflow-cx/commit/d6ef04841975e9076c940802283d1a9ba8e05eb4))

## [1.13.2](https://github.com/googleapis/python-dialogflow-cx/compare/v1.13.1...v1.13.2) (2022-09-02)


### Documentation

* **samples:** Add prebuilt telecom agent webhook code in python ([#434](https://github.com/googleapis/python-dialogflow-cx/issues/434)) ([45926d2](https://github.com/googleapis/python-dialogflow-cx/commit/45926d2fd7bcfb49785ad339e7141349e31f91b4))

## [1.13.1](https://github.com/googleapis/python-dialogflow-cx/compare/v1.13.0...v1.13.1) (2022-08-15)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#435](https://github.com/googleapis/python-dialogflow-cx/issues/435)) ([519012b](https://github.com/googleapis/python-dialogflow-cx/commit/519012bf13179d4fdbe6856ca21fd539b4f776b1))
* **deps:** require proto-plus >= 1.22.0 ([519012b](https://github.com/googleapis/python-dialogflow-cx/commit/519012bf13179d4fdbe6856ca21fd539b4f776b1))

## [1.13.0](https://github.com/googleapis/python-dialogflow-cx/compare/v1.12.1...v1.13.0) (2022-07-15)


### Features

* add audience parameter ([3a356c9](https://github.com/googleapis/python-dialogflow-cx/commit/3a356c951d64f99ca9fb0eb426921f42f5f41abf))
* **v3:** added webhook_config ([3a356c9](https://github.com/googleapis/python-dialogflow-cx/commit/3a356c951d64f99ca9fb0eb426921f42f5f41abf))
* **v3beta1:** added webhook_config ([3a356c9](https://github.com/googleapis/python-dialogflow-cx/commit/3a356c951d64f99ca9fb0eb426921f42f5f41abf))


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0  ([3a356c9](https://github.com/googleapis/python-dialogflow-cx/commit/3a356c951d64f99ca9fb0eb426921f42f5f41abf))
* require python 3.7+ ([4746c9f](https://github.com/googleapis/python-dialogflow-cx/commit/4746c9f1c34e54892c64857751b84b204b6a8871))


### Documentation

* add detect intent with intent input snippet ([#417](https://github.com/googleapis/python-dialogflow-cx/issues/417)) ([04ded3c](https://github.com/googleapis/python-dialogflow-cx/commit/04ded3ce2cdee30bdf0dd91f7164d32fcda204bd))
* add detect intent with sentiment analysis snippet ([#416](https://github.com/googleapis/python-dialogflow-cx/issues/416)) ([dcd8319](https://github.com/googleapis/python-dialogflow-cx/commit/dcd8319e2edef2e99dffea50b202f9b7f5a52c06))
* add detect intent with text-to-speech synthesized output snippet ([#419](https://github.com/googleapis/python-dialogflow-cx/issues/419)) ([ac6aae4](https://github.com/googleapis/python-dialogflow-cx/commit/ac6aae4fa4607bf17aa9934ccba440d976b25f17))
* Add dialogflow cx detect intent with disabled webhook snippet ([#422](https://github.com/googleapis/python-dialogflow-cx/issues/422)) ([406e84d](https://github.com/googleapis/python-dialogflow-cx/commit/406e84dabb889c8f43d4084c6e4ed39fbc6d4ee0))
* add streaming detect intent with partial response sample ([#414](https://github.com/googleapis/python-dialogflow-cx/issues/414)) ([57a0e16](https://github.com/googleapis/python-dialogflow-cx/commit/57a0e16995bf2520306c8d29ee84088345a9b3be))
* clarify descriptions of the AdvancedSettings and WebhookRequest data types ([3a356c9](https://github.com/googleapis/python-dialogflow-cx/commit/3a356c951d64f99ca9fb0eb426921f42f5f41abf))
* Dialogflow cx v3 detect intent event input snippet ([#421](https://github.com/googleapis/python-dialogflow-cx/issues/421)) ([0524558](https://github.com/googleapis/python-dialogflow-cx/commit/052455829c99ff0838a5a140a0496bcff4a45178))
* improve comments for protos ([3a356c9](https://github.com/googleapis/python-dialogflow-cx/commit/3a356c951d64f99ca9fb0eb426921f42f5f41abf))
* Update region_tag: dialogflow_detect_intent_text --> dialogflow_cx_detect_intent_text ([#424](https://github.com/googleapis/python-dialogflow-cx/issues/424)) ([dd2257c](https://github.com/googleapis/python-dialogflow-cx/commit/dd2257c850059e1cb63c11326dd760665079c32b))

## [1.12.1](https://github.com/googleapis/python-dialogflow-cx/compare/v1.12.0...v1.12.1) (2022-06-03)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#396](https://github.com/googleapis/python-dialogflow-cx/issues/396)) ([51be5ca](https://github.com/googleapis/python-dialogflow-cx/commit/51be5ca187e68f17af53e6a41e59bb4cc04086c1))


### Documentation

* fix changelog header to consistent size ([#395](https://github.com/googleapis/python-dialogflow-cx/issues/395)) ([f21bc73](https://github.com/googleapis/python-dialogflow-cx/commit/f21bc7349da7fabe50cc5fb846db43e15da8b71d))

## [1.12.0](https://github.com/googleapis/python-dialogflow-cx/compare/v1.11.0...v1.12.0) (2022-05-09)


### Features

* **v3beta1:** added audio_export_settings ([#311](https://github.com/googleapis/python-dialogflow-cx/issues/311)) ([228ae83](https://github.com/googleapis/python-dialogflow-cx/commit/228ae8310b71412c1636a5ef214f62dad6473e40))


### Documentation

* **v3:** update the doc on diagnostic info ([#314](https://github.com/googleapis/python-dialogflow-cx/issues/314)) ([6109b64](https://github.com/googleapis/python-dialogflow-cx/commit/6109b64efb85480fdd9793476db14e65c40a0333))

## [1.11.0](https://github.com/googleapis/python-dialogflow-cx/compare/v1.10.0...v1.11.0) (2022-05-03)


### Features

* added data format specification for export agent ([1844193](https://github.com/googleapis/python-dialogflow-cx/commit/1844193788ce3d9f66f2822846b31f469f34f530))
* **v3:** add support for locking an agent for changes ([#276](https://github.com/googleapis/python-dialogflow-cx/issues/276)) ([1844193](https://github.com/googleapis/python-dialogflow-cx/commit/1844193788ce3d9f66f2822846b31f469f34f530))
* **v3:** added audio_export_settings ([#300](https://github.com/googleapis/python-dialogflow-cx/issues/300)) ([b225dfe](https://github.com/googleapis/python-dialogflow-cx/commit/b225dfe9371e89ee54e483888b7ed36d8374e011))
* **v3beta1:** added data format specification for export agent ([72e624a](https://github.com/googleapis/python-dialogflow-cx/commit/72e624ae6430fd454380cdf6e348dbe763e56e6f))
* **v3beta1:** added support for locking an agent for changes ([#281](https://github.com/googleapis/python-dialogflow-cx/issues/281)) ([72e624a](https://github.com/googleapis/python-dialogflow-cx/commit/72e624ae6430fd454380cdf6e348dbe763e56e6f))


### Documentation

* improved docs format ([#275](https://github.com/googleapis/python-dialogflow-cx/issues/275)) ([560e6a4](https://github.com/googleapis/python-dialogflow-cx/commit/560e6a478a7daaf1ac9fac23ca01390a6e7699a7))
* minor wording update ([#294](https://github.com/googleapis/python-dialogflow-cx/issues/294)) ([f660888](https://github.com/googleapis/python-dialogflow-cx/commit/f660888d55f5aab2b40d5e7f0b214e3e8ba01864))
* **samples:** Adds snippet for configuring a webhook to enable an agent response. ([#306](https://github.com/googleapis/python-dialogflow-cx/issues/306)) ([c0cc924](https://github.com/googleapis/python-dialogflow-cx/commit/c0cc924a257740e68d244c265c6406a8d6888cc5))
* **samples:** Adds snippet for configuring optional or required form parameters ([#305](https://github.com/googleapis/python-dialogflow-cx/issues/305)) ([720c0bd](https://github.com/googleapis/python-dialogflow-cx/commit/720c0bdd0f5707a2c71c9d32a91f06f86c48a98e))
* **samples:** Adds snippet for validating a form parameter. ([#302](https://github.com/googleapis/python-dialogflow-cx/issues/302)) ([8cfe6a1](https://github.com/googleapis/python-dialogflow-cx/commit/8cfe6a15b18b558faa2cd5ceb8dc7b291add4444))
* **samples:** Configure session parameters snippet ([#303](https://github.com/googleapis/python-dialogflow-cx/issues/303)) ([ace3936](https://github.com/googleapis/python-dialogflow-cx/commit/ace393696fdec8040bd5b23daa09f80183ad9125))
* **samples:** Configure session parameters trigger transition ([#304](https://github.com/googleapis/python-dialogflow-cx/issues/304)) ([d6cab9d](https://github.com/googleapis/python-dialogflow-cx/commit/d6cab9dd6db83aea15548795a0fc449f72a2b56f))
* **v3beta1:** added explanation for uri fields in resources ([#273](https://github.com/googleapis/python-dialogflow-cx/issues/273)) ([01b0f8f](https://github.com/googleapis/python-dialogflow-cx/commit/01b0f8f795d06609b370ba7568db753152764d9b))
* **v3beta1:** improved docs format ([01b0f8f](https://github.com/googleapis/python-dialogflow-cx/commit/01b0f8f795d06609b370ba7568db753152764d9b))

## [1.10.0](https://github.com/googleapis/python-dialogflow-cx/compare/v1.9.1...v1.10.0) (2022-03-10)


### Features

* added page in TestConfig ([#268](https://github.com/googleapis/python-dialogflow-cx/issues/268)) ([61fd2dc](https://github.com/googleapis/python-dialogflow-cx/commit/61fd2dc3512e4bcfdfc51cf085cc12cbbf1e043b))
* **v3beta1:** added page in TestConfig ([#270](https://github.com/googleapis/python-dialogflow-cx/issues/270)) ([a81f0c2](https://github.com/googleapis/python-dialogflow-cx/commit/a81f0c23d5dc835bd6abdccd546ef00f6c421a74))


### Documentation

* clarified wording around Cloud Storage usage ([61fd2dc](https://github.com/googleapis/python-dialogflow-cx/commit/61fd2dc3512e4bcfdfc51cf085cc12cbbf1e043b))

## [1.9.1](https://github.com/googleapis/python-dialogflow-cx/compare/v1.9.0...v1.9.1) (2022-03-05)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#263](https://github.com/googleapis/python-dialogflow-cx/issues/263)) ([6235775](https://github.com/googleapis/python-dialogflow-cx/commit/623577550fc96786c2142d971dea4c31c116181a))
* **deps:** require proto-plus>=1.15.0 ([6235775](https://github.com/googleapis/python-dialogflow-cx/commit/623577550fc96786c2142d971dea4c31c116181a))

## [1.9.0](https://github.com/googleapis/python-dialogflow-cx/compare/v1.8.0...v1.9.0) (2022-02-26)


### Features

* add api_key support ([#240](https://github.com/googleapis/python-dialogflow-cx/issues/240)) ([cf95791](https://github.com/googleapis/python-dialogflow-cx/commit/cf9579171290ecf5afeeb6a38a3504857808a4ef))


### Bug Fixes

* resolve DuplicateCredentialArgs error when using credentials_file ([f3bf440](https://github.com/googleapis/python-dialogflow-cx/commit/f3bf440a081622dfc6d8d8e385f2edb5c3e11202))


### Documentation

* add autogenerated code snippets ([2292ff5](https://github.com/googleapis/python-dialogflow-cx/commit/2292ff540aea24c3c831a5ffe1604c2c022ccb82))

## [1.8.0](https://github.com/googleapis/python-dialogflow-cx/compare/v1.7.0...v1.8.0) (2022-01-14)


### Features

* **v3:** added `TelephonyTransferCall` in response message ([#216](https://github.com/googleapis/python-dialogflow-cx/issues/216)) ([76dae8b](https://github.com/googleapis/python-dialogflow-cx/commit/76dae8b03c0e3bf33123b8001e3f8d40701b5c19))
* **v3:** added the display name of the current page in webhook requests ([#221](https://github.com/googleapis/python-dialogflow-cx/issues/221)) ([aa91b72](https://github.com/googleapis/python-dialogflow-cx/commit/aa91b729ffa07230b011a61d3eb1521f59345fc1))
* **v3:** allow setting custom CA for generic webhooks ([#214](https://github.com/googleapis/python-dialogflow-cx/issues/214)) ([8f3dc03](https://github.com/googleapis/python-dialogflow-cx/commit/8f3dc03835b5bb5baa36224a274f24dda7aa3709))
* **v3beta1:** added `TelephonyTransferCall` in response message ([#217](https://github.com/googleapis/python-dialogflow-cx/issues/217)) ([e24bdfd](https://github.com/googleapis/python-dialogflow-cx/commit/e24bdfd499952199dfbdaa5634061653da8ae1db))
* **v3beta1:** added the display name of the current page in webhook requests ([#222](https://github.com/googleapis/python-dialogflow-cx/issues/222)) ([5956179](https://github.com/googleapis/python-dialogflow-cx/commit/595617990ccdc0575f97ae547984e89f638cb664))
* **v3:** release CompareVersions API ([8f3dc03](https://github.com/googleapis/python-dialogflow-cx/commit/8f3dc03835b5bb5baa36224a274f24dda7aa3709))

## [1.7.0](https://www.github.com/googleapis/python-dialogflow-cx/compare/v1.6.0...v1.7.0) (2021-11-12)


### Features

* allow setting custom CA for generic webhooks ([#207](https://www.github.com/googleapis/python-dialogflow-cx/issues/207)) ([441d66b](https://www.github.com/googleapis/python-dialogflow-cx/commit/441d66b3864c34cf37570b6c58ccf097eb20e919))


### Documentation

* **samples:** added comment to webhook sample ([#211](https://www.github.com/googleapis/python-dialogflow-cx/issues/211)) ([4d36e31](https://www.github.com/googleapis/python-dialogflow-cx/commit/4d36e31f20e38755dd5d4a7a92bb8c48722cb11e))

## [1.6.0](https://www.github.com/googleapis/python-dialogflow-cx/compare/v1.5.0...v1.6.0) (2021-11-05)


### Features

* add support for python 3.10 ([#192](https://www.github.com/googleapis/python-dialogflow-cx/issues/192)) ([527b679](https://www.github.com/googleapis/python-dialogflow-cx/commit/527b679286ce7ed6481bf5c9258858473ca1f601))
* **v3:** added API for changelogs ([#197](https://www.github.com/googleapis/python-dialogflow-cx/issues/197)) ([4f41653](https://www.github.com/googleapis/python-dialogflow-cx/commit/4f41653b08a5be4aa6c871f285d941a2f43740a9))
* **v3beta1:** added API for changelogs ([#198](https://www.github.com/googleapis/python-dialogflow-cx/issues/198)) ([484e13a](https://www.github.com/googleapis/python-dialogflow-cx/commit/484e13a78830a3d0ce8b1745fdf2dfce0f88a21e))
* **v3beta1:** added support for comparing between versions ([#202](https://www.github.com/googleapis/python-dialogflow-cx/issues/202)) ([b8e16f8](https://www.github.com/googleapis/python-dialogflow-cx/commit/b8e16f8a17a49c1fc65f7f4392e33fb273bcd8ca))


### Bug Fixes

* **deps:** drop packaging dependency ([c44582e](https://www.github.com/googleapis/python-dialogflow-cx/commit/c44582e2fe3d49327bb0fc5ba05d2959b6965b7b))
* **deps:** require google-api-core >= 1.28.0 ([c44582e](https://www.github.com/googleapis/python-dialogflow-cx/commit/c44582e2fe3d49327bb0fc5ba05d2959b6965b7b))


### Documentation

* list oneofs in docstring ([c44582e](https://www.github.com/googleapis/python-dialogflow-cx/commit/c44582e2fe3d49327bb0fc5ba05d2959b6965b7b))
* **samples:** add voice selection ([#184](https://www.github.com/googleapis/python-dialogflow-cx/issues/184)) ([778b86f](https://www.github.com/googleapis/python-dialogflow-cx/commit/778b86f69e88ceb884bb9933128d2b14c6689174))
* **samples:** added webhook sample ([#169](https://www.github.com/googleapis/python-dialogflow-cx/issues/169)) ([74cfc9a](https://www.github.com/googleapis/python-dialogflow-cx/commit/74cfc9a7ab9b85fa05565c406534a3cd3391ab4f))
* **samples:** adds list training phrases sample ([#196](https://www.github.com/googleapis/python-dialogflow-cx/issues/196)) ([dfefa4e](https://www.github.com/googleapis/python-dialogflow-cx/commit/dfefa4e21bcd6bf37d341911187fab283152f514))
* **v3beta1:** clarified security settings API reference ([b8e16f8](https://www.github.com/googleapis/python-dialogflow-cx/commit/b8e16f8a17a49c1fc65f7f4392e33fb273bcd8ca))
* **v3:** clarified semantic of the streaming APIs ([4f41653](https://www.github.com/googleapis/python-dialogflow-cx/commit/4f41653b08a5be4aa6c871f285d941a2f43740a9))

## [1.5.0](https://www.github.com/googleapis/python-dialogflow-cx/compare/v1.4.0...v1.5.0) (2021-10-11)


### Features

* add context manager support in client ([#187](https://www.github.com/googleapis/python-dialogflow-cx/issues/187)) ([70d4776](https://www.github.com/googleapis/python-dialogflow-cx/commit/70d4776d80f1f60b3f45e08e8dc64a47e2fae3e6))

## [1.4.0](https://www.github.com/googleapis/python-dialogflow-cx/compare/v1.3.2...v1.4.0) (2021-10-05)


### Features

* expose dtmf input info in the query result ([#181](https://www.github.com/googleapis/python-dialogflow-cx/issues/181)) ([e44d0ce](https://www.github.com/googleapis/python-dialogflow-cx/commit/e44d0cee6b51842e45255773c33ae0bbfc672f30))
* exposed DTMF input info in the query result ([1383bf8](https://www.github.com/googleapis/python-dialogflow-cx/commit/1383bf82b8b2ae0cd92d81768a693a2732a53a46))
* **v3:** added deployment API ([#182](https://www.github.com/googleapis/python-dialogflow-cx/issues/182)) ([1383bf8](https://www.github.com/googleapis/python-dialogflow-cx/commit/1383bf82b8b2ae0cd92d81768a693a2732a53a46))
* **v3beta1:** added support for DeployFlow api under Environments ([977e2aa](https://www.github.com/googleapis/python-dialogflow-cx/commit/977e2aa9c17c235d125c633a6f4ba9f5a1dade7b))
* **v3beta1:** added support for Deployments with ListDeployments and GetDeployment apis  ([#177](https://www.github.com/googleapis/python-dialogflow-cx/issues/177)) ([977e2aa](https://www.github.com/googleapis/python-dialogflow-cx/commit/977e2aa9c17c235d125c633a6f4ba9f5a1dade7b))
* **v3beta1:** added support for TestCasesConfig under Environment ([977e2aa](https://www.github.com/googleapis/python-dialogflow-cx/commit/977e2aa9c17c235d125c633a6f4ba9f5a1dade7b))


### Bug Fixes

* improper types in pagers generation ([615718b](https://www.github.com/googleapis/python-dialogflow-cx/commit/615718bf80e5c2f3060ff38675a7f4fe8deb59b1))
* **v3beta1:** marked resource name of security setting as not-required ([977e2aa](https://www.github.com/googleapis/python-dialogflow-cx/commit/977e2aa9c17c235d125c633a6f4ba9f5a1dade7b))


### Documentation

* added notes on long running operation ([1383bf8](https://www.github.com/googleapis/python-dialogflow-cx/commit/1383bf82b8b2ae0cd92d81768a693a2732a53a46))
* **v3beta1:** added long running operation explanation for several apis ([977e2aa](https://www.github.com/googleapis/python-dialogflow-cx/commit/977e2aa9c17c235d125c633a6f4ba9f5a1dade7b))

## [1.3.2](https://www.github.com/googleapis/python-dialogflow-cx/compare/v1.3.1...v1.3.2) (2021-09-24)


### Bug Fixes

* add 'dict' annotation type to 'request' ([96021b9](https://www.github.com/googleapis/python-dialogflow-cx/commit/96021b9a78a40f3f8f9898d53493912a1621da89))


### Documentation

* **samples:** added filter sample ([#171](https://www.github.com/googleapis/python-dialogflow-cx/issues/171)) ([5b7e6b9](https://www.github.com/googleapis/python-dialogflow-cx/commit/5b7e6b9fcb066e823d58c5ce3af0f32a54d896bc))
* **samples:** added page management samples ([#152](https://www.github.com/googleapis/python-dialogflow-cx/issues/152)) ([41d15f8](https://www.github.com/googleapis/python-dialogflow-cx/commit/41d15f8f212baab09222c6a350efc3376a3bf9ea))

## [1.3.1](https://www.github.com/googleapis/python-dialogflow-cx/compare/v1.3.0...v1.3.1) (2021-08-31)


### Documentation

* **v3beta1:** clarified LRO types ([#161](https://www.github.com/googleapis/python-dialogflow-cx/issues/161)) ([dd2b2fd](https://www.github.com/googleapis/python-dialogflow-cx/commit/dd2b2fd345e91fa3da1290f6896ac6b521c2eb7b))
* **v3beta1:** fixed incorrect update mask descriptions ([dd2b2fd](https://www.github.com/googleapis/python-dialogflow-cx/commit/dd2b2fd345e91fa3da1290f6896ac6b521c2eb7b))

## [1.3.0](https://www.github.com/googleapis/python-dialogflow-cx/compare/v1.2.0...v1.3.0) (2021-08-27)


### Features

* **v3:** added support for DLP templates ([#144](https://www.github.com/googleapis/python-dialogflow-cx/issues/144)) ([c74e3ac](https://www.github.com/googleapis/python-dialogflow-cx/commit/c74e3acb609363cdf941586e98ed2c8c5804980b))
* **v3beta1:** added support for DLP templates ([#143](https://www.github.com/googleapis/python-dialogflow-cx/issues/143)) ([7efb89c](https://www.github.com/googleapis/python-dialogflow-cx/commit/7efb89cc6311e1df9d03740ba6d078af3f79559e))
* **v3beta1:** expose `Locations` service to get/list avaliable locations of Dialogflow products ([7efb89c](https://www.github.com/googleapis/python-dialogflow-cx/commit/7efb89cc6311e1df9d03740ba6d078af3f79559e))
* **v3:** expose `Locations` service to get/list avaliable locations of Dialogflow products ([c74e3ac](https://www.github.com/googleapis/python-dialogflow-cx/commit/c74e3acb609363cdf941586e98ed2c8c5804980b))


### Documentation

* clarified LRO types  ([#156](https://www.github.com/googleapis/python-dialogflow-cx/issues/156)) ([a50e8dc](https://www.github.com/googleapis/python-dialogflow-cx/commit/a50e8dca8952cea19be2587ee68c600a41a92eeb))
* fixed incorrect update mask descriptions ([a50e8dc](https://www.github.com/googleapis/python-dialogflow-cx/commit/a50e8dca8952cea19be2587ee68c600a41a92eeb))
* **samples:** add agent creation code snippet ([#146](https://www.github.com/googleapis/python-dialogflow-cx/issues/146)) ([272fc98](https://www.github.com/googleapis/python-dialogflow-cx/commit/272fc9879e536f7a9ea31d8c10169cf644170769))
* **samples:** add region tags ([#150](https://www.github.com/googleapis/python-dialogflow-cx/issues/150)) ([54ea84d](https://www.github.com/googleapis/python-dialogflow-cx/commit/54ea84d58064a7c8d0a71f020a0c8cf36ac157bd))
* **samples:** add region tags ([#151](https://www.github.com/googleapis/python-dialogflow-cx/issues/151)) ([788b67a](https://www.github.com/googleapis/python-dialogflow-cx/commit/788b67a8c966788a70a5d683a5e79e3a289c7ba3))
* **samples:** add update intent sample ([#142](https://www.github.com/googleapis/python-dialogflow-cx/issues/142)) ([3e80235](https://www.github.com/googleapis/python-dialogflow-cx/commit/3e80235277a0df12644d743f6853ba45263a1239))
* **v3beta1:** reorder some fields ([7efb89c](https://www.github.com/googleapis/python-dialogflow-cx/commit/7efb89cc6311e1df9d03740ba6d078af3f79559e))

## [1.2.0](https://www.github.com/googleapis/python-dialogflow-cx/compare/v1.1.1...v1.2.0) (2021-08-02)


### Features

* **v3:** add advanced settings for agent level ([#137](https://www.github.com/googleapis/python-dialogflow-cx/issues/137)) ([24ef477](https://www.github.com/googleapis/python-dialogflow-cx/commit/24ef4773d4f6392ff39e7cdf70ff67b64ee50449))
* **v3:** add insights export settings for security setting ([24ef477](https://www.github.com/googleapis/python-dialogflow-cx/commit/24ef4773d4f6392ff39e7cdf70ff67b64ee50449))
* **v3:** add language code for streaming recognition result and flow versions for query parameters ([24ef477](https://www.github.com/googleapis/python-dialogflow-cx/commit/24ef4773d4f6392ff39e7cdf70ff67b64ee50449))
* **v3:** add rollout config, state and failure reason for experiment ([24ef477](https://www.github.com/googleapis/python-dialogflow-cx/commit/24ef4773d4f6392ff39e7cdf70ff67b64ee50449))
* **v3beta1:** add advanced settings for agent level ([#138](https://www.github.com/googleapis/python-dialogflow-cx/issues/138)) ([96141a1](https://www.github.com/googleapis/python-dialogflow-cx/commit/96141a11fdba3dcb2a77a261505583bba75fcc77))
* **v3beta1:** add insights export settings for security setting ([96141a1](https://www.github.com/googleapis/python-dialogflow-cx/commit/96141a11fdba3dcb2a77a261505583bba75fcc77))
* **v3beta1:** add language code for streaming recognition result and flow versions for query parameters ([96141a1](https://www.github.com/googleapis/python-dialogflow-cx/commit/96141a11fdba3dcb2a77a261505583bba75fcc77))
* **v3beta1:** add rollout config, state and failure reason for experiment ([96141a1](https://www.github.com/googleapis/python-dialogflow-cx/commit/96141a11fdba3dcb2a77a261505583bba75fcc77))


### Documentation

* **v3beta1:** deprecate legacy logging settings ([96141a1](https://www.github.com/googleapis/python-dialogflow-cx/commit/96141a11fdba3dcb2a77a261505583bba75fcc77))
* **v3:** deprecate legacy logging settings ([24ef477](https://www.github.com/googleapis/python-dialogflow-cx/commit/24ef4773d4f6392ff39e7cdf70ff67b64ee50449))

## [1.1.1](https://www.github.com/googleapis/python-dialogflow-cx/compare/v1.1.0...v1.1.1) (2021-07-24)


### Bug Fixes

* enable self signed jwt for grpc ([#134](https://www.github.com/googleapis/python-dialogflow-cx/issues/134)) ([5e42bd0](https://www.github.com/googleapis/python-dialogflow-cx/commit/5e42bd0786607ed0636e80be073007224bcb520e))

## [1.1.0](https://www.github.com/googleapis/python-dialogflow-cx/compare/v1.0.0...v1.1.0) (2021-07-22)


### Features

* add Samples section to CONTRIBUTING.rst ([#129](https://www.github.com/googleapis/python-dialogflow-cx/issues/129)) ([19238ad](https://www.github.com/googleapis/python-dialogflow-cx/commit/19238ad534b7528e3481e50a44663b541da197ef))


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#128](https://www.github.com/googleapis/python-dialogflow-cx/issues/128)) ([fbe63e8](https://www.github.com/googleapis/python-dialogflow-cx/commit/fbe63e86df05150e009e8e7b7e103735b382556e))

## [1.0.0](https://www.github.com/googleapis/python-dialogflow-cx/compare/v0.8.0...v1.0.0) (2021-06-30)


### Features

* bump release level to production/stable ([#88](https://www.github.com/googleapis/python-dialogflow-cx/issues/88)) ([47739f9](https://www.github.com/googleapis/python-dialogflow-cx/commit/47739f927032ca8701297260f0374f11b2c756b9))

## [0.8.0](https://www.github.com/googleapis/python-dialogflow-cx/compare/v0.7.1...v0.8.0) (2021-06-30)


### Features

* add always_use_jwt_access ([3550fa7](https://www.github.com/googleapis/python-dialogflow-cx/commit/3550fa7fa5863a313bd9288a1f515557f8f9fdea))
* add return_partial response to Fulfillment ([3550fa7](https://www.github.com/googleapis/python-dialogflow-cx/commit/3550fa7fa5863a313bd9288a1f515557f8f9fdea))
* mark agent.default_language_code as required ([3550fa7](https://www.github.com/googleapis/python-dialogflow-cx/commit/3550fa7fa5863a313bd9288a1f515557f8f9fdea))


### Bug Fixes

* disable always_use_jwt_access ([#119](https://www.github.com/googleapis/python-dialogflow-cx/issues/119)) ([3550fa7](https://www.github.com/googleapis/python-dialogflow-cx/commit/3550fa7fa5863a313bd9288a1f515557f8f9fdea))


### Documentation

* add notes to train agent before sending queries ([3550fa7](https://www.github.com/googleapis/python-dialogflow-cx/commit/3550fa7fa5863a313bd9288a1f515557f8f9fdea))
* added notes to train agent before sending queries ([#111](https://www.github.com/googleapis/python-dialogflow-cx/issues/111)) ([8a53800](https://www.github.com/googleapis/python-dialogflow-cx/commit/8a5380055dfa7d58f83be5ce0da310318b54fc51))
* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-dialogflow-cx/issues/1127)) ([#110](https://www.github.com/googleapis/python-dialogflow-cx/issues/110)) ([40974f5](https://www.github.com/googleapis/python-dialogflow-cx/commit/40974f56c27833ab23575426f75d0868e1a10d94)), closes [#1126](https://www.github.com/googleapis/python-dialogflow-cx/issues/1126)

## [0.7.1](https://www.github.com/googleapis/python-dialogflow-cx/compare/v0.7.0...v0.7.1) (2021-06-16)


### Bug Fixes

* **deps:** add packaging requirement ([#105](https://www.github.com/googleapis/python-dialogflow-cx/issues/105)) ([5d47692](https://www.github.com/googleapis/python-dialogflow-cx/commit/5d476920c8c6825050a828896231542f6bfde2e2))

## [0.7.0](https://www.github.com/googleapis/python-dialogflow-cx/compare/v0.6.0...v0.7.0) (2021-06-16)


### Features

* **v3beta1:** Support partial response feature ([5e21ed4](https://www.github.com/googleapis/python-dialogflow-cx/commit/5e21ed454ad6a5d687e634ad4e697f1921104c47))
* **v3beta1:** support sentiment analysis in bot testing ([#100](https://www.github.com/googleapis/python-dialogflow-cx/issues/100)) ([f24f302](https://www.github.com/googleapis/python-dialogflow-cx/commit/f24f3028fa83da14614d1340e5bce7719be287b6))


### Bug Fixes

* exclude docs and tests from package ([#104](https://www.github.com/googleapis/python-dialogflow-cx/issues/104)) ([2ddb70b](https://www.github.com/googleapis/python-dialogflow-cx/commit/2ddb70b5825ad0d59165d7dfbfe36677d586cccf))
* **v3beta1:** Set agent default language code as required ([#103](https://www.github.com/googleapis/python-dialogflow-cx/issues/103)) ([5e21ed4](https://www.github.com/googleapis/python-dialogflow-cx/commit/5e21ed454ad6a5d687e634ad4e697f1921104c47))


### Documentation

* **v3beta1:** Update docs of Agents, Fulfillments, SecuritySettings and Sessions ([5e21ed4](https://www.github.com/googleapis/python-dialogflow-cx/commit/5e21ed454ad6a5d687e634ad4e697f1921104c47))

## [0.6.0](https://www.github.com/googleapis/python-dialogflow-cx/compare/v0.5.0...v0.6.0) (2021-06-07)


### Features

* support sentiment analysis in bot testing ([#98](https://www.github.com/googleapis/python-dialogflow-cx/issues/98)) ([db258bc](https://www.github.com/googleapis/python-dialogflow-cx/commit/db258bcc9971542e347b50f396bd51ec88520fde))

## [0.5.0](https://www.github.com/googleapis/python-dialogflow-cx/compare/v0.4.1...v0.5.0) (2021-05-28)


### Features

* add export / import flow API ([20df7c3](https://www.github.com/googleapis/python-dialogflow-cx/commit/20df7c3bfabef5da23970512a3f925f4dfe7d2f9))
* add support for service directory webhooks ([20df7c3](https://www.github.com/googleapis/python-dialogflow-cx/commit/20df7c3bfabef5da23970512a3f925f4dfe7d2f9))
* added API for continuous test ([#91](https://www.github.com/googleapis/python-dialogflow-cx/issues/91)) ([81d4f53](https://www.github.com/googleapis/python-dialogflow-cx/commit/81d4f53cd4a4080b21221126dacaf2e13ca2efcf))
* added API for running continuous test ([#94](https://www.github.com/googleapis/python-dialogflow-cx/issues/94)) ([cc30fa3](https://www.github.com/googleapis/python-dialogflow-cx/commit/cc30fa3e767bac2f33637ce1c29766ff41e9225b))
* added fallback option when restoring an agent ([20df7c3](https://www.github.com/googleapis/python-dialogflow-cx/commit/20df7c3bfabef5da23970512a3f925f4dfe7d2f9))
* Expose supported languages of the agent; ([20df7c3](https://www.github.com/googleapis/python-dialogflow-cx/commit/20df7c3bfabef5da23970512a3f925f4dfe7d2f9))
* include original user query in WebhookRequest; add GetTextCaseresult API. ([20df7c3](https://www.github.com/googleapis/python-dialogflow-cx/commit/20df7c3bfabef5da23970512a3f925f4dfe7d2f9))
* support self-signed JWT flow for service accounts ([20df7c3](https://www.github.com/googleapis/python-dialogflow-cx/commit/20df7c3bfabef5da23970512a3f925f4dfe7d2f9))


### Bug Fixes

* add async client to %name_%version/init.py ([20df7c3](https://www.github.com/googleapis/python-dialogflow-cx/commit/20df7c3bfabef5da23970512a3f925f4dfe7d2f9))
* require google-api-core>=1.22.2 ([3440f18](https://www.github.com/googleapis/python-dialogflow-cx/commit/3440f186cd879fd4ddc9b3442bf857a4f286698e))
* **v3:** BREAKING rename `UserInput.input_` to `UserInput.input` ([#58](https://www.github.com/googleapis/python-dialogflow-cx/issues/58)) ([3440f18](https://www.github.com/googleapis/python-dialogflow-cx/commit/3440f186cd879fd4ddc9b3442bf857a4f286698e))


### Documentation

* clarified documentation for security settings docs: clarified documentation for session parameters ([#89](https://www.github.com/googleapis/python-dialogflow-cx/issues/89)) ([750a055](https://www.github.com/googleapis/python-dialogflow-cx/commit/750a055b688ebeda8e8882cdb02bdc87524a69a5))
* clarified documentation for security settings docs: clarified documentation for session parameters ([#90](https://www.github.com/googleapis/python-dialogflow-cx/issues/90)) ([c1c0fb9](https://www.github.com/googleapis/python-dialogflow-cx/commit/c1c0fb9eb9e62dc794aef1bac357bb5c20e322dc))
* clarified experiment length ([20df7c3](https://www.github.com/googleapis/python-dialogflow-cx/commit/20df7c3bfabef5da23970512a3f925f4dfe7d2f9))
* clarify resource format for session response. ([20df7c3](https://www.github.com/googleapis/python-dialogflow-cx/commit/20df7c3bfabef5da23970512a3f925f4dfe7d2f9))
* Update docs on Pages, Session, Version, etc. ([20df7c3](https://www.github.com/googleapis/python-dialogflow-cx/commit/20df7c3bfabef5da23970512a3f925f4dfe7d2f9))

## [0.4.1](https://www.github.com/googleapis/python-dialogflow-cx/compare/v0.4.0...v0.4.1) (2021-03-07)


### Documentation

* fix readme ([#52](https://www.github.com/googleapis/python-dialogflow-cx/issues/52)) ([8728ad4](https://www.github.com/googleapis/python-dialogflow-cx/commit/8728ad4018bf9c976cdc469af3d8a7ec89c04671))

## [0.4.0](https://www.github.com/googleapis/python-dialogflow-cx/compare/v0.3.0...v0.4.0) (2021-03-05)


### Features

* add from_service_account_info factory ([d9bd192](https://www.github.com/googleapis/python-dialogflow-cx/commit/d9bd192a87bc8a4462da3bdbda362b359d86dd65))
* Add new Experiment service ([d9bd192](https://www.github.com/googleapis/python-dialogflow-cx/commit/d9bd192a87bc8a4462da3bdbda362b359d86dd65))
* added support for test cases and agent validation ([d9bd192](https://www.github.com/googleapis/python-dialogflow-cx/commit/d9bd192a87bc8a4462da3bdbda362b359d86dd65))
* allow to disable webhook invocation per request ([d9bd192](https://www.github.com/googleapis/python-dialogflow-cx/commit/d9bd192a87bc8a4462da3bdbda362b359d86dd65))
* supports SentimentAnalysisResult in webhook request ([d9bd192](https://www.github.com/googleapis/python-dialogflow-cx/commit/d9bd192a87bc8a4462da3bdbda362b359d86dd65))


### Documentation

* test cases doc update ([d9bd192](https://www.github.com/googleapis/python-dialogflow-cx/commit/d9bd192a87bc8a4462da3bdbda362b359d86dd65))
* update languages link ([d9bd192](https://www.github.com/googleapis/python-dialogflow-cx/commit/d9bd192a87bc8a4462da3bdbda362b359d86dd65))

## [0.3.0](https://www.github.com/googleapis/python-dialogflow-cx/compare/v0.2.0...v0.3.0) (2021-01-29)


### Features

* add experiments API ([#36](https://www.github.com/googleapis/python-dialogflow-cx/issues/36)) ([5381512](https://www.github.com/googleapis/python-dialogflow-cx/commit/5381512872ca2492ddabcbdd7ccde5f054aed011))
* allowed custom to specify webhook headers through query parameters ([#32](https://www.github.com/googleapis/python-dialogflow-cx/issues/32)) ([09919b0](https://www.github.com/googleapis/python-dialogflow-cx/commit/09919b0e45517cedcbb1d8b5b931c7317be549b2))
* allowed custom to specify webhook headers through query parameters ([#32](https://www.github.com/googleapis/python-dialogflow-cx/issues/32)) ([09919b0](https://www.github.com/googleapis/python-dialogflow-cx/commit/09919b0e45517cedcbb1d8b5b931c7317be549b2))


### Bug Fixes

* remove gRPC send/recv limit; add enums to `types/__init__.py` ([09919b0](https://www.github.com/googleapis/python-dialogflow-cx/commit/09919b0e45517cedcbb1d8b5b931c7317be549b2))

## [0.2.0](https://www.github.com/googleapis/python-dialogflow-cx/compare/v0.1.1...v0.2.0) (2020-12-07)


### Features

* add v3 ([#21](https://www.github.com/googleapis/python-dialogflow-cx/issues/21)) ([97c7fb5](https://www.github.com/googleapis/python-dialogflow-cx/commit/97c7fb53e5f6af7d8b0fea3043c60da9ee1f549b))

## [0.1.1](https://www.github.com/googleapis/python-dialogflow-cx/compare/v0.1.0...v0.1.1) (2020-11-17)


### Bug Fixes

* corrects the repo/homepage link ([#15](https://www.github.com/googleapis/python-dialogflow-cx/issues/15)) ([c26852d](https://www.github.com/googleapis/python-dialogflow-cx/commit/c26852d8a3738eb4d67222c555d0197a854e68a9))


### Documentation

* **samples:** add initial sample codes ([#13](https://www.github.com/googleapis/python-dialogflow-cx/issues/13)) ([b590308](https://www.github.com/googleapis/python-dialogflow-cx/commit/b590308b79a230561aed776f55260a73668c8efc)), closes [#12](https://www.github.com/googleapis/python-dialogflow-cx/issues/12)

## 0.1.0 (2020-08-24)


### Features

* generate v3beta1 ([0c6e3a9](https://www.github.com/googleapis/python-dialogflow-cx/commit/0c6e3a9ff1a38f6d6c5f8c2983cbfa1f7ff7536d))
