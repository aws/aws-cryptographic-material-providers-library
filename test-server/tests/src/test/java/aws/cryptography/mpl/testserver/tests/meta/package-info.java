/**
 * Meta tests: the harness's own wire contract, not MPL behavior.
 *
 * <p>These verify guarantees no conformance test could reveal because a conformance
 * failure would be indistinguishable from an MPL failure -- e.g. that modeled errors
 * arrive as distinct types, and that bad handles yield framework errors. They run
 * against one target only; conformance tests fan out across languages.
 */
package aws.cryptography.mpl.testserver.tests.meta;
