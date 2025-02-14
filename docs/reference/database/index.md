---
icon: octicons/database-16
hide:
  - toc
---

Comprehensive database abstraction layer built on SQLAlchemy that provides session management, connection pooling, bulk operations, and type engines for seamless database interactions while supporting multiple database backends.

<nav class="md-tags">
  <span class="md-tag md-tag-icon md-tag--repo">Plateforme</span>
</nav>

<div class="grid cards" markdown>

-   :symbols-manager:{ .lg .middle } **Managers**

    ---

    Database manager interface for handling engine configuration, connection establishment, and operation routing with support for read/write splitting and multiple database instances.

    :octicons-arrow-right-24: [Explore](managers.md)

-   :symbols-routing:{ .lg .middle } **Routing**

    ---

    Database routing system that directs operations to appropriate engines based on configurable rules, with support for read/write splitting and custom routing strategies.

    :octicons-arrow-right-24: [Explore](routing.md)

-   :symbols-action:{ .lg .middle } **Sessions**

    ---

    Database session management system providing transaction handling, unit of work pattern implementation, and session lifecycle management with both sync and async support.

    :octicons-arrow-right-24: [Explore](sessions.md)

-   :symbols-note:{ .lg .middle } **Bulk**

    ---

    Efficient bulk operation system for handling large-scale database operations with optimized memory usage, batching capabilities, and transaction management.

    :octicons-arrow-right-24: [Explore](bulk.md)

-   :symbols-metadata:{ .lg .middle } **Metadata**

    ---

    Database schema tools for table definitions, constraint management, index creation, and schema migrations with support for multiple database dialects.

    :octicons-arrow-right-24: [Explore](metadata.md)

-   :symbols-type:{ .lg .middle } **Types**

    ---

    Extensive collection of database type engines and column type definitions supporting standard and custom types with validation and serialization capabilities.

    :octicons-arrow-right-24: [Explore](types.md)

-   :symbols-tools:{ .lg .middle } **Utilities**

    ---

    Comprehensive set of helper functions for database operations, query building, filtering, and result processing with support for common database patterns.

    :octicons-arrow-right-24: [Explore](utilities.md)

</div>

## External references

SQLAlchemy provides the foundation for the framework's database layer, offering powerful ORM capabilities, SQL abstraction, and comprehensive database tooling. These components are directly integrated and extended within the framework.

<nav class="md-tags">
  <span class="md-tag md-tag-icon md-tag--repo-database">SQLAlchemy</span>
  <span class="md-tag md-tag-icon md-tag--external">External</span>
</nav>

<div class="grid cards" markdown>

-   :symbols-link-external:{ .lg .middle } **Engines**

    ---

    Core database engine functionality providing connection management, dialect support, and execution interface with extensive configuration options for different database backends.

    :octicons-arrow-right-24: [Explore](engines.md)

-   :symbols-link-external:{ .lg .middle } **Events**

    ---

    Event system for database operations allowing hooks into session, transaction, and model lifecycle events with both synchronous and asynchronous event handling.

    :octicons-arrow-right-24: [Explore](events.md)

-   :symbols-link-external:{ .lg .middle } **Expressions**

    ---

    SQL expression language components providing pythonic query construction, column operations, and complex SQL generation with dialect-specific optimizations.

    :octicons-arrow-right-24: [Explore](expressions.md)

-   :symbols-link-external:{ .lg .middle } **Object-Relational Mapping**

    ---

    Comprehensive ORM system handling object persistence, relationship management, inheritance mapping, and query generation with extensive customization options.

    :octicons-arrow-right-24: [Explore](orm.md)

-   :symbols-link-external:{ .lg .middle } **Pool**

    ---

    Connection pool management system providing connection recycling, overflow handling, and connection lifecycle management with configurable pooling strategies.

    :octicons-arrow-right-24: [Explore](pool.md)

</div>
