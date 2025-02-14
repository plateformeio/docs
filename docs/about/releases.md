---
icon: octicons/tag-16
---

!!! note "Current status: `alpha`"

    We're actively working towards our `beta release`. Track our progress [here](roadmap.md#current-progress)!

!!! warning "Alpha phase notice"

    During the `alpha` phase, breaking changes may occur between releases as we establish the core features.

<div class="grid cards" markdown>

-   :octicons-history-24:{ .lg .middle } **Latest release**

    ---

    Version `0.1.0-a1` (Alpha)

    [:octicons-log-16:]({{ links.repo.core }}/releases/0.1-alpha-1)
    [:octicons-archive-16:]({{ links.repo.core }}/releases/0.1-alpha-1)
    &nbsp;&nbsp;&nbsp;:octicons-history-16: _2025-01-16_

-   :fontawesome-brands-python:{ .lg .middle } **Supported versions**

    ---
    
    Python 3.11+
    
    :octicons-arrow-right-24: [Compatibility](#compatibility)

</div>

## Quick start

| Version | Status | Release Date | Links |
|---------|--------|--------------|-------|
| `0.1.0-a1` | active | 2025-01-16 | [:octicons-tag-16:]({{ links.repo.core }}/releases/0.1.0-a1) [:octicons-download-16:]({{ links.repo.core }}/releases/0.1.0-a1) |

Use the following command to install the latest version of Plateforme:

=== "pip"
    ```bash
    pip install plateforme
    ```

=== "uv"
    ```bash
    uv add plateforme
    ```

??? tip "Install a specific version"

    Use the following command to install a specific version or the current development version of Plateforme:

    === "pip"
        ```bash
        # Specific version
        pip install plateforme==[version]

        # Development version
        pip install git+{{ links.repo.core }}.git
        ```

    === "uv"
        ```bash
        # Specific version
        uv add plateforme==[version]

        # Development version
        uv add git+{{ links.repo.core }}.git
        ```

## Feedback and issues

<div class="grid cards" markdown>

-   :octicons-bug-24:{ .lg .middle } __Issue reporting__

    ---

    Found a bug? Have a feature request?

    [:fontawesome-brands-github: Open an Issue]({{ links.repo.core }}/issues){ .md-button }

-   :octicons-comment-discussion-24:{ .lg .middle } **Feedback**

    ---

    Share your experience, questions and ideas

    [:fontawesome-brands-github: Join the discussion]({{ links.repo.core }}/discussions){ .md-button }

</div>

---

## Changelog

### :octicons-tag-24: **`0.1`**

#### :octicons-hash-24: `alpha-1`

> [:octicons-log-16:]({{ links.repo.core }}/releases/0.1-alpha-1)
> [:octicons-archive-16:]({{ links.repo.core }}/releases/0.1-alpha-1)
> &nbsp;•&nbsp;&nbsp;:octicons-history-16: 2025-01-16


=== ":octicons-rocket-16: Featured"

    - {Major feature with brief impact description}
    - {Key enhancement that improves developer experience}

=== ":octicons-tools-16: Added"

    - {New component}: {what it enables}
    - {New API}: {key functionality}

=== ":octicons-bug-16: Fixed"

    - {Issue type}: {what was resolved}
    - {Bug category}: {fix impact}

=== ":octicons-alert-16: Breaking"

    - {API change}: {migration note}
    - {Behavior modification}: {impact}

---

## Compatibility

Plateforme is compatible with **Python 3.11 and later versions**. If you need support for an earlier version, please let us know by joining the discussion.
