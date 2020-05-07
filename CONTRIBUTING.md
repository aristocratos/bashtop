# Contributing guidelines

## When submitting pull requests

* Explain your thinking in why a change or addition is needed.
  * Is it a requested change or feature?
  * If not, open a feature request to get feedback before making a pull request.

* Split up multiple unrelated changes in multiple pull requests.

* [Shellcheck](https://github.com/koalaman/shellcheck) your work. Current shellsheck exeptions at the beginning of [bashtop](bashtop).

* Purely cosmetic changes won't be accepted without a very good explanation of its value.
  * (Some design choices are for better configurability of syntax highlighting.)

## Formatting

### Follow the current syntax design

* Indent type: Tabs

* Tab size: 4

* Use the longer "if, elif, then, else, fi" statements and indent conditionals, loops etc.

* Use "[[ ]]", "(( ))" for conditions and "$( ), <( )" for command substitution.

* Create functions instead of repeating blocks of code.

* Don't stack unrelated blocks of code, leave blank lines for better readability.

* Comment new code that isn't very obvious in it's function.

* Name new variables and functions in lower-case and after what purpose they serve.
  * (Exception arithmetic with many variables, make sure to comment what's happening instead.)

## Optimization

* Avoid forks if possible.

* Avoid writing to disk if possible.

* Make sure variables/arrays are cleaned up if not reused.

* Compare cpu and memory usage with and without your code and look for alternatives if they cause a noticeable negative impact.

For questions contact Aristocratos at admin@qvantnet.com

For proposing changes to this document create a [new issue](https://github.com/aristocratos/bashtop/issues/new/choose).