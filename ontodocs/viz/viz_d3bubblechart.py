# !/usr/bin/env python
#  -*- coding: UTF-8 -*-


import os, sys
import json

from ..core import *
from ..core.utils import *
from ..core.builder import *  # loads and sets up Django
from ..core.viz_factory import VizFactory




# ===========
# D3 BUBBLE CHART
# ===========



class D3BubbleChartViz(VizFactory):
    """
    D3 Bubbles

    """


    def __init__(self, ontospy_graph, title=""):
        """
        Init
        """
        super(D3BubbleChartViz, self).__init__(ontospy_graph, title)
        self.static_files = ["libs/d3-v3", "libs/jquery"]


    def _buildTemplates(self):
        """
        OVERRIDING THIS METHOD from Factory
        """

        jsontree_classes = build_D3bubbleChart(0, 99, 1, self.ontospy_graph.toplayer)
        c_total = len(self.ontospy_graph.classes)

        JSON_DATA_CLASSES = json.dumps({'children': jsontree_classes, 'name': 'owl:Thing',})


        extra_context = {
                        "ontograph": self.ontospy_graph,
    					"TOTAL_CLASSES": c_total,
    					'JSON_DATA_CLASSES' : JSON_DATA_CLASSES,
                        }

        # Ontology - MAIN PAGE
        contents = self._renderTemplate("d3/d3_bubblechart.html", extraContext=extra_context)
        FILE_NAME = "index.html"
        main_url = self._save2File(contents, FILE_NAME, self.output_path)

        return main_url




# if called directly, for testing purposes pick a random ontology

if __name__ == '__main__':

    TEST_ONLINE = False
    try:

        g = get_onto_for_testing(TEST_ONLINE)

        v = D3BubbleChartViz(g, title="")
        v.build()
        v.preview()

        sys.exit(0)

    except KeyboardInterrupt as e:  # Ctrl-C
        raise e
