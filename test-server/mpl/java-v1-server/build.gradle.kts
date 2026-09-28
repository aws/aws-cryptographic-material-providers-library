// Hand-rolled rpcv2Cbor HTTP Language_Server for the MPL TestServer. The wire
// contract is the commons model (aws-crypto-tools-commons,
// mpl/test-server/model/mpl-test-server.smithy); every operation delegates to
// the Java MaterialProviders client from the published
// aws-cryptographic-material-providers artifact on Maven Central.
plugins {
    java
}

repositories {
    mavenCentral()
}

val materialProvidersVersion: String by project
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
