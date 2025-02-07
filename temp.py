import pyautogui as pgui
import time

text = """
The Georgia School of Arts uses Agile methodology to automate its processes over five years. The project begins with a discovery phase, where stakeholders from various departments, led by Sarah (team lead), define high-level requirements like admissions, class registration, and grading. User stories and epics are created and prioritized in a product backlog. Mark, an external consultant, helps the team adopt Agile practices like time-boxed sprints and retrospectives.

In Sprint 1, the team focuses on the admissions system, building an MVP with features like online applications and user authentication. Daily stand-ups, pair programming, and continuous integration ensure smooth progress. Artifacts include wireframes, test cases, and a working prototype. Feedback from stakeholders leads to UI adjustments. Sprint 2 shifts to class registration, where the team uses test-driven development (TDD) and implements role-based access control (RBAC) for security. User feedback and retrospectives guide improvements, such as earlier user involvement and stronger QA processes.

As systems are completed, phased rollouts allow small groups to test features before full deployment. Security audits and monitoring tools ensure stability. Artifacts like API documentation, database designs, and deployment plans support the process. Practices like TDD, sprint reviews, and continuous integration ensure quality and adaptability.

The iterative approach delivers value early, improves based on feedback, and builds the team’s technical skills. Over time, the college modernizes its operations, benefiting students and faculty while maintaining budget constraints.
"""

time.sleep(5)
pgui.write(text)