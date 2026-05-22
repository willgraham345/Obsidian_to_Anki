---
type: note
---
# Background
- How to grab the total physical RAM.
- Windows has something in the GlobalMemoryStatusEx according to [this stack overflow thread](https://stackoverflow.com/questions/8122277/getting-memory-information-with-qt)

# Usage
```cpp
MEMORYSTATUSEX memory_status;
ZeroMemory(&memory_status, sizeof(MEMORYSTATUSEX));
memory_status.dwLength = sizeof(MEMORYSTATUSEX);
if (GlobalMemoryStatusEx(&memory_status)) {
  system_info.append(
        QString("RAM: %1 MB")
        .arg(memory_status.ullTotalPhys / (1024 * 1024)));
} else {
  system_info.append("Unknown RAM");
}
```