---
title: "The Beginner's Guide to iptables, the Linux Firewall"
source: "https://www.howtogeek.com/177621/the-beginners-guide-to-iptables-the-linux-firewall/"
author:
  - "[[Korbin Brown]]"
published: 2014-02-06
created: 2025-10-24
description: "Iptables is an extremely flexible firewall utility built for Linux operating systems."
tags:
  - "clippings"
---
### Jump Links

- [About iptables](https://www.howtogeek.com/177621/the-beginners-guide-to-iptables-the-linux-firewall/#about-iptables)
- [Types of Chains](https://www.howtogeek.com/177621/the-beginners-guide-to-iptables-the-linux-firewall/#types-of-chains)
- [Policy Chain Default Behavior](https://www.howtogeek.com/177621/the-beginners-guide-to-iptables-the-linux-firewall/#policy-chain-default-behavior)
- [Connection-specific Responses](https://www.howtogeek.com/177621/the-beginners-guide-to-iptables-the-linux-firewall/#connection-specific-responses)
- [Allowing or Blocking Specific Connections](https://www.howtogeek.com/177621/the-beginners-guide-to-iptables-the-linux-firewall/#allowing-or-blocking-specific-connections)
- [Connection States](https://www.howtogeek.com/177621/the-beginners-guide-to-iptables-the-linux-firewall/#connection-states)
- [Saving Changes](https://www.howtogeek.com/177621/the-beginners-guide-to-iptables-the-linux-firewall/#saving-changes)
- [Other Commands](https://www.howtogeek.com/177621/the-beginners-guide-to-iptables-the-linux-firewall/#other-commands)

Iptables is an extremely flexible firewall utility built for Linux operating systems. Whether you're a novice Linux geek or a system administrator, there's probably some way that iptables can be a great use to you. Read on as we show you how to configure the most versatile Linux firewall.

*Photo by* [*ezioman*](http://www.flickr.com/photos/ezioman/10492005984/)*.*

## About iptables

iptables is a command-line firewall utility that uses policy chains to allow or block traffic. When a connection tries to establish itself on your system, iptables looks for a rule in its list to match it to. If it doesn't find one, it resorts to the default action.

iptables almost always comes pre-installed on any Linux distribution. To update/install it, just retrieve the iptables package:

> ```javascript
> sudo apt-get install iptables
> ```

There are GUI alternatives to iptables like [Firestarter](https://sourceforge.net/projects/firestarter/), but iptables isn't really that hard once you have a few commands down. You want to be extremely careful when configuring iptables rules, particularly if you're SSH'd into a server, because one wrong command can permanently lock you out until it's manually fixed at the physical machine. And don't forget to [lock down your SSH server](https://www.howtogeek.com/devops/how-to-lock-down-your-ssh-server/) if you open the port.

## Types of Chains

iptables uses three different chains: input, forward, and output.

**Input** - This chain is used to control the behavior for incoming connections. For example, if a user attempts to SSH into your PC/server, iptables will attempt to match the IP address and port to a rule in the input chain.

**Forward** - This chain is used for incoming connections that aren't actually being delivered locally. Think of a router - data is always being sent to it but rarely actually destined for the router itself; the data is just forwarded to its target. Unless you're doing some kind of routing, NATing, or something else on your system that requires forwarding, you won't even use this chain.

There's one sure-fire way to check whether or not your system uses/needs the forward chain.

> ```javascript
> iptables -L -v
> ```

![/wordpress/wp-content/uploads/2013/12/2-packets-processed.jpg](https://static0.howtogeekimages.com/wordpress/wp-content/uploads/2013/12/2-packets-processed.jpg?q=50&fit=crop&w=490&dpr=1.5)

The screenshot above is of a server that's been running for a few weeks and has no restrictions on incoming or outgoing connections. As you can see, the input chain has processed 11GB of packets and the output chain has processed 17GB. The forward chain, on the other hand, has not needed to process a single packet. This is because the server isn't doing any kind of forwarding or being used as a pass-through device.

**Output** - This chain is used for outgoing connections. For example, if you try to ping howtogeek.com, iptables will check its output chain to see what the rules are regarding ping and howtogeek.com before making a decision to allow or deny the connection attempt.

**The caveat**

Even though pinging an external host seems like something that would only need to traverse the output chain, keep in mind that to return the data, the input chain will be used as well. When using iptables to lock down your system, remember that a lot of protocols will require two-way communication, so both the input and output chains will need to be configured properly. SSH is a common protocol that people forget to allow on both chains.

## Policy Chain Default Behavior

Before going in and configuring specific rules, you'll want to decide what you want the default behavior of the three chains to be. In other words, what do you want iptables to do if the connection doesn't match any existing rules?

To see what your policy chains are currently configured to do with unmatched traffic, run the

```javascript
iptables -L
```

command.

![/wordpress/wp-content/uploads/2013/12/3-policy-setting.jpg](https://static0.howtogeekimages.com/wordpress/wp-content/uploads/2013/12/3-policy-setting.jpg?q=50&fit=crop&w=410&dpr=1.5)

As you can see, we also used the grep command to give us cleaner output. In that screenshot, our chains are currently figured to accept traffic.

More times than not, you'll want your system to accept connections by default. Unless you've changed the policy chain rules previously, this setting should already be configured. Either way, here's the command to accept connections by default:

> ```sql
> iptables --policy INPUT ACCEPT
> ```
> ```sql
> iptables --policy OUTPUT ACCEPT
> ```
> ```sql
> iptables --policy FORWARD ACCEPT
> ```

By defaulting to the accept rule, you can then use iptables to deny specific IP addresses or port numbers, while continuing to accept all other connections. We'll get to those commands in a minute.

If you would rather deny all connections and manually specify which ones you want to allow to connect, you should change the default policy of your chains to drop. Doing this would probably only be useful for servers that contain sensitive information and only ever have the same IP addresses connect to them.

> ```sql
> iptables --policy INPUT DROP
> ```
> ```sql
> iptables --policy OUTPUT DROP
> ```
> ```sql
> iptables --policy FORWARD DROP
> ```

## Connection-specific Responses

With your default chain policies configured, you can start adding rules to iptables so it knows what to do when it encounters a connection from or to a particular IP address or port. In this guide, we're going to go over the three most basic and commonly used "responses".

**Accept** - Allow the connection.

**Drop** - Drop the connection, act like it never happened. This is best if you don't want the source to realize your system exists.

**Reject** - Don't allow the connection, but send back an error. This is best if you don't want a particular source to connect to your system, but you want them to know that your firewall blocked them.

The best way to show the difference between these three rules is to show what it looks like when a PC tries to ping a Linux machine with iptables configured for each one of these settings.

Allowing the connection:

![/wordpress/wp-content/uploads/2013/12/4-accept.jpg](https://static0.howtogeekimages.com/wordpress/wp-content/uploads/2013/12/4-accept.jpg?q=50&fit=crop&w=463&dpr=1.5)

Dropping the connection:

![/wordpress/wp-content/uploads/2013/12/5-drop.jpg](https://static0.howtogeekimages.com/wordpress/wp-content/uploads/2013/12/5-drop.jpg?q=50&fit=crop&w=477&dpr=1.5)

Rejecting the connection:

![/wordpress/wp-content/uploads/2013/12/6-reject.jpg](https://static0.howtogeekimages.com/wordpress/wp-content/uploads/2013/12/6-reject.jpg?q=50&fit=crop&w=462&dpr=1.5)

## Allowing or Blocking Specific Connections

With your policy chains configured, you can now configure iptables to allow or block specific addresses, address ranges, and ports. In these examples, we'll set the connections to

```sql
DROP
```

, but you can switch them to

```javascript
ACCEPT
```

or

```javascript
REJECT
```

, depending on your needs and how you configured your policy chains.

Note: In these examples, we're going to use

```javascript
iptables -A
```

to append rules to the existing chain. iptables starts at the top of its list and goes through each rule until it finds one that it matches. If you need to insert a rule above another, you can use

```javascript
iptables -I [chain] [number]
```

to specify the number it should be in the list.

**Connections from a single IP address**

This example shows how to block all connections from the IP address 10.10.10.10.

> ```javascript
> iptables -A INPUT -s 10.10.10.10 -j DROP
> ```

**Connections from a range of IP addresses**

This example shows how to block all of the IP addresses in the 10.10.10.0/24 network range. You can use a netmask or standard slash notation to specify the range of IP addresses.

> ```sql
> iptables -A INPUT -s 10.10.10.0/24 -j DROP
> ```

or

> ```sql
> iptables -A INPUT -s 10.10.10.0/255.255.255.0 -j DROP
> ```

**Connections to a specific port**

This example shows how to block SSH connections from 10.10.10.10.

> ```javascript
> iptables -A INPUT -p tcp --dport ssh -s 10.10.10.10 -j DROP
> ```

You can replace "ssh" with any protocol or port number. The

```javascript
-p tcp
```

part of the code tells iptables what kind of connection the protocol uses. If you were blocking a protocol that uses UDP rather than TCP, then

```javascript
-p udp
```

would be necessary instead.

This example shows how to block SSH connections from any IP address.

> ```sql
> iptables -A INPUT -p tcp --dport ssh -j DROP
> ```

## Connection States

As we mentioned earlier, a lot of protocols are going to require two-way communication. For example, if you want to allow SSH connections to your system, the input and output chains are going to need a rule added to them. But, what if you only want SSH coming into your system to be allowed? Won't adding a rule to the output chain also allow outgoing SSH attempts?

That's where connection states come in, which give you the capability you'd need to allow two way communication but only allow one way connections to be established. Take a look at this example, where SSH connections FROM 10.10.10.10 are permitted, but SSH connections TO 10.10.10.10 are not. However, the system is permitted to send back information over SSH as long as the session has already been established, which makes SSH communication possible between these two hosts.

> ```javascript
> iptables -A INPUT -p tcp --dport ssh -s 10.10.10.10 -m state --state NEW,ESTABLISHED -j ACCEPT
> ```
> ```javascript
> iptables -A OUTPUT -p tcp --sport 22 -d 10.10.10.10 -m state --state ESTABLISHED -j ACCEPT
> ```

## Saving Changes

The changes that you make to your iptables rules will be scrapped the next time that the iptables service gets restarted unless you execute a command to save the changes. This command can differ depending on your distribution:

Ubuntu:

> ```javascript
> sudo /sbin/iptables-save
> ```

Red Hat / CentOS:

> ```javascript
> /sbin/service iptables save
> ```

Or

> ```javascript
> /etc/init.d/iptables save
> ```

## Other Commands

List the currently configured iptables rules:

> ```javascript
> iptables -L
> ```

Adding the

```javascript
-v
```

option will give you packet and byte information, and adding

```javascript
-n
```

will list everything numerically. In other words - hostnames, protocols, and networks are listed as numbers.

To clear all the currently configured rules, you can issue the flush command.

> ```javascript
> iptables -F
> ```

|  | Linux Commands |
| --- | --- |
| Files | [tar](https://www.howtogeek.com/248780/how-to-compress-and-extract-files-using-the-tar-command-on-linux/) **·** [pv](https://www.howtogeek.com/428654/how-to-monitor-the-progress-of-linux-commands-with-pv-and-progress/) **·** [cat](https://www.howtogeek.com/278599/how-to-combine-text-files-using-the-cat-command-in-linux/) **·** [tac](https://www.howtogeek.com/424234/how-to-use-the-linux-cat-and-tac-commands/) **·** [chmod](https://www.howtogeek.com/437958/how-to-use-the-chmod-command-on-linux/) **·** [grep](https://www.howtogeek.com/496056/how-to-use-the-grep-command-on-linux/) **·** [diff](https://www.howtogeek.com/410532/how-to-compare-two-text-files-in-the-linux-terminal/) **·** [sed](https://www.howtogeek.com/666395/how-to-use-the-sed-command-on-linux/) **·** [ar](https://www.howtogeek.com/427086/how-to-use-linuxs-ar-command-to-create-static-libraries/) **·** [man](https://www.howtogeek.com/663440/how-to-use-linuxs-man-command-hidden-secrets-and-basics/) **·** [pushd](https://www.howtogeek.com/659146/how-to-use-pushd-and-popd-on-linux/) **·** [popd](https://www.howtogeek.com/659146/how-to-use-pushd-and-popd-on-linux/) **·** [fsck](https://www.howtogeek.com/745921/how-to-use-the-fsck-command-on-linux/) **·** [testdisk](https://www.howtogeek.com/700310/how-to-recover-deleted-files-on-linux-with-testdisk/) **·** [seq](https://www.howtogeek.com/693549/how-to-use-the-seq-command-on-linux/) **·** [fd](https://www.howtogeek.com/682244/how-to-use-the-fd-command-on-linux/) **·** [pandoc](https://www.howtogeek.com/678022/how-to-use-pandoc-to-convert-files-on-the-linux-command-line/) **·** [cd](https://www.howtogeek.com/666127/how-to-use-the-cd-command-on-linux/) **·** [$PATH](https://www.howtogeek.com/658904/how-to-add-a-directory-to-your-path-in-linux/) **·** [awk](https://www.howtogeek.com/562941/how-to-use-the-awk-command-on-linux/) **·** [join](https://www.howtogeek.com/542677/how-to-use-the-join-command-on-linux/) **·** [jq](https://www.howtogeek.com/529219/how-to-parse-json-files-on-the-linux-command-line-with-jq/) **·** [fold](https://www.howtogeek.com/538778/how-to-use-the-fold-command-on-linux/) **·** [uniq](https://www.howtogeek.com/533406/how-to-use-the-uniq-command-on-linux/) **·** [journalctl](https://www.howtogeek.com/499623/how-to-use-journalctl-to-read-linux-system-logs/) **·** [tail](https://www.howtogeek.com/481766/how-to-use-the-tail-command-on-linux/) **·** [stat](https://www.howtogeek.com/451022/how-to-use-the-stat-command-on-linux/) **·** [ls](https://www.howtogeek.com/448446/how-to-use-the-ls-command-on-linux/) **·** [fstab](https://www.howtogeek.com/444814/how-to-write-an-fstab-file-on-linux/) **·** [echo](https://www.howtogeek.com/446071/how-to-use-the-echo-command-on-linux/) **·** [less](https://www.howtogeek.com/444233/how-to-use-the-less-command-on-linux/) **·** [chgrp](https://www.howtogeek.com/439500/how-to-use-the-chgrp-command-on-linux/) **·** [chown](https://www.howtogeek.com/438435/how-to-use-the-chown-command-on-linux/) **·** [rev](https://www.howtogeek.com/434180/how-to-use-the-rev-command-on-linux/) **·** [look](https://www.howtogeek.com/428742/how-to-use-the-look-command-on-linux/) **·** [strings](https://www.howtogeek.com/427805/how-to-use-the-strings-command-on-linux/) **·** [type](https://www.howtogeek.com/426014/how-to-use-the-linux-type-command/) **·** [rename](https://www.howtogeek.com/423214/how-to-use-the-rename-command-on-linux/) **·** [zip](https://www.howtogeek.com/414082/how-to-zip-or-unzip-files-from-the-linux-terminal/) **·** [unzip](https://www.howtogeek.com/414082/how-to-zip-or-unzip-files-from-the-linux-terminal/) **·** [mount](https://www.howtogeek.com/414082/how-to-zip-or-unzip-files-from-the-linux-terminal/) **·** [umount](https://www.howtogeek.com/414082/how-to-zip-or-unzip-files-from-the-linux-terminal/) **·** [install](https://www.howtogeek.com/411366/how-to-copy-files-with-the-install-command-on-linux/) **·** [fdisk](https://www.howtogeek.com/106873/how-to-use-fdisk-to-manage-partitions-on-linux/) **·** [mkfs](https://www.howtogeek.com/443342/how-to-use-the-mkfs-command-on-linux/) **·** [rm](https://www.howtogeek.com/858815/linux-rm-command/) **·** [rmdir](https://www.howtogeek.com/409115/how-to-delete-files-and-directories-in-the-linux-terminal/) **·** [rsync](https://www.howtogeek.com/427480/how-to-back-up-your-linux-system/) **·** [df](https://www.howtogeek.com/409611/how-to-view-free-disk-space-and-disk-usage-from-the-linux-terminal/) **·** [gpg](https://www.howtogeek.com/427982/how-to-encrypt-and-decrypt-files-with-gpg-on-linux/) **·** [vi](https://www.howtogeek.com/102468/a-beginners-guide-to-editing-text-files-with-vi/) **·** [nano](https://www.howtogeek.com/howto/42980/the-beginners-guide-to-nano-the-linux-command-line-text-editor/) **·** [mkdir](https://www.howtogeek.com/275069/how-to-create-multiple-subdirectories-with-one-linux-command/) **·** [du](https://www.howtogeek.com/450366/how-to-get-the-size-of-a-file-or-directory-in-linux/) **·** [ln](https://www.howtogeek.com/287014/how-to-create-and-use-symbolic-links-aka-symlinks-on-linux/) **·** [patch](https://www.howtogeek.com/415442/how-to-apply-a-patch-to-a-file-and-create-patches-in-linux/) **·** [convert](https://www.howtogeek.com/109369/how-to-quickly-resize-convert-modify-images-from-the-linux-terminal/) **·** [rclone](https://www.howtogeek.com/451262/how-to-use-rclone-to-back-up-to-google-drive-on-linux/) **·** [shred](https://www.howtogeek.com/425232/how-to-securely-delete-files-on-linux/) **·** [srm](https://www.howtogeek.com/425232/how-to-securely-delete-files-on-linux/) **·** [scp](https://www.howtogeek.com/804179/scp-command-linux/) **·** [gzip](https://www.howtogeek.com/791705/zip-and-unzip-files-with-gzip-on-linux/) **·** [chattr](https://www.howtogeek.com/790679/how-to-use-the-chattr-command-on-linux/) **·** [cut](https://www.howtogeek.com/775824/how-to-use-the-linux-cut-command/) **·** [find](https://www.howtogeek.com/771399/how-to-use-the-find-command-in-linux/) **·** [umask](https://www.howtogeek.com/812961/umask-linux/) **·** [wc](https://www.howtogeek.com/812441/wc-command-in-linux/) **·** [tr](https://www.howtogeek.com/886723/how-to-use-the-linux-tr-command/) |  |
| Processes | [alias](https://www.howtogeek.com/439736/how-to-create-aliases-and-shell-functions-on-linux/) **·** [screen](https://www.howtogeek.com/662422/how-to-use-linuxs-screen-command/) **·** [top](https://www.howtogeek.com/668986/how-to-use-the-linux-top-command-and-understand-its-output/) **·** [nice](https://www.howtogeek.com/411979/how-to-set-process-priorities-with-the-nice-and-renice-commands-in-linux/) **·** [renice](https://www.howtogeek.com/411979/how-to-set-process-priorities-with-the-nice-and-renice-commands-in-linux/) **·** [progress](https://www.howtogeek.com/428654/how-to-monitor-the-progress-of-linux-commands-with-pv-and-progress/) **·** [strace](https://www.howtogeek.com/732736/how-to-use-strace-to-monitor-linux-system-calls/) **·** [systemd](https://www.howtogeek.com/687970/how-to-run-a-linux-program-at-startup-with-systemd/) **·** [tmux](https://www.howtogeek.com/671422/how-to-use-tmux-on-linux-and-why-its-better-than-screen/) **·** [chsh](https://www.howtogeek.com/669835/how-to-change-your-default-shell-on-linux-with-chsh/) **·** [history](https://www.howtogeek.com/465243/how-to-use-the-history-command-on-linux/) **·** [at](https://www.howtogeek.com/451386/how-to-use-at-and-batch-on-linux-to-launch-processes/) **·** [batch](https://www.howtogeek.com/451386/how-to-use-at-and-batch-on-linux-to-launch-processes/) **·** [free](https://www.howtogeek.com/456943/how-to-use-the-free-command-on-linux/) **·** [which](https://www.howtogeek.com/450894/how-to-use-the-which-command-on-linux/) **·** [dmesg](https://www.howtogeek.com/449335/how-to-use-the-dmesg-command-on-linux/) **·** [chfn](https://www.howtogeek.com/449160/how-to-change-user-data-with-chfn-and-usermod-on-linux/) **·** [usermod](https://www.howtogeek.com/449160/how-to-change-user-data-with-chfn-and-usermod-on-linux/) **·** [ps](https://www.howtogeek.com/448271/how-to-use-the-ps-command-to-monitor-linux-processes/) **·** [chroot](https://www.howtogeek.com/441534/how-to-use-the-chroot-command-on-linux/) **·** [xargs](https://www.howtogeek.com/435164/how-to-use-the-xargs-command-on-linux/) **·** [tty](https://www.howtogeek.com/428174/what-is-a-tty-on-linux-and-how-to-use-the-tty-command/) **·** [pinky](https://www.howtogeek.com/427004/how-to-use-the-pinky-command-on-linux/) **·** [lsof](https://www.howtogeek.com/426031/how-to-use-the-linux-lsof-command/) **·** [vmstat](https://www.howtogeek.com/424334/how-to-use-the-vmstat-command-on-linux/) **·** [timeout](https://www.howtogeek.com/423286/how-to-use-the-timeout-command-on-linux/) **·** [wall](https://www.howtogeek.com/415914/how-to-use-the-wall-command-on-linux/) **·** [yes](https://www.howtogeek.com/415535/how-to-use-the-yes-command-on-linux/) **·** [kill](https://www.howtogeek.com/413213/how-to-kill-processes-from-the-linux-terminal/) **·** [sleep](https://www.howtogeek.com/410299/how-to-pause-a-bash-script-with-the-linux-sleep-command/) **·** [sudo](https://www.howtogeek.com/111479/htg-explains-whats-the-difference-between-sudo-su/) **·** [su](https://www.howtogeek.com/111479/htg-explains-whats-the-difference-between-sudo-su/) **·** [time](https://www.howtogeek.com/415977/how-to-use-the-time-command-on-linux/) **·** [groupadd](https://www.howtogeek.com/50787/add-a-user-to-a-group-or-second-group-on-linux/) **·** [usermod](https://www.howtogeek.com/50787/add-a-user-to-a-group-or-second-group-on-linux/) **·** [groups](https://www.howtogeek.com/howto/ubuntu/see-which-groups-your-linux-user-belongs-to/) **·** [lshw](https://www.howtogeek.com/508993/how-to-check-which-gpu-is-installed-on-linux/) **·** [shutdown](https://www.howtogeek.com/411925/how-to-reboot-or-shut-down-linux-using-the-command-line/) **·** [reboot](https://www.howtogeek.com/411925/how-to-reboot-or-shut-down-linux-using-the-command-line/) **·** [halt](https://www.howtogeek.com/411925/how-to-reboot-or-shut-down-linux-using-the-command-line/) **·** [poweroff](https://www.howtogeek.com/411925/how-to-reboot-or-shut-down-linux-using-the-command-line/) **·** [passwd](https://www.howtogeek.com/447443/how-to-change-account-passwords-on-linux/) **·** [lscpu](https://www.howtogeek.com/198615/how-to-check-if-your-linux-system-is-32-bit-or-64-bit/) **·** [crontab](https://www.howtogeek.com/101288/how-to-schedule-tasks-on-linux-an-introduction-to-crontab-files/) **·** [date](https://www.howtogeek.com/410442/how-to-display-the-date-and-time-in-the-linux-terminal-and-use-it-in-bash-scripts/) **·** [bg](https://www.howtogeek.com/440848/how-to-run-and-control-background-processes-on-linux/) **·** [fg](https://www.howtogeek.com/440848/how-to-run-and-control-background-processes-on-linux/) **·** [pidof](https://www.howtogeek.com/846713/find-pid-of-process-linux/) **·** [nohup](https://www.howtogeek.com/804823/nohup-command-linux/) **·** [pmap](https://www.howtogeek.com/792783/how-to-use-the-pmap-command-on-linux/) |  |
| Networking | [netstat](https://www.howtogeek.com/513003/how-to-use-netstat-on-linux/) **·** [ping](https://www.howtogeek.com/355664/how-to-use-ping-to-test-your-network/) **·** [traceroute](https://www.howtogeek.com/657780/how-to-use-the-traceroute-command-on-linux/) **·** [ip](https://www.howtogeek.com/657911/how-to-use-the-ip-command-on-linux/) **·** [ss](https://www.howtogeek.com/681468/how-to-use-the-ss-command-on-linux/) **·** [whois](https://www.howtogeek.com/680086/how-to-use-the-whois-command-on-linux/) **·** [fail2ban](https://www.howtogeek.com/675010/how-to-secure-your-linux-computer-with-fail2ban/) **·** [bmon](https://www.howtogeek.com/664589/how-to-use-bmon-to-monitor-network-bandwidth-on-linux/) **·** [dig](https://www.howtogeek.com/663056/how-to-use-the-dig-command-on-linux/) **·** [finger](https://www.howtogeek.com/440391/how-to-use-the-finger-command-on-linux/) **·** [nmap](https://www.howtogeek.com/423709/how-to-see-all-devices-on-your-network-with-nmap-on-linux/) **·** [ftp](https://www.howtogeek.com/412626/how-to-use-the-ftp-command-on-linux/) **·** [curl](https://www.howtogeek.com/447033/how-to-use-curl-to-download-files-from-the-linux-command-line/) **·** [wget](https://www.howtogeek.com/281663/how-to-use-wget-the-ultimate-command-line-downloading-tool/) **·** [who](https://www.howtogeek.com/410423/how-to-determine-the-current-user-account-in-linux/) **·** [whoami](https://www.howtogeek.com/410423/how-to-determine-the-current-user-account-in-linux/) **·** [w](https://www.howtogeek.com/410423/how-to-determine-the-current-user-account-in-linux/) **·** [iptables](https://www.howtogeek.com/177621/the-beginners-guide-to-iptables-the-linux-firewall/) **·** [ssh-keygen](https://www.howtogeek.com/424510/how-to-create-and-install-ssh-keys-from-the-linux-shell/) **·** [ufw](https://www.howtogeek.com/115116/how-to-configure-ubuntus-built-in-firewall/) **·** [arping](https://www.howtogeek.com/813741/linux-arping-command/) **·** [firewalld](https://www.howtogeek.com/807545/how-to-get-started-with-firewalld-on-linux/) |  |

**RELATED:*****[Best Linux Laptops for Developers and Enthusiasts](https://www.howtogeek.com/748445/best-linux-laptops/)***