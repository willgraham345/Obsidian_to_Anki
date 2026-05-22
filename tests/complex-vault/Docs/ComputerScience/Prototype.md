---
summary: Lets you clone objects without coupling code to the class of the object, letting you create instances and carrying over all field values. Very helpful when you have private members that can't easily be cloned. It also abstracts your code away from the "how" of cloning an object.
headings: ["[[#Concepts of Note]]", "[[#Diagrams]]", "[[#Examples]]"]
type: note/concept
similar: ["[[DP Memento]]"]
aliases: [DP Clone]
concept_of: ["[[DP Creational Patterns]]"]
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: sday, September 25th 2025, 11:49:58 am
images: ["[[DP Prototype 2.png]]", "[[DP Prototype.png]]"]
used_by: ["[[DP Composite]]", "[[DP Decorator]]", "[[Factory Method]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Concepts of Note

### Use cases:
- Easily clone objects, especially when those objects may have private fields.
- Most programming languages let you access private fields of other objects belonging to the same class. 

### Pros/Cons
- Pros
	- Clone objects without coupling to concrete classes
	- Get rid of repeated initialization code
	- Produce complex objects more easily
	- Alternative to inheritance when dealing with configuration presets
- Cons
	- Cloning complex objects may have circular references, which can be tricky.
![[DP Prototype 2.png| 500]]
1. The **Prototype** interface declares the cloning methods. In most cases, it’s a single `clone` method.
2. The **Concrete Prototype** class implements the cloning method. In addition to copying the original object’s data to the clone, this method may also handle some edge cases of the cloning process related to cloning linked objects, untangling recursive dependencies, etc.
3. The **Client** can produce a copy of any object that follows the prototype interface.

### Prototype Registry Implementation
1. The **Prototype Registry** provides an easy way to access frequently-used prototypes. It stores a set of pre-built objects that are ready to be copied. The simplest prototype registry is a `name → prototype` hash map. However, if you need better search criteria than a simple name, you can build a much more robust version of the registry.

### Relation to other patterns
- [[Abstract Factory]] can use prototypes to compose [[Factory Method]]s
- Can help when you need to save [[DP Command]]s into history

- Simpler version of Memento

## Diagrams

![[DP Prototype.png| 600]]

## Flashcards
󰠗  When using the Composite and Decorator design patterns, what design pattern can help you clone complex structures rather than re-constructing them from scratch? ;; The prototype = #cs/design_pattern/creational/prototype #cs/design_pattern/structural/decorator #cs/design_pattern/structural/composite
<!--ID: 1759154339912-->

󰠗  What design pattern is useful when you want to save Commands into history? ;; The Prototype = #cs/design_pattern/creational/prototype #cs/design_pattern/behavioral/command
<!--ID: 1759154339916-->

󰠗  What design pattern is helpful when your code shouldn't depend on the concrete classes of objects that you need to copy? ;; The prototype = #cs/design_pattern/creational/prototype 
<!--ID: 1759154339921-->

󰠗  What design pattern should you sue when you want to reduce the number of subclasses that only differ in the way they initialize their respective objects? ;; The prototype = #cs/design_pattern/creational/prototype 
<!--ID: 1759154339925-->


## Examples %% fold %% 


```cpp
using std::string;

// Prototype Design Pattern
//
// Intent: Lets you copy existing objects without making your code dependent on
// their classes.

enum Type {
  PROTOTYPE_1 = 0,
  PROTOTYPE_2
};

/**
 * The example class that has cloning ability. We'll see how the values of field
 * with different types will be cloned.
 */

class Prototype {
 protected:
  string prototype_name_;
  float prototype_field_;

 public:
  Prototype() {}
  Prototype(string prototype_name)
      : prototype_name_(prototype_name) {
  }
  virtual ~Prototype() {}
  virtual Prototype *Clone() const = 0;
  virtual void Method(float prototype_field) {
    this->prototype_field_ = prototype_field;
    std::cout << "Call Method from " << prototype_name_ << " with field : " << prototype_field << std::endl;
  }
};

/**
 * ConcretePrototype1 is a Sub-Class of Prototype and implement the Clone Method
 * In this example all data members of Prototype Class are in the Stack. If you
 * have pointers in your properties for ex: String* name_ ,you will need to
 * implement the Copy-Constructor to make sure you have a deep copy from the
 * clone method
 */

class ConcretePrototype1 : public Prototype {
 private:
  float concrete_prototype_field1_;

 public:
  ConcretePrototype1(string prototype_name, float concrete_prototype_field)
      : Prototype(prototype_name), concrete_prototype_field1_(concrete_prototype_field) {
  }

  /**
   * Notice that Clone method return a Pointer to a new ConcretePrototype1
   * replica. so, the client (who call the clone method) has the responsability
   * to free that memory. If you have smart pointer knowledge you may prefer to
   * use unique_pointer here.
   */
  Prototype *Clone() const override {
    return new ConcretePrototype1(*this);
  }
};

class ConcretePrototype2 : public Prototype {
 private:
  float concrete_prototype_field2_;

 public:
  ConcretePrototype2(string prototype_name, float concrete_prototype_field)
      : Prototype(prototype_name), concrete_prototype_field2_(concrete_prototype_field) {
  }
  Prototype *Clone() const override {
    return new ConcretePrototype2(*this);
  }
};

/**
 * In PrototypeFactory you have two concrete prototypes, one for each concrete
 * prototype class, so each time you want to create a bullet , you can use the
 * existing ones and clone those.
 */

class PrototypeFactory {
 private:
  std::unordered_map<Type, Prototype *, std::hash<int>> prototypes_;

 public:
  PrototypeFactory() {
    prototypes_[Type::PROTOTYPE_1] = new ConcretePrototype1("PROTOTYPE_1 ", 50.f);
    prototypes_[Type::PROTOTYPE_2] = new ConcretePrototype2("PROTOTYPE_2 ", 60.f);
  }

  /**
   * Be carefull of free all memory allocated. Again, if you have smart pointers
   * knowelege will be better to use it here.
   */

  ~PrototypeFactory() {
    delete prototypes_[Type::PROTOTYPE_1];
    delete prototypes_[Type::PROTOTYPE_2];
  }

  /**
   * Notice here that you just need to specify the type of the prototype you
   * want and the method will create from the object with this type.
   */
  Prototype *CreatePrototype(Type type) {
    return prototypes_[type]->Clone();
  }
};

void Client(PrototypeFactory &prototype_factory) {
  std::cout << "Let's create a Prototype 1\n";

  Prototype *prototype = prototype_factory.CreatePrototype(Type::PROTOTYPE_1);
  prototype->Method(90);
  delete prototype;

  std::cout << "\n";

  std::cout << "Let's create a Prototype 2 \n";

  prototype = prototype_factory.CreatePrototype(Type::PROTOTYPE_2);
  prototype->Method(10);

  delete prototype;
}

int main() {
  PrototypeFactory *prototype_factory = new PrototypeFactory();
  Client(*prototype_factory);
  delete prototype_factory;

  return 0;
}
```

Output
```
Let's create a Prototype 1
Call Method from PROTOTYPE_1  with field : 90

Let's create a Prototype 2 
Call Method from PROTOTYPE_2  with field : 10
```
