// Hand-rolled rpcv2Cbor HTTP Language_Server for the Primitives TestServer.
// Every operation is delegated to the Java AtomicPrimitives client from the
// published aws-cryptographic-material-providers artifact on Maven Central,
// which bundles the primitives. Runs on the harness JDK 21.
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
    description = "Start the Primitives TestServer on the port given as the first argument."
    mainClass.set("aws.cryptography.primitives.testserver.server.ServerMain")
    classpath = sourceSets["main"].runtimeClasspath
}
