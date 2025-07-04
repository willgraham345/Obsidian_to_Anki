---
type: note
---
# Background
Enables populating content at configure time via any method supported by the [[CMake.ExternalProject]] module. 

Makes content available immediately, allowing the configure step to use the contents in commands like [[CMake.add_subdirectory]], [[CMake.include]], or [[CMake.file]].

## Declaring Content Details
Content population details should be defined separately from the command that performs actual population. 
- Ensures dependency details are defined before anything might try to use them to populate content. See [[#Declaring Content Details Example]]. 

When using hierarchical project arrangement, projects at higher levels are able to override the declared details of content specified anywhere lower in the project hierarchy. 

The first call that tires to populate a dependency "wins", with subsequent populations reusing the result of the first instead of repeating the population again. 

# Usage
## Declaring Content Details Example
```cmake
FetchContent_Declare(
  googletest
  GIT_REPOSITORY https://github.com/google/googletest.git
  GIT_TAG        703bd9caab50b139428cea1aaff9974ebee5742e # release-1.10.0
)
FetchContent_Declare(
  myCompanyIcons
  URL      https://intranet.mycompany.com/assets/iconset_1.12.tar.gz
  URL_HASH MD5=5588a7b18261c20068beabfb4f530b87
)

FetchContent_MakeAvailable(googletest myCompanyIcons)
```

### FetchContent_Declare
```cmake
	FetchContent_Declare(
	  <name>
	  <contentOptions>...
	  [EXCLUDE_FROM_ALL]
	  [SYSTEM]
	  [OVERRIDE_FIND_PACKAGE |
	   FIND_PACKAGE_ARGS args...]
	)
```

### FetchContent_MakeAvailable
Ensures named dependencies have been populated (either by earlier call, or by populating them itself)
- When performing, it will also add them to the main build, if possible, so that the main build can use the populated projects' targets
