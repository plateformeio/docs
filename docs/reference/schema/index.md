---
icon: octicons/ai-model-16
hide:
  - toc
---

Comprehensive schema definition system built on Pydantic that provides data modeling, validation, serialization and JSON schema generation with extensive customization capabilities.

<nav class="md-tags">
  <span class="md-tag md-tag-icon md-tag--repo">Plateforme</span>
</nav>

<div class="grid cards" markdown>

-   :symbols-model:{ .lg .middle } **Models**

    ---

    Base model system providing data structure definition, inheritance patterns, and validation with support for discriminated unions and root models through configurable model classes.

    :octicons-arrow-right-24: [Explore](models.md)

-   :symbols-field:{ .lg .middle } **Fields**

    ---

    Field definition system handling data type validation, computed fields, and field information with comprehensive configuration options for validation, serialization and documentation.

    :octicons-arrow-right-24: [Explore](fields.md)

-   :symbols-string:{ .lg .middle } **Aliases**

    ---

    Aliasing system providing field name transformation with support for validation and serialization aliases through configurable paths and multiple alias choices.

    :octicons-arrow-right-24: [Explore](aliases.md)

-   :symbols-misc:{ .lg .middle } **Miscellaneous**

    ---

    Additional schema utilities including type adaptation, schema generation helpers and validation tools that enhance the core schema functionality.

    :octicons-arrow-right-24: [Explore](miscellaneous.md)

</div>

## External references

Pydantic provides the foundation for the schema system with powerful data validation and serialization capabilities that are extended and customized within the framework.

<nav class="md-tags">
  <span class="md-tag md-tag-icon md-tag--repo-schema">Pydantic</span>
  <span class="md-tag md-tag-icon md-tag--external">External</span>
</nav>

<div class="grid cards" markdown>

-   :symbols-link-external:{ .lg .middle } **Core**

    ---

    Core schema validation and serialization components implementing data parsing, type coercion and schema generation with extensible validation rules and error handling.

    :octicons-arrow-right-24: [Explore](core.md)

-   :symbols-link-external:{ .lg .middle } **Decorators**

    ---

    Decorator system providing field customization, validation rules and computed field definitions with metadata handling and inheritance support.

    :octicons-arrow-right-24: [Explore](decorators.md)

</div>
