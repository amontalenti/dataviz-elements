====================
Elements of Data Viz
====================

Andrew Montalenti, CTO

.. rst-class:: logo

    .. image:: ./_static/parsely.png
        :width: 40%
        :align: right

What is Parse.ly?
=================

Analytics provider for large-scale content sites.

    .. image:: ./_static/banner_01.png
        :align: center
    .. image:: ./_static/banner_02.png
        :align: center
    .. image:: ./_static/banner_03.png
        :align: center
    .. image:: ./_static/banner_04.png
        :align: center

Why does does online media need visualization?
==============================================

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

Is online journalism special?
=============================

Yes.

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

Summary data
============

.. rst-class:: spaced

    .. image:: ./_static/summary_viz.png
        :align: center

Benchmark data
==============

.. rst-class:: spaced

    .. image:: ./_static/benchmarked_viz.png
        :align: center

Information radiators
=====================

.. rst-class:: spaced

    .. image:: ./_static/glimpse.png
        :width: 100%
        :align: center

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

Demo Time!
=========

.. rst-class:: spaced

    .. image:: ./_static/authority_report.png
        :width: 80%
        :align: center

My Tools
========

    =========== ===================================
    Step        Tools
    =========== ===================================
    acquire     pymongo, solr, apache pig
    parse       python stdlib, custom tools
    filter      ipython notebook, listcomps, pandas
    mine        pandas
    represent   matplotlib, vincent, d3
    refine      d3, chrome inspector
    interact    d3
    =========== ===================================

"Big" Data
==========

.. rst-class:: spaced

    .. image:: ./_static/big_data_viz.png
        :width: 80%
        :align: center

Type Into Browser
=================

.. rst-class:: bigger

    **Links:**

    - bit.ly/becamp2013
    - parse.ly

    **Contacts:**

    - @amontalenti
    - @parsely

    **Questions?**


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
