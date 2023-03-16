# Livemark Project

[![Build](https://img.shields.io/github/actions/workflow/status/frictionlessdata/livemark-project/general.yaml?branch=main)](https://github.com/frictionlessdata/livemark-project/actions)
[![Codebase](https://img.shields.io/badge/codebase-github-brightgreen)](https://github.com/frictionlessdata/livemark-project)
[![Support](https://img.shields.io/badge/support-discord-brightgreen)](https://discord.com/channels/695635777199145130/695635777199145133)

> Edit `index.md` file to explore Livemark's features or just remove everything to start from a scratch.

It's a template document created automatically to introduce Livemark. We will list here core [Livemark](https://livemark.frictionlessdata.io/) features and you can play with theme live editing the document. It's possible to use any standard Markdown features as well.

## Logic

We can pre-process our markdown file using [Jinja](https://jinja.palletsprojects.com/):

{% for car in frictionless.Resource('data/cars.csv').read_rows(size=5) %}
- {{ car.brand }} {{ car.model }}: ${{ car.price }}
{% endfor %}

## Table

We can visualize our data as a table using [DataTables](https://datatables.net/):

```yaml table
data: data/cars.csv
width: 600
order:
  - [3, 'desc']
columns:
  - data: type
  - data: brand
  - data: model
  - data: price
  - data: kmpl
  - data: bhp
```

## Chart

Another option is to draw a chart using [Vega](https://vega.github.io/vega-lite/):

```yaml chart
data:
  url: data/cars.csv
mark: circle
selection:
  brush:
    type: interval
encoding:
  x:
    type: quantitative
    field: kmpl
    scale:
     domain: [12,25]
  y:
    type: quantitative
    field: price
    scale:
     domain: [100,900]
  color:
    condition:
      selection: brush
      field: type
      type: nominal
    value: grey
  size:
    type: quantitative
    field: bhp
width: 500
height: 300
```

## Script

Moreover, we can execute scripts in [Python](https://www.python.org/)/[Bash](https://www.gnu.org/software/bash/):

```python script
for number in range(1, 6):
    print(f'Hello World #{number}!')
```

## Markup

Markdown is not enough? Finally, let's add some markup with [Bootstrap](https://getbootstrap.com/):

```html markup
<div style="max-width: 600px">
<div class="container">
<div class="row">
<div class="col-sm">
  <div class="livemark-markdown">![Package](https://livemark.frictionlessdata.io/assets/data-package.png)</div>
  <div class="text-center">
  <p><strong>Data Package</strong></p>
  <p>A simple container format for describing a coherent collection of data in a single package.</p>
  </div>
</div>
<div class="col-sm">
  <div class="livemark-markdown">![Resource](https://livemark.frictionlessdata.io/assets/data-resource.png)</div>
  <div class="text-center">
  <p><strong>Data Resource</strong></p>
  <p>A simple format to describe and package a single data resource such as a individual table or file.</p>
  </div>
</div>
<div class="col-sm">
  <div class="livemark-markdown">![Schema](https://livemark.frictionlessdata.io/assets/table-schema.png)</div>
  <div class="text-center">
  <p><strong>Table Schema</strong></p>
  <p>A simple format to declare a schema for tabular data. The schema is designed to be expressible in JSON.</p>
  </div>
</div>
</div>
</div>
</div>
```
