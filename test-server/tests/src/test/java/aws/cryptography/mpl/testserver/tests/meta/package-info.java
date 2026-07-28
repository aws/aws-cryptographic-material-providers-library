/**
 * <b>Meta tests: the harness's own wire contract, not MPL behavior.</b>
 *
 * <p>The MPL TestServer follows the rule that the harness IS the tests
 * (Requirement 10.1): there is no test suite validating the harness, because that
 * would be testing the test framework. The narrow exception is this package.
 *
 * <p>What lives here are the guarantees the harness makes that no conformance test
 * could reveal, because a conformance failure would be indistinguishable from an MPL
 * failure:
 *
 * <ul>
 *   <li>{@code CreateMPL} returns a non-empty handle.</li>
 *   <li>An absent, empty, unknown, or wrong-kind handle yields a
 *       {@code GenericServerError}, performs no MPL operation, and registers
 *       nothing.</li>
 *   <li>The two modeled errors arrive at the client as distinct types with their
 *       messages intact -- which requires the {@code __type} discriminator fix.</li>
 * </ul>
 *
 * <p>These run against {@code LanguageServerRegistry.primary()} only. They are
 * <b>not</b> parameterized over the target set: the wire contract is a property of the
 * harness, so verifying it once is enough. Conformance tests -- in the parent package
 * -- are the ones that will fan out across languages (Requirement 10.3).
 */
package aws.cryptography.mpl.testserver.tests.meta;
