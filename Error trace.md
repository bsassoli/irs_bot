(irs_bot) ➜  irs_bot git:(additions) ✗ uv run src/irs_bot/app.py  
Traceback (most recent call last):
  File "/Users/bernardino/projects/irs_bot/src/irs_bot/app.py", line 260, in <module>
    main()
  File "/Users/bernardino/projects/irs_bot/src/irs_bot/app.py", line 248, in main
    add_documents_to_chromadb(collection, documents)
  File "/Users/bernardino/projects/irs_bot/src/irs_bot/app.py", line 122, in add_documents_to_chromadb
    collection.add(
  File "/Users/bernardino/projects/irs_bot/.venv/lib/python3.11/site-packages/chromadb/api/models/Collection.py", line 80, in add
    add_request = self._validate_and_prepare_add_request(
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/bernardino/projects/irs_bot/.venv/lib/python3.11/site-packages/chromadb/api/models/CollectionCommon.py", line 95, in wrapper
    return func(self, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/bernardino/projects/irs_bot/.venv/lib/python3.11/site-packages/chromadb/api/models/CollectionCommon.py", line 236, in _validate_and_prepare_add_request
    add_embeddings = self._embed_record_set(record_set=add_records)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/bernardino/projects/irs_bot/.venv/lib/python3.11/site-packages/chromadb/api/models/CollectionCommon.py", line 558, in _embed_record_set
    return self._embed(input=record_set[field])  # type: ignore[literal-required]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/bernardino/projects/irs_bot/.venv/lib/python3.11/site-packages/chromadb/api/models/CollectionCommon.py", line 571, in _embed
    return self._embedding_function(input=input)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/bernardino/projects/irs_bot/.venv/lib/python3.11/site-packages/chromadb/api/types.py", line 489, in __call__
    result = call(self, input)
             ^^^^^^^^^^^^^^^^^
  File "/Users/bernardino/projects/irs_bot/.venv/lib/python3.11/site-packages/chromadb/utils/embedding_functions/openai_embedding_function.py", line 119, in __call__
    response = self.client.embeddings.create(**embedding_params)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/bernardino/projects/irs_bot/.venv/lib/python3.11/site-packages/openai/resources/embeddings.py", line 128, in create
    return self._post(
           ^^^^^^^^^^^
  File "/Users/bernardino/projects/irs_bot/.venv/lib/python3.11/site-packages/openai/_base_client.py", line 1276, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/bernardino/projects/irs_bot/.venv/lib/python3.11/site-packages/openai/_base_client.py", line 949, in request
    return self._request(
           ^^^^^^^^^^^^^^
  File "/Users/bernardino/projects/irs_bot/.venv/lib/python3.11/site-packages/openai/_base_client.py", line 1057, in _request
    raise self._make_status_error_from_response(err.response) from None
openai.BadRequestError: Error code: 400 - {'error': {'message': "'$.input' is invalid. Please check the API reference: https://platform.openai.com/docs/api-reference.", 'type': 'invalid_request_error', 'param': None, 'code': None}} in add.