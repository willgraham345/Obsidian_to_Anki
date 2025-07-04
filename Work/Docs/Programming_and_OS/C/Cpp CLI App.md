---
summary: Creates a cli program with very few defaults. Need to `#include <App.hpp>`, and should
headings: ["[[#Examples]]", "[[#Methods]]", "[[#Usage]]"]
type: 
class_of: ["[[Cpp CLI11]]", "[[Cpp Input Output]]"]
date created: Tuesday, June 24th 2025, 2:27:02 pm
date modified: Thursday, June 26th 2025, 8:20:51 am
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Methods

- [p] `app.add_option("-f,--file", file, "Require an existing file")` `->required()` `->check(CLI::ExistingFile)` = Adds an option to an existing file. = #code/cpp/IO/cli
<!--ID: 1751434091725-->


- [E] [[Cpp CLI App]] = `app.parse(argc, argv)` = Internal function that takes command line info from C++ and parses it. If there is an error, it will return a `ParseError`.

## Usage
### Modifiers
See more at: [Options · CLI11 Tutorial](https://cliutils.github.io/CLI11/book/chapters/options.html)

|Modifier|Description|
|---|---|
|`->required()`|The program will quit if this option is not present. This is `mandatory` in Plumbum, but required options seems to be a more standard term. For compatibility, `->mandatory()` also works.|
|`->expected(N)`|Take `N` values instead of as many as possible, mainly for vector args.|
|`->expected(Nmin,Nmax)`|Take between `Nmin` and `Nmax` values.|
|`->type_size(N)`|specify that each block of values would consist of N elements|
|`->type_size(Nmin,Nmax)`|specify that each block of values would consist of between Nmin and Nmax elements|
|`->needs(opt)`|This option requires another option to also be present, opt is an `Option` pointer or a string with the name of the option. Can be removed with `->remove_needs(opt)`|
|`->excludes(opt)`|This option cannot be given with `opt` present, opt is an `Option` pointer or a string with the name of the option. Can be removed with `->remove_excludes(opt)`|
|`->envname(name)`|Gets the value from the environment if present and not passed on the command line and passes any validators.|
|`->group(name)`|The help group to put the option in. No effect for positional options. Defaults to `"Options"`. Options given an empty string for the group name will not show up in the help print.|
|`->description(string)`|Set/change the description|
|`->ignore_case()`|Ignore the case on the command line (also works on subcommands, does not affect arguments).|
|`->ignore_underscore()`|Ignore any underscores on the command line (also works on subcommands, does not affect arguments).|
|`->allow_extra_args()`|Allow extra argument values to be included when an option is passed. Enabled by default for vector options.|
|`->disable_flag_override()`|specify that flag options cannot be overridden on the command line use `=<newval>`|
|`->delimiter('<CH>')`|specify a character that can be used to separate elements in a command line argument, default is , common values are ',', and ';'|
|`->multi_option_policy( CLI::MultiOptionPolicy::Throw)`|Sets the policy for handling multiple arguments if the option was received on the command line several times. `Throw`ing an error is the default, but `TakeLast`, `TakeFirst`, `TakeAll`, `Join`, `Reverse`, and `Sum` are also available. See the next four lines for shortcuts to set this more easily.|
|`->take_last()`|Only use the last option if passed several times. This is always true by default for bool options, regardless of the app default, but can be set to false explicitly with `->multi_option_policy()`.|
|`->take_first()`|sets `->multi_option_policy(CLI::MultiOptionPolicy::TakeFirst)`|
|`->take_all()`|sets `->multi_option_policy(CLI::MultiOptionPolicy::TakeAll)`|
|`->join()`|sets `->multi_option_policy(CLI::MultiOptionPolicy::Join)`, which uses newlines or the specified delimiter to join all arguments into a single string output.|
|`->join(delim)`|sets `->multi_option_policy(CLI::MultiOptionPolicy::Join)`, which uses `delim` to join all arguments into a single string output. this also sets the delimiter|
|`->check(Validator)`|perform a check on the returned results to verify they meet some criteria. See [Validators](https://cliutils.github.io/CLI11/book/chapters/validators.html) for more info|
|`->transform(Validator)`|Run a transforming validator on each value passed. See [Validators](https://cliutils.github.io/CLI11/book/chapters/validators.html) for more info|
|`->each(void(std::string))`|Run a function on each parsed value, _in order_.|
|`->default_str(string)`|set a default string for use in the help and as a default value if no arguments are passed and a value is requested|
|`->default_function(std::string())`|Advanced: Change the function that `capture_default_str()` uses.|
|`->default_val(value)`|Generate the default string from a value and validate that the value is also valid. For options that assign directly to a value type the value in that type is also updated. Value must be convertible to a string(one of known types or have a stream operator).|
|`->capture_default_str()`|Store the current value attached and display it in the help string.|
|`->always_capture_default()`|Always run `capture_default_str()` when creating new options. Only useful on an App's `option_defaults`.|
|`->run_callback_for_default()`|Force the option callback to be executed or the variable set when the `default_val` is used.|
|`->force_callback()`|Force the option callback to be executed regardless of whether the option was used or not. Will use the default_str if available, if no default is given the callback will be executed with an empty string as an argument, which will translate to a default initialized value, which can be compiler dependent|
|`->trigger_on_parse()`|Have the option callback be triggered when the value is parsed vs. at the end of all parsing, the option callback can potentially be executed multiple times. Generally only useful if you have a user defined callback or validation check. Or potentially if a vector input is given multiple times as it will clear the results when a repeat option is given via command line. It will trigger the callbacks once per option call on the command line|
|`->option_text(string)`|Sets the text between the option name and description.|

## Examples
```cpp

## Examples

```cpp
#include "CLI/CLI.hpp"
#include <iostream>

int main(int argc, char **argv) {
    CLI::App app{"App description"};

    // Define options
    int p = 0;
    app.add_option("-p", p, "Parameter");

    CLI11_PARSE(app, argc, argv);

    std::cout << "Parameter value: " << p << std::endl;
    return 0;
}
```