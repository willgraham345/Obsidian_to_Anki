---
summary: Single responsibility, open-closed, Substitution, interface segregation, dependency inversion/injection
type: note/concept
headings:
  - "[[#Concepts of Note]]"
  - "[[#Examples]]"
concepts:
  - "[[DP Testing Dependency Injection]]"
concept_of:
  - "[[Design Patterns]]"
date created: Monday, October 7th 2024, 12:11:17 pm
date modified: Friday, March 20th 2026, 5:42:55 pm
tags: [cs/design_pattern/solid-principles]
template:
template-version:
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

[Design Principles — C++ Design Patterns 0.0.1 documentation](https://cpp-design-patterns.readthedocs.io/en/latest/principles.html)

## Concepts of Note
󰙎  Single responsibility principle ;;; A class should only have a single responsibility. 

󰙎  Open-closed principle ;;; Entities should open for extension but closed for modification. 

󰙎  Liskov substitution principle ;;; Objects should be replaceable with instances of their subtypes without altering program correctness. Essentially, `process(Rectangle)` should be just as valid as `process(Square)`.

󰙎  Interface segregation principle ;;; Many client-specific interfaces is better than one general-purpose interface. 
󰙎  Dependency inversion/injection ;;; Dependencies should be abstract rather than concrete. High level modules should *not* rely on low-level modules, but rather both should depend on abstractions. Abstractions should also not depend on details, details should depend on abstractions. 

### Extras
 Law of demeter ;;; Don't talk to strangers (i.e. If your class `A` owns a reference to `B`, don't call `B.doThing().secondCall()`. Only do `B.doThing()`)

## Examples
### Interface segregation principle
```cpp
  Printer printer;
  Scanner scanner;
  Machine machine(printer, scanner);
  std::vector<Document> documents{Document(std::string("Hello")),
                                  Document(std::string("Hello"))};
  machine.print(documents);
  machine.scan(documents);
```

### Dependency inversion/injection
```cpp
// without DI
  std::cout << "without DI\n";
  auto e1 = std::make_shared<Engine>();
  auto logger1 = std::make_shared<ConsoleLogger>();
  auto c1 = std::make_shared<Car>(e1, logger1);
  std::cout << *c1 << std::endl;

  // with DI
  std::cout << "with DI\n";
  using namespace boost;
  // whenever an ILogger is needed a ConsoleLogger instance will be created
  auto injector = di::make_injector(di::bind<ILogger>().to<ConsoleLogger>());
  // engine created with default constructor
  auto c = injector.create<std::shared_ptr<Car>>();

  std::cout << *c << std::endl;
```

