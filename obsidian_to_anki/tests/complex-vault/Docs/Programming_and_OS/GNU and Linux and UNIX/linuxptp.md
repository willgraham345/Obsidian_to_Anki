---
summary: CLI tool for the Linux PTP project
type: note/tool
headings:
  - "[[#Concepts of Note]]"
  - "[[#Configuration]]"
  - "[[#Usage]]"
configurations:
  - "[[linuxptp#/etc/ptp4l.conf Linux Filesystem Hierarchy /etc/ptp4l.conf]]"
implements:
  - "[[PTP Server]]"
date created: Friday, February 20th 2026, 4:34:14 pm
date modified: Tuesday, March 3rd 2026, 2:51:32 pm
tags: []
template: "[[base_note_template]]"
template-version: 1.0.1
tool_of:
  - "[[Linux]]"
  - "[[PTP Server]]"
tools:
  - "[[pmc]]"
uses:
  - "[[@ieee_1588]]"
---

# Summary
󰙎 linuxptp ;; Linux project which provides UDP time synchronization

# Additional Background
[Chapter 23. Configuring PTP Using ptp4l \| Deployment Guide \| Red Hat Enterprise Linux \| 6 \| Red Hat Documentation](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/6/html/deployment_guide/ch-configuring_ptp_using_ptp4l)

## Concepts of Note
󰙎 `ptp4l` ;;; Daemon that synchronizes the PTP hardware clock from the NIC
󰙎 `phc2sys` ;;; Daemon that synchronizes the PTP hardware clock and the system clock

## Configuration
##### /etc/ptp4l.conf: [[Linux Filesystem Hierarchy#/etc/ptp4l.conf]]
󰫧 :
- description: Configuration for a [[PTP Server]]
󰫧 end:

## Usage
 `service ptp4l start` ;;; Starting `ptp4l`
