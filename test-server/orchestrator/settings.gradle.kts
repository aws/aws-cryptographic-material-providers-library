// The MPL TestServer Orchestrator: reads the Configuration_Set, validates it, launches each
// Language_Server on its configured port, runs the Tests against them, and reports fail-open.
//
// NOTE: Gradle extracts the `pluginManagement` block and compiles it in isolation, so it does
// not see this file's imports.
pluginManagement {
    repositories {
        mavenCentral()
        gradlePluginPortal()
    }
}

// The Foojay toolchain resolver lets Gradle DOWNLOAD the pinned Java toolchain when the host
// has no matching JDK.
plugins {
    id("org.gradle.toolchains.foojay-resolver-convention") version "0.9.0"
}

rootProject.name = "mpl-test-server-orchestrator"
