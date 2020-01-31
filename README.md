## TDD Interview Project

Run the tests like so:

    ./run_tests.sh

Use the module by importing the main class:

    from interview_node import InterviewNode

And see `help(InterviewNode)` for usage instructions.

## Shouldawouldacoulda

 * It could do with a couple more tests around circular reference detection.
 * I should be using `assertFoo` rather than `assert` statements, since IIRC they
   play nicer with reporting the expected vs actual.
 * Pylint likely frowns upon this code.
 * The module name ought to have DAG in it or something.
 * Untidy, rushed commits. I usually like a bit of rebasing, squashing and `git add -p`

