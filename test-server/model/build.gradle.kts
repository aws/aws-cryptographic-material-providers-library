// Validates `mpl-test-server.smithy` -- the single source of truth (Requirement 1.1).
//
// No codegen plugin is configured here on purpose: this module's whole job is to
// answer "is the model well-formed and valid?" so that answer never arrives
// disguised as a codegen or compile failure in client-java or servers/java.
//
// The model file lives at the Smithy Gradle plugin's conventional location for the
// `main` source set, `src/main/smithy/`, so no source directory needs overriding.

// Imported explicitly: inside a Gradle Kotlin BUILD script a bare `java.util...`
// resolves `java` to the Java plugin's extension rather than the package.
import java.util.Properties

plugins {
    // The Smithy plugin hangs its model source directories and its `smithyBuild`
    // dependency configuration off the Java source sets, so the `java` plugin must
    // be applied even though this module compiles no Java.
    `java`
    id("software.amazon.smithy.gradle.smithy-base")
}

repositories {
    mavenCentral()
}

val versions = Properties().apply {
    rootDir.resolve("../versions.properties").inputStream().use { load(it) }
}
val smithyProtocolTraitsVersion: String = versions.getProperty("smithyProtocolTraitsVersion")
val javaToolchainVersion: String = versions.getProperty("javaToolchainVersion")

java {
    toolchain {
        languageVersion.set(JavaLanguageVersion.of(javaToolchainVersion.toInt()))
    }
}

dependencies {
    // The rpcv2Cbor protocol trait must be resolvable for the model to validate;
    // `smithy.protocols#rpcv2Cbor` is otherwise an unresolved shape reference.
    smithyBuild("software.amazon.smithy:smithy-protocol-traits:$smithyProtocolTraitsVersion")
}

// This module OWNS the model, but validating it must never rewrite the source of
// truth as a side effect of running a build.
smithy {
    format.set(false)
}
