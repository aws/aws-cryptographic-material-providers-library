// The one and only generated Java Test_Client (Requirement 1.5).
//
// The TestServer generates exactly one client, and it is Java. There is no
// per-language client: a new Language_Server is driven by THIS client, because
// both are generated from the same model with the protocol declared once.
//
// NOTE: Gradle extracts the `pluginManagement` block and compiles it in isolation,
// so it does not see this file's imports -- `java.util.Properties` is spelled out
// in full inside it.
pluginManagement {
    val versions = java.util.Properties().apply {
        rootDir.resolve("../versions.properties").inputStream().use { load(it) }
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

rootProject.name = "mpl-test-server-client-java"
