## TDD Interview Project

Run the tests like so:

    ./run_tests.sh

Use the module by importing the main class:

    from interview_node import InterviewNode

And see `help(InterviewNode)` for usage instructions.

## Shouldawouldacoulda

 * It should have been a subclass of `set` and overrode `add` to force constraints.
 * It could do with a couple more tests around circular reference detection.
 * I should be using `assertFoo` rather than `assert` statements, since IIRC they
   play nicer with reporting the expected vs actual.
 * Pylint likely frowns upon this code.
 * The module and class name ought to have DAG in it or something.
 * Untidy, rushed commits. I usually like a bit of rebasing, squashing and `git add -p`
 * For the real project, I think plain old objects are probably simpler to reason about
   than introducing the complexity of a database and SQL. Maybe an ORM on top of sqlite,
   then move to Postgres if the data becomes bigger than available RAM.
   
