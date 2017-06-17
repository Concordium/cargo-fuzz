# Cargo-fuzz

Command-line wrapper for using `libFuzzer`. Easy to use, no need to recompile LLVM!

Note: `libFuzzer` needs LLVM sanitizer support, so this is only works on x86-64 Linux and x86-64 macOS for now. This also needs a nightly since it uses some unstable command-line flags. You'll also need a C++ compiler with C++11 support.

This crate is currently under some churn -- in case stuff isn't working, please reinstall it (`cargo install cargo-fuzz -f`). Rerunning `cargo fuzz init` after moving your `fuzz` folder and updating this crate may get you a better generated `fuzz/Cargo.toml`. Expect this to settle down soon.

## Installation

```sh
$ cargo install cargo-fuzz
```

## Usage

First, set up your project for fuzzing:

```sh
$ cd /path/to/project
$ cargo fuzz init
```

This will create a `fuzz` folder, containing a fuzzing script called `fuzz_target_1` in the
`fuzz_target_1/` subfolder. It is generally a good idea to check in the files generated by `init`.

`libFuzzer` is going to repeatedly call the body of `fuzz_target!()` with a byte buffer `data`,
until your program hits an error condition (segfault, panic, etc). Write your `fuzz_target!()`
body to hit the entry point you need.

You can add more fuzz target scripts via `cargo fuzz add name_of_script`. There
is a `Cargo.toml` in the `fuzz/` folder where you can add dependencies.

To fuzz a fuzz target, run:

```sh
$ cd /path/to/project
$ cargo fuzz run fuzz_target_1 # or whatever the target is named
```

Then, wait till it finds something! More complex invocations are available as well. Consider
looking at `cargo fuzz --help`, `cargo fuzz run --help` and others.

Once you have found something and believe you have fixed it, re-run the fuzz target with the input:

```sh
$ cargo fuzz run fuzz_target_1 fuzz/artifacts/fuzz_target_1/<file mentioned in crash output>
```

## Trophy case

The trophy case has moved to a separate dedicated repository:

https://github.com/rust-fuzz/trophy-case
