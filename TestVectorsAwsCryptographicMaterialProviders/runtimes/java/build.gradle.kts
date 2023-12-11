// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

val accpLocalJar: String by project
val publishedVersion: String by project

plugins {
    `java-library`
    `maven-publish`
    // OS Detector for Optional ACCP
    id("com.google.osdetector") version "1.7.0"
}

group = "software.amazon.cryptography"
version = "1.0-SNAPSHOT"
description = "TestAwsCryptographicMaterialProviders"

java {
    toolchain.languageVersion.set(JavaLanguageVersion.of(8))
    sourceSets["main"].java {
        srcDir("src/main/java")
        srcDir("src/main/dafny-generated")
        srcDir("src/main/smithy-generated")
    }
    sourceSets["test"].java {
        srcDir("src/test/dafny-generated")
    }
}

repositories {
    mavenCentral()
    mavenLocal()
}

dependencies {
    implementation("org.dafny:DafnyRuntime:4.2.0")
    implementation("software.amazon.smithy.dafny:conversion:0.1")
    implementation("software.amazon.cryptography:aws-cryptographic-material-providers:${
        if (project.hasProperty("publishedVersion")) publishedVersion else "1.0-SNAPSHOT"}")
    implementation(platform("software.amazon.awssdk:bom:2.19.1"))
    implementation("software.amazon.awssdk:dynamodb")
    implementation("software.amazon.awssdk:dynamodb-enhanced")
    implementation("software.amazon.awssdk:kms")
    implementation("software.amazon.awssdk:core:2.19.1")

    // ACCP ONLY supports Linux, otherwise you have to build it from source and provide it
    // https://github.com/corretto/amazon-corretto-crypto-provider/tree/main#compatibility--requirements
    if (project.hasProperty("accpLocalJar")) {
        logger.warn("Using ACCP Local Jar.")
        implementation(files(accpLocalJar)) // Our Code ALWAYS needs ACCP to Compile.
    } else if (osdetector.os.contains("linux")) {
        logger.warn("Using ACCP Linux from Maven with Suffix {}.", osdetector.classifier)
        implementation(
            "software.amazon.cryptools:AmazonCorrettoCryptoProvider:2.3.0:${osdetector.classifier}")
        testImplementation(
            "software.amazon.cryptools:AmazonCorrettoCryptoProvider:2.3.0:${osdetector.classifier}")
    } else {
        logger.warn("Using un-supported ACCP. Overriding detected os `${osdetector.os}` to be `linux`.")
        compileOnly(
            "software.amazon.cryptools:AmazonCorrettoCryptoProvider:2.3.0:${overrideClassifier()}")
        testCompileOnly(
            "software.amazon.cryptools:AmazonCorrettoCryptoProvider:2.3.0:${overrideClassifier()}")
    }
}

fun overrideClassifier(): String {
    if (!osdetector.os.contains("linux")) {
        return "linux-" + osdetector.arch
    }
    return osdetector.classifier
}

publishing {
    publications.create<MavenPublication>("maven") {
        groupId = group as String?
        artifactId = description
        from(components["java"])
    }
    repositories { mavenLocal() }
}

tasks.withType<JavaCompile>() {
    options.encoding = "UTF-8"
}

tasks.register<JavaExec>("runTests") {
    dependsOn("copyKeysJSON")
    mainClass.set("TestsFromDafny")
    classpath = sourceSets["test"].runtimeClasspath
}

tasks.register<Copy>("copyKeysJSON") {
    from(layout.projectDirectory.file("../../dafny/TestVectorsAwsCryptographicMaterialProviders/test/keys.json"))
    into(layout.projectDirectory.dir("dafny/TestVectorsAwsCryptographicMaterialProviders/test"))
}

tasks.wrapper {
    gradleVersion = "7.6"
}

