

# Data Driven Test Exec Script

import Testcases.CollatzStep as TCM  
exec(TCM.tc ([Odd1, 16, 5]))
exec(TCM.tc ([Odd2, 4, 1]))
exec(TCM.tc ([Even1, 16, 8]))
exec(TCM.tc ([Even2, 5, 10]))
