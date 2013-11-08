==============
Rapid Data Viz
==============

Andrew Montalenti, CTO

.. rst-class:: logo

    .. image:: ./_static/parsely.png
        :width: 40%
        :align: right

What do we do?
==============

.. image:: ./_static/parsely.png
    :width: 90%
    :align: center

Parse.ly customers
==================

.. figure:: /_static/logos.png
    :width: 90%
    :align: center

Is online media special?
========================

Websites have a variety of interesting "first-party" metrics:

* pageviews
* unique visitors
* sessions and paths
* time spent
* page engagement (scroll, copy/paste)
* referrers
* search keywords

Third-party metrics emerging
============================

* **Comments**: Disqus, LiveFyre, Wordpress
* **Shares**: Twitter, Google+, LinkedIn, Facebook
* **Pins and Saves**: Pinterest, Delicious
* **Upvotes and Likes**: Reddit, Digg
* **Queues**: Instapaper, Readability

.. image:: ./_static/social_icons.png
    :width: 60%
    :align: center

What about online journalism?
=============================

* **Short Shelf Life**: average content shelf-life <48 hours
* **High Frequency Publishing**: 1000's posts per day
* **Unclear Conversion Goals**: nothing to buy
 
.. image:: ./_static/pulse.png
    :width: 60%
    :align: center

Time series data
================

.. image:: ./_static/sparklines_multiple.png
    :align: center

.. image:: ./_static/sparklines_stacked.png
    :align: center

Summary breakdowns
==================

.. rst-class:: spaced

    .. image:: ./_static/summary_viz.png
        :align: center

Benchmark statistics
====================

.. rst-class:: spaced

    .. image:: ./_static/benchmarked_viz.png
        :align: center

Information radiators
=====================

.. rst-class:: spaced

    .. image:: ./_static/glimpse.png
        :width: 100%
        :align: center

Contextual overlays
===================

.. rst-class:: spaced

    .. image:: ./_static/extension.png
        :width: 100%
        :align: center

How do we do it?
================

.. image:: ./_static/oss_logos.png
    :width: 90%
    :align: center

Parse.ly careers
================

.. figure:: /_static/team_jobs.png
    :width: 70%
    :align: center

Agenda
======

* Data Visualization Theory
* **webrepl**: d3 for browser dataviz
* **pyrepl**: Pandas for data mining
* **vizrepl**: IPython Notebook 2.0-dev

Data Visualization Theory
=========================

Three people:

* Edward Tufte
* Mike Bostock
* Benjamin Fry

Edward Tufte
============

.. rst-class:: spaced

    .. image:: ./_static/et_dash.jpg
        :width: 80%
        :align: center


Tufte: Do Whatever It Takes
===========================

.. rst-class:: spaced

    .. image:: ./_static/minard.png
        :width: 100%
        :align: center

data-ink ratio, cognitive style, chartjunk 

Bostock: Embrace Standards
==========================

.. rst-class:: spaced

    .. image:: ./_static/data_join.png
        :width: 70%
        :align: center

not just charts, data-document joins

Fry: It's a Process
===================

.. rst-class:: spaced

    .. image:: ./_static/process_01.png
        :width: 100%
        :align: center

    .. image:: ./_static/process_02.png
        :width: 100%
        :align: center

multi-disciplanary process, feedback loops, iteration

Chart Types (1)
===============

.. rst-class:: spaced

    .. image:: ./_static/elements_01.png
    .. image:: ./_static/elements_05.png
    .. image:: ./_static/elements_06.png


Chart Types (2)
===============

Paradox of choice?

.. rst-class:: spaced

    .. image:: ./_static/elements_02.png
    .. image:: ./_static/elements_03.png
    .. image:: ./_static/elements_04.png

Encoding Guide (1)
==================

.. rst-class:: spaced

    .. image:: ./_static/viz_elements.png
        :width: 80%
        :align: center


Encoding Guide (2)
==================

.. rst-class:: spaced

    .. image:: ./_static/elements_table.png
        :width: 80%
        :align: center

Dense Displays
==============

.. rst-class:: spaced

    .. image:: ./_static/more_data.png
        :width: 80%
        :align: center

How to iterate?
===============

    .. image:: ./_static/process_03.png
        :width: 100%
        :align: center

Tools for everything, but no **dataviz REPL**.

Or is there? Enter IPython Notebook, Pandas, the web.

pyrepl
======

Let's take a look at "pulse traffic time series".

.. image:: ./_static/pulse.png
    :width: 60%
    :align: center

pandas
======

* dataframes
* loading
* aggregates
* grouping
* sorting
* serializing
* matplotlib
* but, dataviz isn't "product ready"!

Data my browser!
================

CONUNDRUM: Once I have some nice, clean, time series (or other) data rendering
nicely in the IPython Notebook, how do I get it rendering nicely in the
browser?

Options
=======

* d3 bespoke viz: hardest, most flexible
* nvd3 chart models: slightly easier, still very flexible
* vincent/vega: easiest, relatively inflexible
* (these aren't only options, but IMO best ones)

d3-oriented Approach
====================

* iterate with Pandas and matplotlib
* convert dataframe to JSON
* load JSON with d3
* use d3 for final cleaning
* build scales / axes / labels from scratch
* build interaction layer from scratch
* for offline, use PhantomJS render

d3
==

* selections
* svg
* scales
* axes
* joins

Data
====

.. rst-class:: spaced

    .. image:: ./_static/data_set.png
        :width: 80%
        :align: center

Documents
=========

.. rst-class:: spaced

    .. image:: ./_static/data_values.png
        :width: 80%
        :align: center

Data-Driven Documents
=====================

.. rst-class:: spaced

    .. image:: ./_static/data_highlights.png
        :width: 80%
        :align: center


d3 scales
=========

.. sourcecode:: javascript

    var data = [1, 2, 3, 4, 5];

    var width = 200;
    var height = 200;

    var x = d3.scale
                .ordinal()
                .domain(data)
                .rangeBands([0, width]);
    var y = d3.scale
                .linear()
                .domain([0, d3.max(data)])
                .range([0, height]);    
    var pct = d3.scale
                .linear()
                .domain([0, d3.max(data)])
                .range([0.4, 1]);

d3 scaling
==========

.. sourcecode:: javascript

    y(1.7) // -> 68px
    pct(1.7) // -> 60.4%
    y(4.5) // -> 180px
    pct(4.5) // -> 94%
    x(5) // -> 160px
    x.rangeBand() // -> 40px

d3 drawing
==========

.. sourcecode:: javascript

    var chart = d3.select("#container")
      .append("svg")
        .attr("class", "chart")
        .attr("fill", "steelblue")
        .attr("width", width)
        .attr("height", height)
      .append("svg:g");
    
    chart.selectAll("rect")
        .data(data)
        .enter()
            .append("svg:rect")
                .attr("x", x)
                .attr("height", y)
                .attr("opacity", pct)
                .attr("y", function(d, i) { return height - y(d); })
                .attr("width", x.rangeBand());


Prototyping with d3
===================

I built a tool called "webrepl" for this.

* HTML page with codemirror + emmet
* shortcut that installs jquery, bootstrap, d3 on page
* renders JavaScript code into preview iframe
* Browser inspector lets me look into that frame

What about my data?
===================

Need to convert Pandas DataFrame to JSON format of some sort.

Typically: data and labels.

Typically also a pain in the butt!

nvd3 add-on
===========

* use canned nvd3 chart type
* customize interaction layer atop

nvd3 concepts
=============

* models
* charts
* tooltips
* utilities

nvd3 graphs
===========

.. figure:: /_static/nvd3_graphs.png
    :width: 90%
    :align: center

nvd3 approach
=============

Assumes a certain data format, typically an array of dictionaries (series)

.. sourcecode:: javascript

    var data = [
        {"key": "data",
         "values": [
            1, 2, 3, 4, 5
         ]
        }
    ];

The ``values`` array will become your chart series data -- can use your own
structure there.

Model is basically a pre-set of d3 scales, axes, labels, and data joins.

nvd3 model
==========

.. sourcecode:: javascript

    nv.addGraph(function() {
        // build nvd3 chart model
        var chart = nv.models.discreteBarChart()
            .x(function(d, i) { return i })
            .y(function(d) { return d })
                .tooltips(true).showValues(true);

        // plain d3 code to do data-document binding
        d3.select('#chart svg').datum(data)
            .transition().duration(500)
                .call(chart);

        // nv utility for refreshing graph based on window size
        nv.utils.windowResize(chart.update);

        return chart;
    });

nvd3 benefit
============

Still supports full power of d3, but gives you a starting point

.. figure:: /_static/nvd3_bar.png
    :width: 90%
    :align: center

What is Vega?
=============

* Vega is a **declarative** abstraction for dataviz.
* Essentially, a domain-specific language written in JSON.
* Outputs to d3 and also HTML5 Canvas.

.. figure:: /_static/vega_website.png
    :width: 60%
    :align: center

Vega bar example (1)
====================

.. sourcecode:: javascript

    var spec = {
        "width": 200,
        "height": 200,
        "data": [
            {
                "name": "table",
                "values": [
                    {"x":"A", "y":1}, {"x":"B", "y":2}, {"x":"C", "y":3},
                    {"x":"D", "y":4}, {"x":"E", "y":5}
                ]
            }
        ],
        // ...

Vega bar example (2)
====================

.. sourcecode:: javascript

        "scales": [
            {"name": "x", 
             "type": "ordinal", 
             "range": "width", 
             "domain": {"data":"table", "field":"data.x"} },
            {"name": "y", 
             "range": "height", 
             "nice": true, 
             "domain": {"data": "table", "field": "data.y"} },
            {"name": "pct", 
             "range": [0.4, 1], 
             "nice": true, 
             "domain": {"data": "table", "field": "data.y"} }
        ],
        // ...

Vega bar example (3)
====================

.. sourcecode:: javascript

    "marks": [
        {
            "type": "rect",
            "from": {"data": "table"},
            "properties": {
                "enter": {
                    "x": {"scale": "x", "field": "data.x"},
                    "width": {"scale":"x", "band": true, "offset": -1},
                    "y": {"scale": "y", "field": "data.y"},
                    "y2": {"scale": "y", "value": 0},
                    "opacity": {"scale": "pct", "field": "data.y"}
                },
                "update": { 
                    "fill": {"value": "steelblue"} 
                }
            }
        }
    ]

How does Vega work?
===================

* vega runtime generates d3 instructions
* for offline mode, use vg2png/vg2svg

What is Vincent?
================

* vincent is a Python library that "humanizes" vega.
* use vincent inside IPyNB
* export vega JSON from vincent objects
* run vega JS library to parse JSON

Vincent Graphs
==============

.. figure:: /_static/vincent_ipynb.png
    :width: 100%
    :align: center

vincent
=======

* vega (JSON)
* declarative visualizations
* HTML canvas

vincent example
===============

.. sourcecode:: python

    site_stack = vincent.StackedArea(df)
    site_stack.axis_titles(x='Date', y='Pageviews')
    site_stack.legend(title='Sites')
    site_stack.display()

.. figure:: /_static/vincent_stacked.png

My Tools
========

    =========== ===================================
    Step        Tools
    =========== ===================================
    acquire     pymongo, solr, apache pig
    parse       python stdlib, custom tools
    filter      ipython notebook, listcomps
    mine        pandas
    represent   matplotlib, vincent, nvd3
    refine      d3, chrome inspector
    interact    d3
    =========== ===================================

Offline: I use Phantom to run full stack, including d3.

Why is IPyNB so exciting?
=========================

* execution
* display
* saving / sharing
* platform unification

New IPyNB dataviz utilities
===========================

* IPython cell magics (``%%html``, ``%%javascript``)
* display framework
* ipython locate profile for custom CSS/JS

Future Nirvana
==============

* edit data with Pandas in IPyNB
* snapshot data as JSON cell
* edit d3 / nvd3 code in ``%%javascript`` cell
* use ``IPython.display`` to show d3 rendering result
* vincent example leads the way here

My Use Cases
============

* mine network referrers for trends
* compare real-time traffic between publishers

Authority Report
================

.. rst-class:: spaced

    .. image:: ./_static/authority_report.png
        :width: 80%
        :align: center

Extra Time?
===========

Talk about new IPyNB comm capabilities.

* Widget framework?
* Python-to-JavaScript bridge via ``IPython.kernel.comm``?
* IPython JavaScript API for cell reading?

Type Into Browser
=================

.. rst-class:: bigger

    **Links:**

    - parse.ly/jobs
    - parse.ly/authority

    **Contacts:**

    - @amontalenti / @parsely

   Questions? `Tweet me`_!

.. _Tweet me: http://twitter.com/amontalenti

This deck
=========

* `slides`_
* `notes`_
* `code`_

.. _slides: http://pixelmonkey.org/pub/dataviz-elements
.. _notes: http://pixelmonkey.org/pub/dataviz-elements/notes
.. _code: http://bit.ly/dataviz-elements-code

Other resources
===============

* `d3.js library`_ 
* `nvd3 library`_
* `nvd3 live code examples`_
* `trifacta's vega library`_
* `vega live editor`_
* `vincent library`_
* `tributary simple bars`_
* `codemirror`_ 
* `emmet`_

.. _d3.js library: http://d3js.org
.. _nvd3 library: http://nvd3.org/
.. _nvd3 live code examples: http://nvd3.org/livecode/
.. _trifacta's vega library: https://github.com/trifacta/vega
.. _vega live editor: http://trifacta.github.io/vega/editor/
.. _vincent library: https://github.com/wrobstory/vincent
.. _tributary simple bars: http://tributary.io/inlet/7376344
.. _codemirror: http://codemirror.net/
.. _emmet: http://emmet.io/


.. ifnotslides::

    .. raw:: html

        <script>
        $(function() {
            $("body").css("width", "1080px");
            $(".sphinxsidebar").css({"width": "200px", "font-size": "12px"});
            $(".bodywrapper").css("margin", "auto");
            $(".documentwrapper").css("width", "880px");
            $(".logo").removeClass("align-right");
        });
        </script>

.. ifslides::

    .. raw:: html

        <style>
        table { line-height: 1.7em; }
        td:first-child { background-color: #eee; font-weight: bold; }
        .bigger { font-size: 1.8em; line-height: 0.8em; }
        </style>
