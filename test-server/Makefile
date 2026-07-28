# ============================================================================
# MPL TestServer — developer entry point
# ----------------------------------------------------------------------------
# The TestServer is a set of INDEPENDENT Gradle builds sharing one wrapper:
#
#   model/          the single source-of-truth Smithy model (validated alone)
#   client-java/    the one generated Java Test_Client
#   servers/java/   the Java Language_Server
#   tests/          the one Tests suite (conformance + meta)
#   orchestrator/   Configuration_Set -> launch -> run -> report
#
# Each is its own build root (its own settings.gradle.kts), so a target cannot
# invoke another module's task; this Makefile hides that by pointing the shared
# wrapper at the right project directory with `-p`.
#
# THE PREREQUISITE THAT MAKES THIS DIFFERENT FROM A NON-DAFNY TESTSERVER:
# the Artifact_Under_Test does not exist as a consumable artifact until the MPL's
# Dafny source has been transpiled to Java and published to the local Maven
# repository. `mpl-local-publish` does that, and the server build depends on it.
#
# Usage:
#   make                       # help
#   make mpl-local-publish     # transpile Dafny -> Java, publish to ~/.m2
#   make validate              # validate the model on its own
#   make build                 # generate + compile every module
#   make test                  # run the Tests against a server on PORT
#   make run-server            # start the Java Language_Server in the foreground
#   make orchestrate           # full run: launch, test, tear down, report
# ============================================================================

SHELL := bash

MAKEFILE_DIR := $(abspath $(dir $(lastword $(MAKEFILE_LIST))))
REPO_ROOT    := $(abspath $(MAKEFILE_DIR)/..)

MODEL_DIR  := $(MAKEFILE_DIR)/model
CLIENT_DIR := $(MAKEFILE_DIR)/client-java
SERVER_DIR := $(MAKEFILE_DIR)/servers/java
TESTS_DIR  := $(MAKEFILE_DIR)/tests
ORCH_DIR   := $(MAKEFILE_DIR)/orchestrator
CONFIG_DIR := $(MAKEFILE_DIR)/config

GRADLEW    := $(MAKEFILE_DIR)/gradlew
MARKER_DIR := $(MAKEFILE_DIR)/.make

# The port the Java Language_Server binds. Keep in step with the java entry's
# `port` in config/configuration-set.json; the orchestrator reads the file, while
# the manual two-step (`run-server` + `test`) uses this.
PORT ?= 8101

# ----------------------------------------------------------------------------
# Artifact_Under_Test coordinates
# ----------------------------------------------------------------------------
# The MPL's Java version is READ from the repository's own declaration and never
# hard-coded: at the time of writing it is 1.11.1-SNAPSHOT, and 1.11.1 is NOT a
# released version (only 1.11.0 is), so any hard-coded guess resolves nothing.
MPL_VERSION := $(shell sed -n 's/^javaMPLVersion=//p' $(REPO_ROOT)/project.properties)
DAFNY_VERSION := $(shell sed -n 's/^dafnyVersion=//p' $(REPO_ROOT)/project.properties)
MPL_DIR := $(REPO_ROOT)/AwsCryptographicMaterialProviders

# ----------------------------------------------------------------------------
# Toolchain discovery
# ----------------------------------------------------------------------------
# TWO different JDKs are needed, for two different builds:
#
#   JAVA_HOME      -- a JDK 21+ for the TestServer's own Gradle builds
#                     (smithy-java 1.x baselines on Java 21).
#   MPL_JAVA_HOME  -- a JDK the MPL's OWN build can use. That build pins a Java 8
#                     toolchain and ships a Gradle 7.6 wrapper, and Gradle 7.6
#                     cannot run on a JDK newer than 19 -- so the JDK 21+ above
#                     cannot launch it.
#
# Both are overridable: `make JAVA_HOME=/path/to/jdk21 <target>`.

# First existing candidate wins. An empty candidate is skipped, so an unset
# environment variable cannot accidentally match a root-relative path.
define first_existing
$(firstword $(foreach c,$(1),$(if $(and $(c),$(wildcard $(c)/bin/java)),$(c),)))
endef

# JAVA_HOME_<v>_X64 are set by actions/setup-java, so a CI runner is discovered
# without the workflow having to spell the toolcache path out.
JAVA_HOME ?= $(call first_existing,\
	$(JAVA_HOME_21_X64) \
	$(JAVA_HOME_21_ARM64) \
	$(HOME)/tools/corretto-21 \
	/usr/lib/jvm/java-21 \
	/usr/lib/jvm/java-21-amazon-corretto \
	$(wildcard $(HOME)/.gradle/jdks/*/jdk-21*))

MPL_JAVA_HOME ?= $(call first_existing,\
	$(JAVA_HOME_8_X64) \
	$(JAVA_HOME_8_ARM64) \
	$(JAVA_HOME_17_X64) \
	$(JAVA_HOME_17_ARM64) \
	/apollo/env/ApolloCommandLine/jdk1.8 \
	$(wildcard $(HOME)/.gradle/jdks/*/jdk-17*) \
	/usr/lib/jvm/java-17 \
	/usr/lib/jvm/java-1.8.0)

# Dafny must be available at the exact version the repo pins. It may be on PATH
# already -- which is how the repository's own `setup_dafny` CI action provides it --
# or unpacked in a directory we can prepend to PATH.
DAFNY_ON_PATH := $(shell command -v dafny 2>/dev/null)

DAFNY_HOME ?= $(firstword $(foreach c,\
	$(HOME)/tools/dafny-$(DAFNY_VERSION)/dafny \
	$(HOME)/tools/dafny/dafny \
	/opt/dafny,\
	$(if $(wildcard $(c)/dafny),$(c),)))

# Prepend DAFNY_HOME only when there is one; an empty value would put the working
# directory on PATH.
DAFNY_PATH_PREFIX := $(if $(DAFNY_HOME),PATH="$(DAFNY_HOME):$$PATH",)

GRADLE := JAVA_HOME="$(JAVA_HOME)" "$(GRADLEW)"

.DEFAULT_GOAL := help

.PHONY: help check-java check-dafny mpl-local-publish mpl-use-published validate generate \
        build build-client build-server build-tests run-server test \
        orchestrate clean clean-mpl-marker

# ----------------------------------------------------------------------------
help: ## Show this help
	@echo "MPL TestServer targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'
	@echo ""
	@echo "Variables:"
	@echo "  PORT=$(PORT)"
	@echo "  MPL_VERSION=$(MPL_VERSION)   (read from ../project.properties)"
	@echo "  DAFNY_VERSION=$(DAFNY_VERSION) (read from ../project.properties)"
	@echo "  JAVA_HOME=$(if $(strip $(JAVA_HOME)),$(JAVA_HOME),<unresolved - set to a JDK 21+>)"
	@echo "  MPL_JAVA_HOME=$(if $(strip $(MPL_JAVA_HOME)),$(MPL_JAVA_HOME),<unresolved - set to a JDK 8..19>)"
	@echo "  DAFNY_HOME=$(if $(strip $(DAFNY_HOME)),$(DAFNY_HOME),<unresolved - see check-dafny>)"

# ----------------------------------------------------------------------------
check-java: ## Verify a JDK 21+ is resolved (smithy-java requires 21+)
	@if [ -z "$(strip $(JAVA_HOME))" ]; then \
		echo "ERROR: no JDK 21+ found. smithy-java 1.x requires Java 21 or newer." >&2; \
		echo "       Install one, or point at it explicitly:" >&2; \
		echo "         make JAVA_HOME=/path/to/jdk21 <target>" >&2; \
		exit 1; \
	fi
	@version=$$("$(JAVA_HOME)/bin/java" -version 2>&1 | sed -n '1s/.*version "\([0-9]*\).*/\1/p'); \
	if [ -z "$$version" ] || [ "$$version" -lt 21 ]; then \
		echo "ERROR: JAVA_HOME=$(JAVA_HOME) is Java $$version; 21+ is required." >&2; \
		exit 1; \
	fi; \
	echo "==> TestServer builds use JAVA_HOME=$(JAVA_HOME) (Java $$version)"

check-dafny: ## Verify the pinned Dafny and an MPL-compatible JDK are available
	@if [ -z "$(strip $(DAFNY_HOME))" ] && [ -z "$(strip $(DAFNY_ON_PATH))" ]; then \
		echo "ERROR: Dafny $(DAFNY_VERSION) not found, on PATH or at $(HOME)/tools/dafny-$(DAFNY_VERSION)/dafny." >&2; \
		echo "       The MPL pins dafnyVersion in project.properties; install that exact version:" >&2; \
		echo "         curl -sL -o /tmp/dafny.zip \\" >&2; \
		echo "           https://github.com/dafny-lang/dafny/releases/download/v$(DAFNY_VERSION)/dafny-$(DAFNY_VERSION)-x64-ubuntu-20.04.zip" >&2; \
		echo "         mkdir -p $(HOME)/tools/dafny-$(DAFNY_VERSION) && unzip -q /tmp/dafny.zip -d $(HOME)/tools/dafny-$(DAFNY_VERSION)" >&2; \
		echo "       Or point at an existing install: make DAFNY_HOME=/path/to/dafny <target>" >&2; \
		exit 1; \
	fi
	@# The transpiled output is version-sensitive, so a mismatched Dafny is reported rather
	@# than silently producing an artifact that differs from what CI and releases build.
	@found=$$($(DAFNY_PATH_PREFIX) dafny --version 2>/dev/null | head -1); \
	case "$$found" in \
		$(DAFNY_VERSION)*) echo "==> Dafny: $$found" ;; \
		*) echo "ERROR: the repository pins Dafny $(DAFNY_VERSION), but the available Dafny is '$$found'." >&2; \
		   echo "       Transpiled output is version-sensitive; install the pinned version or pass" >&2; \
		   echo "       DAFNY_HOME=/path/to/dafny-$(DAFNY_VERSION)." >&2; \
		   exit 1 ;; \
	esac
	@if [ -z "$(strip $(MPL_JAVA_HOME))" ]; then \
		echo "ERROR: no JDK 8..19 found to launch the MPL's own Gradle 7.6 build." >&2; \
		echo "       The MPL pins a Java 8 toolchain; Gradle 7.6 cannot run on JDK 21+." >&2; \
		echo "         make MPL_JAVA_HOME=/path/to/jdk8 <target>" >&2; \
		exit 1; \
	fi
	@echo "==> MPL build uses MPL_JAVA_HOME=$(MPL_JAVA_HOME)"

# ----------------------------------------------------------------------------
# Build and publish the Artifact_Under_Test.
#
# Marker-file based so the (slow) transpile is not repeated on every build, but
# `make clean-mpl-marker mpl-local-publish` always forces a rebuild.
MPL_MARKER := $(MARKER_DIR)/mpl-published-$(MPL_VERSION)

mpl-local-publish: $(MPL_MARKER) ## Transpile the MPL's Dafny to Java and publish it to ~/.m2

# NOTE: `check-dafny` is invoked inside the recipe, NOT declared as a prerequisite. A .PHONY
# prerequisite is always considered out of date, so naming it here would make this marker
# rule re-run on every build -- defeating the marker entirely and, worse, demanding Dafny on
# a machine that already has the artifact (which is exactly the CI case).
$(MPL_MARKER):
	@$(MAKE) --no-print-directory check-dafny
	@echo "==> Publishing the Artifact_Under_Test: $(MPL_VERSION)"
	@# The MPL sets ENABLE_EXTERN_PROCESSING=1, so transpiling runs `sed` passes that
	@# strip `{:extern ...}` from TRACKED .dfy files and restore them afterwards. A
	@# run that starts from a dirty tree, or is interrupted between the two passes,
	@# leaves tracked source modified. Refuse to start from a dirty tree so a failure
	@# is never confused with a pre-existing edit.
	@if [ -n "$$(cd $(REPO_ROOT) && git status --porcelain -- '*.dfy')" ]; then \
		echo "ERROR: tracked Dafny source is modified. Transpiling rewrites .dfy files" >&2; \
		echo "       in place, so refusing to start from a dirty tree:" >&2; \
		(cd $(REPO_ROOT) && git status --porcelain -- '*.dfy') >&2; \
		exit 1; \
	fi
	@# ENFORCE_DETERMINISM_OPTION is passed EXPLICITLY to bypass a hook in
	@# smithy-dafny/SmithyDafnyMakefile.mk that computes it by running Gradle and
	@# capturing stdout. That Gradle project cannot resolve its own
	@# smithy-python/smithy-rust codegen dependencies, and on a cold wrapper cache
	@# its output begins with the distribution download progress -- which is then
	@# spliced into the `dafny translate` command line and fails the transpile with
	@# "Command-line argument 'Downloading' is neither a recognized option".
	cd $(MPL_DIR) && \
		$(DAFNY_PATH_PREFIX) \
		JAVA_HOME="$(MPL_JAVA_HOME)" \
		$(MAKE) ENFORCE_DETERMINISM_OPTION=--enforce-determinism \
			transpile_java mvn_local_deploy_dependencies mvn_local_deploy
	@# The restore pass must have left tracked source exactly as it was.
	@if [ -n "$$(cd $(REPO_ROOT) && git status --porcelain -- '*.dfy')" ]; then \
		echo "ERROR: transpiling left tracked Dafny source modified; the extern-restore" >&2; \
		echo "       pass did not complete. Inspect and revert before continuing:" >&2; \
		(cd $(REPO_ROOT) && git status --porcelain -- '*.dfy') >&2; \
		exit 1; \
	fi
	@if [ ! -f "$(HOME)/.m2/repository/software/amazon/cryptography/aws-cryptographic-material-providers/$(MPL_VERSION)/aws-cryptographic-material-providers-$(MPL_VERSION).jar" ]; then \
		echo "ERROR: publish reported success but the artifact is not in ~/.m2:" >&2; \
		echo "       software.amazon.cryptography:aws-cryptographic-material-providers:$(MPL_VERSION)" >&2; \
		exit 1; \
	fi
	@mkdir -p $(MARKER_DIR)
	@touch $@
	@echo "==> Published software.amazon.cryptography:aws-cryptographic-material-providers:$(MPL_VERSION)"

clean-mpl-marker: ## Forget that the Artifact_Under_Test was published (forces a re-transpile)
	@rm -f $(MARKER_DIR)/mpl-published-*
	@echo "==> Cleared the publish marker."

# ----------------------------------------------------------------------------
# For CI: accept an Artifact_Under_Test that an EARLIER JOB already published.
#
# The repository's `library_java_build.yml` already transpiles the MPL and uploads
# `~/.m2/repository/software/amazon/` as an artifact. A TestServer job that downloads
# it does not need Dafny, does not need the second JDK, and must not spend ten minutes
# re-transpiling source it already has a build of.
#
# This is deliberately a SEPARATE, opt-in target rather than a fallback inside
# `mpl-local-publish`. Making the publish silently skip when a jar happens to be present
# would mean a developer who edited Dafny source and re-ran the harness would keep
# testing the stale artifact -- the single most confusing failure this harness could have.
mpl-use-published: ## Use an MPL artifact already in ~/.m2 (CI: published by an earlier job)
	@jar="$(HOME)/.m2/repository/software/amazon/cryptography/aws-cryptographic-material-providers/$(MPL_VERSION)/aws-cryptographic-material-providers-$(MPL_VERSION).jar"; \
	if [ ! -f "$$jar" ]; then \
		echo "ERROR: no published Artifact_Under_Test found at:" >&2; \
		echo "         $$jar" >&2; \
		echo "       Expected software.amazon.cryptography:aws-cryptographic-material-providers:$(MPL_VERSION)" >&2; \
		echo "       (version read from ../project.properties)." >&2; \
		echo "       Either run \`make mpl-local-publish\` to build it from this working tree," >&2; \
		echo "       or, in CI, ensure the maven-local artifact was downloaded first." >&2; \
		exit 1; \
	fi; \
	mkdir -p $(MARKER_DIR); \
	touch $(MPL_MARKER); \
	echo "==> Using the already-published $(MPL_VERSION) from ~/.m2 (no transpile)."

# ----------------------------------------------------------------------------
validate: check-java ## Validate the Smithy model on its own
	@echo "==> Validating model/mpl-test-server.smithy"
	@$(GRADLE) -p $(MODEL_DIR) build --console=plain -q
	@echo "==> Model is valid."

# ----------------------------------------------------------------------------
generate: check-java ## Generate the Test_Client and the Language_Server scaffolding
	@echo "==> Generating the Java Test_Client (client-java)"
	@$(GRADLE) -p $(CLIENT_DIR) smithyBuild --console=plain
	@echo "==> Generating the Java Language_Server scaffolding (servers/java)"
	@$(GRADLE) -p $(SERVER_DIR) smithyBuild --console=plain

build: build-client build-server build-tests ## Generate and compile every module
	@echo "==> All modules built."

build-client: check-java ## Compile the generated Java Test_Client
	@echo "==> Building client-java"
	@$(GRADLE) -p $(CLIENT_DIR) build -x test --console=plain

build-server: check-java mpl-local-publish ## Compile the Java Language_Server
	@echo "==> Building servers/java"
	@$(GRADLE) -p $(SERVER_DIR) build -x test --console=plain

build-tests: check-java ## Compile the Tests suite
	@echo "==> Building tests"
	@$(GRADLE) -p $(TESTS_DIR) build -x test --console=plain

# ----------------------------------------------------------------------------
run-server: check-java mpl-local-publish ## Start the Java Language_Server in the FOREGROUND on PORT
	@echo "==> Starting the Java Language_Server on port $(PORT) (Ctrl-C to stop)"
	@$(GRADLE) -p $(SERVER_DIR) runServer --args="$(PORT)" --console=plain

test: check-java ## Run the Tests against a Language_Server already listening on PORT
	@echo "==> Running the Tests against http://127.0.0.1:$(PORT)"
	@$(GRADLE) -p $(TESTS_DIR) cleanTest test --no-daemon --console=plain \
		-Dmpl.testserver.targets=java:1=http://127.0.0.1:$(PORT)

orchestrate: check-java mpl-local-publish ## Full run: read the Configuration_Set, launch, test, tear down, report
	@echo "==> Orchestrating from $(CONFIG_DIR)/configuration-set.json"
	@$(GRADLE) -p $(ORCH_DIR) run --console=plain \
		--args="--configuration-set $(CONFIG_DIR)/configuration-set.json --test-server-root $(MAKEFILE_DIR)"

# ----------------------------------------------------------------------------
clean: ## Remove build output from every module (keeps the publish marker)
	@for d in $(MODEL_DIR) $(CLIENT_DIR) $(SERVER_DIR) $(TESTS_DIR) $(ORCH_DIR); do \
		if [ -f "$$d/settings.gradle.kts" ]; then \
			echo "==> clean $$d"; \
			JAVA_HOME="$(JAVA_HOME)" "$(GRADLEW)" -p "$$d" clean --console=plain -q || exit 1; \
		fi; \
	done
	@echo "==> Cleaned."
