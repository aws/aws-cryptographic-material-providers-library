// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

/*
  First run `make setup_semantic_release` to install the required dependencies.

  Using this config semantic-release will search for the latest tag
  evaluate all commits after that tag
  generate release notes and a version bump.
  It will commit these changes, push these changes, and publish a new version tag.

  This file requires a `--branches` option to function.
  This is to facilitate point releases if needed.

  `npx semantic-release --branches main`
*/

const Runtimes = {
  net: {
    "AwsCryptographicMaterialProviders/runtimes/net/MPL.csproj": {
      dependencies: [],
      assemblyInfo:
        "AwsCryptographicMaterialProviders/runtimes/net/AssemblyInfo.cs",
    },
    "ComAmazonawsKms/runtimes/net/AWS-KMS.csproj": {
      dependencies: [],
      assemblyInfo: "ComAmazonawsKms/runtimes/net/AssemblyInfo.cs",
    },
    "ComAmazonawsDynamodb/runtimes/net/ComAmazonawsDynamodb.csproj": {
      dependencies: [],
      assemblyInfo: "ComAmazonawsDynamodb/runtimes/net/AssemblyInfo.cs",
    },
    "AwsCryptographyPrimitives/runtimes/net/Crypto.csproj": {
      dependencies: [],
      assemblyInfo: "AwsCryptographyPrimitives/runtimes/net/AssemblyInfo.cs",
    },
    "StandardLibrary/runtimes/net/STD.csproj": {
      dependencies: [],
      assemblyInfo: "StandardLibrary/runtimes/net/AssemblyInfo.cs",
    },
  },
};

/**
 * @type {import('semantic-release').GlobalConfig}
 */
module.exports = {
  branches: ["main"],
  repositoryUrl:
    "git@github.com:aws/aws-cryptographic-material-providers-library.git",
  tagFormat: "v${version}-net",
  plugins: [
    // Check the commits since the last release
    [
      "@semantic-release/commit-analyzer",
      {
        preset: "conventionalcommits",
        parserOpts: {
          noteKeywords: ["NET BREAKING CHANGE", "NET BREAKING CHANGES"],
        },
        presetConfig: {
          types: [
            { type: "feat", section: "Features" },
            { type: "fix", section: "Fixes" },
            { type: "chore", section: "Maintenance" },
            { type: "docs", section: "Maintenance" },
            { type: "revert", section: "Fixes" },
            { type: "style", section: "Miscellaneous" },
            { type: "refactor", section: "Miscellaneous" },
            { type: "perf", section: "Miscellaneous" },
            { type: "test", section: "Miscellaneous" },
          ],
        },
        releaseRules: [
          { type: "docs", release: "patch" },
          { type: "revert", release: "patch" },
          { type: "chore", release: "patch" },
        ],
      },
    ],
    // Based on the commits generate release notes
    [
      "@semantic-release/release-notes-generator",
      {
        preset: "conventionalcommits",
        presetConfig: {
          types: [
            {
              type: "feat",
              scope: "dafny",
              section: "Features -- All Languages",
              hidden: false,
            },
            {
              type: "feat",
              scope: "dotnet",
              section: "Features -- DotNet",
              hidden: false,
            },
            { type: "feat", scope: "java", hidden: true },
            { type: "feat", scope: "python", hidden: true },
            { type: "feat", scope: "go", hidden: true },
            { type: "feat", scope: "rust", hidden: true },
            {
              type: "fix",
              scope: "dafny",
              section: "Fixes -- All Languages",
              hidden: false,
            },
            {
              type: "fix",
              scope: "dotnet",
              section: "Fixes -- DotNet",
              hidden: false,
            },
            { type: "fix", scope: "java", hidden: true },
            { type: "fix", scope: "python", hidden: true },
            { type: "fix", scope: "go", hidden: true },
            { type: "fix", scope: "rust", hidden: true },
            {
              type: "chore",
              scope: "dafny",
              section: "Maintenance -- All Languages",
              hidden: false,
            },
            {
              type: "chore",
              scope: "dotnet",
              section: "Maintenance -- DotNet",
              hidden: false,
            },
            { type: "chore", scope: "java", hidden: true },
            { type: "chore", scope: "python", hidden: true },
            { type: "chore", scope: "go", hidden: true },
            { type: "chore", scope: "rust", hidden: true },
            {
              type: "docs",
              scope: "dafny",
              section: "Maintenance -- All Languages",
              hidden: false,
            },
            {
              type: "docs",
              scope: "dotnet",
              section: "Maintenance -- DotNet",
              hidden: false,
            },
            { type: "docs", scope: "java", hidden: true },
            { type: "docs", scope: "python", hidden: true },
            { type: "docs", scope: "go", hidden: true },
            { type: "docs", scope: "rust", hidden: true },
            {
              type: "revert",
              scope: "dafny",
              section: "Fixes -- All Languages",
              hidden: false,
            },
            {
              type: "revert",
              scope: "dotnet",
              section: "Fixes -- DotNet",
              hidden: false,
            },
            { type: "revert", scope: "java", hidden: true },
            { type: "revert", scope: "python", hidden: true },
            { type: "revert", scope: "go", hidden: true },
            { type: "revert", scope: "rust", hidden: true },
            { type: "style", section: "Miscellaneous", hidden: false },
            { type: "refactor", section: "Miscellaneous", hidden: false },
            { type: "perf", section: "Miscellaneous", hidden: false },
            { type: "test", section: "Miscellaneous", hidden: false },
          ],
        },
      },
    ],
    // Update the change log with the generated release notes
    [
      "@semantic-release/changelog",
      {
        changelogFile: "CHANGELOG-dotnet.md",
        changelogTitle: "# Changelog",
      },
    ],

    // Bump the various versions
    [
      "semantic-release-replace-plugin",
      {
        replacements: [
          // Update the version for all DotNet projects
          // Does not update the dependencies
          {
            files: Object.keys(Runtimes.net),
            from: "<Version>.*</Version>",
            to: "<Version>${nextRelease.version}</Version>",
            results: Object.keys(Runtimes.net).map(CheckResults),
            countMatches: true,
          },

          // Update the AssmeblyInfo.cs file of the DotNet projects
          ...Object.entries(Runtimes.net).flatMap(
            ([file, { assemblyInfo }]) => ({
              files: assemblyInfo,
              from: "assembly: AssemblyVersion(.*)",
              to: 'assembly: AssemblyVersion("${nextRelease.version}")]',
              results: [CheckResults(assemblyInfo)],
              countMatches: true,
            }),
          ),
        ],
      },
    ],
    // Commit and push changes the changelog and versions bumps
    [
      "@semantic-release/git",
      {
        assets: [
          "CHANGELOG-dotnet.md",
          ...Object.values(Runtimes.net).flatMap((r) => r.assemblyInfo),
        ],
        message: "chore: ${nextRelease.version} \n\n${nextRelease.notes}",
      },
    ],
  ],
};

function CheckResults(file) {
  return {
    file,
    hasChanged: true,
    numMatches: 1,
    numReplacements: 1,
  };
}
