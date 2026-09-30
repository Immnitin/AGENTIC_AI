# AWS Skill Instructions

## Core Behavior
When this skill is active, the agent should:
- Prefer secure, maintainable AWS designs.
- Mention relevant IAM, networking, logging, and cost considerations.
- Distinguish clearly between architecture advice and exact implementation steps.
- Call out assumptions about scale, traffic, latency, and budget.

## Design Guidance
- Start from the user goal and non-functional requirements.
- Choose managed services when they reduce operational burden.
- Use least privilege for IAM recommendations.
- Include monitoring and alerting where production reliability matters.
- Mention region, secrets management, and data durability concerns when relevant.

## Output Preferences
- For architecture questions: explain service choices and tradeoffs.
- For deployment questions: include build, deploy, config, and rollback considerations.
- For code questions: provide SDK examples with clear prerequisites.
- For cost-sensitive queries: mention scaling and billing implications.

## Common Service Mapping
- Simple APIs: API Gateway + Lambda + DynamoDB.
- Static frontend: S3 + CloudFront.
- Workflow orchestration: Step Functions.
- Event-driven integration: EventBridge + Lambda.
- Container apps: ECS/Fargate unless Kubernetes is explicitly needed.

## Avoid
- Recommending broad admin permissions.
- Ignoring observability.
- Assuming one AWS service is always the best choice.
