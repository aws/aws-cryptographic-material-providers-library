// Builds the single, typed Java Test_Client for the MPL TestServer over rpcv2Cbor
// (Requirement 1.5). Generated from the single source-of-truth model at
// ../model by smithy-java's `java-codegen` plugin in CLIENT mode, then compiled.
//
// Generated sources land under build/ and are NEVER committed (Requirement 1.8), so
// regeneration always overwrites cleanly.

// Imported explicitly: inside a Gradle Kotlin BUILD script a bare `java.util...`
// resolves `java` to the Java plugin's extension rather than the package.
import java.util.Properties

plugins {
    `java-library`
    id("software.amazon.smithy.gradle.smithy-base")
}

repositories {
    mavenCentral()
}

val versions = Properties().apply {
    rootDir.resolve("../versions.properties").inputStream().use { load(it) }
}
val smithyJavaVersion: String = versions.getProperty("smithyJavaVersion")
val smithyProtocolTraitsVersion: String = versions.getProperty("smithyProtocolTraitsVersion")
val javaToolchainVersion: String = versions.getProperty("javaToolchainVersion")

java {
    toolchain {
        languageVersion.set(JavaLanguageVersion.of(javaToolchainVersion.toInt()))
    }
}

dependencies {
    // --- Code generation (smithy build classpath only) ---
    smithyBuild("software.amazon.smithy.java:codegen-plugin:$smithyJavaVersion")
    // The rpcv2Cbor protocol trait must resolve while the model is being built, or
    // `smithy.protocols#rpcv2Cbor` is an unresolved shape reference.
    smithyBuild("software.amazon.smithy:smithy-protocol-traits:$smithyProtocolTraitsVersion")

    // --- Runtime of the generated client ---
    // `api`, not `implementation`: the Tests compile against the client's builder,
    // its protocol, and the generated shape types, so these must be on their
    // compile classpath transitively.
    api("software.amazon.smithy.java:client-core:$smithyJavaVersion")
    api("software.amazon.smithy.java:client-rpcv2-cbor:$smithyJavaVersion")
    api("software.amazon.smithy.java:client-http:$smithyJavaVersion")
}

// The model is owned by ../model; this module only consumes it. Disable the
// formatter so building the client never rewrites the source of truth.
smithy {
    format.set(false)
}

// Consume the ONE model rather than a copy (Requirement 1.1).
sourceSets {
    main {
        smithy {
            srcDir("../model/src/main/smithy")
        }
    }
}

// Compile the generated sources alongside this module.
afterEvaluate {
    val generated = smithy.getPluginProjectionPath(smithy.sourceProjection.get(), "java-codegen").get()
    sourceSets {
        main {
            java { srcDir("$generated/java") }
            resources { srcDir("$generated/resources") }
        }
    }
}

tasks.named("compileJava") { dependsOn("smithyBuild") }
tasks.named("processResources") { dependsOn("smithyBuild") }
