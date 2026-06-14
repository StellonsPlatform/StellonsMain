import re


class TaskExtractor:

    def extract(self, plan: str):

        tasks = []

        lines = plan.split("\n")

        for line in lines:

            if re.match(r"^\d+\.", line.strip()):

                task = line.strip()

                tasks.append(task)

        return tasks