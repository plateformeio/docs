---
icon: symbols/action
tags:
  - Plateforme
---

::: plateforme.core.database.sessions
    options:
      inherited_members: false
      members: false

## Async

::: plateforme.core.database.sessions
    options:
      heading_level: 3
      show_root_heading: false
      show_root_toc_entry: false
      docstring_style: sphinx
      members:
        - 'AsyncSession'
        - 'AsyncSessionBulk'
        - 'AsyncSessionFactory'
        - 'async_session_factory'
        - 'async_session_manager'
      
## Sync

::: plateforme.core.database.sessions
    options:
      heading_level: 3
      show_root_heading: false
      show_root_toc_entry: false
      docstring_style: sphinx
      members:
        - 'Session'
        - 'SessionBulk'
        - 'SessionFactory'
        - 'session_factory'
        - 'session_manager'
