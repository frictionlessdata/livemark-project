# Data Collection

## Loading

Let's load the dataset we're going to use:

```python task id=data
import os
from frictionless import Resource

resource = Resource('https://raw.githubusercontent.com/frictionlessdata/livemark/main/data/cars.csv')
resource.write('data/cars.csv')
```

## Attributions

The data sources we have used:
- The cars example provided by [Visdown](https://visdown.com/) project.
