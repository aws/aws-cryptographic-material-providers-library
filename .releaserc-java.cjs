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
  java: {
    "project.properties": {
      dependencies: [],
    },
  },
};

/**
 * @type {import('semantic-release').GlobalConfig}
 */
module.exports = {
  branches: ["main", "update-changelog-for-java"],
  repositoryUrl:
    "git@github.com:aws/aws-cryptographic-material-providers-library.git",
  tagFormat: "v${version}-java",
  plugins: [
    [
      "@semantic-release/commit-analyzer",
      {
        preset: "conventionalcommits",
        parserOpts: {
          noteKeywords: ["JAVA BREAKING CHANGE", "JAVA BREAKING CHANGES"],
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
          { scope: "python", release: false },
          { scope: "dotnet", release: false },
          { scope: ".net", release: false },
          { scope: "net", release: false },
          { scope: "go", release: false },
          { scope: "rust", release: false },
          { type: "docs", release: "patch" },
          { type: "revert", release: "patch" },
          { type: "chore", release: "patch" },
        ],
      },
    ],
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
              scope: "java",
              section: "Features -- Java",
              hidden: false,
            },
            { type: "feat", scope: ".net", hidden: true },
            { type: "feat", scope: "net", hidden: true },
            { type: "feat", scope: "dotnet", hidden: true },
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
              scope: "java",
              section: "Fixes -- Java",
              hidden: false,
            },
            { type: "fix", scope: ".net", hidden: true },
            { type: "fix", scope: "net", hidden: true },
            { type: "fix", scope: "dotnet", hidden: true },
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
              scope: "java",
              section: "Maintenance -- Java",
              hidden: false,
            },
            { type: "chore", scope: ".net", hidden: true },
            { type: "chore", scope: "net", hidden: true },
            { type: "chore", scope: "dotnet", hidden: true },
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
              scope: "java",
              section: "Maintenance -- Java",
              hidden: false,
            },
            { type: "docs", scope: ".net", hidden: true },
            { type: "docs", scope: "dotnet", hidden: true },
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
              scope: "java",
              section: "Fixes -- Java",
              hidden: false,
            },
            { type: "revert", scope: ".net", hidden: true },
            { type: "revert", scope: "dotnet", hidden: true },
            { type: "revert", scope: "python", hidden: true },
            { type: "revert", scope: "go", hidden: true },
            { type: "revert", scope: "rust", hidden: true },
            { type: "feat", section: "Features -- All Languages", hidden: false },
            { type: "fix", section: "Fixes -- All Languages", hidden: false },
            { type: "chore", section: "Maintenance -- All Languages", hidden: false },
            { type: "docs", section: "Maintenance -- All Languages", hidden: false },
            { type: "revert", section: "Fixes -- All Languages", hidden: false },
            { type: "style", section: "Miscellaneous -- All Languages", hidden: false },
            { type: "refactor", section: "Miscellaneous -- All Languages", hidden: false },
            { type: "perf", section: "Miscellaneous -- All Languages", hidden: false },
            { type: "test", section: "Miscellaneous -- All Languages", hidden: false },
          ],
        },
      },
    ],
    [
      "@semantic-release/changelog",
      {
        changelogFile: "CHANGELOG-java.md",
        changelogTitle:
          "# Changelog",
      },
    ],
    [
      "semantic-release-replace-plugin",
      {
        replacements: [
          {
            files: Object.keys(Runtimes.java),
            from: "javaMPLVersion=.*",
            to: "javaMPLVersion=${nextRelease.version}",
            results: Object.keys(Runtimes.java).map(CheckResults),
            countMatches: true,
          },
          {
            files: ["ComAmazonawsKms/src/Index.dfy"],
            from: 'var version := ".*"',
            to: 'var version := "${nextRelease.version}"',
            results: [CheckResults("ComAmazonawsKms/src/Index.dfy")],
            countMatches: true,
          },
        ],
      },
    ],
    [
      "@semantic-release/git",
      {
        assets: [
          "CHANGELOG-java.md",
          "ComAmazonawsKms/src/Index.dfy",
          ...Object.keys(Runtimes.java),
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
