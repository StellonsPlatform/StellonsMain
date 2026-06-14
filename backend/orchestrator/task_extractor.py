import re


class TaskExtractor:

    def extract(self, plan: str):

        tasks = []

        in_tasks_section = False

        for line in plan.split("\n"):

            line = line.strip()

            if "**Tasks" in line:
                in_tasks_section = True
                continue

            if "**Milestones" in line:
                break

            if "**Dependencies" in line:
                break

            if in_tasks_section:

                if re.match(r"^\d+\.", line):
                    tasks.append(line)

        return tasks