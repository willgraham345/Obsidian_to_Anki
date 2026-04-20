---
title: "flatbuffers/rust/flexbuffers at master · google/flatbuffers"
source: "https://github.com/google/flatbuffers/tree/master/rust/flexbuffers"
author:
  - "[[dbaileychess]]"
published:
created: 2025-09-02
description: "FlatBuffers: Memory Efficient Serialization Library - flatbuffers/rust/flexbuffers at master · google/flatbuffers"
tags:
  - "clippings"
  - "toread"
---
[Skip to content](https://github.com/google/flatbuffers/tree/master/rust/#start-of-content)

[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](https://github.com/codespaces/new/google/flatbuffers/tree/master?resume=1)

## Latest commit

[1c51462](https://github.com/google/flatbuffers/commit/1c514626e83c20fffa8557e75641848e1e15cd5e) ·

## flexbuffers

## README.md

## Flexbuffers

[Flexbuffers](https://google.github.io/flatbuffers/flexbuffers.html) is a schema-less binary format developed at Google. FlexBuffers can be accessed without parsing, copying, or allocation. This is a huge win for efficiency, memory friendly-ness, and allows for unique use cases such as mmap-ing large amounts of free-form data.

FlexBuffers' design and implementation allows for a very compact encoding, with automatic sizing of containers to their smallest possible representation (8/16/32/64 bits). Many values and offsets can be encoded in just 8 bits.

FlexBuffers supports [Serde](https://serde.rs/) for automatically serializing Rust data structures into its binary format.

- [Example](https://github.com/google/flatbuffers/blob/master/samples/sample_flexbuffers.rs)
- [Serde Example](https://github.com/google/flatbuffers/blob/master/samples/sample_flexbuffers_serde.rs)
- [Documentation](https://docs.rs/flexbuffers)

Flexbuffers is the schema-less cousin of [Flatbuffers](https://google.github.io/flatbuffers/).