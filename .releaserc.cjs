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
  java: {
    "project.properties": {
      dependencies: [],
    },
  },
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
  branches: ["main", "jocorell/update-releaserc"],
  repositoryUrl:
    "git@github.com:aws/aws-cryptographic-material-providers-library.git",
  plugins: [
    // Check the commits since the last release
    [
      "@semantic-release/commit-analyzer",
      {
        preset: "conventionalcommits",
        parserOpts: {
          noteKeywords: ["BREAKING CHANGE", "BREAKING CHANGES"],
        },
        presetConfig: {
          types: [
            { type: "feat(dafny)",  section: "Features -- Dafny" },
            { type: "feat(java)",   section: "Features -- Java" },
            { type: "feat(dotnet)", section: "Features -- DotNet" },
            { type: "feat(python)", section: "Features -- Python" },
            { type: "feat(go)",     section: "Features -- Go" },
            { type: "feat(rust)",   section: "Features -- Rust" },
            { type: "fix(dafny)",  section: "Fixes -- Dafny" },
            { type: "fix(java)",   section: "Fixes -- Java" },
            { type: "fix(dotnet)", section: "Fixes -- DotNet" },
            { type: "fix(python)", section: "Fixes -- Python" },
            { type: "fix(go)",     section: "Fixes -- Go" },
            { type: "fix(rust)",   section: "Fixes -- Rust" },
            { type: "chore(dafny)", section: "Maintenance -- Dafny" },
            { type: "chore(java)",  section: "Maintenance -- Java" },
            { type: "chore(dotnet)",section: "Maintenance -- DotNet" },
            { type: "chore(python)",section: "Maintenance -- Python" },
            { type: "chore(go)",    section: "Maintenance -- Go" },
            { type: "chore(rust)",  section: "Maintenance -- Rust" },
            { type: "chore(ci)",    section: "Maintenance -- CI" },
            { type: "docs(java)",   section: "Maintenance -- Dafny" },
            { type: "docs(dotnet)", section: "Maintenance -- Java" },
            { type: "docs(python)", section: "Maintenance -- DotNet" },
            { type: "docs(go)",     section: "Maintenance -- Python" },
            { type: "docs(rust)",   section: "Maintenance -- Go" },
            { type: "docs(dafny)",  section: "Maintenance -- Rust" },
            { type: "revert(dafny)",  section: "Fixes -- Dafny" },
            { type: "revert(java)",   section: "Fixes -- Java" },
            { type: "revert(dotnet)", section: "Fixes -- DotNet" },
            { type: "revert(python)", section: "Fixes -- Python" },
            { type: "revert(go)",     section: "Fixes -- Go" },
            { type: "revert(rust)",   section: "Fixes -- Rust" },
            { type: "style", hidden: true },
            { type: "refactor", hidden: true },
            { type: "perf", hidden: true },
            { type: "test", hidden: true },
          ],
        },
        releaseRules: [
          { type: "docs(dafny)", release: "patch" },
          { type: "docs(java)", release: "patch" },
          { type: "docs(dotnet)", release: "patch" },
          { type: "docs(python)", release: "patch" },
          { type: "docs(go)", release: "patch" },
          { type: "docs(rust)", release: "patch" },
          { type: "revert(dafny)", release: "patch" },
          { type: "revert(java)", release: "patch" },
          { type: "revert(dotnet)", release: "patch" },
          { type: "revert(python)", release: "patch" },
          { type: "revert(go)", release: "patch" },
          { type: "revert(rust)", release: "patch" },
          { type: "chore(dafny)", release: "patch" },
          { type: "chore(java)", release: "patch" },
          { type: "chore(dotnet)", release: "patch" },
          { type: "chore(python)", release: "patch" },
          { type: "chore(go)", release: "patch" },
          { type: "chore(rust)", release: "patch" },
        ],
      },
    ],
    // Based on the commits generate release notes
    [
      "@semantic-release/release-notes-generator",
      {
        "preset": "conventionalcommits",
        "presetConfig": {
          "types": [
            {"type": "feat(dafny)",  "section": "Features -- Dafny", "hidden": false},
            {"type": "feat(java)",   "section": "Features -- Java", "hidden": false},
            {"type": "feat(dotnet)", "section": "Features -- DotNet", "hidden": false},
            {"type": "feat(python)", "section": "Features -- Python", "hidden": false},
            {"type": "feat(go)",     "section": "Features -- Go", "hidden": false},
            {"type": "feat(rust)",   "section": "Features -- Rust", "hidden": false},
            {"type": "fix(dafny)",  "section": "Fixes -- Dafny", "hidden": false},
            {"type": "fix(java)",   "section": "Fixes -- Java", "hidden": false},
            {"type": "fix(dotnet)", "section": "Fixes -- DotNet", "hidden": false},
            {"type": "fix(python)", "section": "Fixes -- Python", "hidden": false},
            {"type": "fix(go)",     "section": "Fixes -- Go", "hidden": false},
            {"type": "fix(rust)",   "section": "Fixes -- Rust", "hidden": false},
            {"type": "chore(dafny)",  "section": "Maintenance -- Dafny", "hidden": false},
            {"type": "chore(java)",   "section": "Maintenance -- Java", "hidden": false },
            {"type": "chore(dotnet)", "section": "Maintenance -- DotNet" , "hidden": false},
            {"type": "chore(python)", "section": "Maintenance -- Python", "hidden": false },
            {"type": "chore(go)",     "section": "Maintenance -- Go" , "hidden": false},
            {"type": "chore(rust)",   "section": "Maintenance -- Rust", "hidden": false },
            {"type": "docs(dafny)",  "section": "Maintenance -- Dafny", "hidden": false},
            {"type": "docs(java)",   "section": "Maintenance -- Java", "hidden": false },
            {"type": "docs(dotnet)", "section": "Maintenance -- DotNet", "hidden": false },
            {"type": "docs(python)", "section": "Maintenance -- Python", "hidden": false },
            {"type": "docs(go)",     "section": "Maintenance -- Go", "hidden": false },
            {"type": "docs(rust)",   "section": "Maintenance -- Rust", "hidden": false },
            {"type": "revert(dafny)",  "section": "Fixes -- Dafny", "hidden": false },
            {"type": "revert(java)",   "section": "Fixes -- Java", "hidden": false },
            {"type": "revert(dotnet)", "section": "Fixes -- DotNet", "hidden": false },
            {"type": "revert(python)", "section": "Fixes -- Python", "hidden": false },
            {"type": "revert(go)",     "section": "Fixes -- Go", "hidden": false },
            {"type": "revert(rust)",   "section": "Fixes -- Rust", "hidden": false },
          ]
        }
      }
    ],
    // Update the change log with the generated release notes
    [
      "@semantic-release/changelog",
      {
        changelogFile: "CHANGELOG.md",
        changelogTitle: "# Changelog",
      },
    ],

    // Bump the various versions
    [
      "semantic-release-replace-plugin",
      {
        replacements: [
          // Update the version for all Gradle Java projects
          // Does not update the dependencies
          {
            files: Object.keys(Runtimes.java),
            from: "mplVersion=.*",
            to: "mplVersion=${nextRelease.version}",
            results: Object.keys(Runtimes.java).map(CheckResults),
            countMatches: true,
          },

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
          "CHANGELOG.md",
          ...Object.values(Runtimes).flatMap((r) => Object.keys(r)),
          ...Object.values(Runtimes.net).flatMap((r) => r.assemblyInfo),
          "**/runtimes/python/**/*.dtr",
        ],
        message:
          "chore(release): ${nextRelease.version} [skip ci]\n\n${nextRelease.notes}",
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
