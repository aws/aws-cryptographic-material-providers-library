// The Java Language_Server for the MPL TestServer. Its request decoding, response
// and error encoding, and routing are generated from the single source-of-truth
// model by smithy-java SERVER codegen (Requirement 1.6); only the operation handler
// bodies, the Resource_Registry, and the error classifier are hand-written.
//
// NOTE: Gradle extracts the `pluginManagement` block and compiles it in isolation,
// so it does not see this file's imports -- `java.util.Properties` is spelled out
// in full inside it.
pluginManagement {
    val versions = java.util.Properties().apply {
        rootDir.resolve("../../versions.properties").inputStream().use { load(it) }
    }
    val smithyGradleVersion: String = versions.getProperty("smithyGradleVersion")

    plugins {
        id("software.amazon.smithy.gradle.smithy-base").version(smithyGradleVersion)
    }

    repositories {
        mavenCentral()
        gradlePluginPortal()
    }
}

// The Foojay toolchain resolver lets Gradle DOWNLOAD the pinned Java toolchain when
// the host has no matching JDK, so a fresh checkout builds without the developer
// first installing one by hand.
plugins {
    id("org.gradle.toolchains.foojay-resolver-convention") version "0.9.0"
}

rootProject.name = "mpl-test-server-java"
