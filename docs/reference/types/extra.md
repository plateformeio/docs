---
icon: symbols/link-external
tags:
  - Pydantic
  - External
---

For types that are more complex, you can find external libraries that provide additional Pydantic-compatible types. For example,
the [Pydantic Extra Types](https://github.com/pydantic/pydantic-extra-types) project.

!!! warning "External dependency"

    To use this project, you need to install the optional [pydantic-extra-types](https://pypi.org/project/pydantic-extra-types) package:

    === "pip"

        ```bash
        pip install pydantic-extra-types
        ```

    === "uv"

        ```bash
        uv add pydantic-extra-types
        ```

The following non-exhaustive list of types are supported by [Pydantic Extra Types](https://github.com/pydantic/pydantic-extra-types):

- **Color Types**: color validation types.
- **Payment Card Numbers**: a type that allows you to store payment card numbers in your model.
- **Phone Numbers**: a type that allows you to store phone numbers in your model.
- **Routing Numbers**: a type that allows you to store ABA transit routing numbers in your model.
- **MAC Address**: a type that allows you to store MAC addresses in your model.
