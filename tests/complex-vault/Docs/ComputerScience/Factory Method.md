---
summary:
type: note/concept
headings:
  - "[[#Concepts of Note]]"
  - "[[#Diagrams]]"
  - "[[#Examples]]"
  - "[[#Usage]]"
examples:
  - "[[Cpp Factory Method (example)]]"
similar:
  - "[[Template Method]]"
next:
  - "[[Abstract Factory]]"
concept_of:
  - "[[DP Creational Patterns]]"
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Tuesday, March 3rd 2026, 12:39:00 pm
implementations:
  - "[[Cpp Class overloading constructors]]"
tags: [cs/design_pattern/behavioral/template-method, cs/design_pattern/creational/factory]
template:
template-version:
uses:
  - "[[Cpp Class virtual functions]]"
  - "[[Prototype|DP Clone]]"
---

# Summary
󰙎 Factory Method ;;; Replace direct object construction calls with calls to a factory method. Put simply, define ctor steps 1, 3, and 4--leave step 2 up to concrete implementations. 

# Additional Background

## Concepts of Note
- Replace direct object construction calls with factory method, which calls `new` for you. 
- Really helpful when you have a class (i.e. `Truck`) that you want to extend into something else (i.e. `Wagon`)
	- Instead, replace direct object construction calls with a factory method. Allows overriding factory method in a subclass and changing the class of products being created.

See [[Template Method]] for something that *does* a thing rather than *build* a thing.

󰙎  Products ;;; Objects returned to you by the factory method

### Use cases
- When you want to provide a way forward to extend your framework/library
- When you aren't sure what dependencies your code should deal with ahead of time.

### Pros/Cons
- Pros:
	- You avoid tight coupling between creator and concrete products
	- Single responsibility principle: creation code is in one place in the program
	- Open/closed principle: Introduce new types of products into the program without breaking existing client code.
- Cons:
	- Code may become more complicated since you need to introduce new subclasses to implement the pattern. Best case scenario is when you're introducing the pattern into an existing hierarchy of creator classes.

## Usage


## Diagrams
![[DP Factory Method-1.png | 550]]


![[DP Factory Method-2.png| 750]]
1. The **Product** declares the interface, which is common to all objects that can be produced by the creator and its subclasses.
2. **Concrete Products** are different implementations of the product interface.
3. The **Creator** class declares the factory method that returns new product objects. It’s important that the return type of this method matches the product interface.
	- You can declare the factory method as `abstract` to force all subclasses to implement their own versions of the method. As an alternative, the base factory method can return some default product type.
	- Note, despite its name, product creation is **not** the primary responsibility of the creator. Usually, the creator class already has some core business logic related to products. The factory method helps to decouple this logic from the concrete product classes. Here is an analogy: a large software development company can have a training department for programmers. However, the primary function of the company as a whole is still writing code, not producing programmers.
4. **Concrete Creators** override the base factory method so it returns a different type of product.
Note that the factory method doesn’t have to **create** new instances all the time. It can also return existing objects from a cache, an object pool, or another source.

## Flashcards

STARTI [Basic] What type of design pattern is this? 
![[DP Factory Method-1.png]] Back: Factory method <!--ID: 1758253289601--> ENDI
STARTI [Basic] What type of design pattern is this?
![[DP Factory Method-2.png]] Back: Factory method <!--ID: 1758253289607--> ENDI
󰠗  When should you use the Factory Method pattern? ;; 1. When you don't know the exact types/dependencies of the objects your code should work with; 2. When you want to provide users of your library/framework with a way to extend internal components; 3. To save system resources by reusing existing objects over rebuilding them each time. = 
󰠗  What are the steps to implement a factory method in a codebase? ;; 1, Make sure all products follow the same interface (declare methods that make sense for every product). 
      2, Add an empty factory method inside the creator class, with the return type matching common product interface
      3, In creator's code, find all references to product constructors. Replace them with calls to the factory method, while extracting the product creation code into the factory method. 
      4, Create a set of creator subclasses for each type of product listed in the factory method. Override the factory method in subclasses, extracting appropriate bits of construction from base method
      5, If too many product types, reuse the control parameter from the base class in subclasses.  
󰠗  What is the Factory method a specialization of? ;; The template method. The Factory method can also serve as step in a large template method. =
<!--ID: 1758253289614-->

         

## Examples %% fold %% 

`main.cpp`
```cpp
/**
 * The Product interface declares the operations that all concrete products must
 * implement.
 */

class Product {
 public:
  virtual ~Product() {}
  virtual std::string Operation() const = 0;
};

/**
 * Concrete Products provide various implementations of the Product interface.
 */
class ConcreteProduct1 : public Product {
 public:
  std::string Operation() const override {
    return "{Result of the ConcreteProduct1}";
  }
};
class ConcreteProduct2 : public Product {
 public:
  std::string Operation() const override {
    return "{Result of the ConcreteProduct2}";
  }
};

/**
 * The Creator class declares the factory method that is supposed to return an
 * object of a Product class. The Creator's subclasses usually provide the
 * implementation of this method.
 */

class Creator {
  /**
   * Note that the Creator may also provide some default implementation of the
   * factory method.
   */
 public:
  virtual ~Creator(){};
  virtual Product* FactoryMethod() const = 0;
  /**
   * Also note that, despite its name, the Creator's primary responsibility is
   * not creating products. Usually, it contains some core business logic that
   * relies on Product objects, returned by the factory method. Subclasses can
   * indirectly change that business logic by overriding the factory method and
   * returning a different type of product from it.
   */

  std::string SomeOperation() const {
    // Call the factory method to create a Product object.
    Product* product = this->FactoryMethod();
    // Now, use the product.
    std::string result = "Creator: The same creator's code has just worked with " + product->Operation();
    delete product;
    return result;
  }
};

/**
 * Concrete Creators override the factory method in order to change the
 * resulting product's type.
 */
class ConcreteCreator1 : public Creator {
  /**
   * Note that the signature of the method still uses the abstract product type,
   * even though the concrete product is actually returned from the method. This
   * way the Creator can stay independent of concrete product classes.
   */
 public:
  Product* FactoryMethod() const override {
    return new ConcreteProduct1();
  }
};

class ConcreteCreator2 : public Creator {
 public:
  Product* FactoryMethod() const override {
    return new ConcreteProduct2();
  }
};

/**
 * The client code works with an instance of a concrete creator, albeit through
 * its base interface. As long as the client keeps working with the creator via
 * the base interface, you can pass it any creator's subclass.
 */
void ClientCode(const Creator& creator) {
  // ...
  std::cout << "Client: I'm not aware of the creator's class, but it still works.\n"
            << creator.SomeOperation() << std::endl;
  // ...
}

/**
 * The Application picks a creator's type depending on the configuration or
 * environment.
 */

int main() {
  std::cout << "App: Launched with the ConcreteCreator1.\n";
  Creator* creator = new ConcreteCreator1();
  ClientCode(*creator);
  std::cout << std::endl;
  std::cout << "App: Launched with the ConcreteCreator2.\n";
  Creator* creator2 = new ConcreteCreator2();
  ClientCode(*creator2);

  delete creator;
  delete creator2;
  return 0;
}
```

Output.txt
```
App: Launched with the ConcreteCreator1.
Client: I'm not aware of the creator's class, but it still works.
Creator: The same creator's code has just worked with {Result of the ConcreteProduct1}

App: Launched with the ConcreteCreator2.
Client: I'm not aware of the creator's class, but it still works.
Creator: The same creator's code has just worked with {Result of the ConcreteProduct2}
```

