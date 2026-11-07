# Reserve picker turns on assignment and consume them on completion

Approved during discovery on 2026-11-07: assigning a picker reserves their turn, confirmed movie-night completion consumes it, and cancellation releases the reservation. Counting assignment or movie selection immediately as a used turn would charge people for canceled nights and mix upcoming plans with completed picker totals; the reservation distinction accepts more lifecycle handling to preserve that meaning. Current-round eligibility remains distinct from lifetime totals, so agreed rotation corrections do not rewrite viewing history, and automatic draws manage only one active round at a time.

See [D09–D11 in the discovery decisions](../DISCOVERY_DECISIONS.md) and the [glossary](../../GLOSSARY.md). No storage or transaction architecture is selected by this record.
