---
type: note/component
date created: Friday, October 11th 2024, 4:13:40 pm
date modified: Friday, October 11th 2024, 4:18:31 pm
---
[summary:: Lets you provide a substitute or placeholder for another object. Proxy controls access to the original object, allowing you to perform something either before or after the request gets through to the original object. ]
down:: [[DP Virtual Proxy]], [[DP Protection Proxy]], [[DP Remote Proxy]], [[DP Logging Proxy]], [[DP Caching Proxy]]
similar:: [[DP Facade]], [[DP Decorator]]

- May be very useful if you have a massive object and you only need it from time to time. Instead, you can create a proxy that passes all the original object's clients. Upon receiving a request from a client, the proxy creates a real service object and delegates all the work to it.  
Pros:
- You can control the service object without clients knowing about it.
- You can manage the lifecycle of the service object when clients don’t care about it.
- The proxy works even if the service object isn’t ready or is not available.
- Open/Closed Principle. You can introduce new proxies without changing the service or clients

Cons:
- Code may become more complicated, since you need more classes
- Response from the service may be delayed. 

Different from a decorator in that the proxy typically manages the life cycle of its service object on its own, whereas the composition of the decorators is always controlled by the client. 

[Proxy](https://refactoring.guru/design-patterns/proxy)
![[DP Proxy.png | 400]]