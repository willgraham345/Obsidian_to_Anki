---
summary: Mechanism for us to set up and tear down common data and objects required by multiple tests within a test suite. Helpful for code reuse.
headings:
  - "[[#Examples]]"
  - "[[#Usage]]"
type: note/component
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Wednesday, June 25th 2025, 12:34:38 pm
concept_of:
  - "[[Cpp GoogleTest|Cpp gtest]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Usage
### Create a Fixture
1. Derive a class from `testing::Test`
	- Start its body with `protected:`, so you can access fixture members from sub-classes.
2. Declare any objects you plan to use
3. If needed: 
	4. write a default constructor `SetUp()` to prepare objects for each test. 
	5. Write a destructor `TearDown()` to release any allocated resources
	6. Define subroutines for tests to share

## Examples
### FIFO queue
Class Interface
```cpp
template <typename E>  // E is the element type.
class Queue {
 public:
  Queue();
  void Enqueue(const E& element);
  E* Dequeue();  // Returns NULL if the queue is empty.
  size_t size() const;
  ...
};
```
Fixture Class
```cpp
class QueueTest : public testing::Test {
 protected:
  QueueTest() {
     // q0_ remains empty
     q1_.Enqueue(1);
     q2_.Enqueue(2);
     q2_.Enqueue(3);
  }

  // ~QueueTest() override = default;

  Queue<int> q0_;
  Queue<int> q1_;
  Queue<int> q2_;
};
```
Fixture
```cpp
TEST_F(QueueTest, IsEmptyInitially) {
  EXPECT_EQ(q0_.size(), 0);
}

TEST_F(QueueTest, DequeueWorks) {
  int* n = q0_.Dequeue();
  EXPECT_EQ(n, nullptr);

  n = q1_.Dequeue();
  ASSERT_NE(n, nullptr);
  EXPECT_EQ(*n, 1);
  EXPECT_EQ(q1_.size(), 0);
  delete n;

  n = q2_.Dequeue();
  ASSERT_NE(n, nullptr);
  EXPECT_EQ(*n, 2);
  EXPECT_EQ(q2_.size(), 1);
  delete n;
}
```
What these tests do:
1. GoogleTest makes a `QueueTest` object (`t1`)
2. First test (`IsEmptyInitially`) runs on `t1`
3. `t1` is destructed
4. Repeat on another `QueueTest` object, running `DequeueWorks`