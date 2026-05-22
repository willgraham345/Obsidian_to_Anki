---
summary:
headings:
type:
source: "https://hackernoon.com/understanding-ufw-8d70d5d8f9d2"
author: ["[[Gokul N K]]"]
created: 2025-10-24
date created: Friday, October 24th 2025, 2:19:56 pm
date modified: Tuesday, November 4th 2025, 9:28:48 am
description: "I have always been scared of IP tables. If you want to know the reason check out the <a href=\"http://ipset.netfilter.org/iptables.man.html\" target=\"_blank\">man page for the same.</a> Though I have heard from many people that IPtables are more robust and secure, I have never used them because it has always been daunting. I personally feel that if I am not comfortable with something like IPtables and still use it I might add more security holes while not leveraging the benefits it provides. So I have stuck to using ufw for now. It is for the same reason that I prerfer Ubuntu over other flavors. Familiarity breeds confidence and I know that I will make less blunders. Donot consider this as a promotion of Ubuntu over other more secure flavors, because it is not. It is just my personal preference."
published: 2019-02-06
tags: ["clippings"]
template:
template-version:
title: "Understanding UFW | HackerNoon"
---

![featured image - Understanding UFW](https://hackernoon.imgix.net/hn-images/1*t5CFOq45fU1qCmdgIksLnQ.jpeg?w=1200)

featured image - Understanding UFW

<audio xmlns="http://www.w3.org/1999/xhtml" src="https://storage.googleapis.com/hackernoon/audios/understanding-ufw-8d70d5d8f9d2-en-US-Wavenet-I-MALE--b3dcf9bd07558.mp3">Your browser does not support the <code>audio</code> element.</audio>

![Catchpoint](https://hackernoon.imgix.net/images/img-y033hdm.png?auto=format&fit=max&w=256)

Catchpoint

## Ubuntu Firewall for humans

I have always been scared of IP tables. If you want to know the reason check out the [man page for the same.](http://ipset.netfilter.org/iptables.man.html?ref=hackernoon.com) Though I have heard from many people that IPtables are more robust and secure, I have never used them because it has always been daunting. I personally feel that if I am not comfortable with something like IPtables and still use it I might add more security holes while not leveraging the benefits it provides. So I have stuck to using ufw for now. It is for the same reason that I prerfer Ubuntu over other flavors. Familiarity breeds confidence and I know that I will make less blunders. Donot consider this as a promotion of Ubuntu over other more secure flavors, because it is not. It is just my personal preference.

**Side note**: Did you know that **“Ubuntu”** is generally translated as [**“I am because we are,"**](https://en.wikipedia.org/wiki/Ubuntu_philosophy?ref=hackernoon.com)

### Before getting started

Keep these things in mind before getting started.

1. Use some form of firewall. If not ufw you can use iptables directly.
2. If you are using ufw, make sure that your ufw [service is started on reboot.](https://medium.com/@gokulnk/linux-systemctl-46bd0a11e27b?ref=hackernoon.com)
3. Understand the defaults of ufw well.
4. Blacklist all and whitelist what is required is always a better option.
5. Set up a [monitoring tool like zabbix](https://medium.com/@gokulnk/linux-systemctl-46bd0a11e27b?ref=hackernoon.com) that gives you a trigger when ufw is down.

### Installing ufw

sudo apt install ufw

### Check status

  

\# ufw statusStatus: inactive

We will enable `ufw` after adding the relevant rules.

### Whitelist ssh

Make sure allow ssh before enabling ufw so that you can access your server from anywhere using ssh.

  

  

sudo ufw allow sshRules updatedRules updated (v6)

### Checking added rules

You cannot check the added rules using `ufw status` when ufw is not active. Instead you can use `ufw show added.` You can use this even after enabling the ufw.

  

  

\# ufw show addedAdded user rules (see 'ufw status' for running firewall):ufw allow 22/tcp

### Enable ufw

Enabling ufw without adding rule for ssh might lock you out of your server. So be careful before enabling ufw. I have not tried it though, so I can’t be sure.:P

  

  

\# ufw enableCommand may disrupt existing ssh connections. Proceed with operation (y|n)? yFirewall is active and enabled on system startup

### Check status

`ufw status` gives you the status of ufw and also lists all the enabled rules.

  

\# ufw statusStatus: active

  

  

  

To Action From-- ------ ----22/tcp ALLOW Anywhere22/tcp (v6) ALLOW Anywhere (v6)

`ufw status` can be problematic as it doesn’t give all the details. Checkout next section.

### UFW Defaults

Not knowing the defaults cost me a couple of hours the other day.

Since **defaults** were not displayed and details under **Action** was not clear enough, I had assumed a few things which cost me dearly. So go through the default options before actually setting up the relevant rules for your applications.

You can get those details using `ufw status verbose`

  

  

  

  

\# ufw status verboseStatus: activeLogging: on (low)Default: deny (incoming), allow (outgoing), disabled (routed)New profiles: skip

  

  

  

To Action From-- ------ ----22/tcp ALLOW IN Anywhere22/tcp (v6) ALLOW IN Anywhere (v6)

As you can see from the output now

1. Defaults are **deny (incoming):** This will make sure that no outside systems can connect to your machine until you add an overriding rule for the same.
2. Defaults are **allow (outgoing):** This means that all outgoing request are enabled. While this setting helps you run commands like `apt-install`, `wget` and `ping` without any issues. But if you want to keep your server secure it is better to make defaults as block outgoing and then allow specific IPs/domains that you need.
3. Default are **disabled (routed)** This means that all routing is disabled and forwarding is blocked. This is a good default provided you are not using your machine as a router.
4. As you can see in Action columns it is “ALLOW IN”. Which means there is also “ALLOW OUT”. You need to add such a rule if you make the default as **deny (outgoing).**

### Changing Defaults

The defaults we see above are equivalent of the following rules.

  

sudo ufw default deny incomingsudo ufw default allow outgoing

If you want to change the default to deny outgoing you can run

  

  

sudo ufw default deny outgoingDefault outgoing policy changed to 'deny'(be sure to update your rules accordingly)

If you set the above default you will need to manually add rules for accessing outside systems. It can be a cumbersome process but much safer.

For example let us say you want to allow outgoing traffic on port 10060 then you can run

ufw allow out 10060

Instead of keeping the `outgoing` default as is, I think it is better to deny outgoing. Whenever you want to perform some upgrades or install software you can add rule like temporarily and then delete it once you are done.

Also if you want to open only specific ports so that you can use apt you can use the following rules that I borrowed [from this answer.](https://serverfault.com/questions/468907/ufw-blocking-apt/736775?ref=hackernoon.com#736775)

```
ufw default deny incomingufw default deny outgoingufw limit sshufw allow svnufw allow gitufw allow out httpufw allow in http ufw allow out httpsufw allow in httpsufw allow out 53ufw logging onufw enable
```

### Show rules

You can use `ufw show added` to show all the added rules.

  

  

  

  

  

\# ufw show addedufw allow 22/tcpufw allow from x.x.x.x to any port 27017ufw allow from x.x.x.x to any port 27017ufw allow from x.x.x.x to any port 10050ufw allow from x.x.x.x to any port 10050

Earlier I was using the command `ufw status numbered` but now I use `ufw show added` and then use the rules from there to delete like following.

ufw delete allow 22/tcp

### Thumb Rules

1. Make sure ufw is started on boot.
2. Change the defaults to make then more restrictive based on your comfort.
3. Deny by default and enabled only what is required.
4. Keep your rules as specific as possible. Example `sudo ufw allow from 192.168.0.0/24 to any port 22 proto tcp`
5. Add a [monitoring tool like Zabbix](http://sudo%20ufw%20allow%20from%20192.168.0.0/24%20to%20any%20port%2022%20proto%20tcp) which check the status of ufw as well any rules that are very critical.

### Further Reading

If you want more details and more query options checkout [https://help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW?ref=hackernoon.com)

I had created done blunders without knowing the ufw clearly. I hope this article can stop you from committing such blunders.

If you liked this article and would like to read similar articles, don’t forget to clap.

Click and drag to clap more than once. 50 is the limit.

You can read the others articles from the series.

  

[**Understanding promises in JavaScript** \_I have had a kind of “love and hate” relationship with JavaScript. But nevertheless JavaScript was always intriguing…\_hackernoon.com](https://hackernoon.com/understanding-promises-in-javascript-13d99df067c1?ref=hackernoon.com "https://hackernoon.com/understanding-promises-in-javascript-13d99df067c1")

  

[**Understanding async-await in Javascript — Gokul N K — Medium** \_Async and Await are extensions of promises. So if you are not clear about the basics of promises please get comfortable…\_hackernoon.com](https://hackernoon.com/understanding-async-await-in-javascript-1d81bb079b2c?ref=hackernoon.com "https://hackernoon.com/understanding-async-await-in-javascript-1d81bb079b2c")

  

[**Should I use Promises or Async-Await** \_I recently read a medium post where the author claimed that using async-await is better than using promises. While this…\_hackernoon.com](https://hackernoon.com/should-i-use-promises-or-async-await-126ab5c98789?ref=hackernoon.com "https://hackernoon.com/should-i-use-promises-or-async-await-126ab5c98789")

If you are interested in cryptocurrencies checkout

  

[**10 things to know/do before investing in cryptocurrencies** \_“Never Invest In Something You Don’t Understand”\_hackernoon.com](https://hackernoon.com/10-things-to-know-do-before-investing-in-cryptocurrencies-a6c72367d854?ref=hackernoon.com "https://hackernoon.com/10-things-to-know-do-before-investing-in-cryptocurrencies-a6c72367d854")

  

[**Beginner’s Guide to “Investing in Cryptocurrencies”** \_It has been more than an year since I started investing in cryptocurrencies. Following Warren Buffet’s advice of “Never…\_hackernoon.com](https://hackernoon.com/beginners-guide-to-investing-in-cryptocurrencies-e2636d9c2fd9?ref=hackernoon.com "https://hackernoon.com/beginners-guide-to-investing-in-cryptocurrencies-e2636d9c2fd9")

  

[**Why comparing cryptocurrency prices is wrong** \_Price is an important indicator. But it can also be misleading in many cases.\_blog.goodaudience.com](https://blog.goodaudience.com/why-comparing-cryptocurrency-prices-is-wrong-2054a9075878?ref=hackernoon.com "https://blog.goodaudience.com/why-comparing-cryptocurrency-prices-is-wrong-2054a9075878")
