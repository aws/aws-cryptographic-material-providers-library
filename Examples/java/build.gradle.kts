// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: CC-BY-SA-4.0
import java.io.File
import java.io.FileInputStream
import java.util.Properties
import java.net.URI
import javax.annotation.Nullable
plugins {
    `java`
    `java-library`
}
var props = Properties().apply {
    load(FileInputStream(File(rootProject.rootDir, "../../project.properties")))
}
var dafnyVersion = props.getProperty("dafnyVersion")
group = "software.amazon.cryptography"
var mplVersion = props.getProperty("mplVersion")
description = "AWS Cryptographic Material Providers Library Examples"
var slf4jVersion = "1.7.32"
var esdkVersion = "3.0.1"
dependencies {
    // The Library being demonstrated
    implementation("software.amazon.cryptography:aws-cryptographic-material-providers:${mplVersion}")
    // Dafny dependencies
    implementation("org.dafny:DafnyRuntime:${dafnyVersion}")
    implementation("software.amazon.smithy.dafny:conversion:0.1.1")    
    // sdk dependencies
    implementation(platform("software.amazon.awssdk:bom:2.26.3"))
    // ESDK uses the MPL
    implementation("com.amazonaws:aws-encryption-sdk-java:${esdkVersion}")        
    // Example Dependencies
    implementation("software.amazon.awssdk:dynamodb")
    implementation("software.amazon.awssdk:kms")    
    implementation("software.amazon.awssdk:arns")
    implementation("software.amazon.awssdk:auth")
    implementation("software.amazon.awssdk:sts")
    implementation("software.amazon.awssdk:utils")
    implementation("software.amazon.awssdk:apache-client")
    annotationProcessor("org.projectlombok:lombok:1.18.30")
    implementation("com.google.code.findbugs:jsr305:3.0.2")
    // Needed to adapt Apache Commons Logging used by Apache HTTP Client to Slf4j to avoid
    // ClassNotFoundException: org.apache.commons.logging.impl.LogFactoryImpl during runtime
    implementation("org.slf4j:slf4j-api:${slf4jVersion}")
    implementation("org.slf4j:slf4j-simple:${slf4jVersion}")
    implementation("org.slf4j:jcl-over-slf4j:${slf4jVersion}")
    // https://mvnrepository.com/artifact/org.testng/testng
    testImplementation("org.testng:testng:7.5")
}
java {
    toolchain.languageVersion.set(JavaLanguageVersion.of(8))
    sourceSets["main"].java {
        srcDir("src/main/java")
    }
    sourceSets["test"].java {
        srcDir("src/test/java")
    }
    withJavadocJar()
    withSourcesJar()
}

repositories {
    mavenCentral()
    mavenLocal()
}

tasks.withType<JavaCompile>() {
    options.encoding = "UTF-8"
}

tasks.test {
    useTestNG()
    // This will show System.out.println statements
    testLogging.showStandardStreams = true
    testLogging { events("passed", "skipped") }
    filter {
        excludeTestsMatching("software.amazon.cryptography.example.hierarchy.concurrent.*")
    }
    // See https://github.com/gradle/kotlin-dsl/issues/836
    addTestListener(object : TestListener {
        override fun beforeSuite(suite: TestDescriptor) {}
        override fun beforeTest(testDescriptor: TestDescriptor) {}
        override fun afterTest(testDescriptor: TestDescriptor, result: TestResult) {}
        override fun afterSuite(suite: TestDescriptor, result: TestResult) {
            if (suite.parent == null) { // root suite
                logger.lifecycle("----")
                logger.lifecycle("Test result: ${result.resultType}")
                logger.lifecycle("Test summary: ${result.testCount} tests, " +
                        "${result.successfulTestCount} succeeded, " +
                        "${result.failedTestCount} failed, " +
                        "${result.skippedTestCount} skipped")
            }
        }
    })
}

val testConcurrent = task<Test>("testConcurrent") {
    description = "Runs concurrency tests."
    group = "verification"
    // This will show System.out.println statements
    testLogging.showStandardStreams = true
    useTestNG() {
        suites("src/test/java/software/amazon/cryptography/example/hierarchy/concurrent/testng-parallel.xml")
        maxParallelForks = 2
    }
    testLogging {
        events("passed")
    }
    filter {
        includeTestsMatching("software.amazon.cryptography.example.hierarchy.concurrent.*")
    }
}
