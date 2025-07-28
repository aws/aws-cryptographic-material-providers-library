[//]: # "Copyright Amazon.com Inc. or its affiliates. All Rights Reserved."
[//]: # "SPDX-License-Identifier: CC-BY-SA-4.0"

# GitHub Actions

The MPL uses GitHub Actions to trigger our testing.
If a GitHub Action job/workflow is going to be added, and that job should always run, it should be added to `ci.yml`.

This stops us from having multiple copies of the same event.

Instead, we build a hierarchy of testing:

- `routine_ci` determines regular testing events, such as daily, PR, or push to main
- `ci.yml` is triggered by `routine_ci` or other events, and runs all the per runtime testing
- `library_<runtime>_tests` are responsible for a runtimes particular testing suite.

# `library_<runtime>_tests`

In general, these should have at least two inputs:

- The Dafny Verision
- Weather Smithy-Dafny should be re-run
