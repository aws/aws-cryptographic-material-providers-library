pub mod software {
    pub mod amazon {
        pub mod cryptography {
            pub mod internaldafny {
                pub mod StormTrackingCMC {
                    pub use crate::storm_tracker::internal_StormTrackingCMC::*;
                    use crate::*;
                }
                pub mod SynchronizedLocalCMC {
                    pub use crate::local_cmc::internal_SynchronizedLocalCMC::*;
                    use crate::*;
                }
            }
        }
    }
}
