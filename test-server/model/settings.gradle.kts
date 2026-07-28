// The model module exists to VALIDATE the single source-of-truth model on its own,
// independently of code generation, so a model mistake is reported as a model
// mistake rather than surfacing later as a confusing codegen or compile failure.
//
// NOTE: Gradle extracts the `pluginManagement` block and compiles it in isolation,
// so it does not see this file's imports -- `java.util.Properties` must be spelled
// out in full inside it. (Unlike a build script, a settings script has no `java`
// extension to shadow the package name.)
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

rootProject.name = "mpl-test-server-model"
