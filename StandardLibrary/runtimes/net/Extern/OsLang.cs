// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

using icharseq = Dafny.ISequence<char>;
using charseq = Dafny.Sequence<char>;

namespace OsLang
{
    public partial class __default
    {
        // returns one of : MacOS, Windows, Unix, Other
        public static icharseq GetOsShort()
        {
            if (System.OperatingSystem.IsMacOS())
            {
                return charseq.FromString("MacOS");
            }
            if (System.OperatingSystem.IsWindows())
            {
                return charseq.FromString("Windows");
            }
            if (System.OperatingSystem.IsLinux())
            {
                return charseq.FromString("Unix");
            }
            if (System.OperatingSystem.IsFreeBSD())
            {
                return charseq.FromString("Unix");
            }
            return charseq.FromString("Other");
        }

        // returns one of : Java, Dotnet, Go, Python, Rust
        public static icharseq GetLanguageShort()
        {
            return charseq.FromString("Dotnet");
        }

        // returns a human readable, language specific, unstable over time, description of the OS
        public static icharseq GetOsLong()
        {
            return charseq.FromString(System.Runtime.InteropServices.RuntimeInformation.OSDescription);
        }

        // returns a human readable, language specific, unstable over time, description of the Language
        public static icharseq GetLanguageLong()
        {
            return charseq.FromString("Dotnet " + Environment.Version.ToString());
        }
    }
}