// Hand-rolled rpcv2Cbor HTTP Language_Server for the MPL TestServer. The wire
// contract is the commons model (aws-crypto-tools-commons,
// mpl/test-server/model/mpl-test-server.smithy); every operation delegates to
// the Java MaterialProviders client built from this repository's source
// (AwsCryptographicMaterialProviders/runtimes/java, `make build_java
// mvn_local_deploy`) and consumed from the local Maven repository, at the
// javaMPLVersion in the repository's project.properties.
import java.util.Properties

plugins {
    java
}

repositories {
    mavenLocal()
    mavenCentral()
}

val materialProvidersVersion: String = Properties().apply {
    rootDir.resolve("../../../project.properties").reader().use { load(it) }
}.getProperty("javaMPLVersion")
val jacksonVersion: String by project

dependencies {
    implementation("software.amazon.cryptography:aws-cryptographic-material-providers:$materialProvidersVersion")
    implementation("com.fasterxml.jackson.core:jackson-databind:$jacksonVersion")
    implementation("com.fasterxml.jackson.dataformat:jackson-dataformat-cbor:$jacksonVersion")
}

tasks.register<JavaExec>("runServer") {
    group = "application"
    description = "Start the MPL TestServer on the port given as the first argument."
    mainClass.set("aws.cryptography.mpl.testserver.server.ServerMain")
    classpath = sourceSets["main"].runtimeClasspath
}
