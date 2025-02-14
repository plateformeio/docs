# Basic example

!!! warning "The documentation is under heavy development!"

    The documentation is actively being developed and might not cover every feature. For full details, refer to the [source code]({{ links.repo.core }}).

## Overview

Below is an example of a basic application using CRUD resources. In this example, we define three resources: `Material`, `Rocket`, and `RocketPart`. The `Material` resource even exposes custom endpoints for updating its name and counting its records.

## Implementation

```python { title="Define basic resources" }
--8<-- "src/examples/basic/example.py:snippet"
```

1. The `rocket_parts` field establishes a reverse relationship to `RocketPart`, enabling bidirectional navigation between materials and their usage in rockets.
2. The `update_name` method is a custom route defined at the resource instance level. It updates the `name` attribute of the `Material` instance and returns a message confirming the update. It can be accessed at the `/materials/{_material_key}/update-name` endpoint.
3. The `count` method is a custom route defined at the resource class level. It queries the database to count the number of `Material` instances and returns the result. It can be accessed at the `/materials/count` endpoint.
4. The `parts` field now references `RocketPart` instead of `Material` directly, allowing for additional attributes on the relationship.
5. A composite index ensures uniqueness of material-rocket combinations, preventing duplicate entries.
6. Forward references using string literals establish proper relationships while avoiding circular imports.

??? quote "Source code in `src/examples/basic/example.py`"

    ```python
    --8<-- "src/examples/basic/example.py"
    ```

---

## Playing with materials

### Add some materials { .hide }

The following example shows how to add multiple materials.

```http { title="Create some materials" .no-copy .no-select }
--8<-- "src/examples/basic/example.http:post-materials-summary"
```

<div class="result" markdown>

??? example "Request"

    ```http
    --8<-- "src/examples/basic/example.http:post-materials"
    ```

??? example "Response"

    ```json
    --8<-- "src/examples/basic/example.jsonl:post-materials"
    ```

</div>

### Fetch materials { .hide }

You can sort or filter the list of materials. For example, to retrieve materials sorted by code:

```http { title="Fetch materials with sorting and limit" }
--8<-- "src/examples/basic/example.http:get-materials-sort"
```

<div class="result" markdown>

??? example "Response"

    ```json
    --8<-- "src/examples/basic/example.jsonl:get-materials-sort"
    ```

</div>

### Filter materials { .hide }

Or, to filter materials whose code matches a pattern:

```http { title="Fetch materials that match specific conditions" }
--8<-- "src/examples/basic/example.http:get-materials-like"
```

<div class="result" markdown>

??? example "Response"

    ```json
    --8<-- "src/examples/basic/example.jsonl:get-materials-like"
    ```

</div>

### Count materials { .hide }

To count the number of material records:

```http { title="Count materials" }
--8<-- "src/examples/basic/example.http:count-materials"
```

<div class="result" markdown>

??? example "Response"

    ```json
    --8<-- "src/examples/basic/example.jsonl:count-materials"
    ```

</div>

### Update material name { .hide }

This example updates the name of a material by calling its custom endpoint.

```http { title="Update a specific material's name" }
--8<-- "src/examples/basic/example.http:update-material-name"
```

<div class="result" markdown>

??? example "Response"

    ```json
    --8<-- "src/examples/basic/example.jsonl:update-material-name"
    ```

</div>

---

## Playing with rockets

### Add some rockets { .hide }

You can create rockets without specifying any parts. For instance:

```http { title="Create some rockets without parts" }
--8<-- "src/examples/basic/example.http:post-rockets-no-parts"
```

<div class="result" markdown>

??? example "Response"

    ```json
    --8<-- "src/examples/basic/example.jsonl:post-rockets-no-parts"
    ```

</div>

Alternatively, rockets can be created with associated parts. In this example, parts are defined by linking to existing materials.

```http { title="Create rockets with associated materials" .no-copy .no-select }
--8<-- "src/examples/basic/example.http:post-rockets-with-parts-summary"
```

<div class="result" markdown>

??? example "Request"

    ```http
    --8<-- "src/examples/basic/example.http:post-rockets-with-parts"
    ```

??? example "Response"

    ```json
    --8<-- "src/examples/basic/example.jsonl:post-rockets-with-parts"
    ```

</div>

### Fetch rockets { .hide }

Retrieve the list of rockets with or without their parts:

```http { title="Fetch all rockets" }
--8<-- "src/examples/basic/example.http:get-rockets"
```

<div class="result" markdown>

??? example "Response"

    ```json
    --8<-- "src/examples/basic/example.jsonl:get-rockets"
    ```

</div>

### Update rocket parts { .hide }

You can update rocket parts by filtering the rocket(s) to update. For example, this call updates a rocket’s parts based on a code filter:

```http { title="Update rocket materials using filter" }
--8<-- "src/examples/basic/example.http:patch-rocket"
```

<div class="result" markdown>

??? example "Response"

    ```json
    --8<-- "src/examples/basic/example.jsonl:patch-rocket"
    ```

</div>

### Fetch rocket parts { .hide }

To retrieve the parts of a specific rocket:

```http { title="Retrieve the updated rocket parts" }
--8<-- "src/examples/basic/example.http:get-rocket-parts"
```

<div class="result" markdown>

??? example "Response"

    ```json
    --8<-- "src/examples/basic/example.jsonl:get-rocket-parts"
    ```

</div>

### Filter rocket parts { .hide }

Finally, you can filter rocket parts by the material's properties. For example, to get parts where the material code matches a given pattern:

```http { title="Fetch rocket parts that match specific conditions" }
--8<-- "src/examples/basic/example.http:get-rockets-match"
```

<div class="result" markdown>

??? example "Response"

    ```json
    --8<-- "src/examples/basic/example.jsonl:get-rockets-match"
    ```

</div>
