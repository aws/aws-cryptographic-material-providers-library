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

// This project has several runtimes
// each one has files that need to be updated.
// We model all the files and the runtimes here in this structure
const Runtimes = {
  // Any change to the size of the `dependencies` list
  // must be accounted for in `CheckDependencyReplacementResults`.
  python: {
    "AwsCryptographicMaterialProviders/runtimes/python/pyproject.toml": {
      dependencies: [
        "AwsCryptographyPrimitives",
        "ComAmazonawsKms",
        "ComAmazonawsDynamodb",
        "StandardLibrary",
      ],
    },
    "AwsCryptographyPrimitives/runtimes/python/pyproject.toml": {
      dependencies: ["StandardLibrary"],
    },
    "ComAmazonawsKms/runtimes/python/pyproject.toml": {
      dependencies: ["StandardLibrary"],
    },
    "ComAmazonawsDynamodb/runtimes/python/pyproject.toml": {
      dependencies: ["StandardLibrary"],
    },
    "StandardLibrary/runtimes/python/pyproject.toml": {
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
  tagFormat: "v${version}-python",
  plugins: [
    // Check the commits since the last release
    [
      "@semantic-release/commit-analyzer",
      {
        preset: "conventionalcommits",
        parserOpts: {
          noteKeywords: ["PYTHON BREAKING CHANGE", "PYTHON BREAKING CHANGES"],
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
              scope: "python",
              section: "Features -- Python",
              hidden: false,
            },
            { type: "feat", scope: "java", hidden: true },
            { type: "feat", scope: "dotnet", hidden: true },
            { type: "feat", scope: ".net", hidden: true },
            { type: "feat", scope: "net", hidden: true },
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
              scope: "python",
              section: "Fixes -- Python",
              hidden: false,
            },
            { type: "fix", scope: "java", hidden: true },
            { type: "fix", scope: "dotnet", hidden: true },
            { type: "fix", scope: ".net", hidden: true },
            { type: "fix", scope: "net", hidden: true },
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
              scope: "python",
              section: "Maintenance -- Python",
              hidden: false,
            },
            { type: "chore", scope: "java", hidden: true },
            { type: "chore", scope: "dotnet", hidden: true },
            { type: "chore", scope: ".net", hidden: true },
            { type: "chore", scope: "net", hidden: true },
            { type: "chore", scope: "go", hidden: true },
            { type: "chore", scope: "rust", hidden: true },
            {
              type: "chore",
              section: "Miscellaneous",
              hidden: false,
            },
            {
              type: "docs",
              scope: "dafny",
              section: "Maintenance -- All Languages",
              hidden: false,
            },
            {
              type: "docs",
              scope: "python",
              section: "Maintenance -- Python",
              hidden: false,
            },
            { type: "docs", scope: "java", hidden: true },
            { type: "docs", scope: "dotnet", hidden: true },
            { type: "docs", scope: ".net", hidden: true },
            { type: "docs", scope: "net", hidden: true },
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
              scope: "python",
              section: "Fixes -- Python",
              hidden: false,
            },
            { type: "revert", scope: "java", hidden: true },
            { type: "revert", scope: "dotnet", hidden: true },
            { type: "revert", scope: ".net", hidden: true },
            { type: "revert", scope: "net", hidden: true },
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
        changelogFile: "CHANGELOG-python.md",
        changelogTitle: "# Changelog",
      },
    ],

    // Bump the various versions
    [
      "semantic-release-replace-plugin",
      {
        replacements: [
          // Update the version in pyproject.toml for all Python projects
          // Does not update the dependencies
          {
            files: Object.keys(Runtimes.python),
            from: 'version = ".*"',
            to: 'version = "${nextRelease.version}"',
            results: Object.keys(Runtimes.python).map(CheckResults),
            countMatches: true,
          },

          // Now update the local filesystem dependencies to PyPI dependencies
          // pinned to the minor MPL version
          {
            files: Object.keys(Runtimes.python),
            from: "{path =.*",
            to: '"${nextRelease.version}"',
            results: Object.keys(Runtimes.python).map(
              CheckDependencyReplacementResults,
            ),
            countMatches: true,
          },
        ],
      },
    ],
    [
      // Re-transpile Python code to update .dtr files as part of the release commit
      "@semantic-release/exec",
      {
        prepareCmd:
          "make -C TestVectorsAwsCryptographicMaterialProviders transpile_python",
      },
    ],
    // Commit and push changes the changelog and versions bumps
    [
      "@semantic-release/git",
      {
        assets: [
          "CHANGELOG-python.md",
          ...Object.values(Runtimes).flatMap((r) => Object.keys(r)),
          "**/runtimes/python/**/*.dtr",
        ],
        message:
          "chore: ${nextRelease.version} [skip ci]\n\n${nextRelease.notes}",
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

// For dependency replacement.
// If the runtime defines dependencies,
// assert the expected number of dependencies were replaced.
function CheckDependencyReplacementResults(file) {
  if (file.includes("AwsCryptographicMaterialProviders")) {
    return {
      file,
      hasChanged: true,
      numMatches: 4,
      numReplacements: 4,
    };
  } else if (file.includes("StandardLibrary")) {
    return {
      file,
      hasChanged: false,
      numMatches: 0,
      numReplacements: 0,
    };
  } else if (file.includes("AwsCryptographyPrimitives")) {
    return {
      file,
      hasChanged: true,
      numMatches: 1,
      numReplacements: 1,
    };
  } else if (file.includes("ComAmazonawsKms")) {
    return {
      file,
      hasChanged: true,
      numMatches: 1,
      numReplacements: 1,
    };
  } else if (file.includes("ComAmazonawsDynamodb")) {
    return {
      file,
      hasChanged: true,
      numMatches: 1,
      numReplacements: 1,
    };
  } else {
    throw new Error(
      `No known dependency replacement result specification for file ${file}`,
    );
  }
}
