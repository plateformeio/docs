---
icon: symbols/link-external
tags:
  - SQLAlchemy
  - External
---

::: plateforme.core.database.engines
    options:
      inherited_members: false
      members: false

## Async

::: plateforme.core.database.engines
    options:
      heading_level: 3
      show_root_heading: false
      show_root_toc_entry: false
      docstring_style: sphinx
      members:
        - 'AsyncConnection'
        - 'AsyncEngine'
        - 'AsyncMappingResult'
        - 'AsyncResult'
        - 'AsyncScalarResult'
        - 'AsyncTransaction'
        - 'AsyncTupleResult'
        - 'async_engine_from_config'
        - 'create_async_engine'
      
## Sync

::: plateforme.core.database.engines
    options:
      heading_level: 3
      show_root_heading: false
      show_root_toc_entry: false
      docstring_style: sphinx
      members:
        - 'Connection'
        - 'Dialect'
        - 'Engine'
        - 'MappingResult'
        - 'Result'
        - 'Row'
        - 'ScalarResult'
        - 'Transaction'
        - 'TupleResult'
        - 'create_engine'
        - 'create_mock_engine'
        - 'engine_from_config'
