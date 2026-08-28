// The one MPL TestServer Tests suite.
//
// There is no `main` source set: the harness IS the tests. Everything here is test
// code, split by package into conformance tests (MPL behavior) and meta tests (the
// harness's own wire contract).

// Imported explicitly: inside a Gradle Kotlin BUILD script a bare `java.util...`
// resolves `java` to the Java plugin's extension rather than the package.
import java.util.Properties

plugins {
    `java`
}

repositories {
    mavenCentral()
}

val versions = Properties().apply {
    rootDir.resolve("../versions.properties").inputStream().use { load(it) }
}
val smithyJavaVersion: String = versions.getProperty("smithyJavaVersion")
val junitVersion: String = versions.getProperty("junitVersion")
val javaToolchainVersion: String = versions.getProperty("javaToolchainVersion")

java {
    toolchain {
        languageVersion.set(JavaLanguageVersion.of(javaToolchainVersion.toInt()))
    }
}

dependencies {
    // The ONE generated Java Test_Client, from the ../client-java included build.
    testImplementation("aws.cryptography.mpl.testserver:mpl-test-server-client-java")

    // The client runtime: the rpcv2Cbor protocol and the JDK HTTP transport.
    testImplementation("software.amazon.smithy.java:client-core:$smithyJavaVersion")
    testImplementation("software.amazon.smithy.java:client-rpcv2-cbor:$smithyJavaVersion")
    testImplementation("software.amazon.smithy.java:client-http:$smithyJavaVersion")
    // ValidationException lives here: smithy-java enforces modeled constraints such as
    // @length in its framework layer, so a constraint violation surfaces as one of these
    // rather than as one of the TestServer's two modeled errors.
    testImplementation("software.amazon.smithy.java:framework-errors:$smithyJavaVersion")

    testImplementation("org.junit.jupiter:junit-jupiter-api:$junitVersion")
    testImplementation("org.junit.jupiter:junit-jupiter-params:$junitVersion")
    testRuntimeOnly("org.junit.jupiter:junit-jupiter-engine:$junitVersion")
    testRuntimeOnly("org.junit.platform:junit-platform-launcher")
}

tasks.withType<Test>().configureEach {
    useJUnitPlatform()

    // Forward every `mpl.testserver.*` property into the forked test JVM, so the
    // Tests learn their targets from runtime configuration and never from a
    // hard-coded endpoint.
    systemProperties(
        System.getProperties()
            .stringPropertyNames()
            .filter { it.startsWith("mpl.testserver.") }
            .associateWith { System.getProperty(it) }
    )

    testLogging {
        events("passed", "skipped", "failed")
        showStandardStreams = true
        showExceptions = true
        showCauses = true
        showStackTraces = true
        exceptionFormat = org.gradle.api.tasks.testing.logging.TestExceptionFormat.FULL
    }
}
