# MPL TestServer

A cross-language conformance harness for the AWS Cryptographic Material Providers
Library. One hand-written Smithy model is the single source of truth; from it,
standard smithy-java code generation produces both the Java client the tests drive
and the Java server's scaffolding. The server delegates to the MPL as transpiled
from this repository's Dafny source.

Phase 1 covers local-only keyrings — Raw AES, Raw RSA, and Multi — so the whole
harness is provable **without AWS credentials and without any AWS resource**.

## Quick start

```bash
cd test-server

make mpl-local-publish   # transpile the MPL's Dafny to Java, install to ~/.m2 (slow, once)
make build               # generate + compile every module
make orchestrate         # launch the server, run the tests, tear down, report
```

`make orchestrate` is the one-command path. For an interactive loop, run the server
in one shell and the tests in another:

```bash
make run-server          # foreground, port 8101
make test                # in another shell
```

## Prerequisites

| Tool           | Why                                        | Notes                                                                                                                                                 |
| -------------- | ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **JDK 21+**    | smithy-java 1.x baselines on Java 21       | `make check-java` verifies it. Auto-discovered, or `make JAVA_HOME=/path/to/jdk21 <target>`                                                           |
| **A JDK 8–19** | to launch the MPL's _own_ Gradle 7.6 build | The MPL pins a Java 8 toolchain, and Gradle 7.6 cannot run on a JDK newer than 19 — so the JDK above cannot launch it. Override with `MPL_JAVA_HOME=` |
| **Dafny**      | to transpile the MPL to Java               | The exact version in `../project.properties` (`dafnyVersion`). `make check-dafny` prints the install command if it is missing                         |

`make help` prints what it resolved for each.

## Why this TestServer is shaped differently

Two facts about the MPL drive nearly every design decision here, and both differ
from the ESDK and DB-ESDK TestServers.

**The MPL lives in one repository.** There is no per-language repository to host a
per-language server, so every language server lives here alongside the model, the
tests, and the orchestrator. The `Configuration_Set` survives for extensibility,
but a `Configuration_Entry` carries **no library-repository coordinates**: the
library is always this working tree. Recording coordinates for it would record a
constant, and imply — falsely — that the library could come from somewhere else.
For the same reason the `Feature_Declaration` is inline in each entry: no MPL
language has its own repository to declare it in.

**The MPL is exclusively Dafny.** The artifact under test does not exist as a
consumable Maven artifact until Dafny has been transpiled and the result published
locally. That is a first-class build step, not an environment assumption — see
below.

A third fact drives the wire format: every MPL constructor returns an
`aws.polymorph#reference` to a resource, and a reference cannot be serialized. So
each `Create*` operation returns an opaque UUID handle into a server-side registry.
That is not an indirection for convenience; it is the only way to model the MPL's
API at all.

## Building the artifact under test

`make mpl-local-publish` runs:

```
make -C ../AwsCryptographicMaterialProviders \
     transpile_java mvn_local_deploy_dependencies mvn_local_deploy
```

Four things about this pipeline are worth knowing before you debug it.

1. **`mvn_local_deploy`, not `build_java`.** `build_java` compiles but does not
   install, leaving `~/.m2` without the SNAPSHOT and the server build unable to
   resolve it. Publishing also skips tests, which matters because the MPL's
   90%-coverage gate reports 0% and fails when no credentials are available to run
   the MPL's own integration tests.
2. **The version is read, never written.** `../project.properties` declares
   `javaMPLVersion`. At the time of writing that is `1.11.1-SNAPSHOT`, and
   `1.11.1` is _not_ a released version — only `1.11.0` is. Hard-coding any version
   invites a build that resolves nothing.
3. **Transpiling rewrites tracked source.** The MPL sets
   `ENABLE_EXTERN_PROCESSING=1`, so `transpile_java` runs `sed` passes that strip
   `{:extern ...}` annotations from tracked `.dfy` files and restore them
   afterwards. `mpl-local-publish` refuses to start from a dirty tree and verifies
   cleanliness afterwards, so an interrupted run cannot be mistaken for a
   pre-existing edit.
4. **A `$(shell)` hook can poison the Dafny command line.**
   `smithy-dafny/SmithyDafnyMakefile.mk` computes `ENFORCE_DETERMINISM_OPTION` by
   running Gradle and capturing its stdout. That Gradle project cannot resolve its
   own smithy-python/smithy-rust codegen dependencies, and on a cold wrapper cache
   its output _begins with the distribution download progress_ — which is then
   spliced into `dafny translate`'s arguments and fails with
   `Command-line argument 'Downloading' is neither a recognized option`. This
   Makefile passes `ENFORCE_DETERMINISM_OPTION` explicitly to bypass the hook.

   Because that hook is an immediate (`:=`) assignment, every sub-make still
   _evaluates_ it, so a publish prints a series of `BUILD FAILED in ~700ms` lines
   from the failing Gradle project. **These are expected and harmless** — the value
   they would have produced is supplied explicitly. Judge the publish by its final
   `==> Published ...` line, not by those.

## Layout

```
test-server/
├── Makefile                 # every target; `make help` lists them
├── versions.properties      # the single version declaration all modules load
├── config/
│   └── configuration-set.json
├── model/                   # THE model + a build that only validates it
├── client-java/             # java-codegen mode: client
├── servers/java/            # java-codegen mode: server + handlers + registry + protocol
├── tests/                   # conformance tests + a `meta` package for the wire contract
└── orchestrator/            # load → validate → launch → run → report
```

Each module is an **independent** Gradle build with its own `settings.gradle.kts`,
sharing one wrapper. The Makefile points the wrapper at the right project with
`-p`, so you cannot invoke one module's task from another's directory.

## Make targets

| Target                       | What it does                                                                          |
| ---------------------------- | ------------------------------------------------------------------------------------- |
| `help`                       | List targets and show the resolved toolchain                                          |
| `check-java` / `check-dafny` | Verify prerequisites, with install instructions on failure                            |
| `mpl-local-publish`          | Transpile the MPL to Java and install it to `~/.m2` (marker-file guarded)             |
| `mpl-use-published`          | Accept an MPL artifact already in `~/.m2` — for CI, where an earlier job published it |
| `clean-mpl-marker`           | Forget the publish, forcing a re-transpile                                            |
| `validate`                   | Validate the model on its own                                                         |
| `generate`                   | Generate the client and the server scaffolding                                        |
| `build`                      | Generate and compile every module                                                     |
| `run-server`                 | Start the server in the foreground on `PORT` (default 8101)                           |
| `test`                       | Run the tests against a server already listening on `PORT`                            |
| `orchestrate`                | The full run: validate, launch, test, tear down, report                               |
| `clean`                      | Remove build output                                                                   |

## The tests

Two packages, split deliberately:

- **`...tests`** — conformance tests. They validate _the MPL's_ behavior: Raw AES
  round-trips across all three wrapping algorithms, Raw RSA round-trips across all
  padding schemes plus its negative cases, and multi-keyring composition. These are
  the tests that will fan out across languages.
- **`...tests.meta`** — the harness's own wire contract: that `CreateMPL` returns a
  usable handle, that a bad handle is refused, and that the two modeled errors
  arrive as distinct types with their messages. Not parameterized over targets.

Beyond those meta tests there is no test suite for the harness itself. The harness
is proven by the conformance runs it performs.

The round-trip is the load-bearing assertion:

```
InitializeEncryptionMaterials(suite, ec)  -> materials with no data key
OnEncrypt(keyring, materials)             -> materials WITH a data key + EDKs
                                             (the test carries EDKs + suite id)
InitializeDecryptionMaterials(suite, ec)  -> materials with no data key
OnDecrypt(keyring, materials, EDKs)       -> materials WITH a data key
assert the two plaintext data keys are equal
```

Nothing server-side links the two halves. That is what will let the encrypt half go
to one language server and the decrypt half to another.

## Continuous integration

`.github/workflows/test_server.yml` runs the harness, and is wired into `pull.yml`
(as a _required_ job), `push.yml`, and `daily_ci.yml`.

It reuses `library_java_build.yml`'s Maven-local artifact rather than transpiling the
MPL again — the same thing `library_java_tests.yml` does. Because the artifact is
already built, the TestServer job needs **neither Dafny nor the Java 8 toolchain**:
`make mpl-use-published` verifies the jar is in `~/.m2` at the version
`project.properties` declares and then proceeds straight to codegen.

**No AWS credentials are required.** The phase-1 suite covers only local keyrings and
makes no AWS call. When the KMS keyrings land, this workflow will need
`configure-aws-credentials` and the `GitHub-CI-MPL-Dafny-Role`, like the other test
workflows.

`mpl-use-published` is deliberately a **separate, opt-in target** rather than a
fallback inside `mpl-local-publish`. If the publish silently skipped whenever a jar
happened to be present, a developer who edited Dafny source and re-ran the harness
would keep testing the stale artifact — the most confusing failure this harness could
have. CI asks for the shortcut explicitly; local development never gets it by
accident.

On every run — pass or fail — the workflow publishes the JUnit report from
`tests/build/{reports,test-results}/test/` as the `test-server-report-*` artifact, and
writes a per-suite summary table to the run's own page. The report is uploaded on
success too, because a report only on failure answers "what broke?" but never "what is
actually covered?", and the second question is the one an engineer evaluating this
harness needs.

### Formatting

The repository's `library_format.yml` runs Prettier (with `prettier-plugin-java`) over
the whole tree, so **Java, JSON, YAML, and Markdown here must be Prettier-formatted**.
From the repository root:

```bash
make setup_prettier
make format_java_misc          # or format_java_misc-check to verify only
```

Generated code under `test-server/**/build/` is excluded, via both
`test-server/.gitignore` and an explicit `.prettierignore` entry.

## Known deviations and limitations

Reported here rather than papered over.

### Materials carry the algorithm suite _id_, not the full `AlgorithmSuiteInfo`

The MPL's materials carry a full `AlgorithmSuiteInfo`: a structure of five nested
unions plus four shapes imported from `aws.cryptography.primitives`, roughly fifteen
extra shapes to mirror. The wire carries `algorithmSuiteId` instead, and the server
rehydrates the full structure with the MPL's own `GetAlgorithmSuiteInfo`.

This is **lossless, not a hidden abstraction**: `AlgorithmSuiteInfo` is a total
function of the id — the MPL provides the lookup and the table behind it is a fixed
compile-time constant — so the server operates on exactly the structure the MPL
associates with the id. What is given up is a test's ability to assert on suite
_properties_ directly. The remedy for that, when a test needs it, is to expose
`GetAlgorithmSuiteInfo` as an operation, **not** to inline the structure into the
materials.

### Unwrapped data keys travel over plaintext HTTP

`EncryptionMaterials.plaintextDataKey` is on the wire, and `OnEncrypt` returns it.
Unwrapped data keys therefore cross an unencrypted HTTP connection.

This is accepted, deliberately. The keys are test-only fixtures committed in plain
sight in `TestKeyMaterial`; they protect nothing. The server binds **loopback only**.
And the alternative — keeping materials server-side behind handles — would prevent a
test from carrying materials from one language's `OnEncrypt` to another language's
`OnDecrypt`, which is the entire point of the eventual cross-language matrix.

**Do not** point this server at real key material, and do not expose it off-host.

### An empty handle is rejected by the framework, not by the two modeled errors

`ResourceId` carries `@length(min: 1)`, and smithy-java enforces modeled constraints
in its framework layer _before_ any handler runs. An empty handle therefore surfaces
as smithy-java's own `ValidationException` rather than as a `GenericServerError`. The
call still fails loudly, naming the offending member, but the "every failure is one
of two modeled errors" guarantee holds for handler outcomes, not for constraint
violations rejected upstream of them.

### The rpcv2Cbor `__type` fix is load-bearing

Stock smithy-java (through 1.4.0) omits the `__type` discriminator when serializing a
modeled error over rpcv2Cbor, so the generated client cannot tell one error shape
from another; both arrive as an untyped `CallException` with a bare HTTP 400. The
`server/protocol/` package fixes this with a subclassed protocol whose codec
serializes a `ModeledException` as a discriminated document. Success responses stay
byte-identical to stock.

If the two modeled errors ever start arriving untyped, check that
`META-INF/services/software.amazon.smithy.java.server.core.ServerProtocolProvider`
still registers the provider — without that line the protocol class is dead code.

A future hand-implemented server in another language must emit exactly:

```
{"__type": "aws.cryptography.materialProviders.testServer#GenericServerError",
 "message": "..."}
```

with a 4xx status.

## Phase 2 backlog

- **AWS KMS keyrings** — `CreateAwsKmsKeyring`, `CreateAwsKmsMultiKeyring`, MRK and
  discovery variants, `CreateAwsKmsRsaKeyring`. Needs a KMS client constructed
  server-side from a region or a client-supplier handle, since a client cannot cross
  the wire. New KMS keys are to be provisioned by a **CloudFormation** template under
  `../cfn/` — this repository uses CFN, not CDK.
- **The hierarchical keyring** and the Key Store it needs: a DynamoDB table plus a
  KMS key, also via `../cfn/`.
- **CMMs** — `CreateDefaultCryptographicMaterialsManager`,
  `CreateRequiredEncryptionContextCMM`, `GetEncryptionMaterials`,
  `DecryptMaterials`. A CMM holds a keyring handle, so handle-to-handle composition
  is already proven by the multi-keyring.
- **Caches** — `CreateCryptographicMaterialsCache` plus `PutCacheEntry`,
  `GetCacheEntry`, `UpdateUsageMetadata`, `DeleteCacheEntry`, and a new
  `ResourceKind`.
- **`ClientSupplier` and `BranchKeyIdSupplier` handles.**
- **`GetAlgorithmSuiteInfo`** as an operation, so a test can assert on suite
  properties (see the deviation above).
- **The pairwise `(encrypt, decrypt)` matrix.** With one server it collapses to a
  single self-pair, which is why it is deferred; the target plumbing is already
  `(language, majorVersion, endpoint)`-shaped so this is a change to
  `LanguageServerRegistry` alone.
- **A second language server** — Python, .NET, Rust, or Go. Adding one is a new
  `servers/<lang>/` plus one `Configuration_Entry`; no change to the model, the
  client, or the tests. The CI workflow's `os` matrix is the place to widen coverage
  if a server ever becomes OS-sensitive.

## Reference

The design and requirements are recorded at
`nextgen/.kiro/specs/mpl-test-server/`.
