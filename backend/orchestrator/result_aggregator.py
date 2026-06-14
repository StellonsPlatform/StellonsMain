class ResultAggregator:

    def aggregate(self, results):

        final_report = ""

        for result in results:

            final_report += (
                f"\n\n"
                f"AGENT: {result['agent']}\n"
                f"TASK: {result['task']}\n\n"
                f"{result['result']}\n"
            )

        return final_report