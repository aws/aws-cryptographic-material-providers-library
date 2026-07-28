// Builds the Java Language_Server: the generated rpcv2Cbor scaffolding plus the
// hand-written handlers that delegate to the Artifact_Under_Test -- the MPL, as
// transpiled from this repository's Dafny source.

// Imported explicitly: inside a Gradle Kotlin BUILD script a bare `java.util...`
// resolves `java` to the Java plugin's extension rather than the package.
import java.util.Properties

plugins {
    `java-library`
    id("software.amazon.smithy.gradle.smithy-base")
}

repositories {
    // mavenLocal() FIRST and deliberately: the MPL artifact this server compiles
    // against is a -SNAPSHOT that exists ONLY after `make mpl-local-publish` has
    // transpiled the repository's Dafny source to Java and installed it here. It is
    // not on Maven Central, and must not be resolved from anywhere else -- the whole
    // point is to test THIS working tree.
    mavenLocal()
    mavenCentral()
}

val versions = Properties().apply {
    rootDir.resolve("../../versions.properties").inputStream().use { load(it) }
}
val smithyJavaVersion: String = versions.getProperty("smithyJavaVersion")
val smithyProtocolTraitsVersion: String = versions.getProperty("smithyProtocolTraitsVersion")
val javaToolchainVersion: String = versions.getProperty("javaToolchainVersion")

// The Artifact_Under_Test's version is READ from the repository's own declaration,
// never hard-coded (Requirement 11.3): at the time of writing it is 1.11.1-SNAPSHOT,
// and 1.11.1 is NOT released -- only 1.11.0 is -- so any hard-coded guess resolves
// nothing. Overridable with -PmplVersion=<v> for a deliberate experiment.
val repoProperties = Properties().apply {
    rootDir.resolve("../../../project.properties").inputStream().use { load(it) }
}
val mplVersion: String = (project.findProperty("mplVersion") as String?)
    ?: repoProperties.getProperty("javaMPLVersion")

java {
    toolchain {
        languageVersion.set(JavaLanguageVersion.of(javaToolchainVersion.toInt()))
    }
}

dependencies {
    // --- Code generation (smithy build classpath only) ---
    smithyBuild("software.amazon.smithy.java:codegen-plugin:$smithyJavaVersion")
    smithyBuild("software.amazon.smithy:smithy-protocol-traits:$smithyProtocolTraitsVersion")

    // --- Runtime of the generated server ---
    api("software.amazon.smithy.java:server-core:$smithyJavaVersion")
    // The stock rpcv2Cbor server protocol. The `__type`-emitting protocol in
    // server/protocol/ SUBCLASSES it rather than replacing it.
    api("software.amazon.smithy.java:server-rpcv2-cbor:$smithyJavaVersion")
    // The CBOR codec is used directly by the discriminating codec.
    implementation("software.amazon.smithy.java:cbor-codec:$smithyJavaVersion")
    // The Netty HTTP server provider, discovered via SPI, so Server.builder() can
    // bind a real endpoint. Needed by the launcher, not by the generated sources.
    runtimeOnly("software.amazon.smithy.java:server-netty:$smithyJavaVersion")

    // --- The Artifact_Under_Test ---
    implementation("software.amazon.cryptography:aws-cryptographic-material-providers:$mplVersion")
}

// The model is owned by ../../model; this module only consumes it. Disable the
// formatter so building the server never rewrites the source of truth.
smithy {
    format.set(false)
}

// Consume the ONE model rather than a copy (Requirement 1.1).
sourceSets {
    main {
        smithy {
            srcDir("../../model/src/main/smithy")
        }
    }
}

// Compile the generated scaffolding alongside the hand-written handlers.
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

// Start the Language_Server in the foreground on a port, for the manual two-step
// run (`make run-server` in one shell, `make test` in another) and for the
// orchestrator's launcher.
tasks.register<JavaExec>("runServer") {
    group = "application"
    description = "Start the Java Language_Server (rpcv2Cbor over HTTP) on a port."
    mainClass.set("aws.cryptography.mpl.testserver.server.launcher.ServerBootstrap")
    classpath = sourceSets["main"].runtimeClasspath
}
