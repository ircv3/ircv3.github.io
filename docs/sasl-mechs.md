---
layout: page
title: SASL Mechanisms
---
IAL primarily uses the same mechanisms as SASL in other protocols. Most commonly:

* [EXTERNAL](https://tools.ietf.org/html/rfc4422#appendix-A) as defined by RFC 4422
* [PLAIN](https://tools.ietf.org/search/rfc4616) as defined by RFC 4616
* [ECDSA-NIST256P-CHALLENGE](https://github.com/kaniini/ecdsatool)
* [SCRAM-SHA-256](https://tools.ietf.org/html/draft-hansen-scram-sha256-02)

as well as custom ones:

* [DH-AES]({{site.baseurl}}/specs/documentation/sasl-dh-aes.html)
* [DH-BLOWFISH]({{site.baseurl}}/specs/documentation/sasl-dh-blowfish.html)

<warn>
    The DH-AES and DH-BLOWFISH SASL mechanisms have been deprecated and are listed here for informational purposes only.
</warn>

<!-- * [ECDSA-NIST256P-CHALLENGE](/baz)
* [CHALLENGE-ED25519](/qux) -->
