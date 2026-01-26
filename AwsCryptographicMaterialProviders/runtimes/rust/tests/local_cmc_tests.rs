// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

#![deny(warnings, unconditional_panic)]
#![deny(nonstandard_style)]
#![deny(clippy::all)]

pub struct BoxError(String);
pub struct BoxError2(String);

impl std::fmt::Debug for BoxError2 {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "{}", self.0)
    }
}

impl From<BoxError> for BoxError2 {
    fn from(error: BoxError) -> Self {
        BoxError2(error.0)
    }
}

impl<T: std::fmt::Debug> From<T> for BoxError {
    fn from(error: T) -> Self {
        let my_str = format!("{error:?}");
        BoxError(my_str)
    }
}

pub mod local_cmc_tests {
    use aws_mpl_legacy::client as mpl_client;
    use aws_mpl_legacy::deps::aws_cryptography_keyStore::types::BeaconKeyMaterials;
    use aws_mpl_legacy::operation::get_cache_entry::GetCacheEntryOutput;
    use aws_mpl_legacy::types::cryptographic_materials_cache::CryptographicMaterialsCacheRef;
    use aws_mpl_legacy::types::error::Error;
    use aws_mpl_legacy::types::material_providers_config::MaterialProvidersConfig;
    use aws_mpl_legacy::types::CacheType;
    use aws_mpl_legacy::types::DefaultCache;
    use aws_mpl_legacy::types::Materials;
    use chrono::Utc;
    use futures::stream::StreamExt;
    use rand::{rng, Rng};
    use std::collections::HashMap;
    // Currently this is commented out to keep it consistent with other
    // runtimes but every language should eventually have a network
    // call delay while testing adding to the StormTrackingCache.
    // use std::time::Duration;

    async fn work_for_thread() -> Result<(), crate::BoxError> {
        let mpl_config: MaterialProvidersConfig = MaterialProvidersConfig::builder().build()?;
        let mpl: mpl_client::Client = mpl_client::Client::from_conf(mpl_config)?;

        let test: CryptographicMaterialsCacheRef = mpl
            .create_cryptographic_materials_cache()
            .cache(CacheType::Default(
                DefaultCache::builder().entry_capacity(10).build()?,
            ))
            .send()
            .await?;

        let identifiers: Vec<&str> = vec![
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
            "ten",
            "eleven",
            "twelve",
            "thirteen",
            "fourteen",
            "fifteen",
            "sixteen",
            "seventeen",
            "eighteen",
            "nineteen",
            "twenty",
            "twenty one",
        ];

        let id_size: usize = identifiers.len();

        let invocations = 300000;
        let concurrent_tasks = 10;

        futures::stream::iter(0..invocations)
            .map(|_i| {
                let identifiers = identifiers.clone();
                let test = test.clone();

                async move {
                    let random = rng().random_range(0..id_size);
                    let beacon_key_identifier: &str = identifiers[random];

                    let cache_identifier: aws_smithy_types::Blob =
                        aws_smithy_types::Blob::new(beacon_key_identifier.as_bytes());

                    let cache_entry_output: Result<GetCacheEntryOutput, Error> = test
                        .get_cache_entry()
                        .identifier(cache_identifier.clone())
                        .send()
                        .await;

                    match cache_entry_output {
                        Ok(_) => {
                            // Cache hit
                        }
                        Err(Error::EntryDoesNotExist { message: _m }) => {
                            let materials = Materials::BeaconKey(
                                BeaconKeyMaterials::builder()
                                    .beacon_key_identifier(beacon_key_identifier.to_string())
                                    // The cacheIdentifier is used as the material
                                    // because we are not testing the cryptography here.
                                    .beacon_key(cache_identifier.clone())
                                    .encryption_context(HashMap::new())
                                    .build()?,
                            );
                            // This sleep time is to mimic a KMS or DDB call
                            // Currently this is commented out to keep it consistent with other
                            // runtimes but every language should eventually have a network
                            // call delay while testing adding to the StormTrackingCache.
                            // The reason why this is commented out and not just set to 0 is because
                            // setting it to 0 adds a significant overhead of task switching, and
                            // with that, testing for 300_000 instances will not be possible.
                            // let network_call_delay: u64 = 50;
                            // tokio::time::sleep(Duration::from_millis(network_call_delay)).await;

                            test.put_cache_entry()
                                .identifier(cache_identifier)
                                .creation_time(Utc::now().timestamp())
                                .expiry_time(Utc::now().timestamp() + 1)
                                .materials(materials)
                                .send()
                                .await?;

                        }
                        Err(e) => {
                            panic!("Unexpected error while accessing cache: {e}");
                        }
                    }

                    Ok::<(), crate::BoxError>(())
                }
            })
            .buffer_unordered(concurrent_tasks)
            .collect::<Vec<_>>()
            .await;

        Ok(())
    }

    #[tokio::test(flavor = "multi_thread")]
    async fn test_a_lot_of_adding() -> Result<(), crate::BoxError2> {
        work_for_thread().await?;
        Ok(())
    }
}
