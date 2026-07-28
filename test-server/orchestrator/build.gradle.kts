// The Orchestrator. Deliberately dependency-light: Jackson to parse the Configuration_Set, and
// nothing else. It drives the server and the Tests as SUBPROCESSES through the shared Gradle
// wrapper rather than linking against them, so it stays agnostic about how any given
// Language_Server is built or what language it is written in -- which is the point, since the
// next server may not be a JVM project at all.

// Imported explicitly: inside a Gradle Kotlin BUILD script a bare `java.util...` resolves
// `java` to the Java plugin's extension rather than the package.
import java.util.Properties

plugins {
    `java`
    application
}

repositories {
    mavenCentral()
}

val versions = Properties().apply {
    rootDir.resolve("../versions.properties").inputStream().use { load(it) }
}
val jacksonVersion: String = versions.getProperty("jacksonVersion")
val junitVersion: String = versions.getProperty("junitVersion")
val javaToolchainVersion: String = versions.getProperty("javaToolchainVersion")

java {
    toolchain {
        languageVersion.set(JavaLanguageVersion.of(javaToolchainVersion.toInt()))
    }
}

dependencies {
    implementation("com.fasterxml.jackson.core:jackson-databind:$jacksonVersion")

    testImplementation("org.junit.jupiter:junit-jupiter-api:$junitVersion")
    testRuntimeOnly("org.junit.jupiter:junit-jupiter-engine:$junitVersion")
    testRuntimeOnly("org.junit.platform:junit-platform-launcher")
}

application {
    mainClass.set("aws.cryptography.mpl.testserver.orchestrator.OrchestratorMain")
}

tasks.withType<Test>().configureEach {
    useJUnitPlatform()
}

// Forward stdout/stderr so the orchestrated run's output is what the developer sees.
tasks.named<JavaExec>("run") {
    standardInput = System.`in`
}
