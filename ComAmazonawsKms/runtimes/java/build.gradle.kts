import java.io.File
import java.io.FileInputStream
import java.util.Properties
import java.net.URI
import javax.annotation.Nullable

plugins {
    `java-library`
    `maven-publish`
}

var props = Properties().apply {
    load(FileInputStream(File(rootProject.rootDir, "../../../project.properties")))
}
var dafnyVersion = props.getProperty("dafnyVersion")


group = "software.amazon.cryptography"
version = "1.0-SNAPSHOT"
description = "ComAmazonawsKms"

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

var caUrl: URI? = null
@Nullable
val caUrlStr: String? = System.getenv("CODEARTIFACT_REPO_URL")
if (!caUrlStr.isNullOrBlank()) {
    caUrl = URI.create(caUrlStr)
}

var caPassword: String? = null
@Nullable
val caPasswordString: String? = System.getenv("CODEARTIFACT_AUTH_TOKEN")
if (!caPasswordString.isNullOrBlank()) {
    caPassword = caPasswordString
}

repositories {
    mavenCentral()
    mavenLocal()
//    if (caUrl != null && caPassword != null) {
//        maven {
//            name = "CodeArtifact"
//            url = caUrl!!
//            credentials {
//                username = "aws"
//                password = caPassword!!
//            }
//        }
//    }
    maven {
        url = URI.create("https://github-mpl-370957321024.d.codeartifact.us-west-2.amazonaws.com/maven/aws-sdk-preview-build/")
        credentials {
            username = "aws"
            password = System.getenv("CODEARTIFACT_AUTH_TOKEN")
        }
    }
}

dependencies {
    implementation("org.dafny:DafnyRuntime:${dafnyVersion}")
    implementation("software.amazon.smithy.dafny:conversion:0.1")
    implementation("software.amazon.cryptography:StandardLibrary:1.0-SNAPSHOT")
    implementation(platform("software.amazon.awssdk:bom:2.25.46"))
    implementation("software.amazon.awssdk:kms:9.0.0-SNAPSHOT")
    implementation("software.amazon.awssdk:apache-client")
}

publishing {
    publications.create<MavenPublication>("mavenLocal") {
        groupId = "software.amazon.cryptography"
        artifactId = "ComAmazonawsKms"
        from(components["java"])
    }
    publications.create<MavenPublication>("maven") {
        groupId = "software.amazon.cryptography"
        artifactId = "ComAmazonawsKms"
        from(components["java"])
    }
    repositories { mavenLocal() }
}

tasks.withType<JavaCompile>() {
    options.encoding = "UTF-8"
}

tasks.withType<Wrapper>() {
    gradleVersion = "7.6"
}

tasks {
    register("runTests", JavaExec::class.java) {
        mainClass.set("TestsFromDafny")
        classpath = sourceSets["test"].runtimeClasspath
    }
}

