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
            // PlatformID.MacOSX doesn't actually work
            String osDesc = System.Runtime.InteropServices.RuntimeInformation.OSDescription;
            if (osDesc.Contains("Darwin"))
            {
                return charseq.FromString("MacOS");
            }
            OperatingSystem os = Environment.OSVersion;
            PlatformID pid = os.Platform;
            switch (pid)
            {
                case PlatformID.Win32NT:
                case PlatformID.Win32S:
                case PlatformID.Win32Windows:
                case PlatformID.WinCE:
                    return charseq.FromString("Windows");
                case PlatformID.Unix:
                    return charseq.FromString("Unix");
                case PlatformID.MacOSX:
                    // This doesn't actually happen on MacOS
                    return charseq.FromString("MacOS");
                default:
                    return charseq.FromString("Other");
            }
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