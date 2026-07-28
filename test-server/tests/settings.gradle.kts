// The single Tests suite: one definition, driving any Language_Server through the ONE
// generated Java Test_Client. There are no per-language copies.
//
// The Tests are ENDPOINT-ONLY: a Language_Server is located exclusively through the
// `mpl.testserver.targets` runtime property the orchestrator supplies. No server build
// is included here, so relocating or adding a server needs no change to this module.
pluginManagement {
    repositories {
        mavenCentral()
        gradlePluginPortal()
    }
}

// The Foojay toolchain resolver lets Gradle DOWNLOAD the pinned Java toolchain when
// the host has no matching JDK.
plugins {
    id("org.gradle.toolchains.foojay-resolver-convention") version "0.9.0"
}

rootProject.name = "mpl-test-server-tests"

// The one and only generated Java Test_Client, consumed as a composite build so the
// client is never regenerated here. Dependency substitution maps a stable coordinate
// onto the included build's root project.
includeBuild("../client-java") {
    dependencySubstitution {
        substitute(module("aws.cryptography.mpl.testserver:mpl-test-server-client-java"))
            .using(project(":"))
    }
}
