class GridPlanner:

    def plan(self, analysis_report):

        if analysis_report["is_long_scroll"]:

            return {
                "strategy": "long_scroll",
                "segment_height": 1500,
                "overlap": 200,
                "reason": "is_long_scroll=True"
            }

        if analysis_report["edge_density"] > 0.08:

            return {
                "strategy": "dense_grid",
                "rows": 3,
                "cols": 3,
                "reason": f'edge_density={analysis_report["edge_density"]}'
            }

        return {
            "strategy": "standard_grid",
            "rows": 2,
            "cols": 2,
            "reason": "default_strategy"
        }