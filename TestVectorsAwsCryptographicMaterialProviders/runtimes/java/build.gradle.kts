import java.io.File
import java.io.FileInputStream
import java.util.Properties
import java.net.URI
import javax.annotation.Nullable

tasks.wrapper {
    gradleVersion = "7.6"
}

plugins {
    `java-library`
    `maven-publish`
    application
}

var props = Properties().apply {
    load(FileInputStream(File(rootProject.rootDir, "../../../project.properties")))
}
var dafnyVersion = props.getProperty("dafnyVersion")

group = "software.amazon.cryptography"
version = "1.5.0-SNAPSHOT"
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

var caUrl: URI? = null
@Nullable
val caUrlStr: String? = System.getenv("CODEARTIFACT_REPO_URL")
if (!caUrlStr.isNullOrBlank()) {
    caUrl = URI.create(caUrlStr)
}

var caPassword: String? = null
@Nullable
val caPasswordString: String? = System.getenv("CODEARTIFACT_TOKEN")
if (!caPasswordString.isNullOrBlank()) {
    caPassword = caPasswordString
}

repositories {
    mavenCentral()
    if (caUrl != null && caPassword != null) {
        maven {
            name = "CodeArtifact"
            url = caUrl!!
            credentials {
                username = "aws"
                password = caPassword!!
            }
        }
    }
}

dependencies {
    implementation("org.dafny:DafnyRuntime:${dafnyVersion}")
    implementation("software.amazon.smithy.dafny:conversion:0.1")
    
    // TODO: Automate keeping MPL version here and in MPL the same
    implementation("software.amazon.cryptography:aws-cryptographic-material-providers:1.5.0")
    
    // The following "transitive" dependencies of the MPL, in Java, are distributed in MPL as a "Fat Jar"
    // But the "Fat Jar"  is not composed in CI, only during publication.
    // So we directly depend on the SNAPSHOT versions, 
    // via the `settings.gradle.kts` file. 
    implementation("software.amazon.cryptography:StandardLibrary:1.0-SNAPSHOT")
    implementation("software.amazon.cryptography:ComAmazonawsKms:1.0-SNAPSHOT")
    implementation("software.amazon.cryptography:ComAmazonawsDynamodb:1.0-SNAPSHOT")
    implementation("software.amazon.cryptography:AwsCryptographyPrimitives:1.0-SNAPSHOT")
    
    implementation(platform("software.amazon.awssdk:bom:2.25.1"))
    
    implementation("software.amazon.awssdk:dynamodb")
    implementation("software.amazon.awssdk:dynamodb-enhanced")
    implementation("software.amazon.awssdk:kms")
}

publishing {
    publications.create<MavenPublication>("maven") {
        groupId = group as String?
        artifactId = description
        from(components["java"])
    }
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

tasks.register<Copy>("copyKeysJSONCurr") {
    from(layout.projectDirectory.file("../../dafny/TestVectorsAwsCryptographicMaterialProviders/test/keys.json"))
    into(layout.projectDirectory.dir("."))
}

application {
    mainClass.set("ImplementationFromDafny")
}
