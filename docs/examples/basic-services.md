# Basic examples with services

!!! warning "The documentation is under heavy development!"

    The documentation is actively being developed and might not cover every feature. For full details, refer to the [source code]({{ links.repo.core }}).

## No specification

The following example demonstrates how to create a basic service without a resource specification. This is useful when you want to create a service that doesn't need any specific resources. Unlike services with specifications, basic services can also be attached directly to packages.

### Implementation

#### Create service { .hide }

```python { title="Create a service without a resource specification" }
--8<-- "src/examples/basic_services/example_no_spec.py:snippet-services"
```

1. We create a simple `POST` endpoint that returns a string message.

#### Assign the service { .hide }

```python { title="Assign the service to a resource" }
--8<-- "src/examples/basic_services/example_no_spec.py:snippet-resources"
```

??? quote "Source code in `src/examples/basic_services/example_no_spec.py`"

    ```python
    --8<-- "src/examples/basic_services/example_no_spec.py"
    ```

### Playground

#### Call `hello` endpoint { .hide }

We can directly call the service `hello` endpoint.

```http { title="Call the service 'hello' endpoint" }
--8<-- "src/examples/basic_services/example_no_spec.http:hello-materials"
```

<div class="result" markdown>

??? example "Response"

    ```json
    --8<-- "src/examples/basic_services/example_no_spec.jsonl:hello-materials"
    ```

</div>

---

## With simple specification

The following example demonstrates how to create a basic service with a simple specification. This is useful when you want to create a service that can be attached to multiple resources. The specification is like a contract that the resources must fulfill to be able to use the service. In this example, we create a service that can be attached to "orderable" resources, i.e. resources that expose a `price` attribute.

### Implementation

#### Create service { .hide }

```python { title="Create a service with a simple specification" }
--8<-- "src/examples/basic_services/example_simple_spec.py:snippet-services"
```

#### Assign the service { .hide }

```python { title="Assign the service to some resources" }
--8<-- "src/examples/basic_services/example_simple_spec.py:snippet-resources"
```

??? quote "Source code in `src/examples/basic_services/example_simple_spec.py`"

    ```python
    --8<-- "src/examples/basic_services/example_simple_spec.py"
    ```

### Playground

#### Add some resources { .hide }

Let's create some materials and rockets.

=== "Materials"

    ```http { title="Add some materials" }
    --8<-- "src/examples/basic_services/example_simple_spec.http:post-materials"
    ```

    <div class="result" markdown>

    ??? example "Response"

        ```json
        --8<-- "src/examples/basic_services/example_simple_spec.jsonl:post-materials"
        ```

    </div>

=== "Rockets"

    ```http { title="Add some rockets" }
    --8<-- "src/examples/basic_services/example_simple_spec.http:post-rockets"
    ```

    <div class="result" markdown>

    ??? example "Response"

        ```json
        --8<-- "src/examples/basic_services/example_simple_spec.jsonl:post-rockets"
        ```

    </div>

#### Call `buy` endpoint { .hide }

We can now call the service `buy` endpoint on materials and rockets.

=== "Materials"

    ```http { title="Call the service 'buy' endpoint" }
    --8<-- "src/examples/basic_services/example_simple_spec.http:buy-materials"
    ```

    <div class="result" markdown>

    ??? example "Response"

        ```json
        --8<-- "src/examples/basic_services/example_simple_spec.jsonl:buy-materials"
        ```

    </div>

=== "Rockets"

    ```http { title="Call the service 'buy' endpoint" }
    --8<-- "src/examples/basic_services/example_simple_spec.http:buy-rockets"
    ```

    <div class="result" markdown>

    ??? example "Response"

        ```json
        --8<-- "src/examples/basic_services/example_simple_spec.jsonl:buy-rockets"
        ```

    </div>

---

## With selection specification

The following example demonstrates how to create a basic service with a selection specification. This is useful when you want to create endpoints either at the resource collection level or at the resource instance level. The selection parameter will be filled at runtime with the selected resources inferred from the URL. In this example, we create a service that can be attached to both materials and rockets.

### Implementation

#### Create service { .hide }

```python { title="Create a service with a selection specification" }
--8<-- "src/examples/basic_services/example_selection_spec.py:snippet-services"
```

#### Assign the service { .hide }

```python { title="Assign the service to some resources" }
--8<-- "src/examples/basic_services/example_selection_spec.py:snippet-resources"
```

??? quote "Source code in `src/examples/basic_services/example_selection_spec.py`"

    ```python
    --8<-- "src/examples/basic_services/example_selection_spec.py"
    ```

### Playground

#### Add some resources { .hide }

Let's create some materials and rockets.

=== "Materials"

    ```http { title="Add some materials" }
    --8<-- "src/examples/basic_services/example_selection_spec.http:post-materials"
    ```

    <div class="result" markdown>

    ??? example "Response"

        ```json
        --8<-- "src/examples/basic_services/example_selection_spec.jsonl:post-materials"
        ```

    </div>

=== "Rockets"

    ```http { title="Add some rockets" }
    --8<-- "src/examples/basic_services/example_selection_spec.http:post-rockets"
    ```

    <div class="result" markdown>

    ??? example "Response"

        ```json
        --8<-- "src/examples/basic_services/example_selection_spec.jsonl:post-rockets"
        ```

    </div>

#### Call `describe-many` endpoint { .hide }

We can now call the service `describe` endpoint on materials and rockets.

=== "Materials"

    ```http { title="Call the service 'describe' endpoint on materials" }
    --8<-- "src/examples/basic_services/example_selection_spec.http:describe-many-materials"
    ```

    <div class="result" markdown>

    ??? example "Response"

        ```json
        --8<-- "src/examples/basic_services/example_selection_spec.jsonl:describe-many-materials"
        ```

    </div>

=== "Rockets"

    ```http { title="Call the service 'describe' endpoint on rockets" }
    --8<-- "src/examples/basic_services/example_selection_spec.http:describe-many-rockets"
    ```

    <div class="result" markdown>

    ??? example "Response"

        ```json
        --8<-- "src/examples/basic_services/example_selection_spec.jsonl:describe-many-rockets"
        ```

    </div>

#### Call `describe-one` endpoint { .hide }

Or, alternatively, we can call the service `describe` endpoint on a specific material or rocket.

=== "Materials"

    ```http { title="Call the service 'describe' endpoint on a specific material" }
    --8<-- "src/examples/basic_services/example_selection_spec.http:describe-one-material"
    ```

    <div class="result" markdown>

    ??? example "Response"

        ```json
        --8<-- "src/examples/basic_services/example_selection_spec.jsonl:describe-one-material"
        ```

    </div>

=== "Rockets"

    ```http { title="Call the service 'describe' endpoint on a specific rocket" }
    --8<-- "src/examples/basic_services/example_selection_spec.http:describe-one-rocket"
    ```

    <div class="result" markdown>

    ??? example "Response"

        ```json
        --8<-- "src/examples/basic_services/example_selection_spec.jsonl:describe-one-rocket"
        ```

    </div>
