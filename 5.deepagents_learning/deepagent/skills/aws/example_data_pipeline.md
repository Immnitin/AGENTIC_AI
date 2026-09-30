# Example: AWS Data Pipeline

## User Query
Create an AWS design for ingesting files from S3, transforming them, and loading them into a queryable store.

## How The Skill Should Help
- Consider S3 events, Lambda or Glue, and Athena or Redshift depending on scale.
- Mention schema evolution and failure handling.
- Include storage format suggestions like Parquet when useful.

## Response Pattern
1. State assumptions about volume and latency.
2. Propose the service flow.
3. Explain operational concerns.
