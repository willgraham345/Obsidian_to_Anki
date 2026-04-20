---
title: "Software Design Patterns For Real Hardware"
source: "https://hackaday.com/2018/01/12/software-design-patterns-for-real-hardware/"
author:
  - "[[by:                Sonya Vasquez]]"
  - "[[Sonya Vasquez]]"
published: 2018-01-12
created: 2025-09-23
description: "Here on Hackaday, we’re generally designers of hacks that live in the real world. Nevertheless, I’m convinced that some of the most interesting feats are at the mercy of what’s po…"
tags:
  - "clippings"
  - "toread"
---
Here on Hackaday, we’re generally designers of hacks that live in the real world. Nevertheless, I’m convinced that some of the most interesting feats are at the mercy of what’s possible in software, not hardware. Without the right software, no 3D printer could print and no quadcopter could fly. The source code that drives these machines may take months of refinement to flesh out their structure. In a nutshell, these software packages are complicated, and they don’t happen overnight.

So how *do* they happen; better yet: how could *we* make that happen? How do we write software that’s flexible enough to coexist peacefully on all sorts of hardware variations?

What separates the big open-source software projects like ROS, LinuxCNC, and Multiwii from the occastional hackathon code are the underlying principles that govern how they’re written. In object-oriented programming, these principles are called *design patterns*. In the next couple posts, I’m going to crack the lid on a few of these. What’s more, I’ll package them into real-world examples so that we can see these patterns interact with real hardware. The next time you pop open the source code for a big open source hardware project, I hope you can tease out some of these patterns in the code. Better yet, I hope you carry these patterns into your next robot and machine project. Let’s get started.

For readability, all of the examples run in Python3. The snippets below are truncated for brevity, but the real examples [in the repository](https://github.com/Poofjunior/object_oriented_hardware) will work if you’ve got a similar hardware setup.

## Software Prophets of Yore

Before jumping in, I need to promise you that these design patterns aren’t mine. In fact, most of them are decades old. If you’re curious, check out the book: [*Design Patterns*](https://en.wikipedia.org/wiki/Design_Patterns), written by a group of authors who’s names are so hard to remember that we shall collectively refer to them as “the Big Four.” For many software engineers, this book stands as the feature-complete reference for object-oriented design patterns, and it’s rock solid. I thought about delivering this post as a book review where I’d drool over all the swanky software patterns that you could put in your next blinky project. The problem? No blinkies! In fact, the entire book builds examples around writing a graphical document editor. For us hardware monkeys, that’s boring and bordering on unacceptable!

With that in mind, I’ll be presenting the words of the wise embellished with the proper treatment of real-world hardware.

## Getting the Most from these Examples

Now for the unanswered question: who are these examples for? Hackaday readers come in all flavors. In writing this piece, I’m hoping to bridge two communities: the software folk eager to dabble in hardware and the hardware folk hungry to write better software. For the software folks, these examples are here to showcase what you already know and give them some real hardware context. For the hardware folks, these design patterns are here to muscle-up your toolbox of software techniques with sensors you’ve likely seen before.

To set the base line for getting the most out of what comes next, I’ll assume two things. (1) You’ve had a taste of object-oriented programming by writing a few classes in Python, and (2) you understand the basics of [class inheritance](https://www.programiz.com/python-programming/inheritance). We’ll be building on more advanced types of inheritance in the coming examples.

## Getting Cozy with the Hardware

Today I’ll get us warmed up with our design patterns by reading a variety of temperature sensors. The plan? I need a code base that provides me with a way to easily read two different temperature sensor types: a thermocouple and a thermistor. The key ideas behind this are three-fold:

- isolate behavior that can stand on it’s own.
- hide (with abstraction) details that are unnecessary for the end-user.
- don’t repeat yourself; share behaviors by following the first clause.

At first, it might seem like we’re just writing a few drivers to read a few temperature sensors. In reality, we have to think at a higher level! Lets ask ourselves: “what’s the core feature that our software provides? How might someone else with a different setup adapt this code to get that same core feature without having to rewrite it?” In our case, we’re providing a common way of performing temperature measurement with a path for expansion to other temperature sensors.

Without further ado, I present today’s hardware setups.

![](https://hackaday.com/wp-content/uploads/2017/12/39490402881_bc735e522c_k.jpg)

Thermocouple Setup

The first setup is a Beaglebone set to read an off-the-shelf I2C-based analog-to-digital converter that’s reading a Thermocouple amplifier.

![](https://hackaday.com/wp-content/uploads/2017/12/27714602659_f2c986095d_k.jpg)

Thermistor Setup

The second setup is Beaglebone set to read the same I2C-based analog-to-digital converter that’s now reading a voltage-divider setup with a thermistor.

With the real hardware in mind, let’s now discuss our design patterns as we build up a flexible codebase to read both sensors.

## Polymorphism

We start by teasing out the underlying objects that will comprise our system. First off, we have two separate real-world sensors, both of which mandate a different way of being read as input. Next, we also know that, although these sensors require slightly-different setups, they’re both measuring the same thing: temperature!

With that in mind, let’s write out some requirements. Let’s say that we need to:

1. isolate device-specific behaviors that are needed to read a particular sensor.
2. provide a common software interface for reading the temperature regardless of temperature sensor type.

Given the requirements, it sounds like we want to write two separate classes, each with specific behavior for reading temperature data. It also sounds like we should make sure that we’re consistent in naming conventions for reading the temperature. Let’s say we write a class for each sensor.

```python
classThermistor:
...
    defread_temperature_c(self):
        # thermistor-specific details here
```

```python
classAD8495ThermocoupleAmplifier:
...
    defread_temperature_c(self):
    # thermocouple-specific details here
```

Here we’ve mocked up something that does just that. Device-specific behavior is wrapped into classes, and all our temperature-reading methods have the same name. We’re done, right?

While this idea works, it’s a bit naive. In the source code above, we’re under no design contract to give these methods the same name. Heck, we could call one **read\_temp**  and another **hi\_mom**, and no one can stop us–not even our mothers! Lucky for us, we can use a design pattern to enforce that these methods be named identically.

Looking at our problem, we have two different types of temperature sensors, but, by golly, I just want a consistent way to ask for the temperature from each of them. Behold, Polymorphism with abstract base classes. Polymorphism is a design pattern that promises a common interface to entities that may not all be the same type. Here, we have three different sensor classes. Polymorphism can ensure that they all use the same method to read out the temperature.

To implement polymorphism, we use an abstract base class. An abstract base class is a special type of base class that can’t stand on it’s own. It *needs* to be inherited. In fact, if we try to instantiate the base class by itself, Python will throw an error. Abstract base classes have one extra bonus feature: abstract methods. These are placeholder methods declared in the abstract base class that don’t do anything. Instead, they serve as tags and force the derived class to define them. If we try to instantiate an child class of the abstract base class without defining all the abstract methods, Python will also throw an error.

With two new ways to throw errors, it’s worth asking: “what’s the benefit of constraining ourselves this way?” It turns out that these constraints are actually a way of making a promise. Here, we’re promising that each child class we write for our temperature sensors will define any abstract methods in the base class.

Since both of these temperature sensors is just that–a type of temperature sensor–we’ll use TemperatureSensor as our base class name.

```python
fromabc importabstractmethod, ABCMeta # abstract base class library tools
 
classTemperatureSensor(object, metaclass=ABCMeta):
...
     @abstractmethod
     defread_temperature_c(self): 
        &quot;&quot;&quot;
        returns the temperature inCelsius
        &quot;&quot;&quot; 
     pass
```

Above is the Python3 way for defining an abstract base class. Here, the method **read\_temperature\_c** is just a placeholder. We don’t need to define what it does here because the details are specific to our sensors. Here we just declare it and decorate it with the **@abstractmethod** decorator to tell Python that any child class of TemperatureSensor  *must* define the  **read\_temperature\_c** method.

To finish this example, lets make our Thermistor class inherit our abstract base class:

```python
classThermistor(TemperatureSensor):
...
    defread_temperature_k(self):
        &quot;&quot;&quot;
        returns the temperature inKelvin
        &quot;&quot;&quot;
        voltage_v =self.voltage_input.read()
        r1_ohms =self._read_resistance(voltage_v)
        return(1/298.15+1/self.b *log(r1_ohms/self.thermistor_ohms))**(-1)
 
    defread_temperature_c(self):
        returnself.read_temperature_k() -273.15
```

First, notice that our Thermistor class inherits our TemperatureSensor class. We’re telling our users: “hey, this is a Thermistor class, but you can read it like a TemperatureSensor.” It also tells us, the writers, “hey, I’m promising to define a **read\_temperature\_c** method.” Finally, we just write out all the code necessary for reading a thermistor and converting it to Celsius. And that’s it!

Let’s take a step back and think about why this is powerful. Our user could be someone who might not know a thing about how thermistors work, but they can still take measurements with the generic **read\_temperature\_c** method. Encapsulating domain-specific information is exactly what we want to do here such that our users don’t need to know every detail about our software stack to get something working. Here, our code is hiding he messy details of converting a resistance to a temperature from a polynomial-fitted line. By hiding those details, we enable them to move on to the next step and write some interesting temperature sensing applications.

## Bridges

In the last section, we blew past one line without discussing it.

```python
voltage_v =self.voltage_input.read()
```

Fear not! We’ll cover that part now.

At this point, we’ve got a common interface to ask for the temperature, but we could have dozens of different ways to actually collect the raw data. How do we write a single class that properly encapsulates the details of each temperature sensor without getting to heavily committed to the downstream devices necessary for reading them?

To get a better picture of the problem, let’s have another look at a block diagram of our physical hardware:

![](https://hackaday.com/wp-content/uploads/2018/01/ad8495_hardware_setup1-rethemed.png?w=800)

But that’s not our only possible configuration. Since I’m using a Beaglebone in these examples, I could also use the built-in ADC on the BeagleBone ARM chip itself. That hardware configuration might look like this:

![](https://hackaday.com/wp-content/uploads/2018/01/thermistor_direct_adc_setup1-rethemed.png?w=800)

What we need to write is a series of classes for our setup that somehow *detach* the thermocouple from the extra hardware that’s being used to read it. To do so, we need to decide what components are specifically necessary for reading this thermocouple and what components can be replaced without changing the end-to-end system behavior. In this case, our AD8495 is tightly coupled with the thermocouple. Without it, we just can’t read it at all! On the other hand, that ADS1015 is just a vanilla analog-to-digital converter. Heck, we could replace it with any A-to-D, and we would still get our thermocouple measurements. For this reason, we’ll start off by writing two classes: a class that encapsulates the AD8495 behavior and a class to handle the analog interface.

![](https://hackaday.com/wp-content/uploads/2018/01/thermocouple_sw_block_diagram1-rethemed.png?w=455)

Now’s a great time to map out our software with a block diagram to get a picture of the code we’ll be writing. As a heads-up: these diagrams aren’t certified “UML class diagrams”; rather, for clarity’s sake, I’ve doodled up a simplification.

Let’s have a look at the block diagram on the left. These boxes represent the relationship between classes. Boxes-within-boxes represent inheritance. We call this the “ [is-a](https://en.wikipedia.org/wiki/Is-a) ” relationship. Arrows from one box to another represent a class attribute that happens to be another class. We call this the “ [has-a](https://en.wikipedia.org/wiki/Has-a) ” relationship.

In our block diagram, the AD8495TCAmplifier *is a* TemperatureSensor because it inherits from the TemperatureSensor class. (That’s the Polymorphism we described above.) The AD8495TCAmplifier also  *has a* VoltageInputInterface. In other words, our AD8495TCAmplifier owns a reference to another class that we can invoke with **self.voltage\_input** (mentioned earlier).

So what exactly is that VoltageInputInterface class, and how does it interact with the real world? Well, the short answer is that it *depends* on our hardware setup! In the first setup, the VoltageInputInterface is one of the four available analog inputs on the AD1015 A-to-D. On the second input, the VoltageInputInterface is a single pin on the Beaglebone’s exposed analog port. In all cases though, each VoltageInputInterface needs to provide a **read** method that does the actual work of reading a single analog input and returning the value in volts. How might we guarantee that? With an abstract base class like we did in the previous section! Now that we understand the relationship, we can refine our software block diagram with both optional setups.

![](https://hackaday.com/wp-content/uploads/2018/01/bridge_sw_block_diagram_options2-rethemed.png?w=800)

Notice how, in both diagrams, the AD8495TCAmplifier owns a different subclass of a VoltageInputInterface, but it treats them like a vanilla VoltageInputInterface. Even though the underlying class is different, we can still treat identically by using the base class **read** method.

What we’re describing is the *bridge* *design pattern*. The  *bridge*, according to the Gang-of-Four, is meant to “decouple an abstraction from its implementation so that the two can vary independently.” Here, our abstraction is a single analog input. Since there are various ways of providing our Beaglebone with an analog input, we need an abstraction such that we can address all sorts of ADC hardware the same way.

This design pattern is rather similar to Polymorphism, which I described first. In fact, just like before, we’ll use Python’s abstract-base class library to implement it. The difference comes in our use-case. Beforehand, we needed a common way to address all types of temperature sensors. Now, we’re trying to separate a temperature sensor from any hardware that’s not specific to the temperature sensor setup.

Now that we have our diagram, we can divvy up system behavior across classes. Everything related to converting voltage to temperature will live in our AD8495TCAmplifier class. Everything relating to reading our analog input will live in a separate class.

Without further ado, let’s write our AD8495TCAmplifier class:

```python
classAD8495TCAmplifier(TemperatureSensor):
     def__init__(self, voltage_input_interface, v1_v=1.25, t1_c=0.0, v2_v=1.5, t2_c=50.0): 
         # generate slop and y-intercept for line formula based on two data points: 
         self.gain =(t1_c -t2_c)/(v1_v -v2_v) 
         self.offset =self.gain *(0-v1_v) +t1_c 
         self.voltage_input =voltage_input_interface
 
    defread_temperature_c(self):
         voltage_v =self.voltage_input.read() 
         returnself.gain *voltage_v +self.offset
```

Just like described before, our AD8495TCAmplifier is just a child class of TemperatureSensor, which means we’ll need to implement a **read\_temperature\_c** method. Next off, to instantiate this class, notice that we pass in a reference to a **voltage\_input\_interface**. That’s our VoltageInputInterface object described above. Notice how, in the  **read\_temperature\_c** method, we call it’s  **read** method to get a voltage out. (Don’t get too bogged down the the other parameters: v1\_v, t1\_c, v2\_v, and t2\_c. Those are just two datapoints that we can derive from the datasheet and the circuit’s reference voltage that will dictate the gain and offset.)

Next off, comes the VoltageInputInterface and ADS1015VoltageInputInterface child class that inherits it.

```python
fromabc importabstractmethod, ABCMeta # abstract base class library tools
 
classVoltageInputInterface(object, metaclass=ABCMeta):
    ...
    @abstractmethoddefread(self):
        &quot;&quot;&quot; returns the analog voltage involts &quot;&quot;&quot;
        pass
 
classADS1015VoltageInputInterface(VoltageInputInterface):
    # Gain to Volts-per-bit conversion from From datasheet Table 1 
    volts_per_bit=\ 
    { 
        2/3: 0.003, 
        1: 0.002, 
        2: 0.001, 
        4: 0.5, 
        8: 0.25, 
        16: 0.125
    } 
     def__init__(self, ads1x15, channel_index, gain=2/3): 
         super().__init__() 
         self.ads1015 =ads1x15 
         self.gain =gain 
         self.channel_index =channel_index 
         self.ads1015.start_adc(channel_index, gain) 
 
     defread(self): 
         raw_bits =self.ads1015.get_last_result() 
         returnraw_bits *self.__class__.volts_per_bit[self.gain]
```

Notice how the ADS1015VoltageInputInterface does quite a bit of heavy lifting to hide away all the details of the actual ADS1015 driver just to expose it with a single **read** method. That’s exactly what we want–to trade all the unnecessary device-specific details of our voltage input for a simple interface.

Now we just write a Python script to “wire them all up,” connecting our object dependencies.

```python
importtime 
fromobject_oriented_hardware.ads1x15 importADS1015 
fromobject_oriented_hardware.ads1x15 importADS1015VoltageInputInterface 
fromobject_oriented_hardware.temperature_sensors importAD8495TCAmplifier 
fromobject_oriented_hardware.beaglebone_i2c importBBI2CBus2 
 
i2c_bus_2 =BBI2CBus2() 
adc_bank =ADS1015(i2c_bus_2) 
voltage_input =ADS1015VoltageInputInterface(adc_bank, channel_index=0) 
thermocouple =AD8495TCAmplifier(voltage_input) 
 
whileTrue: 
 print(thermocouple.read_temperature_c()) 
 time.sleep(0.5)
```

And that’s it! That about covers it for the first week. This time we covered polymorphism, which provides different classes with a common interface, and bridges, which detaches our classes from some implementation-specific components. Both of these patterns make our code more generalizable and flexible across different types of hardware. If you’re looking for more context, or you want to run these examples, have a go at [the source code](https://github.com/Poofjunior/object_oriented_hardware). Until then, tune in next time where we’ll talk singletons and stubs!

- [*![](https://hackaday.com/wp-content/themes/hackaday-2/img/share_face.png)*](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fhackaday.com%2F2018%2F01%2F12%2Fsoftware-design-patterns-for-real-hardware%2F)
- [*![](https://hackaday.com/wp-content/themes/hackaday-2/img/share_twitter.png)*](https://twitter.com/intent/tweet?text=Software%20Design%20Patterns%20For%20Real%20Hardware%20via%20@hackaday&url=https://hackaday.com/2018/01/12/software-design-patterns-for-real-hardware/)
- [*![](https://hackaday.com/wp-content/themes/hackaday-2/img/share_in.png)*](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fhackaday.com%2F2018%2F01%2F12%2Fsoftware-design-patterns-for-real-hardware%2F)
- [*![](https://hackaday.com/wp-content/themes/hackaday-2/img/share_mail1.png)*](https://hackaday.com/2018/01/12/software-design-patterns-for-real-hardware/)

[![](https://images.ads.supplyframe.com/6c4b99aa06c640935d8ff8bdda1cf77d.png)](https://ads.supplyframe.com/openads/www/delivery/ck.php?oaparams=2__bannerid=481783__zoneid=429__cb=5abd4d5251__oadest=%2F%2Fanalytics.supplyframe.com%2Ftrackingservlet%2Ftrack%2F%3Faction%3DadClick%26value1%3D{taxonomy_enc}%26value2%3D481783%26value3%3D2059%26zone%3D429%26uuid%3D%26extra%3Dcontextualmatch%3Dnolimitation%7Clivetax%3D0%7Ccookietax%3D413%7Ccb%3D5abd4d5251%7Ch_value%3Db0a12b455c2a5e121758670568%7Ch_crc%3D2079981926%7Cgeo%3Dus%7Ccnt%3Dna%7Cbp%3D1%7Cbpf%3D0.00000000046570935955438%7Ccp%3D6%7Ch_i%3Dy%7Cgcl%3D%7Cgclsrc%3D%7Cgclts%3D%7Cdi_num%3D%7Cab4%3D%26zone%3D429%26url%3Dhttps%253A%252F%252Fengage.avnet.com%252Findustrial-robotics%252Fp%252F11%253Futm_campaign%253Dfy25-amer-avt-robvert%2526utm_medium%253Dadp%2526utm_source%253Dsyf-hackaday%2526utm_term%253D672-npiburst-300x250-09222025)

## Subscribe

## If you missed it

- [![](https://hackaday.com/wp-content/uploads/2025/09/CRT_thumbnail.png?w=600&h=600)](https://hackaday.com/2025/09/23/the-impending-crt-display-revival-will-be-televised/)
	## The Impending CRT Display Revival Will Be Televised
	[45 Comments](https://hackaday.com/2025/09/23/the-impending-crt-display-revival-will-be-televised//#comments)
- [![](https://hackaday.com/wp-content/uploads/2023/07/JennysDriver_thumbnail.png?w=600&h=600)](https://hackaday.com/2025/09/22/jennys-daily-drivers-kde-linux/)
	## Jenny’s Daily Drivers: KDE Linux
	[25 Comments](https://hackaday.com/2025/09/22/jennys-daily-drivers-kde-linux//#comments)
- [![](https://hackaday.com/wp-content/uploads/2025/08/MetaRayBans_thumbnail.png?w=600&h=600)](https://hackaday.com/2025/09/22/metas-ray-ban-display-glasses-and-the-new-glassholes/)
	## Meta’s Ray-Ban Display Glasses And The New Glassholes
	[92 Comments](https://hackaday.com/2025/09/22/metas-ray-ban-display-glasses-and-the-new-glassholes//#comments)
- [![](https://hackaday.com/wp-content/uploads/2025/09/newcraft_thumb.jpg?w=600&h=600)](https://hackaday.com/2025/09/18/a-new-generation-of-spacecraft-head-to-the-iss/)
	## A New Generation Of Spacecraft Head To The ISS
	[18 Comments](https://hackaday.com/2025/09/18/a-new-generation-of-spacecraft-head-to-the-iss//#comments)
- [![](https://hackaday.com/wp-content/uploads/2025/09/HistoryEmail_thumbnail.png?w=600&h=600)](https://hackaday.com/2025/09/17/forgotten-internet-the-story-of-email/)
	## Forgotten Internet: The Story Of Email
	[24 Comments](https://hackaday.com/2025/09/17/forgotten-internet-the-story-of-email//#comments)

## Our Columns

- [![](https://hackaday.com/wp-content/uploads/2025/09/2025_supercon_header_thumbnail.png?w=600&h=600)](https://hackaday.com/2025/09/23/2025-hackaday-superconference-announcing-our-workshops-and-tickets/)
	## 2025 Hackaday Superconference: Announcing Our Workshops And Tickets
	[3 Comments](https://hackaday.com/2025/09/23/2025-hackaday-superconference-announcing-our-workshops-and-tickets//#comments)
- [![](https://hackaday.com/wp-content/uploads/2023/07/JennysDriver_thumbnail.png?w=600&h=600)](https://hackaday.com/2025/09/22/jennys-daily-drivers-kde-linux/)
	## Jenny’s Daily Drivers: KDE Linux
	[25 Comments](https://hackaday.com/2025/09/22/jennys-daily-drivers-kde-linux//#comments)
- [![](https://hackaday.com/wp-content/uploads/2015/09/links-thumb.jpg?w=600&h=600)](https://hackaday.com/2025/09/21/hackaday-links-september-21-2025/)
	## Hackaday Links: September 21, 2025
	[6 Comments](https://hackaday.com/2025/09/21/hackaday-links-september-21-2025//#comments)
- [![](https://hackaday.com/wp-content/uploads/2016/05/microphone-thumb.jpg?w=600&h=600)](https://hackaday.com/2025/09/19/hackaday-podcast-episode-338-smoothing-3d-prints-reading-cnc-joints-and-detecting-spicy-shrimp/)
	## Hackaday Podcast Episode 338: Smoothing 3D Prints, Reading CNC Joints, And Detecting Spicy Shrimp
	[8 Comments](https://hackaday.com/2025/09/19/hackaday-podcast-episode-338-smoothing-3d-prints-reading-cnc-joints-and-detecting-spicy-shrimp//#comments)
- [![](https://hackaday.com/wp-content/uploads/2016/01/darkarts-thumb.jpg?w=600&h=600)](https://hackaday.com/2025/09/19/this-week-in-security-the-shai-hulud-worm-shadowleak-and-inside-the-great-firewall/)
	## This Week In Security: The Shai-Hulud Worm, ShadowLeak, And Inside The Great Firewall
	[7 Comments](https://hackaday.com/2025/09/19/this-week-in-security-the-shai-hulud-worm-shadowleak-and-inside-the-great-firewall//#comments)