---
icon: octicons/apps-16
hide:
  - toc
---

# Application programming interface

Complete API framework built on FastAPI providing routing, request handling, dependency injection, and OpenAPI documentation with extensive customization capabilities for building robust REST APIs.

<nav class="md-tags">
  <span class="md-tag md-tag-icon md-tag--repo">Plateforme</span>
</nav>

<div class="grid cards" markdown>

-   :symbols-manager:{ .lg .middle } **Managers**

    ---

    API manager system handling router registration, endpoint configuration, and application lifecycle with support for versioning and documentation generation.

    :octicons-arrow-right-24: [Explore](managers.md)

-   :symbols-routing:{ .lg .middle } **Routing**

    ---

    Routing system providing path operations, request handling, and WebSocket support with configurable route generation and validation for resource endpoints.

    :octicons-arrow-right-24: [Explore](routing.md)

-   :symbols-parameter:{ .lg .middle } **Parameters**

    ---

    Parameter handling system for request validation, payload processing and response serialization with support for resource payloads and selection parameters.

    :octicons-arrow-right-24: [Explore](parameters.md)

-   :symbols-hierarchy:{ .lg .middle } **Dependencies**

    ---

    Dependency injection system managing request-scoped dependencies with support for session handling, filtering, and configurable dependency resolution.

    :octicons-arrow-right-24: [Explore](dependencies.md)

-   :symbols-error:{ .lg .middle } **Exceptions**

    ---

    Exception handling system providing custom error responses and standardized error handling with database and session-specific exception handlers.

    :octicons-arrow-right-24: [Explore](exceptions.md)

-   :symbols-middleware:{ .lg .middle } **Middleware**

    ---

    Middleware system implementing request/response processing, bulk operations, and WebSocket handling with configurable middleware chains and error handling.

    :octicons-arrow-right-24: [Explore](middleware.md)

</div>

## External references

FastAPI and Starlette provide the foundation for the API framework with powerful request handling and ASGI capabilities that are extended and customized within the framework.

<nav class="md-tags">
  <span class="md-tag md-tag-icon md-tag--repo-api">FastAPI</span>
  <span class="md-tag md-tag-icon md-tag--repo-api">Starlette</span>
  <span class="md-tag md-tag-icon md-tag--external">External</span>
</nav>

<div class="grid cards" markdown>

-   :symbols-link-external:{ .lg .middle } **I/O**

    ---

    Core input/output handling components providing request parsing, response formatting and WebSocket communication with streaming support and content negotiation.

    :octicons-arrow-right-24: [Explore](data.md)

-   :symbols-link-external:{ .lg .middle } **Security**

    ---

    Security components implementing authentication, authorization and security middleware with configurable security schemes and permission handling.

    :octicons-arrow-right-24: [Explore](security.md)

-   :symbols-link-external:{ .lg .middle } **Status**

    ---

    HTTP status code handling providing standardized response codes and status classification with comprehensive status code mapping.

    :octicons-arrow-right-24: [Explore](status.md)

</div>
